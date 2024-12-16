# Employee Management System

## Overview
The Employee Management System is a Python-based application designed to manage employee records in an organization. It provides functionalities to add, search, update, remove, display, and generate reports for employees.

## Features
1. **Add Employee**: Add a new employee with their name, ID, and salary.
2. **Search Employee**: Search for an employee by name or ID.
3. **Update Employee**: Update an employee's name and salary.
4. **Remove Employee**: Remove an employee by their name.
5. **Display All Employees**: View all employee records in a tabular format.
6. **Report Generation**: Generate a summary report, including total employees, total salary, average salary, and a list of employees sorted by salary.
7. **Exit**: Safely exit the program.

## Requirements
- Python 3.6+
- `prettytable` library for table formatting

To install the required library, run:
```bash
pip install prettytable
```

## How to Use
1. Clone or download the repository.
2. Run the Python script `employee_mgmt.py`.
3. Use the interactive menu to manage employee records:
   - **1**: Generate and display a report.
   - **2**: Add a new employee by providing their details.
   - **3**: Search for an employee by entering their name or ID.
   - **4**: Update an employee's name and salary.
   - **5**: Remove an employee by name.
   - **6**: Display all employees in a formatted table.
   - **7**: Exit the program.

## Example Usage
### Adding an Employee
```bash
Choose from above: 2
Name: John Doe
ID: 101
Salary: 5000
Employee added successfully!
```

### Generating a Report
```bash
Choose from above: 1
Total number of employees: 3
Total salary: $15000.00
Average salary: $5000.00

Employees sorted by salary (highest to lowest):
Name: John Doe, ID: 101, Salary: $5000.00
Name: Jane Smith, ID: 102, Salary: $5000.00
Name: Alex Brown, ID: 103, Salary: $5000.00
```

## Code Structure
1. **`Employee` Class**:
   - Represents an employee with attributes for `name`, `ID`, and `salary`.
   - Includes a method to display employee details.

2. **`DepartmentManagementSystem` Class**:
   - Manages the list of employees and provides methods for:
     - Adding employees
     - Searching employees
     - Removing employees
     - Updating employee details
     - Displaying all employees
     - Generating reports

3. **Main Script**:
   - Provides an interactive menu for users to interact with the system.

## Notes
- Ensure that employee IDs are unique.
- Use valid inputs for names, IDs, and salaries to avoid errors.
- The `prettytable` library is used for better formatting of employee records.


