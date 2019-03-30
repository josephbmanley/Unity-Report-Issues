from flask import *
from github import Github
import requests, json, boto3

#Load config
config = None
with open("report_config.json") as config_file:
  config = json.load(config_file)


#Configure Flask App
app = Flask(__name__)
app.secret_key = config['secret']


#Manage Secret
def GetSecret():
    client = boto3.client('secretsmanager')
    key = config['key-name']
    describe = client.describe_secret(SecretId=key)
    if "ARN" in response:
        return client.get_secret_value(SecretId=key)['SecretString']
    else:
        print("Generating Secret...")
        secret = response = client.get_random_password()
        response = client.create_secret(Name=key, SecretString=secret)
        return secret


#Send message to webhook
def Notification(message):
    requests.post(config['webhook'], data={'content': message})

#Testable GET page
@app.route('/service')
def debug():
    return "Service is running!"

#Endpoint for unity requests
@app.route('/submit_issue/unity/<repository>', methods=['POST'])
def unity_issue(repository):
    intial_report = request.get_json()  
    print("Report recieved...")
    if "Token: " + GetSecret() in request.headers.get("Authorization"):
        print("Authorized succesfully!")
        #Create GitHub client
        g = Github(config['github_token'])

        #Create issue
        repo = g.get_repo(config['git_user'] + "/" + repository)
        issue = repo.create_issue(title=intial_report['Summary'])

        Notification("Issue created: " + issue.html_url)
        
        return "OK"
    else:
        print("BAD AUTH: " + request.headers.get("Authorization"))
        abort(403)