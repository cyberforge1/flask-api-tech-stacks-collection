# app/routes/helloworld.py

from flask_restx import Namespace, Resource

helloworld_bp = Namespace('helloworld', description='Helloworld route')

@helloworld_bp.route("/")
class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World!"}
