from flask import Flask, render_template, request, url_for, redirect, flash
from app import app
from flask_login import login_required, current_user, logout_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import RegistrationForm, LoginForm, PostForm
from .models import User, db, Post
from datetime import datetime
from .utils import search_location, show_images, location_description


# IF SOME OF THESE DONT REDIRECT, TRY REMOVING  IN FRONT OF THE URL DESTINATION


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





@app.route('/')
@app.route('/posts')
def feed():
    posts = Post.query.order_by(Post.date_created.desc()).all()
    return render_template('feed.html', posts=posts)

@app.route('/posts/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():  # This method checks if it is a POST request and if the form is valid.
        title = form.title.data
        img_url = form.img_url.data
        description = form.description.data

        # Assuming Post() takes title, img_url, description, and user_id as arguments
        post = Post(title=title, img_url=img_url, description=description, user_id=current_user.id)

        db.session.add(post)
        db.session.commit()
        flash('You have added a new destination!', 'success')
        # Redirect to a function that shows the individual post, ensure that this function exists and is defined correctly
        return redirect(url_for('individual_post_page', post_id=post.id))
    
    # The return statement here is for a GET request and also acts as a fallback if form validation fails.
    return render_template('create-post.html', form=form)

   

# This route shows individual posts created by users   
@app.route('/posts/<post_id>')
def individual_post_page(post_id):
    post = Post.query.get(post_id)
    print(post.user.username)
    return render_template('individual-post.html', p=post)   
    
    




# Route for Editing a post
@app.route('/posts/update/<int:post_id>', methods=["GET", "POST"])
@login_required
def update_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        flash('That post does not exist', 'danger')
        return redirect(url_for('feed'))
    if current_user.id != post.user_id:
        flash('You cannot edit another user\'s posts', 'danger')
        return redirect(url_for('individual_post_page', post_id=post_id))
    form = PostForm()
    if request.method == "POST":
        if form.validate():
            title = form.title.data
            img_url = form.img_url.data
            description = form.description.data

            post.title = title
            post.img_url = img_url
            post.description = description
            post.last_updated = datetime.utcnow()

            db.session.commit()
            flash('Successfully updated your post.', 'success')
            return redirect(url_for('individual_post_page', post_id=post_id))
    return render_template('update-post.html', p=post, form = form)





@app.route('/posts/delete/<post_id>', methods=["GET"])
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        flash('This post does not exist', 'danger')
        return redirect(url_for('feed'))
    if current_user.id != post.user_id:
        flash('You cannot delete another user\'s posts', 'danger')
        return redirect(url_for('app.individual_post_page', post_id=post_id))
    
    db.session.delete(post)
    db.session.commit()
    flash('Successfully deleted your post', 'success')
    return redirect(url_for('feed'))



@app.route('/search', methods=['GET', 'POST'])
def search_results():
    if request.method == 'POST':
        location = request.form.get('location')
        if location:
            search_results = search_location(location)
            if 'data' in search_results:
                combined_results = []
                for item in search_results['data']:
                    location_id = item.get('location_id')
                    images = show_images(location_id)
                    description = location_description(location_id)
                    # Check if 'data' key exists in images response and description is not None
                    if 'data' in images and description:
                        image_url = images['data'][0]['images']['large']['url'] if 'data' in images and images['data'] else None
                        combined_data = {
                            'name': item.get('name'),
                            'address': item['address_obj']['address_string'],
                            'description': description,
                            'image_url': image_url
                        }
                        combined_results.append(combined_data)
                return render_template('search_results.html', results=combined_results)
            else:
                flash('No results found or an error occurred.', 'danger')
        else:
            flash('Please enter a location to search for.', 'warning')
        return redirect(url_for('search'))
    return render_template('search.html')










