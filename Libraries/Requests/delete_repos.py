import requests
from requests.auth import HTTPBasicAuth

r = requests.delete('https://api.github.com/gists/%s' % '1d9c2c91df9a913c417e0958f71f513a',
                     auth=HTTPBasicAuth('LOGIN', 'PASSWORD'))
print(r.status_code)

r = requests.get('https://api.github.com/users/ajnauleau/gists')
print(len(r.json()))