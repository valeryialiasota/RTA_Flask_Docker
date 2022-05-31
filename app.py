from flask import Flask, request
import pickle
from flask import jsonify

app = Flask(__name__)

@app.route("/")
@app.route('/isAlive')
def index():
    return "true"

@app.route('/prediction/api/v1.0/some_prediction', methods=['GET'])
def get_prediction():
    sepal_length = float(request.args.get('sl'))
    petal_length = float(request.args.get('pl'))
    loaded_model=pickle.load(open('model_rta.pkl', "rb"))
    prediction=loaded_model.predict([[sepal_length, petal_length]])
    return jsonify(features=[sepal_length,petal_length], predicted_class=str(prediction))

if __name__ == '__main__':
   app.run(port=80,host='0.0.0.0')





