[![PyPI](https://img.shields.io/pypi/v/brainplotlib)](https://pypi.org/project/brainplotlib/)
[![Downloads](https://static.pepy.tech/badge/brainplotlib)](https://pepy.tech/project/brainplotlib)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/brainplotlib)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5979819.svg)](https://doi.org/10.5281/zenodo.5979819)

`brainplotlib` is a Python package that plots data on cortical surface.
It's designed to have minimal requirements --- only `NumPy` and `matplotlib`.

![brain image](https://github.com/feilong/brainplotlib/raw/main/images/example_data_with_colorbar.png)

## Installation
The package can be installed with pip:
```bash
pip install brainplotlib
```

## Example usage

**See the [examples gallery](https://feilong.github.io/brainplotlib/examples/index.html) for all code examples with detailed explanations.**

```Python
import numpy as np
from brainplotlib import brain_plot, example_data

# The example_data is icoorder5 resolution (10242 vertices per hemisphere),
# and the non-cortical vertices have been masked out (9372 and 9370 remaining
# vertices for the left and right hemisphere, respectively).

img, scale = brain_plot(
    example_data, vmax=10, vmin=-10, cmap='seismic', return_scale=True)
```

The rendered image is a NumPy array.
It can be rendered using `matplotlib`:
```Python
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(img.shape[1] / 200, img.shape[0] / 200), dpi=200)
plt.imshow(img)
plt.axis('off')
cbar = plt.colorbar(scale, shrink=0.8, aspect=30)
plt.savefig('example_data_with_colorbar.png', bbox_inches='tight')
plt.show()
```

Alternatively, the high-resolution image can be saved directly using `OpenCV`.
```Python
import cv2
cv2.imwrite(
    'example_data.png',
    np.round(img[:, :, [2, 1, 0]] * 255).astype(np.uint8))
```

## Citation
If you use this software in your publications, please cite it [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5979819.svg)](https://doi.org/10.5281/zenodo.5979819)
```bibtex
@software{brainplotlib,
  author       = {Ma Feilong and Guo Jiahui and M. Ida Gobbini and James V. Haxby},
  title        = {brainplotlib: plotting brain data on cortical surface},
  month        = feb,
  year         = 2022,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.5979819},
  url          = {https://doi.org/10.5281/zenodo.5979819}
}
```
