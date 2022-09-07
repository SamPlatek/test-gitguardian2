import requests
from requests.auth import HTTPDigestAuth
import base64

import boto3
import os



name = 'TestDevopsGitGuardian'

access_key1 = 'ABIAZWJRDCYYKG7INEEW'
access_key2 = 'ASIAZWJRDCYJGA6INEEW'



sec_access_key1 = 'hjshnk5ex5u34565d4654HJKGjhz545d89sjkjak'
cli_tok = 'IQoJb3JpZ2luX2VjEGoaCXVzLWVhc3QtMSJHMEUCIQCqb7eWWtTBAzf8XkcSeEWwlgu4rsfypWV4HFx4zyiiDQIgDSU8p29rr/Ys/NDlwatSB0yd+N/8rMM4qB4duzoDAHYqjAMI0///////////ARACGgw3MDg1NzAyMjk0MzkiDKRyw9a+NGM+oMI2iyrgAhYD7JTPP696aLDnFBFyJXGG5VhCD3T4DT+FYu8B/Uqa6a9ow3SqbvFbh/WuzvuiFHhXIOC+HMcqPJ0D5RBt5FRi53CTaAXu+i7JtxYGymAdpYDv1DXkiRbzxA81qBzGGzMgu8ckUw4Mic9qbosOadmTDoVxW97//st/A7XGOETEAdGqtKM3HiX/KTDwFXDjfWTAxMhKSMml4nxeZjiNkKfL9E3R/0aObNC18Ey2f03TbAJVTM9ZndcrY4rPxxi8phrV5ZJly96R+7mqCw7hYI8a2vNW5gSRwkaX938ZsxheW5iIMb0hdlHSAEI/RRAF/diEPnveWL2l+rTBartZw9QHHtI6NaN6s4391EH3j3JoloUkaKwb4fF9w9jmG87vEGeOPdDkncC1srILwqvVXeB1FGHR5KP6isYu3vvdzt0LCF6b/Pq7Cgw0CBPO/zxTSATyuTm6Ao/X2NHor+4tSaMw4IrWigY6pgHebYmvtup+YjlxOVtkSxuAtj4Juw1DoiSBIuyaNJ+5yqdZq6MMCHa96/xHL1NX28/8tBWVZ+nqb96sTHRBW73tBDHmWR/eGa9LRF4NKUjr6Ey9165aeI2+LT9vl2Nh1dWwwkLrCJRScZt1tEN0P3AtddULnWLlXjc0XvZ1HwteJMvGU1SG+0KqyOq7PqhoEQrfa6lPdcdfTUGt9nsm/8EivPdEvohU'

slack_webhook = os.environ.get('SLACK_WEBHOOK_URL', 'hooks.slack.com/services/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')

boto3_session = boto3.Session(
  aws_access_key_id = access_key1,
  aws_secret_access_key = sec_access_key1,
  aws_session_token = cli_tok
)

