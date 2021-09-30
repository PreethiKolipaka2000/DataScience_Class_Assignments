import requests 
def get_req(url):
    r=requests.get(url)
    return r.json()
url="https://api.github.com/events"
r = requests.post('https://httpbin.org/post', data = {'name':'Joe'})
print(r.url)
'''r1=get_req(url)
for i in r1:
    print(i)'''