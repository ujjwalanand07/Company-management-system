Company Database Management System (CLI)

📝 Overview of the Project

This is a comprehensive command-line interface (CLI) application built using Python and the built-in sqlite3 library. The system is designed to manage employee data across three distinct organizational categories: General Employees, the Managing Committee, and Maintenance Staff. It provides a simple, menu-driven interface for administrators to perform essential database operations (CRUD - Create, Read, Update, Delete) and handle specific promotions for each staff type, ensuring organized and efficient record-keeping. The database file used is mydatabase.db.

✨ Features

This application offers the following key functionalities:

Employee Management (Table: employees): Full CRUD operations (Add, Delete, Edit, Show by ID, Display All).

Managing Committee Management (Table: managing_comitee): CRUD-like operations (Add, Expel, Edit, Show by ID) with specialized functions to:

Promote Member: Update a member's designation.

Maintenance Staff Management (Table: maintainance_staf): CRUD-like operations (Add, Delete, Edit, Show by ID) with specialized functions to:

Promote Staff: Update a staff member's role.

Input Validation: Includes basic error handling for non-numeric input for salaries/IDs and prevents the creation of records with duplicate primary keys.

🛠️ Technologies/Tools Used

Tool/Library

Purpose

Python

The core programming language for the CLI logic.

sqlite3

Standard Python library for interacting with the internal SQLite database (mydatabase.db).

🚀 Steps to Install & Run the Project

Prerequisites

Python 3.x installed on your system.

Installation

No external packages are required as the project uses only the standard sqlite3 library.

Save the Code: Save the provided Python code into a file named main.py.

Running the Application

Make sure you are in the directory where you saved main.py.

Execute the main script from your terminal:

python main.py


The application will start, create the necessary database tables (if they don't exist), and present the main menu. Follow the on-screen prompts to interact with the system.

✅ Instructions for Testing

To ensure the system is working correctly across all modules, perform the following manual tests:

Initial Setup: Run the script and confirm the mydatabase.db file is created or accessed successfully.

Employee CRUD Test (Menu 1):

Use option 1 to Add a new employee and option 5 to Display All employees to verify creation.

Use option 3 to Edit the employee's salary and verify the change with option 4 (Show by ID).

Use option 2 to Delete the test employee.

Management Committee Test (Menu 2 - Promotion):

Add a management member with a starting designation (e.g., 'Junior Manager').

Use option 5 (Promote Management Member) and change their designation to 'Senior Manager'. Verify the change using option 4 or 6.

Maintenance Staff Test (Menu 3 - Promotion):

Add a staff member with a starting role (e.g., 'Cleaner').

Use option 5 (Promote Staff Member) and change their role to 'Supervisor'. Verify the change using option 4 or 6.

Error Handling Test: Attempt to add a new employee using an Employee ID that is already in use to verify the "Error: Employee ID already exists" message.
