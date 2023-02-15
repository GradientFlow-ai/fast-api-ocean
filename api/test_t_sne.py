import json
from t_SNE import fit_tsne

f = open("api/demo_embedding.txt", "r")
data_as_string = f.read()
data = json.loads(data_as_string)

def test_t_sne():
    visualisation = fit_tsne(data)

    assert visualisation is not None
