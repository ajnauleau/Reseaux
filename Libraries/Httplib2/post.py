import urllib.request
import urllib.parse
import json
import httplib2

gist_data = {
    "description" : "It's a Gist!",
    "public" : True,
    "files": {
        "gist_file_1.txt" : {
            "content" : "I don't want to talk"

        }
    }
}

params = json.dumps(gist_data).encode('utf8')

h = httplib2.Http()

headers, content = h.request('https://api.github.com/gists',
                             "POST", body=params, headers={'content-type': 'application/json'})
print(headers)
print(content)



