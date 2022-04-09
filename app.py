#!/usr/bin/env python
# coding: utf-8

# In[7]:


from flask import Flask,request,render_template
app = Flask(__name__)
import joblib


# In[8]:


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        print(income,age,default)
        income = float(income)
        age = float(age)
        loan = float(loan)
        model1 = joblib.load("CART")
        pred1 = model1.predict([[income,age,loan]])
        model2 = joblib.load("RF")
        pred2 = model2.predict([[income,age,loan]])
        model3 = joblib.load("GB")
        pred3 = model3.predict([[income,age,loan]])
        return(render_template("index.html", result1=pred1, result2=pred2, result3=pred3))
    else:
        return(render_template("index.html", result1="FAIL", result2="FAIL", result3="FAIL"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




