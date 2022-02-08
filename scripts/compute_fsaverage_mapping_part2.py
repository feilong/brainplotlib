import cv2
import numpy as np


if __name__ == '__main__':
    for surf_type in ['inflated', 'pial', 'midthickness', 'white']:
        img = np.load(f'fsaverage_{surf_type}.npy')
        nv = 4**7 * 10 + 2
        mask = (img[:, :, 3] == 0.0)
        img = np.round(img[:, :, :3] * 255).astype(int)
        v = ((img[:, :, 0] * 256**2) + (img[:, :, 1] * 256) + img[:, :, 2])
        print(v.shape, mask.shape)
        v[mask] = -1
        np.save(f'fsaverage_to_{surf_type}_image.npy', v)
        print(v.max(), v.min(), np.unique(v).shape)
