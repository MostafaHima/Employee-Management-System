from prettytable import PrettyTable, ALL


class Employee:
    def __init__(self, name, ID, salary):
        self.name = name
        self.ID = ID
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, ID: {self.ID}, Salary: ${self.salary:.2f}")


class DepartmentManagementSystem:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, name, ID, salary):
        for emp in self.employee_list:
            if emp.ID == ID:
                print(f"Employee with ID {ID} already exists.")
                return

        new_employee = Employee(name, ID, salary)
        self.employee_list.append(new_employee)
        print("\nEmployee added successfully!")

    def search(self, name=None, ID=None):
        if not self.employee_list:
            print("No employees in the system.")
            return

        for employee in self.employee_list:
            if employee.name == name or employee.ID == ID:
                employee.display()
                return
        print(f"Employee with name '{name}' or ID '{ID}' not found.")

    def remove(self, name):
        if not self.employee_list:
            print("The list doesn't have any employees.")
            return

        for employee in self.employee_list:
            if employee.name == name:
                self.employee_list.remove(employee)
                print(f"Employee '{name}' has been removed.")
                return

        print(f"Employee '{name}' not found.")

    def update(self, name, new_name, new_salary):
        for employee in self.employee_list:
            if employee.name == name:
                employee.name = new_name
                employee.salary = new_salary
                print("Update is successful!")
                return

        print(f"Employee '{name}' not found.")

    def display_all(self):
        if not self.employee_list:
            print("No employees to display.")
            return

        table = PrettyTable()
        table.hrules = ALL
        table.field_names = ["Name", "ID", "Salary"]

        for employee in self.employee_list:
            table.add_row([
                employee.name,
                employee.ID,
                f"{employee.salary:.2f}$"
            ])

        print(table)

    def report(self):
        if not self.employee_list:
            print("No employees to report.")
            return

        count_employee = len(self.employee_list)
        total_salary = sum(employee.salary for employee in self.employee_list)
        average_salary = total_salary / count_employee

        sorted_employees = sorted(self.employee_list, key=lambda emp: emp.salary, reverse=True)

        print(f"\nTotal number of employees: {count_employee}")
        print(f"Total salary: {total_salary:.2f}$")
        print(f"Average salary: {average_salary:.2f}$")
        print("\nEmployees sorted by salary (highest to lowest):")

        for employee in sorted_employees:
            employee.display()


def add_employee(info):
    name = input("Name: ").strip()
    employee_id = int(input("ID: "))
    salary = float(input("Salary: "))
    info.add_employee(name, employee_id, salary)


def search(info):
    name_or_id = input("Enter name or ID: ").strip()
    if name_or_id.isdigit():
        info.search(ID=int(name_or_id))
    else:
        info.search(name=name_or_id)


info = DepartmentManagementSystem()

while True:
    print("""
    1- Report
    2- Add a new employee
    3- Search for an employee
    4- Update an Employee
    5- Remove an Employee
    6- Display All Employees
    7- Exit
    """)

    user_choice = input("Choose from above: ").strip()

    if user_choice == "1":
        info.report()

    elif user_choice == "2":
        add_employee(info)

    elif user_choice == "3":
        search(info)

    elif user_choice == "4":
        last_name = input("What is the employee's current name: ").strip()
        new_name = input("What is the new name: ").strip()
        new_salary = float(input("What is the new salary: "))
        info.update(last_name, new_name, new_salary)

    elif user_choice == "5":
        name = input("Enter the employee's name to remove: ").strip()
        info.remove(name)

    elif user_choice == "6":
        info.display_all()

    elif user_choice == "7":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose again.")
