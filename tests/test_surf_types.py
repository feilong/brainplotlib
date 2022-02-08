import os
import numpy as np
import importlib.util
from brainplotlib import brain_plot


class TestSurfaceTypes:
    def test_inflated_surface(self, tmp_path):
        rng = np.random.default_rng()
        values = rng.random((588, )), rng.random((587, ))
        img, scale = brain_plot(*values, vmax=1, vmin=0, cmap='viridis', return_scale=True, surf_type='inflated')
        from matplotlib import cm
        assert isinstance(scale, cm.ScalarMappable)
        assert img.shape in [(1560, 1728, 4), (1560, 1728, 3)]
        assert img.dtype == np.float64
        assert np.all(img <= 1)
        assert np.all(img >= 0)
        if importlib.util.find_spec('cv2'):
            import cv2
            cv2.imwrite(os.path.join(tmp_path, 'test_inflated.png'), np.round(img * 255).astype(np.uint8)[:, :, [2, 1, 0, 3]])

    def test_pial_surface(self, tmp_path):
        rng = np.random.default_rng()
        values = rng.random((588, )), rng.random((587, ))
        img, scale = brain_plot(*values, vmax=1, vmin=0, cmap='viridis', return_scale=True, surf_type='pial')
        from matplotlib import cm
        assert isinstance(scale, cm.ScalarMappable)
        assert img.shape in [(1560, 1728, 4), (1560, 1728, 3)]
        assert img.dtype == np.float64
        assert np.all(img <= 1)
        assert np.all(img >= 0)
        if importlib.util.find_spec('cv2'):
            import cv2
            cv2.imwrite(os.path.join(tmp_path, 'test_pial.png'), np.round(img * 255).astype(np.uint8)[:, :, [2, 1, 0, 3]])

    def test_midthickness_surface(self, tmp_path):
        rng = np.random.default_rng()
        values = rng.random((588, )), rng.random((587, ))
        img, scale = brain_plot(*values, vmax=1, vmin=0, cmap='viridis', return_scale=True, surf_type='midthickness')
        from matplotlib import cm
        assert isinstance(scale, cm.ScalarMappable)
        assert img.shape in [(1560, 1728, 4), (1560, 1728, 3)]
        assert img.dtype == np.float64
        assert np.all(img <= 1)
        assert np.all(img >= 0)
        if importlib.util.find_spec('cv2'):
            import cv2
            cv2.imwrite(os.path.join(tmp_path, 'test_midthickness.png'), np.round(img * 255).astype(np.uint8)[:, :, [2, 1, 0, 3]])

    def test_white_surface(self, tmp_path):
        rng = np.random.default_rng()
        values = rng.random((588, )), rng.random((587, ))
        img, scale = brain_plot(*values, vmax=1, vmin=0, cmap='viridis', return_scale=True, surf_type='white')
        from matplotlib import cm
        assert isinstance(scale, cm.ScalarMappable)
        assert img.shape in [(1560, 1728, 4), (1560, 1728, 3)]
        assert img.dtype == np.float64
        assert np.all(img <= 1)
        assert np.all(img >= 0)
        if importlib.util.find_spec('cv2'):
            import cv2
            cv2.imwrite(os.path.join(tmp_path, 'test_white.png'), np.round(img * 255).astype(np.uint8)[:, :, [2, 1, 0, 3]])
