import requests
from requests.auth import HTTPDigestAuth
import base64

import boto3



name = 'TestDevopsGitGuardian'

access_key1 = 'ASIA2EHZ5M7JX3GAEO5M'

sec_access_key1 = '3GQ1oJBt0UnfTEt1R/o6i4xVcWl7y6VLtH6FC3HB'
cli_tok = 'IQoJb3JpZ2luX2VjEGoaCXVzLWVhc3QtMSJHMEUCIQCqb7eWWtTBAzf8XkcSeEWwlgu4rsfypWV4HFx4zyiiDQIgDSU8p29rr'



boto3_session = boto3.Session(
  aws_access_key_id = access_key1,
  aws_secret_access_key = sec_access_key1,
  aws_session_token = cli_tok
)

