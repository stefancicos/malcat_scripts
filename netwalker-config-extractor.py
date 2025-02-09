import malcat
from transforms.stream import RC4
malcat.setup()

rsc = analysis.vfiles[0].open().read()
k_len = rsc[0]
key = rsc[4:4+k_len]
data = rsc[4+k_len:]

config = RC4().run(data,key=key)

print(config)
