#!/usr/bin/env python
# coding: utf-8

# # question 01
Q1. Explain GET and POST methods.
GET and POST are HTTP methods that are used to send requests and receive responses between a client and server.

GET method:

The GET method is used to request data from a server, and is the most common HTTP method.
When a client sends a GET request, it includes any parameters or data in the URL itself.
This means that GET requests are visible to the user and can be bookmarked, making them useful for sharing and linking to specific pages or resources.
GET requests are also idempotent, meaning that they can be repeated without causing any side effects on the server.
POST method:

The POST method is used to submit data to a server, typically through an HTML form.
When a client sends a POST request, it includes any parameters or data in the body of the request.
This means that POST requests are not visible to the user and cannot be bookmarked.
POST requests are also not idempotent, meaning that they can have side effects on the server (e.g., updating a database or creating a new resource).
In summary, GET requests are used to retrieve data, while POST requests are used to submit data. GET requests are visible to the user and can be bookmarked, while POST requests are not visible and cannot be bookmarked. GET requests are idempotent, while POST requests are not.
# # question 02
hy is request used in Flask?

In Flask, the request object is used to access incoming request data, such as form data or query parameters, in a Flask view function.

When a client sends a request to a Flask application, the Flask server creates a request object to represent that request. The request object contains information about the request, such as the HTTP method (e.g., GET, POST), request headers, URL parameters, and form data.

The request object can be accessed from within a Flask view function using the request global variable. For example, to access form data submitted in a POST request, you can use request.form.

Here's an example of using the request object to access form data in a Flask view function:
# In[1]:


from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # process login data
        return f'Logged in as {username}'
    else:
        return '''
            <form method="post">
                <input type="text" name="username">
                <input type="password" name="password">
                <input type="submit" value="Log In">
            </form>
        '''


# # question 03
Why is redirect() used in Flask?
In Flask, the redirect() function is used to redirect the user to a different URL. This can be useful in a variety of scenarios, such as after a successful form submission or when a user attempts to access a restricted page without being logged in.

The redirect() function works by sending a response to the client with a new location specified in the Location header. When the client receives this response, it will automatically make a new request to the specified URL.

Here's an example of how redirect() might be used in a Flask application:
# In[2]:


from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # Redirect to the login page
    return redirect(url_for('login'))

@app.route('/login')
def login():
    # Render the login page
    return 'This is the login page'


# # question 04
What are templates in Flask? Why is the render_template() function used?
In Flask, templates are files that contain the HTML and other content that is used to generate dynamic web pages. Templates can include placeholders for data that will be filled in at runtime, as well as logic to control the flow of the page.

The render_template() function in Flask is used to render a template file and generate an HTML response that can be sent back to the client. This function takes the name of the template file as its first argument, and any additional arguments that should be passed to the template as keyword arguments.

Here's an example of how render_template() might be used in a Flask application:
# In[3]:


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render the template named 'index.html' and pass in the title variable
    return render_template('index.html', title='Home Page')


# # question 05
Create a simple API. Use Postman to test it. Attach the screenshot of the output in the Jupyter Notebook.
As an AI language model, I cannot directly attach a screenshot in Jupyter Notebook. However, I can provide you with the code for creating a simple API and testing it using Postman.

To create a simple API in Flask, we can use the Flask class and the @app.route() decorator to define the API endpoints. Here's an example:
# In[4]:


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, world!'})

@app.route('/api/add', methods=['POST'])
def add():
    data = request.get_json()
    if 'a' in data and 'b' in data:
        result = data['a'] + data['b']
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Invalid data'})


# In[ ]:




