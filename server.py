from flask import Flask, request, jsonify
import numpy as np
import joblib
import os

app = Flask(__name__)

if(os.path.exists('./model/model.joblib')):
    with open('./model/model.joblib','rb') as f:
        try:
            model = joblib.load(f)
        except:
            print('Error loading model file.')
else:
    print('Could not locate the model file!')



@app.route('/', methods=['GET'])
def default():
    return 'OK'

@app.route('/', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    array = np.array([[data['LSTAT'], data['RM']]])
    prediction = model.predict(array)
    response_data ={}
    response_data['response'] = prediction.tolist()
    response_data['message'] = 'Success!'
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')