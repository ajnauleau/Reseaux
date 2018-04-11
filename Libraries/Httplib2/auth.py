import urllib.request
import urllib.parse
import json
import httplib2


h = httplib2.Http()

h.add_credentials('LOGIN', 'PASSWD')

headers, content = h.request("https://api.github.com/users/kennethreitz/repos", "GET")

print(headers)
print(content)



