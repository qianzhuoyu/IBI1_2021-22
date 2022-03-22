# we need to import the module called matplotlib to help us complete the boxplot
import matplotlib.pyplot as plt

# it is the number of the dots
n = 8
# marks is a list which we should input
marks = [45, 36, 86, 57, 53, 92, 65, 45]
# this step sort the marks and mutates the marks
marks.sort()
print(marks)
# now, it's time to begin to draw a boxplot. The following are the various parameters of the boxplot
plt.boxplot(marks,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False)
# we can add a title
plt.title('boxplot')
# show the boxplot
plt.show()
# Next, we should calculate the average of marks. I try calculating the total first then  divide 8 to get the average.
total = 0
for i in range(len(marks)):
    total += marks[i]
average = total / 8
# compare average to 60
average > 60
# False, Rob's average is smaller than 60.
