# Report Issues for Unity Cloud Diagnostics

Zappa script that takes information from Unity Cloud Diagnostics and creates GitHub issues

## Configure Environment

### Report Issues Config

Copy `report_config_template.json` to `report_config.json` and fill in values for your own environment.

### Zappa Config and Deployment

Run `zappa init` to fill out basic configuration

Run `zappa deploy [env]` to deploy application to AWS

[To learn more about how to use Zappa, see their page](https://github.com/Miserlou/Zappa)