'''a=10;b=25;c=15;d=30;e=2;f=3;g=5
x=a+b-c
y=d**e
z=f%g
print(x,y,z)

sum=0.5
for i in range(5):
    if i % 2==0:
        sum=int(sum+i)
        print("even",sum)
    else:
        sum=sum+i
        print("odd",sum)

print(sum)

for i in range(1,11):
    count=i
    while count>0:
        print(i,end=" ")
        count=count-1
    print()'''
for i in (1,100,5):
    print(i)
