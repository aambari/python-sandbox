__author__ = 'aambari'

import pymongo
import json

from pymongo import Connection

c = Connection()
db = c.tutorial
items = db.items

print (items)


oneItem =  {'Type': 'Laptop', 'ItemNumber' : '123456789', 'Status' : 'In use',  'Location' : { 'Departement' : 'Dev',  'Building' : '28',  'Floor' : 12,   'Desk' : 12001, 'Owner' : 'Anderson, Thomas' }, 'tags' : ['Laptop', 'Development', 'In use'] }





items.insert(oneItem)
