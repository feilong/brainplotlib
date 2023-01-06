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

# Plot a colorbar along with the image

This example shows how to plot a colorbar besides the brain.

```{glue:} with_colorbar
```

```{margin} Example data
The example data is a NumPy array combining masked data of both hemispheres, based on a face-selectivity map from [Jiahui et al. (2020)](https://doi.org/10.1016/j.neuroimage.2019.116458) [Figure 5](https://www.sciencedirect.com/science/article/pii/S1053811919310493#fig5).
```
```{code-cell}python
import numpy as np
from brainplotlib import brain_plot, example_data
import matplotlib.pyplot as plt

print(example_data.shape, example_data.dtype)
```
```{margin} Get color scale information
The `return_scale` parameter allows returning the color scale information along with the image itself, which can then be used by `plt.colorbar`.
```
```{code-cell}python
img, scale = brain_plot(
    example_data, vmax=10, vmin=-10, cmap='seismic', return_scale=True)
```
```{code-cell}python
:tags: ["remove-output"]
fig = plt.figure(
    figsize=(img.shape[1] / 300, img.shape[0] / 300), dpi=300)
plt.imshow(img)
plt.axis('off')
cbar = plt.colorbar(scale, shrink=0.8, aspect=30)
plt.show()
```

```{code-cell}python
:tags: ["remove-cell"]
from myst_nb import glue
glue('with_colorbar', fig, display=False)
```

{{ gallery_link }}
