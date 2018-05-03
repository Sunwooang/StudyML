# mjh
# session04

import pickle
from sklearn.linear_model import SGDRegressor

path = '../../session04.pkl'

with open(path, 'rb') as f:
    data = pickle.load(f)

X = data['X']
Y = data['Y']

model = SGDRegressor(loss='squared_loss', max_iter=5000, eta0=0.01, learning_rate='constant',
                     penalty=None)

model.fit(X, Y)
print(model.coef_)
print(model.score(X, Y))  # 0.969137312717

