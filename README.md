# altschool-mongodb-eduhub-project
MongoDB-powered backend for EduHub – an e-learning platform focused on African and Diaspora art and history. 

EduHub MongoDB Project: African and Diaspora Art & History E-Learning Platform

Overview

EduHub is a MongoDB-backed e-learning platform focused on teaching African and diaspora art, history, and culture. Inspired by the interactive and modular structure of Khan Academy, EduHub allows students and instructors to explore rich content, track progress, and engage with multimedia educational resources.

This project demonstrates proficiency in:

MongoDB schema design and validation

CRUD operations and indexing

Aggregation pipelines for analytics

Query optimization and error handling

Setup Instructions

Prerequisites

MongoDB v8.0+

MongoDB Compass (optional GUI)

Python 3.8+

Jupyter Notebook

Python Libraries

Install with pip:

pip install pymongo pandas notebook

Run Instructions

Start your local MongoDB server.

Open and run the notebooks/eduhub_mongodb_project.ipynb file.

Explore CRUD operations, aggregation, indexing, and validations in interactive cells.

Project Structure

mongodb-eduhub-project/
├── README.md
├── notebooks/
│   └── eduhub_mongodb_project.ipynb
├── src/
│   └── eduhub_queries.py
├── data/
│   ├── sample_data.json
│   └── schema_validation.json
├── docs/
│   ├── performance_analysis.md
│   └── presentation.pptx
└── .gitignore

Collections and Relationships

users

Fields: userId, email, firstName, lastName, role, dateJoined, profile, isActive

Roles: student, instructor

courses

Fields: courseId, title, instructorId, category, level, tags, isPublished

Related to: users (via instructorId)

enrollments

Fields: studentId, courseId, progress, completed

Related to: users, courses

lessons

Fields: lessonId, courseId, title, content, duration, order

Related to: courses

assignments / submissions

Allow students to submit work and receive instructor feedback and grades

Core Functionalities

User Management

Registration, login, role-based permissions, and profile management

Course Management

Instructors create/publish courses and add lessons/assignments

Enrollment & Progress Tracking

Students enroll in and complete courses, submit assignments, receive grades

Analytics

Aggregated metrics for platform usage, instructor stats, and learning outcomes

Performance

Efficient indexing for fast searches

Aggregation pipelines used for reporting and instructor dashboards

Performance Analysis

See docs/performance_analysis.md for:

Query performance before and after indexing

Timing benchmarks

Optimized aggregation pipelines

Sample Data

Located in data/sample_data.json, including:

20 users (students/instructors)

8 courses across African History

Lessons and assignments covering diverse topics

Challenges & Solutions

Referential integrity: Managed through manual referencing (NoSQL best practice)

Search performance: Solved with compound indexes on courses

Validation: Schema rules implemented at collection level for data quality

License

MIT License

Author

Terri Nwanma — [GitHub Profile / Contact Info]
