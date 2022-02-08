This is a Python package that plots data on cortical surface.

![brain image](https://github.com/feilong/brainplotlib/raw/main/images/random_data_with_colorbar.png)

## Installation
The package can be installed with pip:
```bash
pip install brainplotlib
```

## Example usage

```Python
import numpy as np
from brainplotlib import brain_plot

## Generate some random data
# In this case it's icoorder3 resolution (642 vertices per hemisphere), and
# the non-cortical vertices have been masked out (588 and 587 remaining
# vertices for the left and right hemisphere, respectively).
rng = np.random.default_rng(0)
v = rng.random((1175, ))

img, scale = brain_plot(v, vmax=1, vmin=0, cmap='viridis', return_scale=True)
```

The rendered image is a NumPy array.
It can be rendered using `matplotlib`:
```Python
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(img.shape[1] / 200, img.shape[0] / 200), dpi=200)
plt.imshow(img)
plt.axis('off')
cbar = plt.colorbar(scale, shrink=0.8, aspect=30)
plt.savefig('random_data_with_colorbar.png', bbox_inches='tight')
plt.show()
```

Alternatively, the high-resolution image can be saved directly using `cv2`.
```Python
import cv2
cv2.imwrite(
    'random_data.png',
    np.round(img[:, :, [2, 1, 0]] * 255).astype(np.uint8))
```

## Citation
If you use this software in your publications, please cite it [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5979819.svg)](https://doi.org/10.5281/zenodo.5979819)
```bibtex
@software{brainplotlib,
  author       = {Ma Feilong and
                  Guo Jiahui and
                  M. Ida Gobbini and
                  James V. Haxby},
  title        = {{brainplotlib: plotting brain data on cortical 
                   surface}},
  month        = feb,
  year         = 2022,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.5979819},
  url          = {https://doi.org/10.5281/zenodo.5979819}
}
```
