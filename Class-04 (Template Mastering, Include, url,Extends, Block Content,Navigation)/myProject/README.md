# Class 04
<details>
<summary><b>Template Mastering, Include, url,Extends, Block Content,Navigation</b></summary>


#### 1. Creating HTML Templates

- **Create HTML Pages**: Start by creating HTML pages (`master.html` and `Home.html` etc) within the `template` directory of my Django project.

#### 2. Define Views

- **Define View Functions**: In my project's `views.py`, define view functions to render these HTML templates.

   ```python
   # views.py
   
   from django.shortcuts import render,redirect,HttpResponse


    def home(request):
        return render(request, 'index.html',tableDict)

    def about(request):
        return render(request, 'about.html')

    def news(request):
        return render(request, 'news.html')

    def contact(request):
        return render(request, 'contact.html')
   ```

#### 3. URL Mapping

- **URL Configuration**: Map these view functions to URLs in `urls.py` of my project.

   ```python
   # urls.py
   
   from django.urls import path
   from myProject.views import *
   
   urlpatterns = [
        path('admin/', admin.site.urls),
        path('Home',Home,name="Home"),
        path('News',News,name="News"),
        path('Contact',Contact,name="Contact"),
        
   ]
   ```

#### 4. Creating a Navbar

- **HTML Navbar**: Implement a navbar in a separate HTML file (`navigator.html`). This file will be included in other templates.

   ```html
   <!-- navbar.html -->
   <ul>
    <a class="active" href="{% url 'homePage' %}">Home</a>
    <a href="{% url 'newsPage' %}">News</a>
    <a href="{% url 'contactPage' %}">Contact</a>
    <li style="float:right"><a class="active" href="{% url 'About' %}">About</a></li>
  </ul>
  
   ```

   - Use `{% url 'name' %}` to dynamically generate URLs.
  

#### 5. Including Navbar in Templates

- **Include Navbar**: Include the navbar in `master.html` using Django's `{% include %}` tag.

   ```html
   <!-- master.html -->
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Home</title>
   </head>
   <body>
       {% include 'navbar.html' %}
   </body>
   </html>
   ```

#### 6. Extending Templates

- **Template Inheritance**: Extend `master.html` in `index.html` to maintain consistent structure and styles.

   ```html
   <!-- index.html -->
   {% extends "master.html" %} 
    {% block content %}

    <h1>This is Home Page</h1>

    {% endblock content %}
   ```

   - `{% block content %}` allows you to override content specific to each page while keeping the overall structure from `master.html`.

### Note

This step-by-step guide helps you implement navigation using a navbar and master template structure using include and extend techniques in Django. Ensure consistency in naming conventions, HTML structure, and Django template tags for smooth navigation and efficient template management.

</details>