import requests

r = requests.get('https://api.github.com/users/kennethreitz/repos',
                 params = {'type':'member'})

print(r.status_code)
print(r.text)
print(r.json())



