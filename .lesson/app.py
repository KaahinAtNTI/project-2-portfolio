from flask import Flask, jsonify, render_template, request
from slugify import slugify

app = Flask(__name__)


# Utilities
def generate_project_slug(data):
  name = data.get("name")
  slug = slugify(name)
  count = 1
  unique_slug = slug
  while unique_slug in projects:
    unique_slug = f"{slug}-{count}"
    count += 1
  return unique_slug


# Projects Container
projects = {}

# CMS


@app.get('/cms')
def cms():
  return render_template("cms/cms.html")


@app.get('/cms/project_manager')
def project_manager():
  return render_template("cms/project_manager.html")


# 3.1 - Create
@app.post('/projects')
def create_project():
  data = request.json
  project_slug = generate_project_slug(data)
  projects[project_slug] = data
  return jsonify({project_slug: projects[project_slug]}), 201


# Portfolio
@app.get('/')
def home():
  return render_template("portfolio/home.html")


@app.get('/projects')
def display_projects():
  print(projects)
  return render_template("portfolio/projects.html", projects=projects)


@app.post("/projects/<string:project_slug>")
def show_project(project_slug):
  project = projects.get(project_slug)
  if project is None:
    return "Project not found", 404
  return render_template("portfolio/view_project.html", project=project)


@app.get('/contact')
def contact():
  return render_template("portfolio/contact.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81, debug=True)
