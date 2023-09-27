#WAPP to check no. is armstrong or not.
num=int(input('enter any no:'))
r=0
t=num
while(num>0):
    a=num%10
    r=r+a*a*a
    num=num//10
if(r==t):
    print('Armstrong no.')
else:
    print('Not an armstrong no.')
