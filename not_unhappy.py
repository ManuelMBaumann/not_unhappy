from matplotlib import pyplot as plt
import numpy as np

plt.xkcd()

fig = plt.figure()
ax = fig.add_axes((0.1, 0.1, 0.8, 0.7))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([-0.1, 1.2])
# set the y-spine
ax.spines['bottom'].set_position('zero')

e_one_beer = 70, 1
e_movies = 150, 0.9
e_one_whisky = 350, 0.5

events = np.array([ (-20, 1), e_one_beer, (100, 0.9), e_movies, (190, 0.5), e_one_whisky, (400, -0.5) ])

plt.annotate('"I guess I can \nhave one beer"'.upper(), xy=e_one_beer, arrowprops=dict(arrowstyle='->'), xytext=(15, 0.7))
plt.annotate('Esther: "I\'m going\nto the movies"'.upper(), xy=e_movies, arrowprops=dict(arrowstyle='->'), xytext=(130, 1))
plt.annotate('"I guess I can \nhave one whisky"'.upper(), xy=e_one_whisky, arrowprops=dict(arrowstyle='->'), xytext=(300, 0.7))
plt.annotate('Over the line!!'.upper(), xy=(375, 0), arrowprops=dict(arrowstyle='->'), xytext=(400, 0.35))

plt.plot(events[:,0], events[:,1], 'k')

plt.suptitle('Likelihood that Guido will take the train to Utrecht'.upper(), y=0.93)
plt.xlabel('Friday evening advances'.upper())
plt.ylabel('likelihood of safe return'.upper())

t = [(18,0), (20,30), (22,0), (26,30)]
s = [i*60+j for i, j in t]
ax.set_xlim(-20, s[-1]-s[0]+20)
plt.xticks([i-s[0] for i in s], ['{:02}:{:02}'.format(i%24, j) for i, j in t])
plt.yticks([1], ['1.0'])


plt.show()
