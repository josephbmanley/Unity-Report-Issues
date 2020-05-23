import boto3
from botocore.exceptions import ClientError
import json, os, os.path

ssm = boto3.client('ssm')

class Config:
    def __init__(self):

        # Load config file into memory
        config_file_name = "report_config.json"
        if os.path.isfile(config_file_name)
        with open(config_file_name) as config_file:
            self.config_file = json.load(config_file)

    def get(key, default_val=None, SsmDecryption = False):
        # Check environment variables
        if key in os.environ:
            return os.environ[key]
        # Else check config file
        elif key in self.config_file:
            return self.config_file[key]
        # Else check SSM
        else:
            try:
                # Request parameter /[PROJECT]/[STAGE]/key
                resp = ssm.get_parameter(Name="/" + os.environ['PROJECT'] +
                    "/" + os.environ['STAGE'] + "/" + key, WithDecryption = SsmDecryption)

                if 'Parameter' in resp:
                    if 'Value' in resp['Parameter']:
                        return resp['Parameter']['Value']
            except ClientError as e:
                if e.response['Error']['Code'] == "SSM.Client.exceptions.ParameterNotFound":
                    print("Could not find parameter with key: " + key)
                else:
                    raise e
        # Nothing is found
        return default_val