#   Author  :   XhannAmatH

def swap_case(s):
    swaped=""
    for a in s:
        if(a.isupper()):
            swaped+= a.lower()
        elif(a.islower()):
            swaped+= a.upper()
        else:
            swaped+= a
            
    return swaped

__name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
