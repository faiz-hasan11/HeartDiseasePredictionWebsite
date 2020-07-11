from django.shortcuts import render
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler
# Create your views here.

reloadModel = joblib.load('./models/ModelForHeartDiseasePrediction2.pkl')

def home(request):
    return render(request,'home.html')

def predictResult(request):
    if request.method == 'POST':
        temp={}
        arr = []
        temp['age'] = request.POST.get('ageVal')
        temp['sex'] = request.POST.get('genderVal')
        temp['cp'] = request.POST.get('chestpainVal')
        temp['trestbps'] = request.POST.get('trestbpsVal')
        temp['chol'] = request.POST.get('cholVal')
        temp['fbs'] = request.POST.get('fbsVal')
        temp['restecg'] = request.POST.get('restecgVal')
        temp['thalach'] = request.POST.get('thalachVal')
        temp['exang'] = request.POST.get('exangVal')
        temp['oldpeak'] = request.POST.get('oldpeakVal')
        temp['slope'] = request.POST.get('slopeVal')
        temp['ca'] = request.POST.get('caVal')
        temp['thal'] = request.POST.get('thalVal')
        arr.append(temp['age'])
        arr.append(temp['sex'])
        arr.append(temp['cp'])
        arr.append(temp['trestbps'])
        arr.append(temp['chol'])
        arr.append(temp['fbs'])
        arr.append(temp['restecg'])
        arr.append(temp['thalach'])
        arr.append(temp['exang'])
        arr.append(temp['oldpeak'])
        arr.append(temp['slope'])
        arr.append(temp['ca'])
        arr.append(temp['thal'])
    scoreval = reloadModel.predict([arr])
    return render(request,'pred.html',{'scoreval':scoreval})
