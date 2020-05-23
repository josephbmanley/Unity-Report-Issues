from flask import Flask, request
from github import Github
import config_manager
import requests

#Load config
config = config_manager.Config()


#Configure Flask App
app = Flask(__name__)
app.secret_key = config.get('secret', 'default_secret')

#Send message to webhook
def Notification(message):
    webhook = config.get('notification_webhook')
    if webhook:
        requests.post(webhook, data={'content': message})

# Healthcheck endpoint
@app.route('/service')
def debug():
    return "Service is running!"

#Endpoint for unity requests
@app.route('/submit_issue/unity', methods=['POST'])
def unity_issue():
    intial_report = request.get_json()
    repository = config.get('repository')

    #Create GitHub client
    g = Github(config.get('github_token', None, True))

    #Create issue
    repo = g.get_repo(config.get('git_user') + "/" + repository)
    issue = repo.create_issue(title=intial_report['Summary'])

    Notification("Issue created: " + issue.html_url)
    
    return "OK"