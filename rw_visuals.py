import matplotlib.pyplot as plt
from random_walks import RandomWalk

# Make a random walk
rw = RandomWalk(50_000)
rw.fill_walk()

# Plot the points in the walk
plt.style.use('classic')               
fig,ax = plt.subplots(figsize=(10,5))
# Coloring the points
point_numbers = range(rw.num_points)
# Plotting the first and last numbers
ax.scatter(0,0,c='Green',edgecolor='Blue',s=50)
ax.scatter(rw.x_value[-1],rw.y_value[-1],c='red',edgecolor='Black',s=50)
ax.scatter(rw.x_value,rw.y_value,c=point_numbers,cmap=plt.cm.rainbow,edgecolor='None',s=40)


# Removing the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
# Plotting the plot
plt.show()