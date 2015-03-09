import matplotlib.pyplot as plt

W_max = +075
W_min = 0.25
W = 0.5
LTP = 0.05

X = []
Y = []
for i in range(100):
   W = W + LTP*(W_max-W)*(W-W_min)
   X.append(i)
   Y.append(W)

plt.plot(X,Y)
plt.show()
