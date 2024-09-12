# UoT-EE432-project
The final project for the EE432 Data Structure course in the University of Tripoli Department of Electrical and Electronic Engineering Spring-2024.
# University Management System

## Table of Contents
1. [Introduction](#introduction)
2. [System Architecture](#system-architecture)
3. [Modules](#modules)
4. [Key Functionalities](#key-functionalities)
5. [User Guide](#user-guide)
5. [Commands](#Commands)
6. [License](#license)
7. [Acknowledgements](#acknowledgements)

## Introduction

This University Management System is designed to streamline administrative tasks in educational institutions. It provides comprehensive functionality for managing users (students, teachers, and administrators), subjects, subject groups, grades, and enrollments, all through a Command Line Interface (CLI).

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

### Database

The `database.py` file initializes the system's database by:
1. Creating necessary tables if they don't exist
2. Creating a database file in the `data` directory if it's missing

This design allows for easy database import/export by simply copying the file in the data folder.

## Key Functionalities

1. User Authentication and Authorization
2. User Management (CRUD operations for all user types)
3. Subject and Subject Group Management (CRUD operations)
4. Grade Management (CRUD operations)
5. Enrollment Management with Capacity Control
6. Password Management with Hashing
7. Viewing Student Grades, Semesters, and Enrollments
8. Teacher Control over Assigned Subject Groups and Grading
9. Role-based Command Access
10. Input Validation and Error Handling

## User Guide

### First-time Setup
Make sure that all required packages are installed. To install required packages, open a CLI window. Navigate to the main folder of this program. Input the command:
`pip install -r requirements.txt`

To connect with the database, open the `sys_env.json` file and set the value of `database` to the desired path of the data relative to main.py file. The path MUST be surrounded by quotation marks. (i.e `"database": "..\\university.db"`)

Default is:`"..\\university.db"`

On first run (with an empty database), the system automatically:
1. Creates necessary database tables
2. Creates an admin user with ID=`1` and password=`admin`

Note that the default password value is a VERY WEAK password and poses a significant threath to the security of the interface. Therefore, it is recommended that it be changed after the initial setup.


### General Usage

1. Login using your assigned ID and password.
2. Upon first login, all users should change their initial password.
3. Use the `help` command to view available commands for your user role.
4. Admin users have access to all commands, while teachers and students have limited access based on their roles.
5. Attempting to use an unavailable command will result in an error message.


#### General Notes

- All users should change their initial password upon first login.
- Passwords must meet specific strength criteria (details in password change function).
- The system prevents deletion of the last admin user to ensure continued system access.
- A command is available to set the current semester, which is necessary for subject enrollment.
- A subject group must be created before any enrollment could be made.
- Enrollment is only possible for subject groups in the current semester.
- The system enforces minimum and maximum unit limits for enrollments, with prerequisites and corequisites check.
- Special "force enroll" and "force drop out" commands are available to bypass normal restrictions.

### User Types and ID Generation

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

## Commands

This section provides an overview of all available commands in the university Management System.

### User Authentication
- login: login or switch to a different user account.
- exit: Close the application.

### General
- help: Display a list of available commands for the current user role.
- help `command`: Displays more information on a specific command.

### Subject Management
- add subject: Create a new subject in the system.
- update subject: Modify details of an existing subject.
- delete subject: Remove a subject from the system.
- list subjects: Display all subjects in the system.

### Subject Group Management
- add subject group: Create a new subject group for a specific semester.
- update subject group: Modify details of an existing subject group.
- delete subject group: Remove a subject group from the system.
- list subject groups: Display all subject groups of a specific subject.

### Grade Management
- add grade: Add a new grade entry for a student in a subject.
- get grade: Retrieve a student’s grade for a specific subject and semester.
- update grade: Modify an existing grade entry.
- assign grade: Assign grades to students in a subject group.
- delete grade: Remove a grade entry from the system.
- show subject grades: Display all grades for a specific subject.
- show student grades: Show all grades for a particular student.
- show semester grades: Display grades and enrollments of a specific student for a semester.

### User Management
- add user: Create a new user account (admin, teacher, or student).
- delete user: Remove a user account from the system.
- update user: Modify details of an existing user account.
- update password: Update the password for the logged-in user.
- get user: Retrieve details of a specific user.
- list users: Display all users in the system.

### Enrollment Management
- enroll: Enroll a student in a subject group for the current semester.
- drop out: Remove a student from a subject group they're enrolled in.
- force enroll: Enroll a student in a subject group, bypassing normal restrictions.
- force drop out: Remove a student from a subject group, bypassing normal restrictions.

### Semester Management
- set current semester: Set the current semester for enrollment operations.
- get current semester: Display the currently active semester.

Note: The availability of these commands depends on the user's role (admin, teacher, or student). Use the help command after logging in to see which commands are available for your role.

## Testing Environment
A prepared database with preset subject and random student records can be created for the purposes of testing and experimenting with the commands. To create the test database, update the key `"database"` in `sys_env.json` to the path where the database is to be created. Then execute the `src\Insert_data.py` file. this database can be inspected using the built-in CLI, or normally accessed by running `main.py`. 

## License

This project is licensed under The GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details

## Acknowledgements

Special thanks to Dr. Nuri BenBarka for his invaluable guidance and support throughout this course 
His expertise and encouragement were instrumental in the successful completion of this University Management System.
