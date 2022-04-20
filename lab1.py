import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("/content/student_scores - student_scores.csv")
data.head()
data.isnull().sum()
X=data.Hours
X.head()
y=data.Scores
y.head()
n=len(X)
m=0
c=0
L=0.01
loss=[]
for i in range(10000):
  ypred=m*X+c
  MSE=(1/n)*sum((ypred-y)*2)
  dm=(2/n)*sum(X*(ypred-y))
  dc=(2/n)*sum(ypred-y)
  c=c-L*dc
  m=m-L*dm
  loss.append(MSE)
  print(m,c)
  y_pred=m*X+c
plt.scatter(X,y,color="red")
plt.plot(X,y_pred)
plt.xlabel("Study hours")
plt.ylabel("Scores")
plt.title("Study hours vs Scores")
plt.plot(loss)
plt.xlabel("iteration")
plt.ylabel("loss")