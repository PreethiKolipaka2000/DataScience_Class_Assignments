import requests 
r=requests.get("https://cdn2.thedogapi.com/images/-HgpNnGXl.jpg")
print(r.status_code)
print(r.ok)
print(r.headers)
with open("dog_1.png","wb") as f:
    f.write(r.content)