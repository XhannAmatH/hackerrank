#   Author  :   XhannAmatH

import re

vowels = re.findall(r'(?<=[^AEIOUaeiou])([AEIOUaeiou]{2,})(?=[^AEIOUaeiou])', input())

if vowels:
    [print(vow) for vow in vowels]
else:
    print(-1)

#[print(vowel) if vowel else print(-1) for vowel in vowels]

