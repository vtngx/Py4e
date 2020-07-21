import urllib.request as ur
import json


json_url = input("Enter location: ")
if len(json_url) < 1 :
    json_url = 'http://py4e-data.dr-chuck.net/comments_579720.json'
print("Retrieving ", json_url)
data = ur.urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_data = json.loads(data)

sum = 0
count = 0

for comment in json_data["comments"]:
    sum += int(comment["count"])
    count += 1

print('Count:', count)
print('Sum:', sum)
