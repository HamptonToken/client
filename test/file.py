#
# IPFS Python library
#
# use python wrapper over IPFS to interact with IPFS
# download IPFS API from https://github.com/ipfs/py-ipfs-api.git
# or pip install ipfs-api
#

import ipfsapi

api = ipfsapi.connect('127.0.0.1', 15001)

hmeta_meta = api.add('hmeta.config')

# {'Name': 'hmeta.config', 'Hash': 'QmWvgsuZkaWxN1iC7GDciEGsAqphmDyCsk3CVHh7XVUUHq', 'Size': '28'}

#display
api.cat('QmWvgsuZkaWxN1iC7GDciEGsAqphmDyCsk3CVHh7XVUUHq')

import requests
params = (
('arg','QmeY7x2rEzyUxh2uwhXMqgBnPvcxzgNcQcUQWJG94Hv9ki')
)
response = requests.post('https://ipfs.dev.infura.org:5001/api/v0/pin/rm',params=params, auth=(<project_id>,<project_secret>)
print(response.json())
