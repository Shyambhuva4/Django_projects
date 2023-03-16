import json
import requests

URL='http://127.0.0.1:8000/stucreate'

data={
    'name':'Tony',
    'city':'Bombay'
}
json_data=json.dumps(data)
print(json_data)
r=requests.post(url=URL, data=json_data)
contents = json.loads(str(r))
print(contents)
# data=r.json()
# # data = json.loads(r.text)
# print(data)