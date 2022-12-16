from flask import render_template
from modules import modules
from flask import request, jsonify
from flask_cors import cross_origin
from modules import modules, cyk

def configure_routes(app):
    @app.route("/")
    def index():
        hello = modules.hello()
        content = modules.content()
        return render_template("index.html", hello=hello, content=content)
    
    @app.route("/parser", methods=['POST'])
    @cross_origin()
    def parser():
        requestString = request.get_json()
        string = requestString['string']
        result = cyk.is_accepted(string)
        return jsonify({
            'result': result
        })
