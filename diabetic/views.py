from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

def modeler(preg,glu,bp,st,ins,bmi,dpf,age):
    diabetes_dataset = pd.read_csv('C:/Users/Nitro/Desktop/diab/diabetics/diabetic/dib.csv')
    X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
    Y = diabetes_dataset['Outcome']
    print(bp+preg+glu+st+ins+bmi+dpf+age)
    scaler = StandardScaler()
    scaler.fit(X)
    standardized_data = scaler.transform(X)
    X = standardized_data
    Y = diabetes_dataset['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)
    classifier = svm.SVC(kernel='linear')
    classifier.fit(X_train, Y_train)
    
    input_data = (preg,glu,bp,st,ins,bmi,dpf,age)
    input_data_array = np.asarray(input_data)
    input_data_reshaped = input_data_array.reshape(1,-1)
    std_data = scaler.transform(input_data_reshaped)
    prediction = classifier.predict(std_data)
    if (prediction[0] == 0):
        return 0
        print('0')
    else:
        print('1')
        return 1

    
# Create your views here.
def diabetic(request):
    res = 2
    bp =request.GET.get('BP')
    pregnency = request.GET.get('Pregnency')
    glucose = (request.GET.get('Glucose'))
    st = (request.GET.get('ST'))
    insulin = (request.GET.get('Insulin'))
    bmi = (request.GET.get('BMI'))
    dpf = (request.GET.get('DPF'))
    age = (request.GET.get('Age'))
    if(bp!=None):
        res = modeler(int(pregnency),int(glucose),int(bp),int(st),int(insulin),float(bmi),float(dpf),int(age))
    
    
    context = {
        'res':res,
    }
    
    template = loader.get_template('index.html')
    return render(request,'index.html',context)