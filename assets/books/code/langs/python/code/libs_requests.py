'''
requests

Makes web requests really simple
Building on the most downloaded Python library in the world, urllib3. It 
https://pypi.org/project/requests
https://requests.readthedocs.io/en/master/
'''

import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
# 200
r.headers['content-type']
# 'application/json; charset=utf8'
r.encoding
# 'utf-8'
r.text
# u'{"type":"User"...'
r.json()
# {u'disk_usage': 368627, u'private_gists': 484, ...}