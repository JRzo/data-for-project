import matplotlib.pyplot as plt
plt.style.available

plt.style.use('seaborn')
x_values = range(1,5001)
y_values = [x**3 for x in x_values]

fig,ax = plt.subplots()
ax.scatter(x_values,y_values, c=x_values, cmap=plt.cm.Reds,s=10)

# Display the charts and labels of the grap
ax.set_title('Amount of wasted second in a Days')
ax.set_xlabel('Days')
ax.set_ylabel('Values')

ax.tick_params(axis='both', which='major',labelsize=15)
ax.axis([0,5000,1,30950000])


plt.show()