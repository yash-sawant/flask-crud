# Flask SQLite CRUD Example

This is a simple example of a Flask web application that performs CRUD (Create, Read, Update, Delete) operations on a SQLite database. The application allows you to add, edit, delete and view student records in a table. 

[![Check it out live][run_img]][run_link]

[run_img]: https://storage.googleapis.com/cloudrun/button.svg
[run_link]: https://flask-crud-pssahwnxxa-pd.a.run.app

## Prerequisites

To run this application, you'll need:

- Python 3.x
- Flask
- SQLite

You can install Flask and SQLite using `pip`:

```sh
pip install Flask
pip install sqlite3
```

Usage
To run the application, first clone the repository:

```sh
git clone https://github.com/yash-sawant/flask-crud.git
```

Then, navigate to the project directory and start the Flask server:

```sh
python app.py
```

This will start the server on http://localhost:5000. You can access the web interface by navigating to that URL in your browser.

API endpoints
The application provides the following API endpoints:

POST /create_student: Returns a list of all students in the database.
GET /read_student: Adds a new student to the database.
POST /update_student/: Updates the details of a student with the given ID.
GET /delete_student/: Deletes a student with the given ID.
GET /all_students/: Returns all students.

Example API usage
You can test the API using a tool like curl:
