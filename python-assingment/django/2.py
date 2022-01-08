{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django Base Template</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
   
    <nav>
     <a href="{% url 'index' %}">Home</a>
    <a href="{% url 'about' %}">About</a>
    <a href="{% url 'skills' %}">Skill</a>
    <a href="{% url 'contact' %}">Contact</a>
    </nav>
    <h1>About page </h1>
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>