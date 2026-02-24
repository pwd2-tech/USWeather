import matplotlib.pyplot as plt

input_values = [x for x in range(1,6)]
squares = [x**2 for x in range(1,6)]
print(squares)

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value',fontsize=14)
ax.set_ylabel('Square of Value',fontsize=24)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()