from flask import Flask,render_template,request,jsonify
app = Flask(__name__ , template_folder='templates')
import pickle
import joblib
from joblib import dump, load
model = joblib.load('marriage_age_predict_model.pkl')

@app.route('/' )
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict' ,methods = ["POST"])
def submit ():
    if request.method == "POST":
        height_cms = int(request.form['height_cms'])
        gender = int(request.form['gender'])
        religion = int(request.form['religion'])
        caste = int(request.form['caste'])
        mother_tongue = int(request.form['mother_tongue'])
        country = int(request.form['country'])
        #result = model.predict([[height_cms, gender, religion, caste, mother_tongue, country]])
        result = [height_cms, gender, religion, caste, mother_tongue, country]
        print(result)
        result1 = model.predict([result])
        print(result1)
        display = "Prediction of ideal age for marriage {}".format(str(round(result1[0],1)))
        return render_template("home.html", data=[display])


    else :
        return "Something Went wrong"






if __name__ == "__main__":
    app.run(debug=True)
