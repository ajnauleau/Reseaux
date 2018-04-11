import requests
from requests.auth import HTTPBasicAuth

gist_data = { "description" : "It is the Gist !",
              "public" : True,
              "files" : {
                  "gist_file_1.txt" : {
                    "content" : "I wonder if the moon tastes like vanilla"
        }
    }
}

r = requests.patch('https://api.github.com/gists/1d9c2c91df9a913c417e0958f71f513a',
                   json = gist_data,
                   auth=HTTPBasicAuth('LOGIN', 'PASSWORD'))

print(r.status_code)
print(r.json())
