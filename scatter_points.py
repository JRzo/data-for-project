import matplotlib.pyplot as plt
plt.style.available

plt.style.use('seaborn')
x_values = range(1,1100)
y_values = [x**2 for x in x_values]

fig,ax = plt.subplots()
ax.scatter(x_values,y_values,c=x_values, cmap=plt.cm.Greys,s=10)

# Displaying the tittle and the label
ax.set_title('Squares of numbers',fontsize=25)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Squares out put(M)',fontsize=14)

# Settings the tick params
ax.tick_params(axis='both',which='major',labelsize=14)
ax.axis([0,1100,0,1100000])


plt.savefig('scatter_plot_2.png')