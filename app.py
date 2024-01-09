from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.get('/')
def home():
  return render_template("home.html")


@app.get('/projects')
def display_projects():
  return render_template("projects.html")


@app.post('/cms/project/add')
def add_project():
  title = request.form.get('name', 'not found')
  description = request.form.get('description', 'not found')
  print(title)
  print(description)
  return redirect(url_for('project_manager'))


@app.get('/cms')
def cms():
  return render_template("cms.html")


@app.get('/cms/project_manager')
def project_manager():
  return render_template("project_manager.html")


# @app.get('/contact')
# def contact():
#   return render_template("contact.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81, debug=True)
