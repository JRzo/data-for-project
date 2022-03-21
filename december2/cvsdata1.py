import csv
import matplotlib.pyplot as plt
from datetime import datetime as dt



filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	# Printing the header and it's position
	for index,column_header in enumerate(header_row):
		print(f"{index,column_header}")

	# Getting the dates and high/small temapures for this file
	dates,highs,smalls = [],[],[]
	n = next(reader,2)
	for row in reader:

		high = int(row[5])
		small = int(row[6])
		if high > 65.5:

			current_date = dt.strptime(row[2],"%Y-%m-%d")
			dates.append(current_date)
			highs.append(f'{high}')
			smalls.append(f'{small}')
	print(highs,smalls)

# Plot the high temperatures 
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates,smalls,c='lightblue')
ax.plot(dates,highs, c='red')
ax.fill_between(dates,highs,smalls,facecolor='yellow',alpha=0.5)


# Format the plot
ax.set_title('Daily High Temp, in 2018',fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize= 16)

plt.show()