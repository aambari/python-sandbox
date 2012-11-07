__author__ = 'aambari'

item =  " {'Type': 'Laptop', 'ItemNumber' : '123456789', 'Status' : 'In use',  'Location' : { 'Departement' : 'Dev',  'Building' : '28',  'Floor' : 12,   'Desk' : 12001, 'Owner' : 'Anderson, Thomas' }, 'tags' : ['Laptop', 'Development', 'In use'] }"


import jsonpickle as pic


dump = pic.decode(item)

print(type(dump))
print dump

