#
# https://github.com/ipfs/py-ipfs-api.git
#

import ipfsapi

api = ipfsapi.connect('127.0.0.1', 5001)

hmeta_meta = api.add('hmeta.config')

# {'Name': 'hmeta.config', 'Hash': 'QmWvgsuZkaWxN1iC7GDciEGsAqphmDyCsk3CVHh7XVUUHq', 'Size': '28'}

#display
api.cat('QmWvgsuZkaWxN1iC7GDciEGsAqphmDyCsk3CVHh7XVUUHq')

