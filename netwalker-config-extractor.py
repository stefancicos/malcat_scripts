import malcat
from transforms.stream import RC4
malcat.setup()

for i in analysis.vfiles:
	if i.path == "1337/31337/unk":
		rsc = i.open().read()
k_len = rsc[0]
key = rsc[4:4+k_len]
data = rsc[4+k_len:]

config = RC4().run(data,key=key)

print(config)
