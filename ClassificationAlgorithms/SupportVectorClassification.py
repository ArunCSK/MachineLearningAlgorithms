#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection  import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix , accuracy_score
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
X_test = sc_X.transform(X_test)
#print(X_test)
#prediction
classifier = SVC(kernel='linear', random_state=0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(y_pred)
#confusion metrices
cm = confusion_matrix(y_test, y_pred)

X_set, y_set = X_train, y_train

#x0 = X[np.where(y == 0)]
#x1 = X[np.where(y == 1)]

#plt.scatter(x0[:, 0], x0[:, 1], c = 'b' , label='Will buy')
#plt.scatter(x1[:, 0], x1[:, 1], c = 'r' , label='Will not buy')


#kuch samja nahi
#print("x0:",x0.shape)
#X1,X2=np.meshgrid(np.arange(start=X_set[:,0].min() -1,stop=X_set[:,0].max() +1,step=0.01),
#np.arange(start=X_set[:,1].min()-1,stop=X_set[:,1].max() +1 ,step=0.01))

#plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape), alpha = 0.75,
#cmap = ListedColormap(('red','green')))

#plt.xlim(X1.min(), X1.max())
#plt.ylim(X2.min(), X2.max())
#for i, j  in enumerate(np.unique(y_set)):
    #plt.scatter(X_set[y_set == j,0],X_set[y_set == j, 1],c=ListedColormap(('r','g'))(i),label=j)

#plt.xlabel("Age")
#plt.ylabel("Estimated Salary")
#plt.legend()
#plt.show()


#saving model
file_name = "SupportVectorClassification.pkl"
pkl_file = open(file_name, 'wb')
model = pickle.dump(classifier, pkl_file)




