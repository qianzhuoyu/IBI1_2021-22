# a is the case of COVID-19 in the UK till 2022
a = 19245301
# b is the case of COVID-19 in the UK till 2021
b = 4218520
# c is the case of COVID-19 in the UK till 2020
c = 271
# d is the difference between the numbers of cases in 2020 and 2021
d = b - c
# e is the difference between the numbers of cases in 2021 and 2022
e = a - b
# compare d to e
if d > e:
    print("d is greater")
elif (d == e):
    print("they are the same")
else:
    print("e is greater")
# False，e is greater than d

# 3.2 boolean variables
# create two boolean variables
X = True
Y = True
# W is X and Y
W = X and Y
print("when X is", str(X), "Y is", str(Y), ", W is", str(W))

# change the variable values, repeat the steps above
X = True
Y = False
W = X and Y
print("when X is", str(X), "Y is", str(Y), ", W is", str(W))

# change the variable values, repeat the steps above
X = False
Y = True
W = X and Y
print("when X is", str(X), "Y is", str(Y), ", W is", str(W))

# change the variable values, repeat the steps above
X = False
Y = False
W = X and Y
print("when X is", str(X), "Y is", str(Y), ", W is", str(W))
