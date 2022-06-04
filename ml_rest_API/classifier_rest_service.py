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
    # new_predict_proba = local_classifier.predict_proba(local_scaler.transform(np.array([[age, salary]])))[:,1]
    return "The Prediction is {}".format(new_predict)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
