import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

diabetes_dataset = pd.read_csv('C:/Users/Nitro/Desktop/diab/diabetics/diabetic/dib.csv')
X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
Y = diabetes_dataset['Outcome']
scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)
X = standardized_data
Y = diabetes_dataset['Outcome']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)
input_data = (51,16,100,10,175,12.2,0.8,11)
input_data_array = np.asarray(input_data)
input_data_reshaped = input_data_array.reshape(1,-1)
std_data = scaler.transform(input_data_reshaped)
print(std_data)
prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  
  print('The person is not Diabetic 0')
else:
  print('The person is Diabetic  1')
