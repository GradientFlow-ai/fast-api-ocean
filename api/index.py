from flask import Flask, request
import json

from .db_access import find_embeddings
from .t_SNE import fit_tsne

app = Flask(__name__)

@app.route("/api", methods = ['POST', 'GET'])
def hello_world():
    data = find_embeddings()
    tsne = fit_tsne(data)
    print(tsne[0:5])

    response = {
        "message": "Hello, World!",
        "location": "AWS Lambda"
    }

    if request.method == 'POST':
        print(request.json)
    return "<p>Hello, World!</p>"
