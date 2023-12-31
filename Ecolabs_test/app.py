from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse, abort
import random
import json

'''
-pip install falsk
-pip install flask_restful
-pip install json
'''

app = Flask(__name__)
api = Api(app)
labs = {
    "1": {"Name": "ecolab 1", "temperature": round(random.uniform(-10, 45), 0),
          "humidity": round(random.uniform(40, 70), 0),
          "pressure": round(random.uniform(980, 1020), 0)},
    "2": {"Name": "ecolab 2", "temperature": round(random.uniform(-10, 45), 0),
          "humidity": round(random.uniform(40, 70), 0),
          "pressure": round(random.uniform(980, 1020), 0)},
    "3": {"Name": "ecolab 3", "temperature": round(random.uniform(-10, 45), 0),
          "humidity": round(random.uniform(40, 70), 0),
          "pressure": round(random.uniform(980, 1020), 0)},
    "4": {"Name": "ecolab 4", "temperature": round(random.uniform(-10, 45), 0),
          "humidity": round(random.uniform(40, 70), 0),
          "pressure": round(random.uniform(980, 1020), 0)},
    "5": {"Name": "ecolab 5", "temperature": round(random.uniform(-10, 45), 0),
          "humidity": round(random.uniform(40, 70), 0),
          "pressure": round(random.uniform(980, 1020), 0)}
}

with open('Ecolabs.json', 'w') as out_fill:
    json.dump(labs, out_fill)
    print("écriture terminer")

with open('Ecolabs.json', 'r') as labo:
    ecolabs = json.load(labo)

parser = reqparse.RequestParser()
parser.add_argument('param', type=str, help='Parameter to update')
parser.add_argument('values', type=str, help='Values to update')
class Ecolabs(Resource):
    def get(self):
        return ecolabs


class Ecolab(Resource):
    def get(self, id):
        return ecolabs[id]

    def post(self, id):
        args = parser.parse_args()
        param = args['param']
        values = args['values']

        if id in ecolabs:
            ecolabs[id][param] = values
            with open('Ecolabs.json', 'w') as out_file:
                json.dump(ecolabs, out_file)
            return ecolabs[id]
        else:
            abort(404, message="Ecolab {} doesn't exist".format(id))


@app.route('/')
def index():
    return render_template('index.html', ecolabs=ecolabs)


api.add_resource(Ecolabs, '/ecolabs')
api.add_resource(Ecolab, '/ecolab/<id>')

if __name__ == '__main__':
    app.run(port=7000, debug=True)
