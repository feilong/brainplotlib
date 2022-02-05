This is a Python package that plots data on cortical surface.

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

img = brain_plot(v, vmax=1, vmin=0, cmap='viridis')
```

The rendered image is a NumPy array.
It can be rendered using `matplotlib`:
```Python
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(img.shape[1] / 100, img.shape[0] / 100), dpi=100)
plt.imshow(img)
plt.axis('off')
plt.show()
```

Alternatively, the high-resolution image can be saved directly using `cv2`.
```Python
import cv2
cv2.imwrite(
    'random_data.png',
    np.round(img[:, :, [2, 1, 0]] * 255).astype(np.uint8))
```

![brain image](https://github.com/feilong/brainplotlib/raw/main/images/random_data.png)
