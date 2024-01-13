from flask import Flask, render_template, request
#import jsonify
from keras.models import load_model
import requests
import pickle
import pandas as pd
import numpy as np
import matplotlib

app = Flask(__name__)
model = pickle.load(open(r'E:\DATA SCIENCE\TechQ-Konnect_Internship\Project_2(Cancer Category Prediction)\Model\model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("login.html")
database={'admin':'123'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('index.html')

#@app.route('/', methods=['GET'])
#def Home():
 #   return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        value1= float(request.form['value1'])
        value2= float(request.form['value2'])
        value3= float(request.form['value3'])
        value4= float(request.form['value4'])
        value5= float(request.form['value5'])
        value6= float(request.form['value6'])
        value7= float(request.form['value7'])
        value8= float(request.form['value8'])
        value9= float(request.form['value9'])
        value10= float(request.form['value10'])
        
        
        print("Donne")
        prediction = model.predict([[value1,value2,value3,value4,value5,value6,value7,value8,value9,value10
                                     ,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10
                                     ,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10
                                     ,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10
                                     ,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10
                                     ,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10
                                     ,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10
                                     ,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10
                                     ,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10
                                     ,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10
                                     ,value1,value2,value3,value4,value5,value6]])
        print("Done")
        
        
        return render_template('index.html', prediction_text = prediction )
                
if __name__=="__main__":
    app.run(debug=True)
