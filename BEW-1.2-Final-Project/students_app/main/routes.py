from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from students_app.models import  User, Student
from students_app.main.forms import StudentForm
from students_app import bcrypt

# Import app and db
from students_app import app, db
main = Blueprint('main', __name__)

# Create your routes here.
@main.route('/')
def homepage():
    # meta = db.metadata
    # for table in reversed(meta.sorted_tables):
    #     print ('Clear table %s' % table)
    #     db.session.execute(table.delete())
    # db.session.commit()

    all_students = Student.query.all()
    return render_template('home.html',
        all_students=all_students)

@main.route('/create_student', methods=['GET', 'POST'])
@login_required
def create_student():
    form = StudentForm()

    # if form was submitted and contained no errors
    if form.validate_on_submit(): 
        new_student = Student(
            first_name=form.first_name.data,
            last_name=form.last_name.data
        )
        db.session.add(new_student)
        db.session.commit()

        flash('New student was created successfully.')
        return redirect(url_for('main.student_detail', student_id=new_student.id))
    return render_template('create_student.html', form=form)

@main.route('/student/<student_id>', methods=['GET', 'POST'])
@login_required
def student_detail(student_id):
    student = Student.query.get(student_id)
    form = StudentForm(obj=student)
    print(student.first_name)

    # if form was submitted and contained no errors
    if form.validate_on_submit(): 
        student.first_name = form.first_name.data
        student.last_name = form.last_name.data

        db.session.commit()

        flash('New student was updated successfully.')
        return redirect(url_for('main.student_detail', student_id=student_id))

    return render_template('student_detail.html', student=student, form=form)