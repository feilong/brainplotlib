---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Save the high-res image

This example shows how to plot random data on the brain and save it as an image file.

![](save_image_pillow.png)


## Render the image

The `brain_plot` function renders the image based on data `v` and returns a NumPy array.
The Numpy array has a `np.float64` dtype, and the range of its values is 0--1.

```{code-cell}python
import numpy as np
from brainplotlib import brain_plot

rng = np.random.default_rng(0)
v = rng.random((1175, ))

img = brain_plot(v, vmax=1, vmin=0, cmap='viridis')

print(img.dtype, img.shape)
print(img.max(), img.min())
```


## Save the image
The rendered image can be saved using the package of your choice:

```{code-cell}python
:tags: ["remove-cell"]
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(img.shape[1] / 200, img.shape[0] / 200), dpi=200)
ax = fig.add_axes([0, 0, 1, 1])
ax.imshow(img)
ax.axis('off')
plt.savefig('save_image_matplotlib.png')
plt.close()
```
```{code-cell}python
:tags: ["remove-cell"]
from PIL import Image
im = Image.fromarray(
    np.round(img * 255).astype(np.uint8))
im.save('save_image_pillow.png')
```
```{code-cell}python
:tags: ["remove-cell"]
from myst_nb import glue
glue('save_image', im, display=False)
```
```{code-cell}python
:tags: ["remove-cell"]
import cv2
## The default channel order of OpenCV is BGR rather than RGB.
reorder = {3: [2, 1, 0], 4: [2, 1, 0, 3]}[img.shape[2]]
cv2.imwrite(
    'save_image_opencv.png',
    np.round(img[:, :, reorder] * 255).astype(np.uint8))
```

````{tabbed} Using matplotlib
```python
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(img.shape[1] / 200, img.shape[0] / 200), dpi=200)
ax = fig.add_axes([0, 0, 1, 1])
ax.imshow(img)
ax.axis('off')
plt.savefig('save_image_matplotlib.png')
plt.close()
```
````
````{tabbed} Using Pillow
```python
from PIL import Image
im = Image.fromarray(
    np.round(img * 255).astype(np.uint8))
im.save('save_image_pillow.png')
```
```{note}
The code block above requires that the [Pillow package](https://pillow.readthedocs.io/en/stable/index.html) has been installed.
```
````
````{tabbed} Using OpenCV
```python
import cv2
## The default channel order of OpenCV is BGR rather than RGB.
reorder = {3: [2, 1, 0], 4: [2, 1, 0, 3]}[img.shape[2]]
cv2.imwrite(
    'save_image_opencv.png',
    np.round(img[:, :, reorder] * 255).astype(np.uint8))
```
```{note}
The code block above requires that [OpenCV](https://opencv.org/) and its Python bindings to be installed.
```
````

## Comparison of saved images
````{panels}
:column: col-4

Using matplotlib
^^^
![](save_image_matplotlib.png)
---

Using Pillow
^^^
![](save_image_pillow.png)
---

Using OpenCV
^^^
![](save_image_opencv.png)

````

{{ gallery_link }}
