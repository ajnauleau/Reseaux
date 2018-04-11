import urllib.request
import urllib.parse

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = "https://api.github.com"

password_mgr.add_password(None, top_level_url, 'USER', 'PASSWD')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open("https://api.github.com")

urllib.request.install_opener(opener)
op_url = urllib.request.urlopen('https://api.github.com')
