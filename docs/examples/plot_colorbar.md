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

```{code-cell}python
import numpy as np
from brainplotlib import brain_plot
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
v = rng.random((1175, ))
```
```{margin} Get color scale information
The `return_scale` parameter allows returning the color scale information along with the image itself, which can then be used by `plt.colorbar`.
```
```{code-cell}python
img, scale = brain_plot(v, vmax=1, vmin=0, cmap='viridis', return_scale=True)
```
```{code-cell}python
:tags: ["remove-output"]
fig = plt.figure(figsize=(img.shape[1] / 300, img.shape[0] / 300), dpi=300)
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
