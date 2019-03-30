from flask import *
import requests, json

#Load config
config = None
with open("report_config.json") as config_file:
  config = json.load(config_file)


#Configure Flask App
app = Flask(__name__)
app.secret_key = config['secret']

#Send message to webhook
def Notification(message):
    requests.post(config['webhook'], data={'content': message})

#Testable GET page
@app.route('/service')
def debug():
    Notification("Service pinged!")
    return "Service is running!"

#Endpoint for unity requests
@app.route('/submit_issue/unity', methods=['POST'])
def unity_issue():
    Notification(json.dumps(request.get_json()))
    return "OK"