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

plt.annotate('I guess I can \nhave one beer',
             xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

plt.plot(data)

plt.title('Likelihood that Guido will take the train to Utrecht')
plt.xlabel('Friday evening advances')
plt.ylabel('likelihood of safe return')

plt.xticks([10, 40, 60, 85], ['18:00','20:30', '22:00', '02:30'])
plt.yticks([0.9], ['1.0'])


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
