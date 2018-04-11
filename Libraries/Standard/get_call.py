import urllib.request
import urllib.parse

opn_url = urllib.request.urlopen('https://api.github.com/')
dir_api = opn_url.read()
print(dir_api)

params = {'type':'member'}
data = urllib.parse.urlencode(params)

resp = urllib.request.urlopen('https://api.github.com/users/kennethreitz/repos?' + data)
text_resp = resp.read()
print(text_resp)

