from crypt import methods

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:anuj2006@localhost/todo_list'
app.secret_key = "mahi@1234"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    password = db.Column(db.String(200),nullable=False)
    tasks = db.relationship('Task',backref='user',lazy=True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    # Define the __init__ method
    def __init__(self, task, user_id, done=False):
        self.task = task
        self.user_id = user_id
        self.done = done

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session["user_id"]
    tasks = Task.query.filter_by(user_id=user_id).all()
    return render_template(
        "index.html",tasks=tasks)

@app.route('/add',methods=["POST"])
def add_task():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    task_content = request.form.get('task')
    user_id = session['user_id']
    new_task = Task(task = task_content,user_id=user_id)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    task = Task.query.get(task_id)
    if task and task.user_id == session["user_id"]:
        task.done = not task.done
        db.session.commit()
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    task = Task.query.get(task_id)
    if task and task.user_id == session["user_id"]:
        db.session.delete(task)
        db.session.commit()
    return redirect('/')


@app.route('/register',methods=["GET","POST"])
def register():
    if request.method=="POST":
        username = request.form['username']
        password = generate_password_hash(request.form['password'],method='pbkdf2:sha256')
        if User.query.filter_by(username=username).first():
            return "Username already Exists"
        new_user = User(username=username,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password,password):
            session['user_id'] = user.id
            return redirect('/')
        return "Invalid Credentials"
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    with app.app_context():  # Ensure the app context is active
        db.create_all()  # Create tables
    app.run(debug=True)
