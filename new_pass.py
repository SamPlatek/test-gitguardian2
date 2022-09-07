import requests
from requests.auth import HTTPDigestAuth
import base64

import boto3
import os



name = 'TestDevopsGitGuardian'

access_key1 = 'AKIAX52MPYOTPRUCRC22'



sec_access_key1 = 'S0ugN5wv2mBHr+i7AN7rTrg6Aa6b4l5V0xDIfn2S'
cli_tok = 'IQoJb3JpZ2luX2VjEGoaCXVzLWVhc3QtMSJHMEUCIQCqb7eWWtTBAzf8XkcSeEWwlgu4rsfypWV4HFx4zyiiDQIgDSU8p29rr'


boto3_session = boto3.Session(
  aws_access_key_id = access_key1,
  aws_secret_access_key = sec_access_key1,
  aws_session_token = cli_tok
)

