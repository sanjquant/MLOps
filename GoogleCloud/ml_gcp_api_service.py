from flask import Flask, request

import pickle
import numpy as np


local_classifier = pickle.load(open('../pickle_files/classifier.pickle', 'rb'))
local_scaler = pickle.load(open('../pickle_files/sc.pickle', 'rb'))

app = Flask(__name__)


@app.route('/model', methods=['POST'])
def predict_purchase():
    request_data = request.get_json(force=True)
    age = request_data['age']
    print(age)
    salary = request_data['salary']
    print(salary)
    new_predict = local_classifier.predict(
        local_scaler.transform(np.array([[age, salary]])))

    return "The Prediction from GCP API is {}".format(new_predict)



"""
If you want to run the app in the Cloud - Say Goofle cloud.
"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8005, debug=True)   ## putting host -'0.0.0.0' makes the app available outside the google local cloud instance
