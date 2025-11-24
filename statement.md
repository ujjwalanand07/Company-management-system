Project Statement: Company Database Management System (CLI)

1. Problem Statement

Many small to medium-sized organizations lack a unified, cost-effective, and user-friendly system for managing diverse employee data. Storing general employees, high-level management (Managing Committee), and essential support staff (Maintenance Staff) in disparate, non-standardized records leads to:

Inefficiency: Slow and manual processes for adding, updating, and retrieving employee information.

Inaccuracy: Difficulty in maintaining data integrity across different employee categories.

Lack of Control: Absence of specialized functions, such as role-based promotions, within a single system.

The core problem is the need for a simple, consolidated, and functional administrative tool for personnel record management using a readily available technology stack.

2. Scope of the Project

The scope of the Company Database Management System is strictly limited to a Command-Line Interface (CLI) application focusing on back-end data management.

In-Scope:

Data Persistence: Managing data using a single SQLite database file (mydatabase.db).

Core Logic: Implementing Python functions to establish a connection, execute SQL commands (CRUD), and close the connection for three distinct database tables (employees, managing_comitee, maintainance_staf).

User Interaction: Providing a main menu with sub-menus for each employee category accessible via text-based inputs.

Specialized Functions: Including logic for promoting or updating the specific roles/designations of Management Committee members and Maintenance Staff.

Error Handling: Basic handling for input errors (non-numeric, format errors) and database integrity errors (duplicate IDs).

Out-of-Scope:

Graphical User Interface (GUI) development.

Network/Web deployment or multi-user access.

Advanced security features (e.g., encryption, user authentication beyond the initial application entry).

Reporting or complex data querying (e.g., aggregation, complex joins).

3. Target Users

The primary target users are:

System Administrators: Individuals responsible for the official maintenance and administration of employee records.

HR Personnel: Staff who need direct access to personnel files for updates, retrieval, and verification.

Database Managers: Users requiring direct interaction with the data layer for bulk operations or debugging.

4. High-Level Features

The application provides segregated management capability through three main modules:

General Employee Module: Standard management of employee records (ID, name, role, address, salary, joining date).

Managing Committee Module: Management of high-level personnel with additional details like Cabin Number and Landline Number, and a dedicated Designation Promotion feature.

Maintenance Staff Module: Management of support staff with a dedicated Role Promotion feature.