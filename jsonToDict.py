__author__ = 'aambari'

item =  {'Type': 'Laptop',
             'ItemNumber' : '123456789',
             'Status' : 'In use',
             'Location' : {
                 'Departement' : 'Dev',
                 'Building' : '28',
                 'Floor' : 12,
                 'Desk' : 12001,
                 'Owner' : 'Anderson, Thomas'
             },
             "tags" : ["Laptop", "Development", "In use"]
            }

import simplejson as json

dump = json.dumps(item, separators=(',', ':'))

print(type(dump))
print dump

d = eval(dump)
d["tags"]=[1, 2, 3]

print(d["tags"])


s = json.dumps(d, sort_keys=True, indent='    ')
print '\n'.join([l.rstrip() for l in  s.splitlines()])
