import os
import numpy as np
from matplotlib import cm, colors


DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')

PLOT_MAPPING = {surf_type: np.load(os.path.join(DATA_DIR, f'fsaverage_to_{surf_type}_image.npy'))
    for surf_type in ['inflated', 'pial', 'midthickness', 'white']}

example_data = np.load(os.path.join(DATA_DIR, 'example_data.npy'))

GUESS_SEPARATE = {
    ## masked data
    # (588, 587): ('fsaverage5', 3, True),
    # (588, 587): ('fsaverage6', 3, True),
    (588, 587): ('fsaverage', 3, True),

    (2341, 2346): ('fsaverage5', 4, True),
    (2343, 2347): ('fsaverage6', 4, True),
    (2343, 2344): ('fsaverage', 4, True),

    (9354, 9361): ('fsaverage5', 5, True),
    (9372, 9369): ('fsaverage6', 5, True),
    (9372, 9370): ('fsaverage', 5, True),

    (37476, 37471): ('fsaverage6', 6, True),
    (37487, 37482): ('fsaverage', 6, True),

    (149955, 149926): ('fsaverage', 7, True),

    ## unmasked data
    (642, 642): ('fsaverage', 3, False),
    (2562, 2562): ('fsaverage', 4, False),
    (10242, 10242): ('fsaverage', 5, False),
    (40962, 40962): ('fsaverage', 6, False),
    (163842, 163842): ('fsaverage', 7, False),
}

GUESS_COMBINED = {
    ## masked data
    # 1175: ('fsaverage5', 3, True, [588]),
    # 1175: ('fsaverage6', 3, True, [588]),
    1175: ('fsaverage', 3, True, [588]),

    # 4687: ('fsaverage5', 4, True, [2341]),
    4690: ('fsaverage6', 4, True, [2343]),
    4687: ('fsaverage', 4, True, [2343]),

    18715: ('fsaverage5', 5, True, [9354]),
    18741: ('fsaverage6', 5, True, [9372]),
    18742: ('fsaverage', 5, True, [9372]),

    74947: ('fsaverage6', 6, True, [37476]),
    74969: ('fsaverage', 6, True, [37487]),

    299881: ('fsaverage', 7, True, [149955]),

    ## unmasked data
    1284: ('fsaverage', 3, False, [642]),
    5124: ('fsaverage', 4, False, [2562]),
    20484: ('fsaverage', 5, False, [10242]),
    81924: ('fsaverage', 6, False, [40962]),
    327684: ('fsaverage', 7, False, [163842]),
}


def unmask_and_upsample(lh, rh, space, icoorder, masked):
    nv = 4**icoorder * 10 + 2
    new_values = []
    for v, lr in zip([lh, rh], 'lr'):
        if masked:
            mask = np.load(os.path.join(DATA_DIR, f'mask_{space}_{lr}h.npy'))[:nv]
            vv = np.full((nv, ) + v.shape[1:], np.nan)
            vv[mask] = v
        else:
            vv = v

        if icoorder < 7:
            voronoi = np.load(os.path.join(DATA_DIR, f'voronoi_fsaverage_{lr}h_icoorder{icoorder}.npy'))
            vv = vv[voronoi]
        new_values.append(vv)
    new_values = np.concatenate(new_values, axis=0)
    return new_values


def prepare_data(*values):
    while isinstance(values, (tuple, list)) and len(values) == 1:
        values = values[0]

    if isinstance(values, (tuple, list)) and len(values) == 2:
        ## separate left and right hemisphere
        lh, rh = values
        shapes = (lh.shape[0], rh.shape[0])
        space, icoorder, masked = GUESS_SEPARATE[shapes]
        new_values = unmask_and_upsample(lh, rh, space, icoorder, masked)

    else:
        ## combined hemispheres
        space, icoorder, masked, sections = GUESS_COMBINED[values.shape[0]]
        lh, rh = np.array_split(values, sections, axis=0)
        new_values = unmask_and_upsample(lh, rh, space, icoorder, masked)

    return new_values


def brain_plot(*values, vmax, vmin, cmap=None, medial_wall_color=[0.8, 0.8, 0.8, 1.0], background_color=[1.0, 1.0, 1.0, 0.0], return_scale=False, surf_type='inflated'):
    values = prepare_data(*values)
    nan_mask = np.isnan(values)
    r = (values - vmin) / (vmax - vmin)
    r = np.clip(r, 0.0, 1.0)
    cmap = cm.get_cmap(cmap)
    c = cmap(r)
    c[nan_mask] = medial_wall_color
    c = np.concatenate([c, [_[:c.shape[1]] for _ in [medial_wall_color, background_color]]], axis=0)
    img = c[PLOT_MAPPING[surf_type]]
    if return_scale:
        norm = colors.Normalize(vmax=vmax, vmin=vmin, clip=True)
        scale = cm.ScalarMappable(norm=norm, cmap=cmap)
        return img, scale
    return img
