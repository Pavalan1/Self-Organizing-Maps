import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from minisom import MiniSom

data = pd.read_csv('./data/winequality-red.csv', delimiter=',')
X = data.drop('quality', axis=1).values
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

som = MiniSom(x=10, y=10, input_len=X.shape[1], sigma=1.0, learning_rate=0.5)
som.random_weights_init(X)
som.train_random(data=X, num_iteration=100)

plt.figure(figsize=(10, 10))
for i, x in enumerate(X):
    w = som.winner(x)
    plt.text(w[0] + .5, w[1] + .5, str(data['quality'].values[i]),
             color=plt.cm.rainbow(data['quality'].values[i] / 10), fontdict={'size': 10})

plt.pcolor(som.distance_map().T, cmap='bone_r')
plt.colorbar()
plt.show()
