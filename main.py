import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Function to perform Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                yield arr
                swapped = True

# Initialize a random list of values
array = [random.randint(1, 100) for _ in range(20)]

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_title("Bubble Sort")

# Initialize a bar plot
bars = ax.bar(range(len(array)), array, align="edge")

# Function to update the plot during animation
def update_fig(arr, bars):
    for bar, val in zip(bars, arr):
        bar.set_height(val)

# Create an animation
ani = animation.FuncAnimation(fig, func=update_fig, frames=bubble_sort(array), repeat=False)

# Display the animation
plt.show()
