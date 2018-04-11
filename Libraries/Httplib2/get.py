import httplib2

h = httplib2.Http()
#h = httplib2.Http(".cache")

headers, content = h.request("https://api.github.com/users/kennethreitz/repos", "GET")

print(headers)
print(content)
