#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection  import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap
import pickle

#Load Data
dataset = pd.read_csv("Social_Network_Ads.csv")
X = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:,4].values
#print(X, y)

#Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25 , random_state = 0 )
#print(X_test)
#feature scaling
sc_X = StandardScaler()

X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)
#print(X_test)
#prediction


classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
#print(y_pred)

cm = confusion_matrix(y_test, y_pred)
#print(cm)


#saving model
file_name = "DecissionTreeClassification.pkl"
pkl_file = open(file_name, 'wb')
model = pickle.dump(classifier, pkl_file)