#!/usr/bin/env python
# coding: utf-8

# In[39]:


# index.html (Introduction page)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Documentation - Introduction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
        }
        #sidebar {
            width: 250px;
            background-color: #f8f9fa;
            padding: 15px;
            height: 100vh;
            box-shadow: 2px 0px 5px rgba(0, 0, 0, 0.1);
        }
        #sidebar ul {
            list-style-type: none;
            padding: 0;
        }
        #sidebar ul li {
            padding: 10px 0;
        }
        #sidebar ul li a {
            text-decoration: none;
            color: #007bff;
        }
        #sidebar ul li a:hover {
            text-decoration: underline;
        }
        #main-content {
            flex-grow: 1;
            padding: 20px;
        }
        h1, h2 {
            color: #333;
        }
    </style>
</head>
<body>
    <div id="sidebar">
        <h2>Documentation</h2>
        <ul>
            <li><a href="index.html">Introduction</a></li>
            <li><a href="getting_started.html">Getting Started</a></li>
            <li><a href="features.html">Features</a></li>
            <li><a href="installation.html">Installation</a></li>
        </ul>
    </div>
    <div id="main-content">
        <h1>Introduction</h1>
        <p>slay.</p>
    </div>
</body>
</html>
"""

# Write this HTML content to a file
with open("index.html", "w") as file:
    file.write(html_content)


# In[40]:


# getting_started.html (Getting Started page)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Documentation - Getting Started</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
        }
        #sidebar {
            width: 250px;
            background-color: #f8f9fa;
            padding: 15px;
            height: 100vh;
            box-shadow: 2px 0px 5px rgba(0, 0, 0, 0.1);
        }
        #sidebar ul {
            list-style-type: none;
            padding: 0;
        }
        #sidebar ul li {
            padding: 10px 0;
        }
        #sidebar ul li a {
            text-decoration: none;
            color: #007bff;
        }
        #sidebar ul li a:hover {
            text-decoration: underline;
        }
        #main-content {
            flex-grow: 1;
            padding: 20px;
        }
        h1, h2 {
            color: #333;
        }
    </style>
</head>
<body>
    <div id="sidebar">
        <h2>Documentation</h2>
        <ul>
            <li><a href="index.html">Introduction</a></li>
            <li><a href="getting_started.html">Getting Started</a></li>
            <li><a href="features.html">Features</a></li>
            <li><a href="installation.html">Installation</a></li>
        </ul>
    </div>
    <div id="main-content">
        <h1>Getting Started</h1>
        <p>absolute slay</p>
    </div>
</body>
</html>
"""

# Write this HTML content to a file
with open("getting_started.html", "w") as file:
    file.write(html_content)


# In[41]:


# features.html (Features page)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Documentation - Features</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
        }
        #sidebar {
            width: 250px;
            background-color: #f8f9fa;
            padding: 15px;
            height: 100vh;
            box-shadow: 2px 0px 5px rgba(0, 0, 0, 0.1);
        }
        #sidebar ul {
            list-style-type: none;
            padding: 0;
        }
        #sidebar ul li {
            padding: 10px 0;
        }
        #sidebar ul li a {
            text-decoration: none;
            color: #007bff;
        }
        #sidebar ul li a:hover {
            text-decoration: underline;
        }
        #main-content {
            flex-grow: 1;
            padding: 20px;
        }
        h1, h2 {
            color: #333;
        }
    </style>
</head>
<body>
    <div id="sidebar">
        <h2>Documentation</h2>
        <ul>
            <li><a href="index.html">Introduction</a></li>
            <li><a href="getting_started.html">Getting Started</a></li>
            <li><a href="features.html">Features</a></li>
            <li><a href="installation.html">Installation</a></li>
        </ul>
    </div>
    <div id="main-content">
        <h1>Features</h1>
        <p>wowi</p>
    </div>
</body>
</html>
"""

# Write this HTML content to a file
with open("features.html", "w") as file:
    file.write(html_content)


# In[42]:


# installation.html (Installation page)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Documentation - Installation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
        }
        #sidebar {
            width: 250px;
            background-color: #f8f9fa;
            padding: 15px;
            height: 100vh;
            box-shadow: 2px 0px 5px rgba(0, 0, 0, 0.1);
        }
        #sidebar ul {
            list-style-type: none;
            padding: 0;
        }
        #sidebar ul li {
            padding: 10px 0;
        }
        #sidebar ul li a {
            text-decoration: none;
            color: #007bff;
        }
        #sidebar ul li a:hover {
            text-decoration: underline;
        }
        #main-content {
            flex-grow: 1;
            padding: 20px;
        }
        h1, h2 {
            color: #333;
        }
    </style>
</head>
<body>
    <div id="sidebar">
        <h2>Documentation</h2>
        <ul>
            <li><a href="index.html">Introduction</a></li>
            <li><a href="getting_started.html">Getting Started</a></li>
            <li><a href="features.html">Features</a></li>
            <li><a href="installation.html">Installation</a></li>
        </ul>
    </div>
    <div id="main-content">
        <h1>Installation</h1>
        <p>wowi^2</p>
    </div>
</body>
</html>
"""

# Write this HTML content to a file
with open("installation.html", "w") as file:
    file.write(html_content)


# In[43]:


import webbrowser
import os

# Open the index.html file in the default web browser
webbrowser.open("file://" + os.path.realpath("index.html"))


# In[ ]:




