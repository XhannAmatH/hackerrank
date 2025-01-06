#   Author  :   XhannAmatH


if __name__ == '__main__':
    n = int(input().strip())
    
    if(n%2!=0):
        print("Weird")
    else:
        if(n<6 and n>1):
            print("Not Weird")
        elif(n<21 and n>5):
            print("Weird")
        elif(n>20):
            print("Not Weird")
