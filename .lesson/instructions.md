Html koden ska klistras in i filen project_manager.html i mappen templates. Skapa filen om det inte finns i mappen.

```html
  {% extends "cms.html" %}
  <!-- Project Manager -->
  {% block content %}
  <div class="container">
    <div class="row justify-content-center mt-4">
      <div class="col-12 col-md-8 col-lg-6">
        <h3 class="display-4 mb-4 text-center">Project Manager</h3>
        <form id="project_form" onsubmit="createProject(event)">
          <div class="mb-3">
            <label for="name" class="form-label">Project Name:</label>
            <input type="text" id="name" name="name" class="form-control" required />
          </div>
          <div class="mb-3">
            <label for="description" class="form-label">Description:</label>
            <textarea id="description" name="description" class="form-control" rows="4" required></textarea>
          </div>
          <div class="text-center">
            <button type="submit" class="btn btn-primary">Add Project</button>
          </div>
        </form>
        <hr />
      </div>
    </div>
  </div>
  <script src="{{ url_for('static', filename='form_handler.js') }}"></script>
  {% endblock %}
  
```

Javascript koden ska klistras in i filen `form_handler.js` som ska ligga i mappen `static`. Skapa filen om det inte finns i mappen. Skapa mappen om det inte heller finns 

```javascript
async function createProject(event) {
    event.preventDefault();

    const formData = {
        name: document.getElementById('name').value,
        description: document.getElementById('description').value
    };

    try {
        const response = await fetch('/projects', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            throw new Error(`HTTP Error Status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Project Created:', data);
    } catch (error) {
        console.error('Error:', error);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('projectForm');
    form.addEventListener('submit', createProject);
});



```