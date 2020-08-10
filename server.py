from flask import Flask, request, jsonify
import requests
import numpy as np
import joblib
import boto3
import os

app = Flask(__name__)

def configure_boto3():
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    response = s3.get_object(Bucket='mlbucketbp', Key='model.joblib')
    s3.Bucket('mlbucketbp').download_file('model.joblib', 'model.joblib')

if(os.path.exists('./model/model.joblib')):
    with open('./model/model.joblib','rb') as f:
        try:
            model = joblib.load(f)
        except:
            print('Error loading model file.')
elif('S3_BUCKET_NAME' in os.environ):
    print('Heroku environment detected.')
    try:
        configure_boto3()
        model = joblib.load('model.joblib')
    except:
        print('There was an error obtaining the file from S3.')


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