# UoT-EE432-project
The final project for the EE432 Data Structure course in the University of Tripoli Department of Electrical and Electronic Engineering Spring-2024.
# School Management System

## Table of Contents
1. [Introduction](#introduction)
2. [System Architecture](#system-architecture)
3. [Modules](#modules)
4. [Key Functionalities](#key-functionalities)
5. [User Guide](#user-guide)
6. [Database](#database)
7. [User Types and ID Generation](#user-types-and-id-generation)
8. [License](#license)
9. [Acknowledgements](#acknowledgements)

## Introduction

This School Management System is designed to streamline administrative tasks in educational institutions. It provides comprehensive functionality for managing users (students, teachers, and administrators), subjects, subject groups, grades, and enrollments, all through a Command Line Interface (CLI).

## System Architecture


1. CLI Interface: Handled by the `menu.py` file, which provides the main interface and calls other management modules.
2. Management Modules: Implement commands that can be executed by the system (e.g., `user_management.py`, `subject_management.py`).
3. Service Modules: Handle database queries and interactions (e.g., `user_service.py`, `subject_service.py`).
4. Database Initialization: Managed through the `database.py` file.
5. Models: Defined in separate files for each entity type (e.g., `student.py`, `teacher.py`, `admin.py`, `subject.py`).
6. Utilities: Helper functions and validations in `utils/helpers.py` and `utils/validation.py`.

## Modules

1. Menu (`src/CLI/menu.py`):
   - Main CLI interface
   - Provides initial input/output and calls to management modules

2. Management Modules:
   - User Management (`src/commands/user_management.py`)
   - Subject Management (`src/commands/subject_management.py`)
   - Subject Group Management (`src/commands/subject_group_management.py`)
   - Grade Management (`src/commands/grade_management.py`)
   - Enrollment Management (`src/commands/enrollment_management.py`)

3. Service Modules:
   - User Service (`src/services/user_service.py`)
   - Subject Service (`src/services/subject_service.py`)
   - Subject Group Service (`src/services/subject_group_service.py`)
   - Grade Service (`src/services/grade_service.py`)
   - Enrollment Service (`src/services/enrollment_service.py`)

4. Models:
   - User (`src/models/user.py`)
   - Student (`src/models/student.py`)
   - Teacher (`src/models/teacher.py`)
   - Admin (`src/models/admin.py`)
   - Subject (`src/models/subject.py`)
   - Subject Group (`src/models/subject_group.py`)
   - Grade (`src/models/grade.py`)

5. Utilities:
   - Helpers (`src/utils/helpers.py`): Contains utility functions like password hashing and role verification.
   - Validation (`src/utils/validation.py`): Implements input validation functions to ensure data integrity.

## Key Functionalities

1. User Authentication and Authorization
2. User Management (CRUD operations for all user types)
3. Subject and Subject Group Management (CRUD operations)
4. Grade Management (CRUD operations)
5. Enrollment Management with Capacity Control
6. Password Management with Hashing
7. Viewing Student Grades, Semesters, and Enrollments
8. Teacher Control over Assigned Subject Groups and Grading

## User Guide

### First-time Setup
Make sure that all required packages are installed. To install required packages, open a CLI window. Navigate to the main folder of this program. Input the command:
`pip install -r requirements.txt`

To connect with the database, open the `sys_env.json` file and set the value of `database` to the desired path of the data. The path MUST be surrounded by quotation marks. (i.e `"database": "..\\data\\university.db"`)

Default is:`"..\\data\\university.db"`

On first run (with an empty database), the system automatically:
1. Creates necessary database tables
2. Creates an admin user with ID=`1` and password=`admin`

Note that the default password value is a VERY WEAK password and poses a significant threath to the security of the interface. Therefore, it is recommended that it be changed after the initial setup.

### For Administrators

1. Login using ID and password.
2. Manage Users (Add, Update, Delete, View)
3. Manage Subjects and Subject Groups
4. Oversee Enrollments and Grades

### For Teachers

1. Login using assigned ID (initially, password is the same as ID)
2. Change password
3. View and manage assigned subject groups
4. Assign grades to students in their subject groups

### For Students

1. Login using assigned ID (initially, password is the same as ID)
2. Change password
3. View grades, semesters, and enrollments

### General Notes

- All users should change their initial password upon first login
- Passwords must meet specific strength criteria (details in password change function)
- The system includes safeguards to prevent deleting the last admin user

## Database

The `database.py` file initializes the system's database by:
1. Creating necessary tables if they don't exist
2. Creating a database file in the `data` directory if it's missing

This design allows for easy database import/export by simply copying the file in the data folder.

## User Types and ID Generation

1. Admin:
   - ID starts from 1
   - Each new admin gets an incremented ID or fills a vacant ID number

2. Student:
   - 10-digit ID
   - First digits refer to enrollment date, rest are randomly generated

3. Teacher:
   - 12-digit ID
   - Starts with '120', followed by random digits

The system allows the use of previously generated IDs when creating a new user, provided the ID adheres to the system rules and is not currently in use.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgements

[Insert any acknowledgements or credits here]
