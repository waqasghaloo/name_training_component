import configparser
import boto3
# Read the configuration file
config = configparser.ConfigParser()
# config = configparser.configparser()
config.read('projects/name_training_component/config.ini')

# Get the AWS credentials
access_key = config['AWS']['access_key']
secret_key = config['AWS']['secret_key']

# Use the credentials to create an S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)
