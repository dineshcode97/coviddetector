import numpy as np
from flask import Flask,render_template,request
import pickle
import joblib as jb

app = Flask(__name__)
model = jb.load('mycovidmodel.pkl')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect',methods=['POST'])
def detect():
    int_features = [x for x in request.form.values()]
    if float((x[1]) >=96 and float(x[1])) <98.6:
        t1=0
        t2=0
    elif float((x[1]) >=98.6 and float(x[1])) <102:
        t1=1
        t2=0
    else:
        t1=0
        t2=1
    gen=int(x[2])
    if int(x[3]) >=1 int(x[3])<15:
        a1,a2,a3,a4=0,0,0,0
    elif int(x[3]) >=15 int(x[3])<35:
        a1,a2,a3,a4=1,0,0,0
    elif int(x[3]) >=35 int(x[3])<55:
        a1,a2,a3,a4=0,1,0,0
    elif int(x[3]) >=55 int(x[3])<75:
        a1,a2,a3,a4=0,0,1,0
    else:
        a1,a2,a3,a4=0,0,0,1
    travel=int(x[4])
    cough=int(x[5])
    sore=int(x[6])
    sleep=int(x[7])
    weakness==int(x[8])
    los=int(x[9])
    diab==int(x[10])
    bp=int(x[11])
    immunity=int(x[12])
    appetide=int(x[13])
    chestpain==int(x[14])
    heartproblem=int(x[15])
    breathing=int(x[16])
    lungdiseases=int(x[17])
    kidneydiseases=int(x[18])
    test=np.array([gen,cough,sore,weakness,breathing,sleep,chestpain,travel,diab,heartproblem,lungdiseases,immunity,bp,kidneydiseases,appetide,los,a1,a2,a3,a4,t1,t2])
    predict=model.predict([[test]])
    if predict == 0:
        return render_template('norisk.html')
    elif predict == 1:
        return render_template('lowrisk.html')
    else:
        return render_template('highrisk.html')

if __name__ == "__main__":
    app.run(debug=True)
