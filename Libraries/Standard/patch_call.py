import urllib.request
import urllib.parse
import json

gist_data = {
    "description" : "Patching Up",
    "public" : True,
    "files": {
        "gist_file_1.txt" : {
            "content" : "I don't want to talk anymore"

        }
    }
}

params = json.dumps(gist_data).encode('utf8')
req = urllib.request.Request(url='https://api.github.com/gists',
                             data=params,
                             headers = {'content-type' : 'application/json'})

req.get_method = lambda : 'PATCH'

response = urllib.request.urlopen(req)
page = response.read()
print(page)



