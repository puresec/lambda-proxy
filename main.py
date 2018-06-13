from flask import Flask, request
import boto3
import json

app = Flask(__name__)


@app.route('/functions/<profile_name>/<region_name>/<function_name>', methods=['POST'])
def invoke(profile_name, region_name, function_name):
    session = boto3.Session(profile_name=profile_name)
    lambda_client = session.client('lambda', region_name=region_name)
    event = request.get_json(force=True)
    response = lambda_client.invoke(FunctionName=function_name, Payload=json.dumps(event))
    return response['Payload'].read().decode('utf-8')


app.run(host="127.0.0.1", port=8082)
