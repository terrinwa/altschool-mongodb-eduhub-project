# File: src/eduhub_queries.py

from pymongo import MongoClient, ASCENDING, DESCENDING
from datetime import datetime, timedelta
import pandas as pd

# === Connect to MongoDB ===
client = MongoClient("mongodb://localhost:27017/")
db = client["eduhub_db"]

# === Create Collections with Schema Validation (Simplified) ===
from bson.json_util import loads

user_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["userId", "email", "firstName", "lastName", "role", "dateJoined"],
        "properties": {
            "userId": {"bsonType": "string"},
            "email": {"bsonType": "string"},
            "firstName": {"bsonType": "string"},
            "lastName": {"bsonType": "string"},
            "role": {"enum": ["student", "instructor"]},
            "dateJoined": {"bsonType": "date"},
            "profile": {
                "bsonType": "object",
                "properties": {
                    "bio": {"bsonType": "string"},
                    "avatar": {"bsonType": "string"},
                    "skills": {"bsonType": "array", "items": {"bsonType": "string"}}
                }
            },
            "isActive": {"bsonType": "bool"}
        }
    }
}

db.create_collection("users", validator=user_validator)
# Repeat similar creation for other collections (courses, enrollments, etc.)

# === Sample Insertion of Users ===
users = [
    {
        "userId": f"user{i}",
        "email": f"user{i}@edu.africa",
        "firstName": f"First{i}",
        "lastName": f"Last{i}",
        "role": "student" if i % 2 == 0 else "instructor",
        "dateJoined": datetime.now(),
        "profile": {"bio": "Passionate about African culture.", "avatar": "", "skills": ["storytelling", "research"]},
        "isActive": True
    } for i in range(1, 21)
]
db.users.insert_many(users)

# === Sample Insertion of Courses ===
courses = [
    {
        "courseId": f"course{i}",
        "title": f"History of West African Empires {i}",
        "description": "Explore pre-colonial African civilizations.",
        "instructorId": "user1",
        "category": "African History",
        "level": "beginner",
        "duration": 10,
        "price": 49.99,
        "tags": ["history", "Africa", "culture"],
        "createdAt": datetime.now(),
        "updatedAt": datetime.now(),
        "isPublished": True
    } for i in range(1, 9)
]
db.courses.insert_many(courses)

# === Enrollment Example ===
db.enrollments.insert_one({
    "studentId": "user2",
    "courseId": "course1",
    "enrolledAt": datetime.now(),
    "progress": 0,
    "completed": False
})

# === CRUD: Add Lesson to a Course ===
db.lessons.insert_one({
    "lessonId": "lesson1",
    "courseId": "course1",
    "title": "The Mali Empire",
    "content": "A deep dive into Mali's rise and culture.",
    "order": 1,
    "duration": 30,
    "resources": []
})

# === Query: Find All Active Students ===
active_students = list(db.users.find({"role": "student", "isActive": True}))
print("Active Students:", active_students)

# === Aggregation: Course Enrollment Stats ===
course_stats = list(db.enrollments.aggregate([
    {"$group": {"_id": "$courseId", "enrollments": {"$sum": 1}}}
]))
print("Course Enrollment Stats:", course_stats)

# === Indexing ===
db.users.create_index("email", unique=True)
db.courses.create_index([("title", ASCENDING), ("category", ASCENDING)])
db.assignments.create_index("dueDate")
db.enrollments.create_index([("studentId", ASCENDING), ("courseId", ASCENDING)])

# === Query Optimization with explain() ===
explain_result = db.users.find({"email": "user1@edu.africa"}).explain()
print("Explain Result for email query:", explain_result)

# === Error Handling Example ===
try:
    db.users.insert_one({"userId": "user1", "email": "user1@edu.africa"})
except Exception as e:
    print("Error inserting duplicate user:", e)

# NOTE: For full implementation, repeat for all CRUD tasks, advanced queries, and validation.
