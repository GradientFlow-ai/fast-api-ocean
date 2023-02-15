from sklearn.manifold import TSNE
import numpy as np

# n_components: The dimension of the space to embed into. So 2d for a 2d plot
def fit_tsne(data, n_components=2, perplexity=15.0, learning_rate=200.0, random_state=42, init='random'):

    # Convert to a list of lists of floats
    matrix = np.array(data)

    # Create a t-SNE model and transform the data
    tsne = TSNE(n_components=n_components, perplexity=perplexity, random_state=random_state, init=init, learning_rate=learning_rate)

    vis_dims = tsne.fit_transform(matrix)

    return vis_dims.tolist()
