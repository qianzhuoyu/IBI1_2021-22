# we need to define two variables. here, I define the n and p.
n = 0
p = 0
# whether p is greater or equal to 64
#    if yes:done
#    if no: keep looping
while p < 64:
    n += 1
    p = (n ** 2 + n + 2) / 2
# print a sentence
print(n, "straight cuts can have", p, "pizza slices for each member of the IBI1 class")
