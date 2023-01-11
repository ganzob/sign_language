from sklearn.decomposition import PCA
import numpy as np


def run_pca(embeddings, dim=3):
    pca = PCA(n_components=dim)
    temp = embeddings-np.mean(embeddings, axis=0)
    a = pca.fit_transform(temp)
    return a
