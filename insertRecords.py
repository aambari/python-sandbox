_author__ = 'aambari'

import pymongo
import json

from pymongo import Connection

c = Connection()
db = c.tutorial
items = db.items

item = "{'Type': 'Laptop', 'ItemNumber' : '123456789', 'Status' : 'In use',  'Location' : { 'Departement' : 'Dev',  'Building' : '28',  'Floor' : 12,   'Desk' : 12001, 'Owner' : 'Anderson, Thomas' }, 'tags' : ['Laptop', 'Development', 'In use'] }"

import jsonpickle as pic

for i in range(0, 100, 1):
        pyobj = pic.decode(item)
        pyobj["ItemNumber"] = i
        pyobj["Location"]["Owner"]= "Owner" + str(i)
        items.insert(pyobj)

