# DCG_PYTHON_TEST
Repo with working code of DCG python test 
There are **2 Types of views** 

 - A Django classed based views more inclined towards Django jinja templating 
 - DRF based viewset which is more inclined towards REST API to be consumed by react or similar endpoint consumers 

# How to run the project 

 - create a virtualenv and activate it 
 - pip3 install -r requirements.txt 
 - python3 manage.py migrate 
 - python3 manage.py runserver

# API Endpoints 

 - create a client : http://localhost:8000/add-client/
 - edit a client : http://localhost:8000/edit-client/1/   (1 is primary key (id) )
 - list client : http://localhost:8000/list-client/
 - search client: http://localhost:8000/list-client/?search=search_text
 - order client: http://localhost:8000/list-client/?order=name
 - REST API : http://localhost:8000/api/client/


# Disclaimer 
I have not used any frontend frameworks like bootstrap etc .
It's plain html just to show that the functionality works. 

# Images of working example 
https://drive.google.com/drive/folders/13a1RjJDwIz7vxOsyy0xu44g4Q5w7L0-s?usp=sharing

