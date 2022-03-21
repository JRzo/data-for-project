from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die()

# Make some rools, and store results in a list.

results = []
for x in range(200_000):
	result = die_1.roll() * die_2.roll()
	results.append(result)

new_result = [x for x in results]

# Analazing the results 
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for valueF in range(1, max_result+1):
	# We count the each value that has been recorde
	friencies = results.count(valueF)
	# We add each value to it
	frequencies.append(friencies)

new_frequencies = [x for x in frequencies]
print(new_frequencies)

# Visualazing the data
x_values = list(range(1,max_result+1))
data = [Bar(x=x_values,y=new_frequencies)]

x_axis_configure = {'title':'Results','dtick':1}
y_axis_configure = {'title':'Frequency of Results'}

# The layout of the histogram
my_layout = Layout(title='Results of rolling Two D8 1000 times',xaxis=x_axis_configure,yaxis=y_axis_configure)

offline.plot({'data':data, 'layout':my_layout},filename='d6_2.html')