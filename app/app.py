from flask import Flask,g, render_template, request, redirect, flash, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import login_user, logout_user, login_required, current_user

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your-secret-key'# secret key for securely signing session data
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/shahmirdbms'

#global variables
@app.before_request
def before_request():
    g.sem_id = 2
    g.registration = True # Assume registration is open by default
    g.faculty_id = session.get('faculty_id')
    g.fees=session['fee_pr_crd_hr']


# Initialize SQLAlchemy(library of python )
db = SQLAlchemy(app)

class Student(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    DOB = db.Column(db.DateTime, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    section = db.Column(db.String(7), nullable=False)
    degree = db.Column(db.String(10), nullable=False)
    campus = db.Column(db.String(15), nullable=False)
    batch = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    gender = db.Column(db.String(10), nullable=False) 
    email = db.Column(db.String(100), nullable=False, unique=True)
    cnic = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    password = db.Column(db.String(50), nullable=False)  
    user_id = db.Column(db.String(20), nullable=False)
   
    enrollments = db.relationship('Enrollment', backref='student_enrollment')

    @property
    def generate_user_id(self):
        return f"{self.batch[-2:]}k-{str(self.sno).zfill(4)}"

    
    def check_password(self, password):
        return self.password == password

    

class Faculty(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    gender = db.Column(db.String(10), nullable=False)   
    address = db.Column(db.String(300), nullable=False)
    department = db.Column(db.String(100), nullable=False)  
    date_hired = db.Column(db.DateTime, default=datetime.utcnow) 
    password = db.Column(db.String(50), nullable=False)   

    def check_password(self, password):
        return self.password == password 
    
class Admin(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)  
    password = db.Column(db.String(50), nullable=False)
    
    def check_password(self, password):
        return self.password == password

class Course(db.Model):
  C_id =db.Column(db.Integer,  primary_key=True)
  CourseName=db.Column(db.String(50), nullable=False)
  crdHours= db.Column(db.Integer, nullable=False)
  CourseCode=db.Column(db.String(50), nullable=False)

  enrollments = db.relationship('Enrollment', backref='course_enrollment')


class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    
    student_sno = db.Column(db.Integer, db.ForeignKey('student.sno'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.C_id'), primary_key=True)
    semester_id = db.Column(db.Integer, db.ForeignKey('semester.sem_id'), nullable=False)

    
    
    semester = db.relationship('Semester', backref='semester_enrollment')

class Semester(db.Model):
    __tablename__ = 'semester'

    sem_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    semester = db.Column(db.String(50), nullable=False)

    
    enrollments = db.relationship('Enrollment', backref='semester_enrollment')

class TeacherCourse(db.Model):
    __tablename__ = 'teachercourse'
    id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.sno'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.C_id'), nullable=False)
    section = db.Column(db.String(7), nullable=False)  # New section column

    faculty = db.relationship('Faculty', backref='teacher_courses')
    course = db.relationship('Course', backref='teacher_courses')

class Attendance(db.Model):
    __tablename__ = 'attendance'

    id = db.Column(db.Integer, primary_key=True)
    sem_id = db.Column(db.Integer, db.ForeignKey('semester.sem_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.C_id'), nullable=False)
    student_sno = db.Column(db.Integer, db.ForeignKey('student.sno'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(10), nullable=False) 

    semester = db.relationship('Semester', backref='attendance_records')
    course = db.relationship('Course', backref='attendance_records')
    student = db.relationship('Student', backref='attendance_records')    

class Marks(db.Model):
    __tablename__ = 'marks'
    id = db.Column(db.Integer, primary_key=True)
    student_sno = db.Column(db.Integer, db.ForeignKey('student.sno'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.C_id'), nullable=False)

class Assessment(db.Model):
    __tablename__ = 'assessment'
    id = db.Column(db.Integer, primary_key=True)
    marks_id = db.Column(db.Integer, db.ForeignKey('marks.id'), nullable=False)  
    assessment_type = db.Column(db.String(50), nullable=False) 
    marks = db.Column(db.Float, nullable=False) 

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    student_sno = db.Column(db.Integer, db.ForeignKey('student.sno'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.C_id'), nullable=False)
    semester_id = db.Column(db.Integer, db.ForeignKey('semester.sem_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # Rating from 0 to 100
    section = db.Column(db.String(7), nullable=False)
    
    student = db.relationship('Student', backref='feedbacks')
    course = db.relationship('Course', backref='feedbacks')
    semester = db.relationship('Semester', backref='feedbacks')

def calculate_gpa(sgpa):
    if sgpa >= 90:
        return 4.0
    elif sgpa >= 85:
        return 3.7
    elif sgpa >= 80:
        return 3.3
    elif sgpa >= 75:
        return 3.0
    elif sgpa >= 70:
        return 2.7
    elif sgpa >= 65:
        return 2.3
    elif sgpa >= 60:
        return 2.0
    elif sgpa >= 55:
        return 1.7
    elif sgpa >= 50:
        return 1.3
    elif sgpa >= 45:
        return 1.0
    else:
        return 0.0
def calculate_grade(marks):
    if marks >= 86:
        return 'A'
    elif marks >= 82:
        return 'A-'
    elif marks >= 78:
        return 'B+'
    elif marks >= 74:
        return 'B'
    elif marks >= 70:
        return 'B-'
    elif marks >= 66:
        return 'C+'
    elif marks >= 62:
        return 'C'
    elif marks >= 58:
        return 'C-'
    elif marks >= 54:
        return 'D+'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'    
MAX_CREDIT_HOURS = 18 

# Home route
@app.route('/')
def home():
    
    first_name = session.get('first_name')
    return render_template('index.html', first_name=first_name)

#?                 ///////////////////////////student//////////////////////////

#login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        user = Student.query.filter_by(user_id=user_id).first()

        if user and user.check_password(password):
            session['user_id'] = user.user_id
            session['first_name'] = user.first_name
            session['student_id2']=user.sno
            
            return redirect('/std_dashboard')  # Redirect to the main page after login
        else:
            flash("Invalid credentials", "danger")
            return render_template('login.html')    

    return render_template('login.html') 

@app.route('/logout')
def logout():
    session.pop('first_name', None)  
    return redirect('/')  # Redirect to the login page

@app.route('/std_dashboard')   
def std_dashboard():
    user = Student.query.filter_by(user_id=session['user_id']).first() if 'user_id' in session else None
    return render_template('std_dashboard.html', user=user)  # Adjusted render

# Add student route
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        first_name = request.form['first_name']        
        last_name = request.form['last_name']
        DOB = request.form['DOB']
        section = request.form['section']
        degree = request.form['degree']
        campus = request.form['campus']
        batch = request.form['batch']
        phone = request.form['phone']
        gender = request.form['gender'] 
        email = request.form['email']
        cnic = request.form['cnic']
        address = request.form['address']
        password = request.form['password']  
        
        student = Student(
            first_name=first_name,
            last_name=last_name, 
            DOB=DOB,
            section=section,
            degree=degree,
            campus=campus,
            batch=batch,
            phone=phone,
            gender=gender,
            email=email,
            cnic=cnic,
            address=address,
            password=password,       )

        db.session.add(student)
        db.session.commit()
        student.user_id = student.generate_user_id
        db.session.commit()
        flash('Student data has been submitted successfully!', 'success')

    allStudent = Student.query.all()
    return render_template('add_student.html', allStudent=allStudent)

# Show student data route
@app.route('/std_data', methods=['GET'])
def show_std_data():
    allStudent = Student.query.all()
    return render_template('student_data.html', allStudent=allStudent)



# Update student route
@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    student = Student.query.filter_by(sno=sno).first()
    if request.method == 'POST':
        student.first_name = request.form['first_name']
        student.last_name = request.form['last_name']
        student.DOB = request.form['DOB']
        student.section = request.form['section']
        student.degree = request.form['degree']
        student.campus = request.form['campus']
        student.batch = request.form['batch']
        student.phone = request.form['phone']
        student.gender = request.form['gender']
        student.email = request.form['email']
        student.cnic = request.form['cnic']
        student.address = request.form['address']
        student.password = request.form['password']  

        db.session.commit()
        flash('Student data has been updated successfully!', 'success')
        return redirect("/std_data")

    return render_template('update.html', student=student)

# Delete student route
@app.route('/delete/<int:sno>')
def delete(sno):
    student = Student.query.filter_by(sno=sno).first()
    db.session.delete(student)
    db.session.commit()
    flash('Student data has been deleted successfully!', 'success')
    return redirect("/std_data")

#student profile
@app.route('/std_profile')
def std_profile():
    
    if 'student_id2' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login'))  

    student_sno = session['student_id2']
    student = Student.query.get(student_sno)

    if not student:
        flash('Student not found.', 'danger')
        return redirect(url_for('login')) 

    return render_template('student_profile.html', student=student)

# STUDENT COURSE REGISTERATION
@app.route('/register_course', methods=['GET', 'POST'])
def register_course():
    g.registration = session.get('registration_status', None)
    if 'user_id' not in session:
        flash("You need to log in first!", "danger")
        return redirect('/login')

    if g.registration == True:#REGISTRATION IS OPEN
        user = Student.query.filter_by(user_id=session['user_id']).first() if 'user_id' in session else None
        courses = Course.query.all()  # Get all courses

        if request.method == 'POST':
            selected_courses = request.form.getlist('courses') 
            
            
            total_credit_hours = 0
            for course_id in selected_courses:
                course = Course.query.get(course_id)
                if course:
                    total_credit_hours += course.crdHours #if not exceed limit

            
            if total_credit_hours > MAX_CREDIT_HOURS:
                flash(f'Total credit hours ({total_credit_hours}) exceed the limit of {MAX_CREDIT_HOURS}. Registration failed!', 'danger')
                return redirect('/register_course')

            # Start a transaction
            try:
                for course_id in selected_courses:
                    # Check if the student is already registered for the course
                    existing_enrollment = Enrollment.query.filter_by(student_sno=user.sno, course_id=course_id, semester_id=session.get('semesterid1', None)).first()
                    
                    if existing_enrollment is None:
                        enrollment = Enrollment(student_sno=user.sno, course_id=course_id, semester_id=session.get('semesterid1', None))
                        db.session.add(enrollment)
                    else:
                        print(f"This enrollment already exists: {user.sno}, {course_id}")

                db.session.commit()  # Commit
                flash('You have successfully registered for the selected courses!', 'success')
                return redirect('/std_dashboard') 

            except Exception as e:
                db.session.rollback()  # Rollback 
                flash('An error occurred while registering for the courses. Please try again.', 'danger')
                return redirect('/register_course')

    else:
        flash('Registration is closed!', 'danger')
        return redirect('/std_dashboard')

    return render_template('register_course.html', user=user, courses=courses)  # Pass courses to the template

# registered courses(STUDENT) 
@app.route('/registered_courses')
def registered_courses():
    if 'user_id' not in session:
        flash("You need to log in first!", "danger")
        return redirect('/login')

    # Fetch the logged-in user
    user = Student.query.filter_by(user_id=session['user_id']).first()
    
    enrollments = (
        db.session.query(Enrollment)
        .join(Course)
        .join(Semester)
        .filter(Enrollment.student_sno == user.sno)
        .all()    )
        
    courses_by_semester = {}
    for enrollment in enrollments:
        semester_name = enrollment.semester.semester  
        course_name = enrollment.course_enrollment.CourseName  
        # courses=enrollment.course

        if semester_name not in courses_by_semester:
            courses_by_semester[semester_name] = []
        
        courses_by_semester[semester_name].append(course_name)
        g.sem_id=session.get('semesterid1', None)
        semester_name = Semester.query.filter_by(sem_id=g.sem_id).first()        
    return render_template('registered_courses.html', user=user,courses_by_semester=courses_by_semester,semname=semester_name)

# STUDENT drop semester
@app.route('/drop_course/<string:course_name>/<int:sem_id>/<int:user_sno>', methods=['GET'])
def drop_course(course_name, sem_id, user_sno):
    # Find the course ID based on the course name
    course = Course.query.filter_by(CourseName=course_name).first()
     
    # Now that we have the course_id, check if the enrollment exists
    enrollment = Enrollment.query.filter_by(semester_id=sem_id, course_id=course.C_id, student_sno=user_sno).first()
    
    if enrollment:
        db.session.delete(enrollment)
        db.session.commit()
        flash('COURSE has been dropped successfully!', 'success')
    else:
        flash('Enrollment not found!', 'error')
    
    return redirect("/registered_courses")

# (STUDENT) FOR MARKS OF SPECIFIC COURSE
@app.route('/select_course_for_marks', methods=['GET', 'POST'])
def select_course_for_marks():
    student_id = session.get('student_id2')
    semester_id = session.get('semesterid1')  

    
    if student_id is None:
        return "No student ID found in session.", 400

    if semester_id is None:
        return "No semester ID provided.", 400

    if request.method == 'POST':
        selected_course_id = request.form.get('course_id')
        #redirect to route with parameter
        return redirect(url_for('show_assessment_marks', course_id=selected_course_id))

    
    enrollments = Enrollment.query.filter_by(student_sno=student_id, semester_id=semester_id).all()

    
    if not enrollments:
        return "No enrollments found for the specified student and semester.", 404

    #1 Extract courses from enrollments instance/object
    #course_enrollment is define in enrollment class
    courses = [enrollment.course_enrollment for enrollment in enrollments]
    #courses will have instances of course class(means all attribute of course) IF WRITE course_enrollment.C_ID THE ONLY ID 

    
    if not courses:
        return "No courses found for the specified enrollments.", 404

    return render_template('select_course_for_marks.html', courses=courses)

#MArks shown (STUDENT)
@app.route('/assessment_marks/<course_id>', methods=['GET'])
def show_assessment_marks(course_id):
    student_id = session.get('student_id2')

    
    marks = Assessment.query.join(Marks).filter(Marks.student_sno == student_id, Marks.course_id == course_id).all()

    # dictionary
    marks_dict = {
        'Final': 0,
        'Midterm': 0,
        'Quiz': 0,
        'Project': 0
    }

    for mark in marks:
        if mark.assessment_type in marks_dict:
            marks_dict[mark.assessment_type] = mark.marks

    return render_template('assessment_marks.html', marks=marks_dict)

#fees
@app.route('/calculate_fees', methods=['GET'])
def calculate_fees():
    student_id = session.get('student_id2')
    semester_id = session.get('semesterid1')
    
    student = Student.query.get(student_id)    
    semester = Semester.query.get(semester_id)    
    enrollments = Enrollment.query.filter_by(student_sno=student_id, semester_id=semester_id).all()

    total_credit_hours = 0
    total_fees = 0.0
    #1 Calculate total credit hours and fees
    for enrollment in enrollments:
        course = Course.query.get(enrollment.course_id)
        if course:
            total_credit_hours += course.crdHours
            total_fees += course.crdHours * g.fees    
    return render_template('fee_challan.html', student=student, semester=semester, total_credit_hours=total_credit_hours, total_fees=total_fees, enrollments=enrollments,fee_per_credit_hour=g.fees)

#transcript
@app.route('/transcript', methods=['GET'])
def transcript():
    student_id = session.get('student_id2')

    
    enrollments = Enrollment.query.filter_by(student_sno=student_id).all()

    semester_data = {}

    #1 Loop through enrollments to gather data
    for enrollment in enrollments:
        semester_id = enrollment.semester_id #for each semester
        course = Course.query.get(enrollment.course_id)

        # Fetch all assessments for the current course,semester and student
        assessments = Assessment.query.join(Marks).filter(
            Marks.student_sno == student_id,
            Marks.course_id == enrollment.course_id
        ).all()
        #sum of ass of one course in in semester
        total_marks = sum(assessment.marks for assessment in assessments)  
        #if first course of that semester so initialize semester_data
        if semester_id not in semester_data:
            semester_data[semester_id] = {
                'courses': [],
                'total_marks': 0,
                'total_credit_hours': 0,
                'sgpa': 0,
                'course_count': 0  # Initialize course count
            }

        #  row is semester coloum is course  of object array having marks and other details
        semester_data[semester_id]['courses'].append({
            'course_name': course.CourseName,
            'credit_hours': course.crdHours,
            'marks': total_marks,
            'grade': calculate_grade(total_marks)  # Calculate grade based on total marks
        })
        
        # Update total marks and total credit hours for the semester
        semester_data[semester_id]['total_marks'] += total_marks
        semester_data[semester_id]['total_credit_hours'] += course.crdHours
        semester_data[semester_id]['course_count'] += 1  # Increment course count

    # Calculate SGPA and CGPA
    for semester_id, data in semester_data.items():
        if data['course_count'] > 0:
            data['sgpa'] = data['total_marks'] / data['course_count']  # Average marks per course
            data['gpa'] = calculate_gpa(data['sgpa'])  # Calculated SGPA

    # Calculate CGPA
    total_sgpa_sum = sum(data['gpa'] for data in semester_data.values() if data['course_count'] > 0)
    total_semesters = sum(1 for data in semester_data.values() if data['course_count'] > 0)
    cgpa = total_sgpa_sum / total_semesters if total_semesters > 0 else 0
    # making dictionary where keys are id and values are name of semester from all semester
    semester_names = {semester.sem_id: semester.semester for semester in Semester.query.all()}
    return render_template('transcript.html', semester_data=semester_data, cgpa=cgpa,semester_names=semester_names)

# Feedback
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    student_id = session.get('student_id2')
    semester_id = session.get('semesterid1')

    if request.method == 'POST':
        
        student = Student.query.get(student_id)
        section = student.section if student else None  

        # Process the feedback submission
        for course_id in request.form.getlist('course_id'):
            rating = request.form.get(f'rating_{course_id}')
            if rating:
                feedback_entry = Feedback(
                    student_sno=student_id,
                    course_id=course_id,
                    semester_id=semester_id,
                    rating=int(rating),
                    section=section  
                )
                db.session.add(feedback_entry)
        db.session.commit()
        flash('Feedback submitted successfully!', 'success')
        return redirect(url_for('feedback'))

    # Fetch enrolled courses for the student in the specified semester
    enrollments = Enrollment.query.filter_by(student_sno=student_id, semester_id=semester_id).all()
    courses = [Course.query.get(enrollment.course_id) for enrollment in enrollments]

    return render_template('feedback.html', courses=courses)

#STUDENT 
@app.route('/view_attendance', methods=['GET', 'POST'])
def view_attendance():
    if 'student_id2' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login'))  # Redirect to login page

    student_sno = session['student_id2']
    sem_id = session.get('registration_status', None)

    enrolled_courses = Enrollment.query.filter_by(student_sno=student_sno).all()

    # Prepare a list of course details
    courses = []
    for enrollment in enrolled_courses:
        course = Course.query.get(enrollment.course_id)
        if course:
            courses.append(course)

    # If the form is submitted, get the selected course
    if request.method == 'POST':
        course_id = request.form.get('course_id')
        # Query the attendance records for the student
        attendance_records = Attendance.query.filter_by(
            student_sno=student_sno,
            sem_id=sem_id,
            course_id=course_id
        ).all()

        # Calculate attendance percentage
        total_classes = len(attendance_records)
        present_count = sum(1 for record in attendance_records if record.status == 'Present')
        attendance_percentage = (present_count / total_classes * 100) if total_classes > 0 else 0

        return render_template('attendance_records.html', records=attendance_records, courses=courses, selected_course_id=course_id, attendance_percentage=attendance_percentage)

    return render_template('view_attendance.html', courses=courses)

#?            ///////////////////////////           FACULTY       ////////////////////

#login
@app.route('/login_faculty', methods=['POST', 'GET'])
def login_faculty():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = Faculty.query.filter_by(email=email).first()
        if not user:
            flash("User not exist", "primary")
            return render_template('login_faculty.html')  


        if user and user.check_password(password):
            session['email'] = user.email
            session['first_name'] = user.first_name
            session['faculty_id'] = user.sno 
            
            return redirect('/faculty_dashboard')  
        else:
            flash("Invalid credentials", "danger")
            return render_template('login_faculty.html')    

    return render_template('login_faculty.html') 

#LOGOUT
@app.route('/logout_faculty')
def logout_faculty():
    session.pop('first_name', None)  
    return redirect('/')  # Redirect to the login page

#FACULTY DASHBOARD
@app.route('/faculty_dashboard')   
def faculty_dashboard():
    user = Faculty.query.filter_by(email=session['email']).first() if 'email' in session else None
    return render_template('faculty_dashboard.html', user=user)  # Adjusted render

# REGISTER FACULTY
@app.route('/add_faculty', methods=['GET', 'POST'])
def add_faculty():
    if request.method == 'POST':
        first_name = request.form['first_name']        
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        address = request.form['address']
        department = request.form['department']
        password = request.form['password']   

        faculty = Faculty(
            email=email,
            password=password,   
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            gender=gender,
            address=address,
            department=department
        )

        db.session.add(faculty)
        db.session.commit()
        flash('Faculty data has been submitted successfully!', 'success')

    allFaculty = Faculty.query.all()
    return render_template('add_faculty.html', allFaculty=allFaculty)

#REGISTERED FACULTY DATA
@app.route('/faculty_data', methods=['GET'])
def faculty_data():
    allFaculty = Faculty.query.all()
    return render_template('faculty_data.html', allFaculty=allFaculty)

# Update faculty route
@app.route('/update_faculty/<int:sno>', methods=['GET', 'POST'])
def update_faculty(sno):
    faculty = Faculty.query.filter_by(sno=sno).first()
    if request.method == 'POST':
        faculty.first_name = request.form['first_name']
        faculty.last_name = request.form['last_name']
        faculty.email = request.form['email']
        faculty.phone = request.form['phone']
        faculty.gender = request.form['gender']
        faculty.address = request.form['address']
        faculty.department = request.form['department']
        faculty.password = request.form['password']   

        db.session.commit()
        flash('Faculty data has been updated successfully!', 'success')
        return redirect("/faculty_data")

    return render_template('update_faculty.html', faculty=faculty)

# Delete faculty route
@app.route('/delete_faculty/<int:sno>')
def delete_faculty(sno):
    faculty = Faculty.query.filter_by(sno=sno).first()
    db.session.delete(faculty)
    db.session.commit()
    flash('Faculty data has been deleted successfully!', 'success')
    return redirect("/faculty_data")


#FACULTY PROFILE
@app.route('/faculty_profile')
def faculty_profile():
    
    if 'faculty_id' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login'))

    faculty_sno = session['faculty_id']
    faculty = Faculty.query.get(faculty_sno)

    if not faculty:
        flash('Faculty not found.', 'danger')
        return redirect(url_for('login')) 

    return render_template('faculty_profile.html', faculty=faculty)

# SELECTING COURSE TO ASSIGN ASSIGN MARKLS
@app.route('/assign_marks', methods=['GET', 'POST'])
def assign_marks():
    if request.method == 'POST':
        
        course_id = request.form.get('course_id')
        assessment_type = request.form.get('assessment_type')

        # Redirect to the new route to enter marks WITH PARAMETERS
        return redirect(url_for('enter_marks', course_id=course_id, assessment_type=assessment_type))

    # Get the list of courses for the logged-in faculty
    if g.faculty_id is None:
        flash('You must be logged in to assign marks.', 'danger')
        return redirect(url_for('login'))  

    courses = TeacherCourse.query.filter_by(faculty_id=g.faculty_id).all()
    return render_template('assign_marks.html', courses=courses)

#faculty ENTER MARKS  for students
@app.route('/enter_marks', methods=['GET', 'POST'])
def enter_marks():
    course_id = request.args.get('course_id')
    assessment_type = request.args.get('assessment_type')#1 from parameter in assign marks route

    enrolled_students = Enrollment.query.filter_by(course_id=course_id).all()

    if request.method == 'POST':
        for student in enrolled_students:
            marks = request.form.get(f'marks_{student.student_sno}')
            if marks:
                # Create a new Marks entry
                new_marks = Marks(student_sno=student.student_sno, course_id=course_id)
                db.session.add(new_marks)
                db.session.flush()  # Flush to get the new marks ID
                
                # Create a new Assessment entry
                new_assessment = Assessment(marks_id=new_marks.id, assessment_type=assessment_type, marks=float(marks))
                db.session.add(new_assessment)

        db.session.commit()
        #flash('Marks assigned successfully!', 'success')
        return redirect(url_for('assign_marks'))  # Redirect back to the assign marks page

    return render_template('enter_marks.html', enrolled_students=enrolled_students, assessment_type=assessment_type)

#Feedback
@app.route('/average_ratings', methods=['GET'])
def average_ratings():
    faculty_id = session.get('faculty_id')
    semester_id = session.get('semesterid1')
    
    teacher_courses = TeacherCourse.query.filter_by(faculty_id=faculty_id).all()

    # Prepare a dictionary to hold average ratings
    average_ratings = {}

    for teacher_course in teacher_courses:
        course_id = teacher_course.course_id
        section = teacher_course.section

        # Query to find students in the same section for the course
        students_in_section = Student.query.filter_by(section=section).all()
        student_snos = [student.sno for student in students_in_section]#student_id

        # Query to find feedback for the course from students in the same section
        feedbacks = Feedback.query.filter(
            Feedback.course_id == course_id,
            Feedback.student_sno.in_(student_snos),
            Feedback.semester_id == semester_id
        ).all()

        # Fetch course details for html to print name also
        course = Course.query.filter_by(C_id=course_id).first()
        
        # Calculate average rating for specific course
        if feedbacks:
            average_rating = sum(feedback.rating for feedback in feedbacks) / len(feedbacks)
            average_ratings[course] = average_rating  # Store the course object as the key
        else:
            average_ratings[course] = None  

    return render_template('average_ratings.html', average_ratings=average_ratings)

#FACULTY SELECT DETAILS TO MARK ATTENDENCE
@app.route('/select_attendance', methods=['GET', 'POST'])
def select_attendance():
    if request.method == 'POST':
        sem_id = request.form.get('sem_id')
        course_id = request.form.get('course_id')
        date = request.form.get('date')

        # Redirect to the mark attendance route with selected parameters
        redirect_url = url_for('mark_attendance', sem_id=sem_id, course_id=course_id, date=date)    
        return redirect(redirect_url)
        
    # Fetch registered courses and semesters for the faculty member
    faculty_id = session.get('faculty_id')  
    teacher_courses = TeacherCourse.query.filter_by(faculty_id=faculty_id).all()
    courses = [course.course for course in teacher_courses]  # Get the Course objects with ids
    semesters = Semester.query.all()

    return render_template('select_detail_attendance.html', courses=courses, semesters=semesters)

#1 FACULTY MARK ATTENDANCE
@app.route('/mark_attendance', methods=['GET', 'POST'])
def mark_attendance():
    students = []  # Initialize students as an empty list

    if request.method == 'POST':
        sem_id = request.form.get('sem_id')
        course_id = request.form.get('course_id')
        date = request.form.get('date')

        # Get the list of enrollments for the selected course and semester
        enrollments = Enrollment.query.filter_by(semester_id=sem_id, course_id=course_id).all()

        # Fetch the student numbers from the enrollments
        student_snos = [enrollment.student_sno for enrollment in enrollments]

        # Now fetch the students based on the student_snos
        students = Student.query.filter(Student.sno.in_(student_snos)).all()

        for enrollment in enrollments:
            status = request.form.get(f'student_status_{enrollment.student_sno}')
            #adding attendence of each 
            attendance_record = Attendance(
                sem_id=sem_id,
                course_id=course_id,
                student_sno=enrollment.student_sno,
                date=date,
                status=status
            )
            db.session.add(attendance_record)

        db.session.commit()
        flash('Attendance marked successfully!', 'success')
        return redirect(url_for('select_attendance'))

    # If GET request, fetch students based on selected semester and course
    sem_id = request.args.get('sem_id')
    course_id = request.args.get('course_id')
    date = request.args.get('date')

    if sem_id and course_id and date:
        enrollments = Enrollment.query.filter_by(semester_id=sem_id, course_id=course_id).all()
        student_snos = [enrollment.student_sno for enrollment in enrollments]
        students = Student.query.filter(Student.sno.in_(student_snos)).all()

    return render_template('mark_attendance.html', students=students, sem_id=sem_id, course_id=course_id, date=date)




#           ///////////////////////        ADMIN      /////////////////////

#LOGIN
@app.route('/login_admin', methods=['POST', 'GET'])
def login_admin():
    if request.method == "POST":
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        user = Admin.query.filter_by(user_name=user_name).first()
        if not user:
            flash("User not exist", "primary")
            return render_template('login_admin.html')  


        if user and user.check_password(password):
            session['user_name'] = user.user_name
            
            
            return redirect('/admin_dashboard')  
        else:
            flash("Invalid credentials", "danger")
            return render_template('login_admin.html')    

    return render_template('login_admin.html') 

#LOGOUT
@app.route('/logout_admin')
def logout_admin():
    session.pop('user_name', None) 
    return redirect('/')  

#ADMIN HOME
@app.route('/admin_dashboard')   
def admin_dashboard():
    user = Admin.query.filter_by(user_name=session['user_name']).first() if 'email' in session else None
    return render_template('adm_home.html', user=user)  

#ADD NEW ADMIN
@app.route('/add_admin', methods=['GET', 'POST'])
def add_admin():
    if request.method == 'POST':
        user_name = request.form['user_name']                
        password = request.form['password']   
        
        admin= Admin(
            user_name=user_name,
            password=password,
            )

        db.session.add(admin)
        db.session.commit()
        
        flash('New admin has created!', 'success')

    allAdmin= Admin.query.all()
    return render_template('add_admin.html', allAdmin=allAdmin)

#SHOW ADMIN DATA
@app.route('/admin_data', methods=['GET'])
def admin_data():
    allAdmin = Admin.query.all()
    return render_template('admin_data.html', allAdmin=allAdmin)

#UPDATE admin route
@app.route('/update_admin/<int:id>', methods=['GET', 'POST'])
def update_admin(id):
    admin = Admin.query.filter_by(id=id).first()
    if request.method == 'POST':
        admin.user_name = request.form['user_name']
        admin.password = request.form['password']   

        db.session.commit()
        flash('Admin data has been updated  successfully!', 'success')
        return redirect("/admin_data")

    return render_template('update_admin.html', admin=admin)

# Delete admin route
@app.route('/delete_admin/<int:id>')
def delete_admin(id):
    admin = Admin.query.filter_by(id=id).first()
    db.session.delete(admin)
    db.session.commit()
    flash('Admin data has been deleted successfully!', 'success')
    return redirect("/admin_data")

#ADD NEW COURSE
@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        CourseName = request.form['CourseName']                
        crdHours = request.form['crdHours']   
        CourseCode = request.form['CourseCode'] 
        course= Course(
            CourseName=CourseName,
            crdHours =crdHours ,
            CourseCode=CourseCode,            
            )

        db.session.add(course)
        db.session.commit()
        
        flash('New course has created!', 'success')

    allCourse= Course.query.all()
    return render_template('add_course.html', allCourse=allCourse)

#ALL COURSES 
@app.route('/course_data', methods=['GET'])
def course_data():
    allCourse = Course.query.all()
    return render_template('course_data.html', allCourse=allCourse)

#DELETE COURSE
@app.route('/delete_course/<int:C_id>')
def delete_course(C_id):
    course = Course.query.filter_by(C_id=C_id).first()
    db.session.delete(course)
    db.session.commit()
    flash('Course data has been deleted successfully!', 'success')
    return redirect("/course_data")

#Assign COURSE TO FACULTY
@app.route('/assign_courses', methods=['GET', 'POST'])
def assign_courses():
    teachers = Faculty.query.all()  # Fetch all faculty members
    courses = Course.query.all()  # Fetch all courses

    if request.method == 'POST':
        for teacher in teachers:  # Loop through each teacher
            selected_courses = request.form.getlist(f'courses_{teacher.sno}')  # Get the selected courses for the teacher

            # Assign selected courses to the teacher
            for course_id in selected_courses:
                section = request.form.get(f'section_{course_id}_{teacher.sno}')  # Get the section for the course

                # Check if the assignment already exists
                existing_assignment = TeacherCourse.query.filter_by(faculty_id=teacher.sno, course_id=course_id).first()
                
                if not existing_assignment:  # If no existing assignment found, create a new one
                    new_assignment = TeacherCourse(faculty_id=teacher.sno, course_id=course_id, section=section)
                    db.session.add(new_assignment)

        db.session.commit()  # Commit all the new assignments at once
        flash("Courses assigned successfully!", "success")
        return redirect('/assign_courses')

    return render_template('assign_courses.html', teachers=teachers, courses=courses)



# ADMIN NEW SEMESTER REGISTRATION OPEN/CLOSE
@app.route('/close_register', methods=['GET', 'POST'])
def close_register():
    semester_options = db.session.query(Semester).all()
    
    if request.method == 'POST':
        # Get the action, semester, and fee per credit hour from the form
        action = request.form.get('action')
        semester_id = request.form.get('semester')
        fee_per_credit_hour = request.form.get('fee_pr_crd_hr')

        # Update registration status
        if action == 'open':
            session['registration_status'] = True
            g.registration = True
            flash('Registration is now open!', 'success')
        elif action == 'close':
            session['registration_status'] = False
            g.registration = False
            flash('Registration is now closed!', 'success')

        # Update semester if provided
        if semester_id:
            selected_semester = Semester.query.get(semester_id)
            if selected_semester:
                sem = Semester.query.filter_by(semester=selected_semester.semester).first()  # Use first() to get the first result

                if sem:
                    session['semesterid1'] = sem.sem_id
                    g.sem_id = sem.sem_id  # Set the sem_id globally

                flash(f'Semester set to {selected_semester.semester}!', 'success')

        # Update fee per credit hour
        if fee_per_credit_hour:
            try:
                session['fee_pr_crd_hr'] = float(fee_per_credit_hour)  # Store fee in session
                g.fees = float(fee_per_credit_hour)  # Set globally for immediate use
                flash(f'Fee per credit hour set to {fee_per_credit_hour}!', 'success')
            except ValueError:
                flash('Invalid fee value. Please enter a valid number.', 'danger')

        return redirect('/close_register')  # Redirect to the same page to show the updated status
        
    return render_template(
        'registration.html',
        registration=session.get('registration_status', None),
        semesters=semester_options,
        current_fee=session.get('fee_pr_crd_hr', None)  # Send current fee value to template
    )





if __name__ == "__main__":
    app.run(debug=True, port=8000)
