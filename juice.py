way=int(input())
bj=0
j=0
while(way>0):
    j=way%10
    bj=bj+j
    way=way//10
print(bj)
