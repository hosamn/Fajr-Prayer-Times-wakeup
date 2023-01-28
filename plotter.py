# import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


times = pd.read_csv('PrayerTimes2020.csv', index_col=[0], parse_dates=[0, 1, 2, 3, 4, 5, 6]).reset_index(drop=True)
# print(times.head(1))
# times.info()


# times = pd.concat([times, times, times, times], axis=0).reset_index(drop=True)
times = times[['Fajr', 'Sunrise']]    # Currently looking at fajr only!

# print(times.head(1))
# times.info()


plt.plot(times)

# print(min(times.loc[times['Fajr']]))

plt.gca().fill_between(range(1, 367), times['Fajr'], times['Sunrise'])


# Max & Min lines
plt.axhline(max(times['Fajr']), xmin=0, xmax=1, linewidth=1, color='grey', linestyle=":")
plt.axhline(min(times['Fajr']), xmin=0, xmax=1, linewidth=1, color='grey', linestyle=":")

plt.axhline(max(times['Sunrise']), xmin=0, xmax=1, linewidth=1, color='orange', linestyle=":")
plt.axhline(min(times['Sunrise']), xmin=0, xmax=1, linewidth=1, color='orange', linestyle=":")


# plot format
plt.title("Fajr Prayer times all year round\n", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Time", fontsize=12)

plt.gcf().set_size_inches(12, 6)
plt.legend(times.columns.values, loc="upper right", fontsize=12)


# Axe formats
plt.xticks(ticks=[16, 46, 76, 106, 137, 167, 198, 229, 259, 290, 320, 351])

plt.gca().invert_yaxis()
plt.gca().set_xlim(min(times.index), max(times.index))

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%h'))
plt.gca().yaxis.set_major_formatter(mdates.DateFormatter('%I:%M %p'))


# sns.lineplot(x=times['Date'], y=times['Fajr'])
plt.show()
