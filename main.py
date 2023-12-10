from flask import Flask, send_file,request
from flask_cors import CORS, cross_origin
from wp_dockercompose import wp_docker_compose, convert_txt_to_yml
app = Flask(__name__)

@app.route('/')
def index():
    return("Welcome to Dockercompose API for WordPress")

@app.route('/download/',methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)

def download_file(na=None):
    file_data = request.args
    # Specify the directory path where the file is located
    name=file_data["name"]
    web_port=file_data["web_port"]
    db_port=file_data["db_port"]
    wp_docker_compose(name,web_port,db_port)
    convert_txt_to_yml(f'dockercompose.txt',"docker compose.yml")
    return send_file("docker compose.yml", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
