from flask import Flask, jsonify, request, render_template
from db_funcs import *
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/create_student', methods=['POST'])
def create_student_api():
    data = request.form
    create_student(data['student_id'], data['first_name'], data['last_name'], data['dob'], data['amount_due'])
    return jsonify({'message': f'Student {data["student_id"]} created successfully'}), 201


@app.route('/read_student/', methods=['GET'])
def read_student_api():
    student = read_student(request.args.get('student_id'))
    if student:
        return jsonify({
            'student_id': student[0],
            'first_name': student[1],
            'last_name': student[2],
            'dob': student[3],
            'amount_due': student[4]
        }), 200
    else:
        return jsonify({'message': 'Student not found'}), 404


@app.route('/update_student/', methods=['POST'])
def update_student_api():
    data = request.form
    field = data['field']
    value = data['value']
    student_id = data['student_id']
    update_student(student_id, field, value)
    return jsonify({'message': f'Student {student_id} updated successfully'}), 200


@app.route('/delete_student/', methods=['GET'])
def delete_student_api():
    id = request.args.get('student_id')
    delete_student(id)
    return jsonify({'message': f'Student {id} deleted successfully'}), 200


@app.route('/all_students/', methods=['GET'])
def get_all_students_api():
    data = get_all_students()
    return render_template('display_all.html', students=data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
