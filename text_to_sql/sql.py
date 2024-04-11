import sqlite3

conn = sqlite3.connect('employees.db')

cur = conn.cursor()

# creating the table

table_query = '''
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    job_title VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10, 2)
);
'''

cur.execute(table_query)

cur.execute("""INSERT INTO employees (employee_id, first_name, last_name, job_title, hire_date, salary)
VALUES (1, 'John', 'Doe', 'Software Engineer', '2023-01-15', 75000.00);""")

cur.execute("""
INSERT INTO employees (employee_id, first_name, last_name, job_title, hire_date, salary)
VALUES 
    (2, 'Jane', 'Smith', 'Data Scientist', '2022-09-20', 80000.00),
    (3, 'Bob', 'Johnson', 'Project Manager', '2023-03-10', 90000.00),
    (4, 'Alice', 'Brown', 'UX Designer', '2022-12-05', 70000.00);           
            """)

print('Reocrds Inserted.......')

data = cur.execute('''select * from employees''')

for row in data:
    print(row)

conn.commit()

conn.close()