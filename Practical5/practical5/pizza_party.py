#we need to define two variables.
n=0
p=0
#whether p is greater or equal to 64
#    if yes:done
#    if no: keep looping
while p<64:
    p=(n**2+n+2)/2
    n+=1
#we need to minus 1 here
n=n-1
print(n, "stright cuts can have", p, "pizza slices for each member of the IBI1 class")

