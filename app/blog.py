import os
import frontmatter
import glob
import markdown
from datetime import datetime

# Blog configuration
POSTS_DIR = os.path.join(os.path.dirname(__file__), '..', '_posts')
PROJECTS_DIR = os.path.join(os.path.dirname(__file__), '..', '_projects')

def get_posts():
    """Get all blog posts, sorted by date."""
    posts = []
    for filepath in glob.glob(os.path.join(POSTS_DIR, '*.md')):
        with open(filepath, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            post.slug = os.path.splitext(os.path.basename(filepath))[0]
            # frontmatter stores metadata in .metadata dict
            post.date = post.metadata.get('date', datetime.now())
            post.date_formatted = post.date.strftime('%B %d, %Y')
            # Convert Markdown to HTML
            post.content = markdown.markdown(post.content)
            posts.append(post)
    return sorted(posts, key=lambda p: p.date, reverse=True)

def get_post(slug):
    """Get a single blog post by slug."""
    filepath = os.path.join(POSTS_DIR, f'{slug}.md')
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
        post.slug = slug
        post.date = post.metadata.get('date', datetime.now())
        post.date_formatted = post.date.strftime('%B %d, %Y')
        # Convert Markdown to HTML
        post.content = markdown.markdown(post.content)
        return post

def get_projects():
    """Get all projects."""
    projects = []
    for filepath in glob.glob(os.path.join(PROJECTS_DIR, '*.md')):
        with open(filepath, 'r', encoding='utf-8') as f:
            project = frontmatter.load(f)
            project.slug = os.path.splitext(os.path.basename(filepath))[0]
            project.date = project.metadata.get('date', datetime.now())
            project.date_formatted = project.date.strftime('%B %Y') if project.date else ''
            # Convert Markdown to HTML
            project.content = markdown.markdown(project.content)
            projects.append(project)
    return sorted(projects, key=lambda p: p.date, reverse=True) if projects else projects

def get_project(slug):
    """Get a single project by slug."""
    filepath = os.path.join(PROJECTS_DIR, f'{slug}.md')
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        project = frontmatter.load(f)
        project.slug = slug
        project.date = project.metadata.get('date', datetime.now())
        project.date_formatted = project.date.strftime('%B %Y') if project.date else ''
        # Convert Markdown to HTML
        project.content = markdown.markdown(project.content)
        return project
