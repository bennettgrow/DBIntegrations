import token
from simple_salesforce import Salesforce
import json


login = open("logininfo.txt").readlines()
info = []
for line in login:
    info.append(line.strip('\n'))
sf = Salesforce(username=info[0], password=info[1], security_token=info[2])

obj = sf.query_all("SELECT Id, Name FROM Product2 ")
all = json.dumps(obj, indent=4)
print(all)




#sf = Salesforce(username="b.grow.dev@innovasia.com",password="350Inn0v!", security_token="tys7tK8AHsEq20Z73zGae4iA")
