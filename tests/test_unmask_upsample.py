import numpy as np
from brainplotlib import prepare_data, unmask_and_upsample


class TestUnmaskUpsample:
    def test_icoorder5_masked(self):
        lh = np.arange(9372)
        rh = np.arange(9370) + 9372
        values = unmask_and_upsample(lh, rh, 'fsaverage', 5, True)
        assert np.nanmin(values) == 0
        assert np.nanmax(values) == 18741
        assert np.any(np.isnan(values))

    def test_icoorder5_nonmasked(self):
        lh = np.arange(10242)
        rh = np.arange(10242) + 10242
        values = unmask_and_upsample(lh, rh, 'fsaverage', 5, False)
        assert values.min() == 0
        assert values.max() == 20483
        assert np.all(np.isfinite(values))

    def test_icoorder7_nonmasked(self):
        lh = np.arange(163842)
        rh = np.arange(163842) + 163842
        values = unmask_and_upsample(lh, rh, 'fsaverage', 7, False)
        assert values.min() == 0
        assert values.max() == 327683
        assert np.all(np.isfinite(values))

class TestPrepareData:
    def test_tuple_input(self):
        lh = np.arange(9372)
        rh = np.arange(9370) + 9372
        values = prepare_data((lh, rh))
        assert values.shape == (327684, )

    def test_list_input(self):
        lh = np.arange(9372)
        rh = np.arange(9370) + 9372
        values = prepare_data([lh, rh])
        assert values.shape == (327684, )

    def test_serial_input(self):
        lh = np.arange(9372)
        rh = np.arange(9370) + 9372
        values = prepare_data(lh, rh)
        assert values.shape == (327684, )

    def test_concatenated_input(self):
        lh = np.arange(9372)
        rh = np.arange(9370) + 9372
        values = prepare_data(np.concatenate([lh, rh], axis=0))
        assert values.shape == (327684, )
