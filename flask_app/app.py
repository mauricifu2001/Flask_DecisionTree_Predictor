"""
This code is used to predict whether or not a student drops out 
of school based on some socioeconomic variables such as mother's occupation 
and father's occupation. We use 2 paths, origin and outcome. Finally, we use a 
decision tree model to make predictions.
"""

from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('DecisionTree_model.pkl')


@app.route('/', methods=['GET', 'POST'])
def index():
    global prediction
    prediction = None   
    if request.method == 'POST':
        try:
            data = {
                # Extract data from home.html
                'Marital status' : [int(request.form['Estado civil'])],
                'Application mode': [int(request.form['Aplication mode'])],
                'Application order' : [float(request.form['Aplication order'])],
                'Course' : [int(request.form['Course'])],
                "Daytime/evening attendance\t" : [int(request.form['Daytime'])],
                'Previous qualification' : [int(request.form['Previous qualification'])],
                'Previous qualification (grade)' : [float(request.form['Previous qualification grade'])],
                'Nacionality' : [int(request.form['Nacionality'])],
                "Mother's qualification" : [int(request.form['Mother qualification'])],
                "Father's qualification" : [int(request.form['Father qualification'])],
                "Mother's occupation" : [int(request.form['Mother occupation'])],
                "Father's occupation" : [int(request.form['Father occupation'])],
                'Admission grade' : [float(request.form['Admision grade'])],
                'Displaced' : [int(request.form['Displaced'])],
                'Educational special needs' : [int(request.form['Special needs'])],
                'Debtor' : [int(request.form['Deptor'])],
                'Tuition fees up to date' : [int(request.form['Tuition fees'])],
                'Gender' : [int(request.form['Gender'])],
                'Scholarship holder' : [int(request.form['Scholarship'])],
                'Age at enrollment' : [float(request.form['Age'])],
                'International' : [int(request.form['International'])],
                'Curricular units 1st sem (credited)' : [float(request.form['Curricular credited'])],
                'Curricular units 1st sem (enrolled)' : [float(request.form['Curricular enrolled'])],
                'Curricular units 1st sem (evaluations)' : [float(request.form['Curricular evaluations'])],
                'Curricular units 1st sem (approved)' : [float(request.form['Curricular approved'])],
                'Curricular units 1st sem (grade)' : [float(request.form['Curricular grade'])],
                'Curricular units 1st sem (without evaluations)' : [float(request.form['Curricular without evaluations'])],
                'Curricular units 2nd sem (credited)' : [float(request.form['Curricular credited2'])],
                'Curricular units 2nd sem (enrolled)' : [float(request.form['Curricular enrolled2'])],
                'Curricular units 2nd sem (evaluations)' : [float(request.form['Curricular evaluations2'])],
                'Curricular units 2nd sem (approved)' : [float(request.form['Curricular approved2'])],
                'Curricular units 2nd sem (grade)' : [float(request.form['Curricular grade2'])],
                'Curricular units 2nd sem (without evaluations)' : [float(request.form['Curricular without evaluations2'])],
                'Unemployment rate' : [float(request.form['Unemployment rate'])],
                'Inflation rate' : [float(request.form['Inflation rate'])],
                'GDP' : [float(request.form['GDP'])]
            }
        
            # Create a dataframe using 'data' dictionary
            df = pd.DataFrame(data)
            

            # Make prediction
            prediction_val = model.predict(df)
            if prediction_val == "Dropout":
                prediction = 'Dropout'
            else:
                prediction = 'Graduate'
            
        except Exception as e:
            # print(e) # Log the error for debugging
            prediction = "Error processing data. Check the inputs, please"
        # It redirect us to result page using "def result()""
        return redirect(url_for('result'))
    
    return render_template('home.html', prediction=prediction) 

# Result Showed
@app.route('/result')
def result():
    # Retrieves the prediction from the global variable or database.
    return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
