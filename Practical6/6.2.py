# we need to import the module called matplotlib to help us complete the scatter
import matplotlib.pyplot as plt

# it is the number of dots
N = 10
# the following two are list which we need to input
paternal_age = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
chd = [1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94]
# we can make a dictionary that matched paternal age to heart disease risk
my_dict = {30: 1.03, 35: 1.07, 40: 1.11, 45: 1.17, 50: 1.23, 55: 1.32, 60: 1.42, 65: 1.55, 70: 1.72, 75: 1.94}
# draw a scatter, X=paternal_age, Y=chd
plt.scatter(paternal_age, chd, marker='o')
# show the scatter
plt.show()
