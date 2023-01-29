# import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


times = pd.read_csv('PrayerTimes2020.csv', index_col=[0], parse_dates=[0, 1, 2, 3, 4, 5, 6]).reset_index(drop=True)
# print(times.head(1))
# times.info()


# times = pd.concat([times, times, times, times], axis=0).reset_index(drop=True)
times = times[['Fajr', 'Sunrise']]                          # Currently looking at fajr only!

# print(times.head(1))
# times.info()


plt.plot(range(1, 367), times, label='_nolegend_')          # added empirical x values to fix strange shift.
# print(min(times.loc[times['Fajr']]))
# plt.gca().fill_between(range(1, 367), times['Fajr'], times['Sunrise'], color='none', hatch='|', edgecolor="pink", label='Fajr 2 Sunrise')
plt.gca().fill_between(range(1, 367), times['Fajr'], times['Sunrise'], color='yellow', alpha=.3, edgecolor='black', label='Fajr 2 Sunrise')


# Max & Min lines
plt.axhline(max(times['Fajr']), xmin=0, xmax=1, linewidth=1, color='grey', linestyle=":", label='_nolegend_')
plt.axhline(min(times['Fajr']), xmin=0, xmax=1, linewidth=1, color='grey', linestyle=":", label='_nolegend_')

plt.axhline(max(times['Sunrise']), xmin=0, xmax=1, linewidth=1, color='grey', linestyle=":", label='_nolegend_')
plt.axhline(min(times['Sunrise']), xmin=0, xmax=1, linewidth=1, color='grey', linestyle=":", label='_nolegend_')


# what time to rule them all
plt.axhline(min(times['Sunrise']) - pd.Timedelta(minutes=20), xmin=0, xmax=1, linewidth=2, color='green', linestyle="--")
# plt.axhline(min(times['Sunrise']) - pd.Timedelta(hours=6, minutes=20), xmin=0, xmax=1, linewidth=2, color='green', linestyle="--")


# plot format
plt.title("Fajr Prayer Times All Year Round\n", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Time", fontsize=12)

plt.gcf().set_size_inches(12, 6)
# plt.legend(times.columns.values, loc="upper right", fontsize=12)
plt.legend(['Fajr to Sunrise', 'Best Wakeup Time', 'Best Sleep Time'], loc="upper right", fontsize=12)
# print(times.columns.values)

# Axe formats
plt.xticks(ticks=[16, 46, 76, 106, 137, 167, 198, 229, 259, 290, 320, 351])

plt.gca().invert_yaxis()
plt.gca().set_xlim(min(times.index), max(times.index))

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%h'))
plt.gca().yaxis.set_major_formatter(mdates.DateFormatter('%I:%M %p'))


# sns.lineplot(x=times['Date'], y=times['Fajr'])
plt.savefig("1.jpg")
plt.show()
