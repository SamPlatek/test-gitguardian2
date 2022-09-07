import requests
from requests.auth import HTTPDigestAuth
import base64

import boto3
import os



name = 'TestDevopsGitGuardian'

access_key1 = 'ABIAZWJRDCYYKG7INEEW'
access_key2 = 'ASIAZWJRDCYJGA6INEEW'



sec_access_key1 = 'hjshnk5ex5u34565d4654HJKGjhz545d89sjkjak'
cli_tok = 'FwoGZXIvYXdzEBAaDLHxhjed4A6ABQplMyKBAd0Jzohb7hRtcvWvjWSNw5bVcn5al0jGu9Cl7W2ijDztOnmLZICjbsFBYgO7mt2J1AM9CO0nrL9qBatm9'

slack_webhook = os.environ.get('SLACK_WEBHOOK_URL', 'hooks.slack.com/services/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')

boto3_session = boto3.Session(
  aws_access_key_id = access_key1,
  aws_secret_access_key = sec_access_key1,
  aws_session_token = cli_tok
)

