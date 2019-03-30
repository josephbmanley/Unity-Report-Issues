# Report Issues for Unity Cloud Diagnostics
![Functionality](https://img.shields.io/badge/Build-Not%20Functional-red.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/toda-studios/Report-Issues.svg)
![Discord](https://img.shields.io/discord/559845341185310724.svg)

Zappa script that takes information from Unity Cloud Diagnostics and creates GitHub issues

[Have any questions? Jump into our Discord!](https://discord.gg/UCgkKDv)

## Project Mangement

We use ZenHub which is intergrated with GitHub issues.

## Setting up environment

Make sure you have git installed and run the command:

`git clone https://github.com/josephbmanley/Report-Issues.git`

or use [GitHub Desktop](https://desktop.github.com) to manage your repository.


### Commiting and Pushing Changes

#### Create a new branch

**DO NOT DIRECTLY COMMIT TO `master` OR `develop`!**

Before you make any changes, be sure to create a new branch for your code. You can do that in the cli by running the command `git checkout -b [your new branch]`

Or go to `Branch > New Branch` on GitHub desktop.



--
#### Commit changes

_Witg Git CLI:_

1. Add the files you made changes to with `git add [filename]`. To see what files you made changes to, you can run the command `git status`.

2. Once you have added all the files you made changes to you can commit to the repository with a message. To do this use the command `git commit -m [message]`

3. Send your commits back to GitHub by running the command `git push origin` or `git push origin [branch]`

_With GitHub Desktop:_

1. To add your changes to the repository, open the GitHub window.

    `Windows > GitHub`


2. Next, go to the Changes tab and select all the files that you have made want to send.

3. Give a summary and description of the changes you made then click the commit button.

4. Then click the Push button at the top left.

#### Pull Request & Request Review

1. Go to the repository page on GitHub and go to your branch.

2. Next to the branch dropdown, click `New pull request` and fill the form

3. To request someone to review your pull request, click the cog next to `Reviewers` and select who you would like to request to review your changes.

4. Click the merge button once your request is approved.

5. Congratulations, you've successfully contributed your code!

### Pulling Changes
To pull changes from the repository, open the GitHub window.

`Windows > GitHub`

Make sure you are logged in, then click the pull button at the top left.

## Configure Environment

### Report Issues Config

Copy `report_config_template.json` to `report_config.json` and fill in values for your own environment.

### Zappa Config and Deployment

Run `zappa init` to fill out basic configuration

Run `zappa deploy [env]` to deploy application to AWS

[To learn more about how to use Zappa, see their page](https://github.com/Miserlou/Zappa)