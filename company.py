import sqlite3

DB_NAME = 'mydatabase.db'

def add_employee():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        empid = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        role = input("Enter Role: ")
        address = input("Enter Address: ")
        salary = float(input("Enter Salary: "))
        joining_date = input("Enter Joining Date (YYYY-MM-DD): ")
        cursor.execute(
            "INSERT INTO employees(empid, name, role, address, salary, joining_date) VALUES (?, ?, ?, ?, ?, ?)",
            (empid, name, role, address, salary, joining_date)
        )
        conn.commit()
        print("Employee added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Employee ID already exists.")
    except ValueError:
        print("Invalid input. Please enter data in correct format.")
    finally:
        cursor.close()
        conn.close()

def delete_employee():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    empid = input("Enter Employee ID to delete: ")
    cursor.execute("DELETE FROM employees WHERE empid = ?", (empid,))
    conn.commit()
    if cursor.rowcount == 0:
        print("No employee found with this ID.")
    else:
        print("Employee deleted successfully.")
    cursor.close()
    conn.close()

def edit_employee():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    empid = input("Enter Employee ID to edit: ")
    cursor.execute("SELECT * FROM employees WHERE empid = ?", (empid,))
    data = cursor.fetchone()
    if data:
        print(f"Current Data: ID={data[0]}, Name={data[1]}, Role={data[2]}, Address={data[3]}, Salary={data[4]}, Joining Date={data[5]}")
        name = input("Enter new Name (press enter to keep current): ") or data[1]
        role = input("Enter new Role (press enter to keep current): ") or data[2]
        address = input("Enter new Address (press enter to keep current): ") or data[3]
        salary_input = input("Enter new Salary (press enter to keep current): ")
        salary = float(salary_input) if salary_input else data[4]
        joining_date = input("Enter new Joining Date (YYYY-MM-DD) (press enter to keep current): ") or data[5]

        cursor.execute(
            "UPDATE employees SET name=?, role=?, address=?, salary=?, joining_date=? WHERE empid=?",
            (name, role, address, salary, joining_date, empid)
        )
        conn.commit()
        print("Employee updated successfully.")
    else:
        print("No employee found with this ID.")
    cursor.close()
    conn.close()

def show_employee():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    empid = input("Enter Employee ID to show: ")
    cursor.execute("SELECT * FROM employees WHERE empid = ?", (empid,))
    data = cursor.fetchone()
    if data:
        print(f"Employee Details:\nID: {data[0]}\nName: {data[1]}\nRole: {data[2]}\nAddress: {data[3]}\nSalary: {data[4]}\nJoining Date: {data[5]}")
    else:
        print("No employee found with this ID.")
    cursor.close()
    conn.close()

def display_employees():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    if rows:
        print("All Employees:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Role: {row[2]}, Address: {row[3]}, Salary: {row[4]}, Joining Date: {row[5]}")
    else:
        print("No employees found.")
    cursor.close()
    conn.close()

def menu1():
    while True:
        print("\nEmployee Database Menu")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Edit Employee")
        print("4. Show Employee by ID")
        print("5. Display All Employees")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            delete_employee()
        elif choice == '3':
            edit_employee()
        elif choice == '4':
            show_employee()
        elif choice == '5':
            display_employees()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
#employee table end here
import sqlite3

DB_NAME = 'mydatabase.db'

def add_management_member():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        mgmtid = int(input("Enter Management ID: "))
        name = input("Enter Name: ")
        designation = input("Enter Designation: ")
        address = input("Enter Address: ")
        salary = float(input("Enter Salary: "))
        cabin_no = input("Enter Cabin No.: ")
        landline_no = input("Enter Landline No.: ")
        cursor.execute(
            "INSERT INTO managing_comitee(mgmtid, name, designation, address, salary, cabin_no, landline_no) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (mgmtid, name, designation, address, salary, cabin_no, landline_no)
        )
        conn.commit()
        print("Management member added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Management ID already exists.")
    except ValueError:
        print("Invalid input. Please enter data in correct format.")
    finally:
        cursor.close()
        conn.close()

