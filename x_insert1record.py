__author__ = 'aambari'

import pymongo
import json

from pymongo import Connection

c = Connection()
db = c.tutorial
items = db.items

print (items)


twoItems = {"Type": "Laptop",
        "ItemNumber" : "123456789",
        "Status" : "In use",
        "Location" : {
                "Departement" : "Dev",
                "Building" : "28",
                "Floor" : 12,
                "Desk" : 12001,
                "Owner" : "Anderson, Thomas"
        },
        "tags" : ["Laptop", "Development", "In use"]
        }





print (items.insert(twoItems))
'''print (items.find_one());'''

for item in items.find():
    print(item)
    ''' print json.dumps(item, separators=(',',':'))'''

print ("\n")
for item in items.find({"Location.Owner" : "Cooper, James"}):
    print(item)



print ("\n")

for item in items.find({"tags" : "Big"}):
    print(item)