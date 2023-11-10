from flask import Flask, render_template, request, url_for, redirect, flash
from app import app
from flask_login import login_required, current_user, logout_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import RegistrationForm, LoginForm
from .models import User, db

@app.route('/')
def home():
  return render_template('index.html')

#Registration Route
@app.route('/register', methods=['GET','POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  
  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = generate_password_hash(form.password.data)
    user = User(username = form.username.data, password= hashed_password)
    db.session.add(user)
    db.session.commit()
    flash('Good Job Creating Your Account', 'success')
    return redirect(url_for('login'))
  return render_template('register.html', form=form)

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if request.method == 'POST':
      if form.validate_on_submit():
          user = User.query.filter_by(username=form.username.data).first()
          if user and check_password_hash(user.password, form.password.data):
              
              login_user(user, remember=False)
              return redirect(url_for('home'))
          else: 
             flash('Invalid Cridentials', 'danger')
      else:
              flash('Login unsuccessful. Please check your username and password.', 'danger')
    return render_template('login.html', form=form)


# Route for logging out
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



# Route for Creating a post

    




# Route for Editing a post





# Route for Deleting a Post




# Route for Reading others Posts