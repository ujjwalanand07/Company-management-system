import sqlite3

DATABASE = "company.db"

def add_employee():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    empid = int(input("Enter empid (integer): "))
    name = input("Enter name: ")
    role = input("Enter role: ")
    address = input("Enter address: ")
    salary = float(input("Enter salary: "))
    joiningdate = input("Enter joining date (YYYY-MM-DD): ")

    cursor.execute("INSERT INTO employees (empid, name, role, address, salary, joiningdate) VALUES (?, ?, ?, ?, ?, ?)",
                   (empid, name, role, address, salary, joiningdate))
    conn.commit()
    conn.close()
    print("Employee added successfully.")

def delete_employee():
    empid = int(input("Enter empid to delete: "))
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE empid = ?", (empid,))
    if cursor.rowcount == 0:
        print("No employee found with that empid.")
    else:
        print("Employee deleted successfully.")
    conn.commit()
    conn.close()

def edit_employee():
    empid = int(input("Enter empid to edit: "))
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE empid = ?", (empid,))
    row = cursor.fetchone()
    if not row:
        print("No employee found with that empid.")
        conn.close()
        return

    print("Current details:")
    print(f"Name: {row[1]}, Role: {row[2]}, Address: {row[3]}, Salary: {row[4]}, Joining Date: {row[5]}")
    name = input("Enter new name (leave blank to keep current): ") or row[1]
    role = input("Enter new role (leave blank to keep current): ") or row[2]
    address = input("Enter new address (leave blank to keep current): ") or row[3]
    salary_input = input("Enter new salary (leave blank to keep current): ")
    salary = float(salary_input) if salary_input else row[4]
    joiningdate = input("Enter new joining date (YYYY-MM-DD, leave blank to keep current): ") or row[5]

    cursor.execute("""UPDATE employees SET name = ?, role = ?, address = ?, salary = ?, joiningdate = ? WHERE empid = ?""",
                   (name, role, address, salary, joiningdate, empid))
    conn.commit()
    conn.close()
    print("Employee updated successfully.")

def show_employee():
    empid = int(input("Enter empid to show: "))
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE empid = ?", (empid,))
    row = cursor.fetchone()
    conn.close()
    if row:
        print(f"empid: {row[0]}, Name: {row[1]}, Role: {row[2]}, Address: {row[3]}, Salary: {row[4]}, Joining Date: {row[5]}")
    else:
        print("No employee found with that empid.")

def display_all_employees():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(f"empid: {row[0]}, Name: {row[1]}, Role: {row[2]}, Address: {row[3]}, Salary: {row[4]}, Joining Date: {row[5]}")
    else:
        print("No employees found.")

def menu1():
    while True:
        print("\nEmployee Management Menu:")
        print("1. Add New Employee")
        print("2. Delete Employee")
        print("3. Edit Employee Details")
        print("4. Show Employee by empid")
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
            display_all_employees()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")
#empoy code ends

DATABASE = "company.db"

