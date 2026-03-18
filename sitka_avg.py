import csv
import matplotlib.pyplot as plt
from datetime import datetime

#filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/data_Sitka_2016_2026.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row1 = next(reader)
    header_row2 = next(reader)
    header_row3 = next(reader)
    #first_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, avgs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0],'%Y%m')
        avg = float(row[1])
        dates.append(current_date)
        avgs.append(avg)

    print(avgs)

# Plot the avg temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,avgs, c='orange')
ax.scatter(dates,avgs, c='red', linewidths=0.8)

# Format the plot.
ax.set_title("Sitka (AK) Avg temp 2016 to 2026", fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

 