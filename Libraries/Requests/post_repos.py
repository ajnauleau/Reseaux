import requests
from requests.auth import HTTPBasicAuth

gist_data = { "description" : "It is the Gist !",
              "public" : True,
              "files" : {
                  "gist_file_1.txt" : {
                    "content" : "I don't want to talk!"
        }
    }
}

r = requests.post('https://api.github.com/gists', json = gist_data,
                  auth=HTTPBasicAuth('LOGIN', 'PASSWORD'))
print(r.status_code)

r = requests.get('https://api.github.com/users/ajnauleau/gists')
print(len(r.json()))