def expel_management_member():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    mgmtid = input("Enter Management ID to expel: ")
    cursor.execute("DELETE FROM managing_comitee WHERE mgmtid = ?", (mgmtid,))
    conn.commit()
    if cursor.rowcount == 0:
        print("No management member found with this ID.")
    else:
        print("Management member expelled successfully.")
    cursor.close()
    conn.close()

def edit_management_member():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    mgmtid = input("Enter Management ID to edit: ")
    cursor.execute("SELECT * FROM managing_comitee WHERE mgmtid = ?", (mgmtid,))
    data = cursor.fetchone()
    if data:
        print(f"Current Data: ID={data[0]}, Name={data[1]}, Designation={data[2]}, Address={data[3]}, Salary={data[4]}, Cabin No={data[5]}, Landline No={data[6]}")
        name = input("Enter new Name (press enter to keep current): ") or data[1]
        designation = input("Enter new Designation (press enter to keep current): ") or data[2]
        address = input("Enter new Address (press enter to keep current): ") or data[3]
        salary_input = input("Enter new Salary (press enter to keep current): ")
        salary = float(salary_input) if salary_input else data[4]
        cabin_no = input("Enter new Cabin No. (press enter to keep current): ") or data[5]
        landline_no = input("Enter new Landline No. (press enter to keep current): ") or data[6]
        cursor.execute(
            """UPDATE managing_comitee 
            SET name=?, designation=?, address=?, salary=?, cabin_no=?, landline_no=? 
            WHERE mgmtid=?""",
            (name, designation, address, salary, cabin_no, landline_no, mgmtid)
        )
        conn.commit()
        print("Management member updated successfully.")
    else:
        print("No management member found with this ID.")
    cursor.close()
    conn.close()

def show_management_member():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    mgmtid = input("Enter Management ID to show: ")
    cursor.execute("SELECT * FROM managing_comitee WHERE mgmtid = ?", (mgmtid,))
    data = cursor.fetchone()
    if data:
        print(f"""Management Member Details:
ID: {data[0]}
Name: {data[1]}
Designation: {data[2]}
Address: {data[3]}
Salary: {data[4]}
Cabin No.: {data[5]}
Landline No.: {data[6]}""")
    else:
        print("No management member found with this ID.")
    cursor.close()
    conn.close()

def promote_management_member():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    mgmtid = input("Enter Management ID to promote: ")
    cursor.execute("SELECT designation FROM managing_comitee WHERE mgmtid = ?", (mgmtid,))
    data = cursor.fetchone()
    if data:
        current_designation = data[0]
        print(f"Current Designation: {current_designation}")
        new_designation = input("Enter new Designation: ")
        cursor.execute("UPDATE managing_comitee SET designation = ? WHERE mgmtid = ?", (new_designation, mgmtid))
        conn.commit()
        print("Management member promoted successfully.")
    else:
        print("No management member found with this ID.")
    cursor.close()
    conn.close()

def display_management_members():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM managing_comitee")
    rows = cursor.fetchall()
    if rows:
        print("All Management Members:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Designation: {row[2]}, Address: {row[3]}, Salary: {row[4]}, Cabin No.: {row[5]}, Landline No.: {row[6]}")
    else:
        print("No management members found.")
    cursor.close()
    conn.close()

def menu2():
    while True:
        print("\nManaging Committee Database Menu")
        print("1. Add Management Member")
        print("2. Expel Management Member")
        print("3. Edit Management Member")
        print("4. Show Management Member by ID")
        print("5. Promote Management Member")
        print("6. Display All Management Members")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_management_member()
        elif choice == '2':
            expel_management_member()
        elif choice == '3':
            edit_management_member()
        elif choice == '4':
            show_management_member()
        elif choice == '5':
            promote_management_member()
        elif choice == '6':
            display_management_members()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
#managing table ends here
import sqlite3

DB_NAME = 'mydatabase.db'

def add_staff_member():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        hsid = int(input("Enter Staff ID: "))
        name = input("Enter Name: ")
        role = input("Enter Role: ")
        salary = float(input("Enter Salary: "))
        joining_date = input("Enter Joining Date (YYYY-MM-DD): ")
        cursor.execute(
            "INSERT INTO maintainance_staf(hsid, name, role, salary, joining_date) VALUES (?, ?, ?, ?, ?)",
            (hsid, name, role, salary, joining_date)
        )
        conn.commit()
        print("Staff member added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Staff ID already exists.")
    except ValueError:
        print("Invalid input. Please enter data in correct format.")
    finally:
        cursor.close()
        conn.close()

