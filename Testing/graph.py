import matplotlib.pyplot as plt

pi_regular=[0.0628265,	5.975803716,	1.094421616]
pi_docker=[0.057315,	5.981491566,	0.925099245]

matrix_regular=[0.3844,	1.7822721,	0.005252247]
matrix_docker=[0.40343,	1.153576612,	0.037946895]

dns_regular=[0.013965,	1.297849138,	1.032497329]
dns_docker=[0.01289,	2.357259364,	0.900495424]

langs = ['C', 'Python', 'Go']

ax.bar(langs,pi_regular)
plt.show()