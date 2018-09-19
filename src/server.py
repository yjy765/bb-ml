# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import json
import pandas as pd
from bb_data_tore import unlabeled_raw_data, labeled_raw_data
from random_forest import get_random_forest_classification

app = Flask(__name__)
api = Api(app, prefix="/api")
CORS(app)

class Classify(Resource):
    def post(self):
        fossil_assemblage = request.get_json(force=True)
        df = pd.DataFrame(data=fossil_assemblage, index=[0])
        return {"classification":str(get_random_forest_classification(df)[0])}

api.add_resource(Classify, '/post_classification')

if __name__ == '__main__':
   app.run(port=5002, debug=True)