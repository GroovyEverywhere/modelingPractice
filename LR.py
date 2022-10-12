#Linear regression

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

def multi_Lr():
    data = pd.read_csv('C:\\Users\\tan_b\\Downloads\\000001.csv',encoding='latin-1')
    sns.pairplot(data, x_vars=['50'],y_vars='sz',kind="reg",size=5,aspect=0.7)
    plt.show()
    X = data.loc[:,('50')]
    y = data.loc[:,'zs']
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=100)
    linreg = LinearRegression()
    model = linreg.fit(X_train,y_train)
    print(model)
    print(linreg.intercept_)
    print(linreg.coef_)

    y_pred = linreg.predict(X_test)
    print(y_pred)
    


