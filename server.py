from flask import Flask, request, jsonify
import requests
import numpy as np
import joblib
import boto3
import os
import time

app = Flask(__name__)

def get_model_from_s3():
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    s3 = boto3.resource('s3', aws_access_key_id=access_key,
     aws_secret_access_key=secret_key)
    s3.Bucket('mlbucketbp').download_file('model.joblib',
     'model.joblib')

if(os.path.exists('./model/model.joblib')):
    with open('./model/model.joblib','rb') as f:
        try:
            model = joblib.load(f)
        except:
            print('Error loading model file.')
elif('HEROKU' in os.environ):
    print('Heroku environment detected.')
    try:
        get_model_from_s3()
        model = joblib.load('model.joblib')
    except:
        print('There was an error obtaining the file from S3.')


@app.route('/', methods=['GET'])
def default():
    return 'OK'

@app.route('/', methods=['POST'])
def simulate_prediction():
    prediction = {}
    
    for _ in range(400):
        prediction = predict(request)
    return prediction

def predict(request):
    data = request.get_json(force=True)
    array = np.array([[data['LSTAT'], data['RM']]])
    prediction = model.predict(array)
    response_data ={}
    response_data['response'] = prediction.tolist()
    response_data['message'] = 'Success!'
    return jsonify(response_data)

if __name__ == '__main__':
    time.sleep(20)
    app.run(host='0.0.0.0')
    print('Started!')