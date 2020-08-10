from flask import Flask, request, jsonify
import requests
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
elif('S3_BUCKET_NAME' in os.environ):
    print('Heroku environment detected.')
    try:
        url = 'http://s3.amazonaws.com/mlbucketbp/model.joblib'
        model = requests.get(url)
    except:
        print('Error loading model file from AWS S3.')
    




@app.route('/', methods=['GET'])
def default():
    return 'OK'

@app.route('/', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    array = np.array([[data['LSTAT'], data['RM']]])
    prediction = model.predict(array)
    response_data ={}
    for i in range(0, 10000):
        print(i)
    response_data['response'] = prediction.tolist()
    response_data['message'] = 'Success!'
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')