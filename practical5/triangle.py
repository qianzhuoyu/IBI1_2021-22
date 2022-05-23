# we need to define a variable first, j is the variable.
j = 1
# there is an equation y=x*(x+1)/2 between j and k.  k is the dot of the triangle.
# k==j*(j+1)/2
# we need a loop to increase the j to calculate the k.
while j < 11:
    k = j * (j + 1) / 2
# print a sentence
    print('triangle', j, 'has', k, 'dots')
    # the j should be added one by one.
    j = j + 1