def delete_staff_member():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    hsid = input("Enter Staff ID to delete: ")
    cursor.execute("DELETE FROM maintainance_staf WHERE hsid = ?", (hsid,))
    conn.commit()
    if cursor.rowcount == 0:
        print("No staff member found with this ID.")
    else:
        print("Staff member deleted successfully.")
    cursor.close()
    conn.close()

def edit_staff_member():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    hsid = input("Enter Staff ID to edit: ")
    cursor.execute("SELECT * FROM maintainance_staf WHERE hsid = ?", (hsid,))
    data = cursor.fetchone()
    if data:
        print(f"Current Data: ID={data[0]}, Name={data[1]}, Role={data[2]}, Salary={data[3]}, Joining Date={data[4]}")
        name = input("Enter new Name (press enter to keep current): ") or data[1]
        role = input("Enter new Role (press enter to keep current): ") or data[2]
        salary_input = input("Enter new Salary (press enter to keep current): ")
        salary = float(salary_input) if salary_input else data[3]
        joining_date = input("Enter new Joining Date (YYYY-MM-DD) (press enter to keep current): ") or data[4]

        cursor.execute(
            "UPDATE maintainance_staf SET name=?, role=?, salary=?, joining_date=? WHERE hsid=?",
            (name, role, salary, joining_date, hsid)
        )
        conn.commit()
        print("Staff member updated successfully.")
    else:
        print("No staff member found with this ID.")
    cursor.close()
    conn.close()

def show_staff_member():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    hsid = input("Enter Staff ID to show: ")
    cursor.execute("SELECT * FROM maintainance_staf WHERE hsid = ?", (hsid,))
    data = cursor.fetchone()
    if data:
        print(f"""Staff Member Details:
ID: {data[0]}
Name: {data[1]}
Role: {data[2]}
Salary: {data[3]}
Joining Date: {data[4]}""")
    else:
        print("No staff member found with this ID.")
    cursor.close()
    conn.close()

def promote_staff_member():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    hsid = input("Enter Staff ID to promote: ")
    cursor.execute("SELECT role FROM maintainance_staf WHERE hsid = ?", (hsid,))
    data = cursor.fetchone()
    if data:
        current_role = data[0]
        print(f"Current Role: {current_role}")
        new_role = input("Enter new Role: ")
        cursor.execute("UPDATE maintainance_staf SET role = ? WHERE hsid = ?", (new_role, hsid))
        conn.commit()
        print("Staff member promoted successfully.")
    else:
        print("No staff member found with this ID.")
    cursor.close()
    conn.close()

def display_staff_members():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM maintainance_staf")
    rows = cursor.fetchall()
    if rows:
        print("All Staff Members:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Role: {row[2]}, Salary: {row[3]}, Joining Date: {row[4]}")
    else:
        print("No staff members found.")
    cursor.close()
    conn.close()

def menu3():
    while True:
        print("\nMaintenance Staff Database Menu")
        print("1. Add Staff Member")
        print("2. Delete Staff Member")
        print("3. Edit Staff Member")
        print("4. Show Staff Member by ID")
        print("5. Promote Staff Member")
        print("6. Display All Staff Members")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_staff_member()
        elif choice == '2':
            delete_staff_member()
        elif choice == '3':
            edit_staff_member()
        elif choice == '4':
            show_staff_member()
        elif choice == '5':
            promote_staff_member()
        elif choice == '6':
            display_staff_members()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
ans='y'
if ans in "yY":
    print('1.manage employees\n2.manage the managing committee\n3.manage the helping staff\n4.exit\n')
    ans1=int(input('enter the task you want to perfornm'))
    if ans1==1:
        menu1()
    elif ans1==2:
        menu2()
    elif ans1==3:
        menu3()
    elif ans1==4:
        exit()
    else:
        exit()
    ans=input('do u want to continue y/Y') 