#importing necessary libraries
import pandas as pd
import numpy as np
from flask import Flask,render_template,flash,request,flash, session



app=Flask(__name__)

app.secret_key="CBJcb786874wrf78chdchsdcv"

@app.route('/')
def index():
    return render_template('index.html')



import pickle
@app.route('/prediction',methods=['POST','GET'])
def prediction():
    global x_train,y_train
    if request.method == "POST":
        f1 = request.form['f1']
        f2 = request.form['f2']
        f3 = request.form['f3']
        f4 = request.form['f4']
        f5 = request.form['f5']
        f6 = request.form['f6']
        f7 = request.form['f7']
        f8 = request.form['f8']
        f9 = request.form['f9']
        f10 = request.form['f10']
        f11 = request.form['f11']

        list = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11]

        #load the model
        model = pickle.load(open('Decision Tree.pkl','rb'))
        print(list)




        result =model.predict([list])
        result=result[0]
        print(result)
        msg = "The predicted Sale value is "+str(result)

        return render_template('prediction.html',msg=msg)

    return render_template('prediction.html')







if __name__=='__main__':
    app.run(debug=True)