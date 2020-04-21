from flask import Flask, request, jsonify
import pickle
import numpy as np
from waitress import serve

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    array = np.array([[data['LSTAT'], data['RM']]])
    prediction = model.predict(array)
    response_data ={}
    response_data['response'] = prediction.tolist()
    response_data['message'] = 'Success!'
    return jsonify(response_data)

serve(app, host='0.0.0.0', port=5000)