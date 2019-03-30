from flask import *
from github import Github
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
@app.route('/submit_issue/unity/<repository>', methods=['POST'])
def unity_issue(repository):
    intial_report = request.get_json()

    #Create GitHub client
    g = Github(config['github_token'])

    #Create issue
    repo = g.get_repo(config['git_user'] + "/" + repository)
    issue = repo.create_issue(title=intial_report['Summary'])

    Notification("Issue created: " + issue.html_url)
    
    return "OK"