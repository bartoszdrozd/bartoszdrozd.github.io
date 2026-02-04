from flask import Flask, render_template, abort, url_for
from app import app
from app.blog import get_posts, get_post, get_projects, get_project

# Existing routes...
@app.route('/')
def home():
    posts = get_posts()[:3]
    projects = get_projects()[:3]
    return render_template('home.html', posts=posts, projects=projects)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/my-projects/')
def portfolio():
    return render_template('my-projects.html')

@app.route('/my-resume/')
def resume():
    return render_template('my-resume.html')

@app.route('/my-trips/')
def trips():
    return render_template('my-trips.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

# Blog routes
@app.route('/blog/')
def blog():
    posts = get_posts()
    return render_template('blog.html', posts=posts)

@app.route('/blog/<slug>/')
def blog_post(slug):
    post = get_post(slug)
    if not post:
        abort(404)
    return render_template('post.html', post=post)

# Projects routes
@app.route('/projects/')
def projects():
    projects_list = get_projects()
    return render_template('projects.html', projects=projects_list)

@app.route('/projects/<slug>/')
def project_detail(slug):
    project = get_project(slug)
    if not project:
        abort(404)
    return render_template('project.html', project=project)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
