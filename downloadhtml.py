# download and parsing web site
# author Bulat

import requests

url = "https//:some-web-site.com"
r = requests.get(url)
with open("test.html", "w") as file:
    file.write(r.text)
