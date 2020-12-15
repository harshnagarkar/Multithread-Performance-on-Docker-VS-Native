import matplotlib.pyplot as plt
import numpy as np
pi_regular=[0.0628265,	5.975803716,	1.094421616]
pi_docker=[0.057315,	5.981491566,	0.925099245]

matrix_regular=[0.673198095	,1.777031633,	0.005252247]
matrix_docker=[0.671426667,	1.152656317,	0.037946895]

dns_regular=[0.013965,	1.297849138,	1.032497329]
dns_docker=[0.01289,	2.357259364,	0.900495424]

# X = [list(e) for e in zip(pi_regular, pi_docker,)]


# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# langs = ['C', 'Python', 'Go']
# plt.ylabel('some numbers')
# plt.xlabel('some numbers')
# plt.xticks(np.arange(3), langs)
# # ax.set_xticklabels(['zero','two','four'])
# plt.yticks(np.arange(0, 11, 1))
# # plt.yticks(np.arange(0, 7, step=0.2))
# ax.bar(np.arange(3),pi_regular,color=["red","green","purple"])
# # plt.yscale("log")
# plt.show()

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ("C", "Python", "Go")
y_pos = np.arange(len(objects))
y=performance = dns_docker

bars=plt.bar(y_pos, performance, align='center',color=["red","green","purple"])
plt.xticks(y_pos, objects)
plt.ylabel('Time Taken')
plt.xlabel('Programming Languages')
plt.title('Docker DNS resolver')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + .005, yval)

plt.show()

# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# langs = ['C', 'C++', 'Java', 'Python', 'PHP']
# students = [23,17,35,29,12]
# ax.bar(langs,students)
# plt.show()