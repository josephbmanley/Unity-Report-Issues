# Report Issues for Unity Cloud Diagnostics

Zappa script that takes information from Unity Cloud Diagnostics and creates GitHub issues

## Endpoints

### `/submit_issue/unity`

Webhook endpoint for Unity Cloud Diagnostics.

### `/service`

Health check endpoint

## Configuring Environment

Configurable values:

|Value|Required|Description|
|---|---|---|
|github_token|true|GitHub API token used to create issues|
|git_user|true|Owner of the GitHub repository|
|repository|true|GitHub repository in which issues are created|
|notification_webhook|false|Discord, Slack, or other webhook endpoint|

### Config Priority

1. Environment

2. Config File

3. SSM Parameters

### Environment Variables

Environment varibles can either be set manually within the generated lambda in AWS or by placing it in the `zappa_settings` file.

Example `zappa_settings.yaml`:

```yaml
dev:
    environment_variables:
        git_user: josephbmanley
        repository: example
```

### Config File

Copy `report_config_template.json` to `report_config.json` and fill in values for your own environment.

```json
{
    "git_user" : "josephbmanley",
    "repository" : "example"
}
```

### SSM Parameters

SSM Parameters with this app use the path: `/[ZAPPA PROJECT]/[ZAPPA STAGE]/[VARIABLE]`

So in the case we want to create an encrypted parameter for our GitHub token for the `game` project in our `dev` environment, the path would be: `/game/dev/github_token`

#### Tips

It is recommended that your GitHub token is encrypted and placed here.

_**NOTE:** For any encryped SSM Parameter, you will have to update the Lambda executors IAM permissions_

## Deploying App

1. Run `zappa init` to fill out basic configuration

2. Configure Environment

3. Run `zappa deploy [env]` to deploy application to AWS

[To learn more about how to use Zappa, see their page](https://github.com/Miserlou/Zappa)


### Configuring Unity Cloud

After setting up Unity Cloud Diagnostics in your project.
Go add an intergation to your project using a webhook. Your webhook value, woud be your API endpoint `/submit_issue/unity`.

For example, if I deploy my API with the domain `test.cloudsumu.com`, the webhook value would be `test.cloudsumu.com/submit_issue/unity`