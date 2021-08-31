from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class GetJDCode(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user', type=str)
        parser.add_argument('code', type=str)
        print(parser.parse_args())
        return parser.parse_args()

api.add_resource(GetJDCode, '/publish')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)