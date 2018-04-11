import urllib.request
import urllib.parse
import json

gist_data = {
    "description" : "It's a Giat!",
    "public" : True,
    "files": {
        "gist_file_1.txt" : {
            "content" : "I don't want to talk"

        }
    }
}

params = json.dumps(gist_data).encode('utf8')
req = urllib.request.Request('https://api.github.com/gists',
                             data = params,
                             headers = {'content-type' : 'application/json'})

response = urllib.request.urlopen(req)
page = response.read()
print(page)



