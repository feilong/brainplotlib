import os
import numpy as np
from matplotlib import cm


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
mapping = np.load(os.path.join(DIR_PATH, 'data', 'icoorder3_mapping.npy'))


def brain_plot(values, vmax, vmin, cmap=None):
    r = (vmax - values) / (vmax - vmin)
    r = np.clip(r, 0.0, 1.0)
    cmap = cm.get_cmap(cmap)
    c = cmap(r)
    c = np.concatenate([c, [[0.8] * c.shape[1], [1.0] * c.shape[1]]], axis=0)
    img = c[mapping]
    return img
