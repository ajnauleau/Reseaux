import requests
from requests.auth import HTTPBasicAuth

r = requests.get('https://github.com/user', auth=HTTPBasicAuth('LOGIN', 'PASSWORD'))

print(r.status_code)
print(r.json())
