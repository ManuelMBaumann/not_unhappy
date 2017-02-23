from matplotlib import pyplot as plt
import matplotlib.patches
import numpy as np

plt.xkcd()

cm_per_inch = 2.54
fig = plt.figure(figsize=(15*2/cm_per_inch, 10*2/cm_per_inch))
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

plt.annotate('git commit -m\n"And fuck the shit"'.upper(), xy=(0,1), arrowprops=dict(arrowstyle='->'), xytext=(0, 1.1))
plt.annotate('"I guess I can \nhave one beer"'.upper(), xy=e_one_beer, arrowprops=dict(arrowstyle='->'), xytext=(15, 0.7))
plt.annotate('Esther: "I\'m going\nto the movies"'.upper(), xy=e_movies, arrowprops=dict(arrowstyle='->'), xytext=(130, 1))
plt.annotate('"I guess I can \nhave one whisky"'.upper(), xy=e_one_whisky, arrowprops=dict(arrowstyle='->'), xytext=(300, 0.7))
plt.annotate('Over the line!!'.upper(), xy=(375, 0), arrowprops=dict(arrowstyle='->'), xytext=(400, 0.35))

plt.plot(events[:,0], events[:,1], 'k')

w = 25
h = 0.1
ax.add_patch(matplotlib.patches.Ellipse((200, 0.08), w, h, fill=False, edgecolor='k', linewidth=2))
ax.add_patch(matplotlib.patches.Ellipse((200, 0.08), w/10, h/10, fill=True, edgecolor='k', facecolor='k'))
ax.add_patch(matplotlib.patches.Ellipse((200-2*w/10, 0.08+h/10), w/10, h/10, fill=True, edgecolor='k', facecolor='k'))
ax.add_patch(matplotlib.patches.Ellipse((200-2.2*w/10, 0.08-2*h/10), w/10, h/10, fill=True, edgecolor='k', facecolor='k'))
ax.plot([161, 182], [0.05, 0.05], 'k', linewidth=1)
ax.plot([159, 178], [0.08, 0.08], 'k', linewidth=1)
ax.plot([164, 181], [0.11, 0.11], 'k', linewidth=1)

plt.suptitle('Likelihood that Guido will take the train to Utrecht'.upper(), y=0.93)
plt.xlabel('Friday evening advances'.upper())
plt.ylabel('likelihood of safe return'.upper())

t = [(18,0), (20,30), (22,0), (26,30)]
s = [i*60+j for i, j in t]
ax.set_xlim(-20, s[-1]-s[0]+20)
plt.xticks([i-s[0] for i in s], ['{:02}:{:02}'.format(i%24, j) for i, j in t])
plt.yticks([1], ['1.0'])

plt.savefig('not_unhappy.png', dpi=300)
plt.show()
