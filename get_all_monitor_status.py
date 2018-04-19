from datadog import initialize, api
from datadog.api.constants import CheckStatus
import json

"""
You have to enter your own api_key and app_key
in the following section.
"""

options = {'api_key': 'XXXX',
           'app_key': 'XXXX'}

initialize(**options)

print "Dumping all monitor details now"

status = api.Monitor.get_all()
print status 

for item in map(lambda a: a['id'], status):
    print(item)

"""
We can also get the monitor id with this.
"""

print status[0]["id"]       #Gives first monitor id
print status[1]["id"]       #Gives second monitor id
