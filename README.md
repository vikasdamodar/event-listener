# Email Events
Get email events from mandrill and display in a template using django websockets

# Requirements
- Project added with Django
- Redis cache server
- install requirements.txt

# Quick Start
 - Run Migrations
 
        python manage.py migrate
 - Run project
 
        python manage.py runserver
 
 # App Details
 
 - webhook URL: <domain_name>:PORT/webhook/
 
        Eg: http://localhost:8000/webhook/
 - Add the webhook URL to mandrill events/ any app webhook URL list. Please not that only POST requests will be accepted.
 - Websocket template URL: <domain_name>:PORT//ws/
 
        Eg: http://localhost:8000/ws/
 - The template have js script which will get the data from websocket BE and displays it. 
 - The websocket URL: ws://<domain_name>:PORT/ws/data/
 
        ws://localhost:8000/ws/data/
