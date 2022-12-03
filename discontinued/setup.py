import requests
import zipfile

#url = ''
#r = requests.get(url, allow_redirects=True)
#open('facebook.ico', 'wb').write(r.content)
with zipfile.ZipFile("C:\\Users\\montchik\\Desktop\\crwlspace\\python\\python.zip", "r") as zip_ref:
    zip_ref.extractall("C:\\Users\\montchik\\Desktop\\crwlspace\\python\\python_t")
