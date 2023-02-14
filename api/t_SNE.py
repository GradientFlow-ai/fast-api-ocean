from sklearn.manifold import TSNE
import numpy as np

def fit_tsne(data, n_components=2, perplexity=15.0, learning_rate=200.0, random_state=42, init='random'):

    # Convert to a list of lists of floats
    matrix = np.array(data)

    # Create a t-SNE model and transform the data
    tsne = TSNE(n_components, perplexity, random_state, init, learning_rate)
    vis_dims = tsne.fit_transform(matrix)
    print( vis_dims.shape )

    return vis_dims



# def fit_tsne(data, n_components=2, perplexity=15.0, early_exaggeration=12.0, learning_rate=200.0, n_iter=1000, n_iter_without_progress=300, min_grad_norm=1e-07, metric='euclidean', init='random', verbose=0, random_state=None, method='barnes_hut', angle=0.5):
