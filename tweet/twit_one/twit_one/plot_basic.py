import matplotlib.pyplot as plt

slices = [1, 2, 2, 5]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')

plt.title('Interesting Graph\nCheck it out')
plt.show()