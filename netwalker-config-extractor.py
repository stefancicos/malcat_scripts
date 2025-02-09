"""
name: Netwalker
category: config extractors
author: Stefan Cicos

Decrypt config (unpacked) netwalker ransomware sample
"""

import malcat
from transforms.stream import RC4
malcat.setup()

for i in analysis.vfiles:
	if i.path == "1337/31337/unk":
		rsc = i.open().read()
		break
	else:
		raise ValueError("No rsrc named 31337 could be found")	
k_len = rsc[0]
key = rsc[4:4+k_len]
data = rsc[4+k_len:]

config = RC4().run(data,key=key)

print(config)
