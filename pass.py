import requests
from requests.auth import HTTPDigestAuth
import base64

import boto3



name = 'TestDevopsGitGuardian'

access_key1 = 'ABIAX52MPYOTPRUCRC22'

sec_access_key1 = 'hjshnk5ex5u34565d4654HJKGjhz545d89sjkjak'



boto3_session = boto3.Session(
  aws_access_key_id = access_key1,
  aws_secret_access_key = sec_access_key1,
)