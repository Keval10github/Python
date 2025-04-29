import matplotlib.pyplot as plt
x = [12,13,20,26]
y = [10,20,30,40]
plt.bar(x, y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Bar Chart')
#plt.show()

plt.scatter(x, y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Scatter Plot')
plt.show()