def add_management_member():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    mgmtid = int(input("Enter mgmtid (integer): "))
    name = input("Enter name: ")
    designation = input("Enter designation: ")
    address = input("Enter address: ")
    salary = float(input("Enter salary: "))
    cabinno = input("Enter cabin number: ")
    landline_no = input("Enter landline number: ")

    cursor.execute("""
        INSERT INTO managing_comitee
        (mgmtid, name, designation, address, salary, cabinno, landline_no)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (mgmtid, name, designation, address, salary, cabinno, landline_no))

    conn.commit()
    conn.close()
    print("Management member added successfully.")

def expel_management_member():
    mgmtid = int(input("Enter mgmtid to expel: "))
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM managing_comitee WHERE mgmtid = ?", (mgmtid,))
    if cursor.rowcount == 0:
        print("No management member found with that mgmtid.")
    else:
        print("Management member expelled successfully.")

    conn.commit()
    conn.close()

def edit_management_member():
    mgmtid = int(input("Enter mgmtid to edit: "))
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM managing_comitee WHERE mgmtid = ?", (mgmtid,))
    row = cursor.fetchone()
    if not row:
        print("No management member found with that mgmtid.")
        conn.close()
        return

    print("Current details:")
    print(f"Name: {row[1]}, Designation: {row[2]}, Address: {row[3]}, Salary: {row[4]}, CabinNo: {row[5]}, Landline No: {row[6]}")

    name = input("Enter new name (leave blank to keep current): ") or row[1]
    designation = input("Enter new designation (leave blank to keep current): ") or row[2]
    address = input("Enter new address (leave blank to keep current): ") or row[3]
    salary_input = input("Enter new salary (leave blank to keep current): ")
    salary = float(salary_input) if salary_input else row[4]
    cabinno = input("Enter new cabin number (leave blank to keep current): ") or row[5]
    landline_no = input("Enter new landline number (leave blank to keep current): ") or row[6]

    cursor.execute("""
        UPDATE managing_comitee
        SET name = ?, designation = ?, address = ?, salary = ?, cabinno = ?, landline_no = ?
        WHERE mgmtid = ?
    """, (name, designation, address, salary, cabinno, landline_no, mgmtid))

    conn.commit()
    conn.close()
    print("Management member details updated successfully.")

def promote_management_member():
    mgmtid = int(input("Enter mgmtid to promote: "))
    new_designation = input("Enter new designation: ")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM managing_comitee WHERE mgmtid = ?", (mgmtid,))
    if cursor.fetchone() is None:
        print("No management member found with that mgmtid.")
    else:
        cursor.execute("UPDATE managing_comitee SET designation = ? WHERE mgmtid = ?", (new_designation, mgmtid))
        conn.commit()
        print("Management member promoted successfully.")

    conn.close()

def show_management_by_designation():
    designation = input("Enter designation to filter: ")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM managing_comitee WHERE designation = ?", (designation,))
    rows = cursor.fetchall()
    conn.close()

    if rows:
        for r in rows:
            print(f"mgmtid: {r[0]}, Name: {r[1]}, Designation: {r[2]}, Address: {r[3]}, Salary: {r[4]}, CabinNo: {r[5]}, Landline No: {r[6]}")
    else:
        print("No management members found with that designation.")

def display_all_management():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM managing_comitee")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        for r in rows:
            print(f"mgmtid: {r[0]}, Name: {r[1]}, Designation: {r[2]}, Address: {r[3]}, Salary: {r[4]}, CabinNo: {r[5]}, Landline No: {r[6]}")
    else:
        print("No management members found.")

def menu2():
    while True:
        print("\nManagement Committee Menu:")
        print("1. Add New Management Member")
        print("2. Expel Management Member")
        print("3. Edit Management Member Details")
        print("4. Promote Management Member")
        print("5. Show Management by Designation")
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
            promote_management_member()
        elif choice == '5':
            show_management_by_designation()
        elif choice == '6':
            display_all_management()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")
#management code ends

DATABASE = "company.db"

def add_staff_member():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    hsid = int(input("Enter hsid (integer): "))
    name = input("Enter name: ")
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))
    joiningdate = input("Enter joining date (YYYY-MM-DD): ")
    cursor.execute("""
        INSERT INTO maintainance_staff (hsid, name, role, salary, joiningdate)
        VALUES (?, ?, ?, ?, ?)
    """, (hsid, name, role, salary, joiningdate))
    conn.commit()
    conn.close()
    print("Staff member added successfully.")

def delete_staff_member():
    hsid = int(input("Enter hsid to delete: "))
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM maintainance_staff WHERE hsid = ?", (hsid,))
    if cursor.rowcount == 0:
        print("No staff member found with that hsid.")
    else:
        print("Staff member deleted successfully.")
    conn.commit()
    conn.close()

def edit_staff_member():
    hsid = int(input("Enter hsid to edit: "))
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM maintainance_staff WHERE hsid = ?", (hsid,))
    row = cursor.fetchone()
    if not row:
        print("No staff member found with that hsid.")
        conn.close()
        return
    print(f"Current details:\nName: {row[1]}, Role: {row[2]}, Salary: {row[3]}, Joining Date: {row[4]}")
    name = input("Enter new name (leave blank to keep current): ") or row[1]
    role = input("Enter new role (leave blank to keep current): ") or row[2]
    salary_input = input("Enter new salary (leave blank to keep current): ")
    salary = float(salary_input) if salary_input else row[3]
    joiningdate = input("Enter new joining date (YYYY-MM-DD, leave blank to keep current): ") or row[4]
    cursor.execute("""
        UPDATE maintainance_staff
        SET name = ?, role = ?, salary = ?, joiningdate = ?
        WHERE hsid = ?
    """, (name, role, salary, joiningdate, hsid))
    conn.commit()
    conn.close()
    print("Staff member details updated successfully.")

def promote_staff_member():
    hsid = int(input("Enter hsid to promote: "))
    new_role = input("Enter new role: ")
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM maintainance_staff WHERE hsid = ?", (hsid,))
    if cursor.fetchone() is None:
        print("No staff member found with that hsid.")
    else:
        cursor.execute("UPDATE maintainance_staff SET role = ? WHERE hsid = ?", (new_role, hsid))
        conn.commit()
        print("Staff member promoted successfully.")
    conn.close()

def show_staff_member():
    hsid = int(input("Enter hsid to show: "))
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM maintainance_staff WHERE hsid = ?", (hsid,))
    row = cursor.fetchone()
    conn.close()
    if row:
        print(f"hsid: {row[0]}, Name: {row[1]}, Role: {row[2]}, Salary: {row[3]}, Joining Date: {row[4]}")
    else:
        print("No staff member found with that hsid.")

def display_all_staff():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM maintainance_staff")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(f"hsid: {row[0]}, Name: {row[1]}, Role: {row[2]}, Salary: {row[3]}, Joining Date: {row[4]}")
    else:
        print("No staff members found.")

def menu3():
    while True:
        print("\nMaintenance Staff Management Menu:")
        print("1. Add New Staff Member")
        print("2. Delete Staff Member")
        print("3. Edit Staff Member Details")
        print("4. Promote Staff Member")
        print("5. Show Staff Member by hsid")
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
            promote_staff_member()
        elif choice == '5':
            show_staff_member()
        elif choice == '6':
            display_all_staff()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")
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













