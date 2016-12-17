from matplotlib import pyplot as plt
import numpy as np

plt.xkcd()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([-30, 10])

data = np.ones(100)
data[70:] -= np.arange(30)

plt.annotate('THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
             xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

plt.plot(data)

plt.title('I am not unhappy with this result')
plt.xlabel('number of beers')
plt.ylabel('likelihood of Guido taking the train to Utrecht')

#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
#ax.bar([-0.125, 1.0-0.125], [0, 100], 0.25)
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.set_xticks([0, 1])
#ax.set_xlim([-0.5, 1.5])
#ax.set_ylim([0, 110])
#ax.set_xticklabels(['CONFIRMED BY\nEXPERIMENT', 'REFUTED BY\nEXPERIMENT'])
#plt.yticks([])

#plt.title("CLAIMS OF SUPERNATURAL POWERS")

plt.show()
