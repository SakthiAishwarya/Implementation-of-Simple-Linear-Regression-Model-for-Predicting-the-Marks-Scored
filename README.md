# Implementation-of-Simple-Linear-Regression-Model-for-Predicting-the-Marks-Scored

## AIM:
To write a program to implement the simple linear regression model for predicting the marks scored.

## Equipments Required:
1. Hardware – PCs
2. Anaconda – Python 3.7 Installation / Moodle-Code Runner

## Algorithm
1.Import the standard Libraries.

2.Set variables for assigning dataset values.

3.Import linear regression from sklearn.

4.Assign the points for representing in the graph

5.Predict the regression for marks by using the representation of the graph.

6.Compare the graphs and hence we obtained the linear regression for the given datas.
 

## Program:
```
/*
Program to implement the simple linear regression model for predicting the marks scored.
Developed by: SAKTHI AISHWARYA .S
RegisterNumber:  212219040132

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
navu=pd.read_csv('/content/student_scores - student_scores.csv')
navu.head()
X=navu.iloc[:,:-1].values
X
y=navu.iloc[:,1].values
y
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=1/3,random_state=0)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test)
y_pred
y_test
plt.scatter(X_train,y_train,color='blue')
plt.plot(X_train,regressor.predict(X_train),color="brown")
plt.title("h vs s (Training Set)")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.show()
plt.scatter(X_test,y_test,color='black')
plt.plot(X_test,regressor.predict(X_test),color="orange")
plt.title("h vs s (Testing Set)")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.show()


*/
```

## Output:
![image](https://user-images.githubusercontent.com/67967960/169561620-8b8c6cc1-67a3-4536-8db4-329d25d18a5a.png)
![image](https://user-images.githubusercontent.com/67967960/169561734-3f75d175-eae6-4c18-8bce-0650752ee1f9.png)



## Result:
Thus the program to implement the simple linear regression model for predicting the marks scored is written and verified using python programming.
