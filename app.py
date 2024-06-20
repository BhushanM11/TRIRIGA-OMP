# from flask import Flask, request
# import requests
# from requests.auth import HTTPBasicAuth

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return app.send_static_file('index.html')

# @app.route('/create-package', methods=['POST'])
# def create_package():
#     # Get data from request
#     data = request.get_json()
#     username = data.get('username')
#     package_name = data.get('packageName')
#     password = "1Password*"  # This should be hidden in production level applications
#     environment = "https://microsoft-dev.iwmsapp.com/tririga"
#     package_description = "test-pipeline-omp-description"    
    
#     # Create request URL
#     url = f'{environment}/api/p/v1/om/createEmptyPackage?packageName={package_name}&packageDescription={package_description}'

#     # Make the GET request with basic auth
#     response = requests.get(url, auth=HTTPBasicAuth(username, password))
#     return response.json()

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request
from flask_cors import CORS
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
 return app.send_static_file('index.html')

# @app.route('/create-package', methods=['POST'])
# def create_package():
#     # Get data from request
#     data = request.get_json()
#     username = data.get('username')
#     package_name = data.get('packageName')
#     password = "1Password*"  # This should be hidden in production level applications
#     environment = "https://microsoft-dev.iwmsapp.com/tririga"
#     package_description = "test-pipeline-omp-description"    
    
#     # Create request URL
#     url = f'{environment}/api/p/v1/om/createEmptyPackage?packageName={package_name}&packageDescription={package_description}'

#     # Make the GET request with basic auth
#     response = requests.get(url, auth=HTTPBasicAuth(username, password))
#     return response.json()



@app.route('/create-package', methods=['POST'])
def create_package():
    # Get data from request form (not JSON)
    data = request.form.to_dict()
    username = data['username']
    package_name = data['packageName']
    password = data['password']
    environment = data['environment']
    package_description = "test-pipeline-omp-description"

    # ... rest of the code   
    
    # Create request URL
    url = f'{environment}/api/p/v1/om/createEmptyPackage?packageName={package_name}&packageDescription={package_description}'

    # Make the GET request with basic auth
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)