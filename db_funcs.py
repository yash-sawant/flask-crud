import sqlite3


def init_db():
    # Create a connection to the SQLite database
    conn = sqlite3.connect('student_info.db')

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # Create the students table with the required columns
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            dob DATE,
            amount_due REAL
        );
    ''')

    # Commit the changes to the database
    conn.commit()
    conn.close()


# Define functions for CRUD operations

def create_student(student_id, first_name, last_name, dob, amount_due):
    conn = sqlite3.connect('student_info.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO students VALUES (?, ?, ?, ?, ?)', (student_id, first_name, last_name, dob, amount_due))
    conn.commit()
    print(f'Student {student_id} created successfully')
    conn.close()


def read_student(student_id):
    conn = sqlite3.connect('student_info.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
    student = cur.fetchone()
    conn.close()
    if student:
        print(
            f'Student ID: {student[0]}\nFirst Name: {student[1]}\nLast Name: {student[2]}\nDOB: {student[3]}\nAmount Due: {student[4]}')
        return student
    else:
        print('Student not found')
        return None


def update_student(student_id, field, value):
    conn = sqlite3.connect('student_info.db')
    cur = conn.cursor()
    cur.execute(f'UPDATE students SET {field} = ? WHERE student_id = ?', (value, student_id))
    conn.commit()
    conn.close()
    print(f'Student {student_id} updated successfully')


def delete_student(student_id):
    conn = sqlite3.connect('student_info.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
    conn.commit()
    conn.close()
    print(f'Student {student_id} deleted successfully')


def get_all_students():
    conn = sqlite3.connect('student_info.db')
    cur = conn.cursor()
    # Retrieve all the data from the "student_info" table
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    # Convert the data into a list of dictionaries
    students = []
    for row in rows:
        student = {'student_id': row[0], 'first_name': row[1], 'last_name': row[2], 'dob': row[3], 'amount_due': row[4]}
        students.append(student)
    conn.close()
    return students


# Test the functions
def test_CRUD():
    # Create a student
    create_student(1, 'John', 'Doe', '1995-05-01', 1000.0)

    # Read a student
    read_student(1)

    # Update a student
    update_student(1, 'amount_due', 2000.0)
    read_student(1)

    # Delete a student
    delete_student(1)
    read_student(1)

    # Close the cursor and connection
    cur.close()
    conn.close()
