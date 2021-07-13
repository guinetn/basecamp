import matplotlib.pyplot as plt

nums = [1, 2, 3, 4, 5]
classes = ['one', 'two', 'three', 'four']
plt.bar(classes, nums, width=0.5)
plt.title("Bar Graph of Train Data")
plt.xlabel("Classes")
plt.ylabel("Counts")