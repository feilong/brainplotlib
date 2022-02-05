import os
import numpy as np
import importlib.util
from brainplotlib import brain_plot


class TestPlotting:
    def test_icoorder5_masked(self, tmp_path):
        values = np.arange(9372), np.arange(9370)
        img = brain_plot(*values, vmax=18741, vmin=0, cmap=None)
        assert img.shape in [(1560, 1728, 4), (1560, 1728, 3)]
        assert img.dtype == np.float64
        assert np.all(img <= 1)
        assert np.all(img >= 0)
        if importlib.util.find_spec('cv2'):
            import cv2
            cv2.imwrite(os.path.join(tmp_path, 'test_icoorder5_masked.png'), np.round(img * 255).astype(np.uint8)[:, :, [2, 1, 0, 3]])

    def test_icoorder5_masked_random(self, tmp_path):
        rng = np.random.default_rng()
        values = rng.random((9372, )), rng.random((9370, ))
        img = brain_plot(*values, vmax=1, vmin=0, cmap=None)
        assert img.shape in [(1560, 1728, 4), (1560, 1728, 3)]
        assert img.dtype == np.float64
        assert np.all(img <= 1)
        assert np.all(img >= 0)
        if importlib.util.find_spec('cv2'):
            import cv2
            cv2.imwrite(os.path.join(tmp_path, 'test_icoorder5_masked_random.png'), np.round(img * 255).astype(np.uint8)[:, :, [2, 1, 0, 3]])

    def test_icoorder5_nonmasked(self, tmp_path):
        values = np.arange(10242), np.arange(10242)
        img = brain_plot(*values, vmax=20483, vmin=0, cmap=None)
        assert img.shape in [(1560, 1728, 4), (1560, 1728, 3)]
        assert img.dtype == np.float64
        assert np.all(img <= 1)
        assert np.all(img >= 0)
        if importlib.util.find_spec('cv2'):
            import cv2
            cv2.imwrite(os.path.join(tmp_path, 'test_icoorder5_nonmasked.png'), np.round(img * 255).astype(np.uint8)[:, :, [2, 1, 0, 3]])

    def test_icoorder5_nonmasked_random(self, tmp_path):
        rng = np.random.default_rng()
        values = rng.random((10242, )), rng.random((10242, ))
        img = brain_plot(*values, vmax=1, vmin=0, cmap=None)
        assert img.shape in [(1560, 1728, 4), (1560, 1728, 3)]
        assert img.dtype == np.float64
        assert np.all(img <= 1)
        assert np.all(img >= 0)
        if importlib.util.find_spec('cv2'):
            import cv2
            cv2.imwrite(os.path.join(tmp_path, 'test_icoorder5_nonmasked_random.png'), np.round(img * 255).astype(np.uint8)[:, :, [2, 1, 0, 3]])

    def test_icoorder3_masked(self, tmp_path):
        values = np.arange(588), np.arange(587)
        img = brain_plot(*values, vmax=1174, vmin=0, cmap=None)
        assert img.shape in [(1560, 1728, 4), (1560, 1728, 3)]
        assert img.dtype == np.float64
        assert np.all(img <= 1)
        assert np.all(img >= 0)
        if importlib.util.find_spec('cv2'):
            import cv2
            cv2.imwrite(os.path.join(tmp_path, 'test_icoorder3_masked.png'), np.round(img * 255).astype(np.uint8)[:, :, [2, 1, 0, 3]])

    def test_icoorder3_masked_random(self, tmp_path):
        rng = np.random.default_rng()
        values = rng.random((588, )), rng.random((587, ))
        img = brain_plot(*values, vmax=1, vmin=0, cmap=None)
        assert img.shape in [(1560, 1728, 4), (1560, 1728, 3)]
        assert img.dtype == np.float64
        assert np.all(img <= 1)
        assert np.all(img >= 0)
        if importlib.util.find_spec('cv2'):
            import cv2
            cv2.imwrite(os.path.join(tmp_path, 'test_icoorder3_masked_random.png'), np.round(img * 255).astype(np.uint8)[:, :, [2, 1, 0, 3]])

    def test_icoorder3_nonmasked(self, tmp_path):
        values = np.arange(642), np.arange(642)
        img = brain_plot(*values, vmax=1283, vmin=0, cmap=None)
        assert img.shape in [(1560, 1728, 4), (1560, 1728, 3)]
        assert img.dtype == np.float64
        assert np.all(img <= 1)
        assert np.all(img >= 0)
        if importlib.util.find_spec('cv2'):
            import cv2
            cv2.imwrite(os.path.join(tmp_path, 'test_icoorder3_nonmasked.png'), np.round(img * 255).astype(np.uint8)[:, :, [2, 1, 0, 3]])

    def test_icoorder3_nonmasked(self, tmp_path):
        rng = np.random.default_rng()
        values = rng.random((642, )), rng.random((642, ))
        img = brain_plot(*values, vmax=1, vmin=0, cmap=None)
        assert img.shape in [(1560, 1728, 4), (1560, 1728, 3)]
        assert img.dtype == np.float64
        assert np.all(img <= 1)
        assert np.all(img >= 0)
        if importlib.util.find_spec('cv2'):
            import cv2
            cv2.imwrite(os.path.join(tmp_path, 'test_icoorder3_nonmasked_random.png'), np.round(img * 255).astype(np.uint8)[:, :, [2, 1, 0, 3]])


class TestColormaps:
    def test_bwr_cmap(self, tmp_path):
        rng = np.random.default_rng()
        values = rng.random((588, )), rng.random((587, ))
        img = brain_plot(*values, vmax=1, vmin=0, cmap='bwr')
        assert img.shape in [(1560, 1728, 4), (1560, 1728, 3)]
        assert img.dtype == np.float64
        assert np.all(img <= 1)
        assert np.all(img >= 0)
        if importlib.util.find_spec('cv2'):
            import cv2
            cv2.imwrite(os.path.join(tmp_path, 'test_bwr_cmap.png'), np.round(img * 255).astype(np.uint8)[:, :, [2, 1, 0, 3]])

    def test_jet_cmap(self, tmp_path):
        rng = np.random.default_rng()
        values = rng.random((588, )), rng.random((587, ))
        img = brain_plot(*values, vmax=1, vmin=0, cmap='jet')
        assert img.shape in [(1560, 1728, 4), (1560, 1728, 3)]
        assert img.dtype == np.float64
        assert np.all(img <= 1)
        assert np.all(img >= 0)
        if importlib.util.find_spec('cv2'):
            import cv2
            cv2.imwrite(os.path.join(tmp_path, 'test_jet_cmap.png'), np.round(img * 255).astype(np.uint8)[:, :, [2, 1, 0, 3]])
