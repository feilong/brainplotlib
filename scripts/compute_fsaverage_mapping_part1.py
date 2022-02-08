import os
import numpy as np

from brainplotlib3d import ValuesIcoorder, Surface, plot_to_file


if __name__ == '__main__':
    # nv = 1175  # 588 + 587
    nv = 4**7 * 10 + 2
    v = np.arange(nv * 2, dtype=int)
    c1 = v // 256 **2
    c2 = (v // 256) % 256
    c3 = v % 256
    c = np.stack([c1, c2, c3], axis=1) / 255.
    v = np.array_split(c, 2, axis=0)
    values = ValuesIcoorder(v[0], v[1], fill_nan=0.8, space='fsaverage', icoorder=7)

    for surf_type in ['inflated', 'pial', 'midthickness', 'white']:
        out_fn = f'fsaverage_{surf_type}.npy'
        if os.path.exists(out_fn):
            continue

        zoom = 0.015
        if surf_type == 'inflated':
            zoom = 0.013

        surf = Surface(surf_type, 'FS')
        surf.add_colors(values)
        actors = surf.get_actors(ambient=1, diffuse=0, specular=0)

        img = plot_to_file([actors[0]], [actors[1]],
                    surf.focal_points, out_fn=None,
                    zoom=zoom, magnification=1, aa_frames=1)
        np.save(out_fn, img)
        exit(0)
