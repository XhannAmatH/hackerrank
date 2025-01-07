#   Author  :   XhannAmatH

import re

m = re.findall(r'([a-zA-Z0-9])\1+', input().strip())

if(len(m) != 0):
    print(m[0])
else:
    print(-1)
