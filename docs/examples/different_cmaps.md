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

# Use different colormaps

This example shows how to use different colormaps.

```{glue:} different_cmaps
```

```{code-cell}python
import numpy as np
from brainplotlib import brain_plot
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
v = rng.random((1175, ))
```
```{margin} Change the colormap
The `cmap` parameter of `brain_plot` can use any `matplotlib` colormaps in a similar way as `plt.plot`.
```
```{code-cell}python
:tags: ["remove-output"]
fig, axs = plt.subplots(2, 2, dpi=300, figsize=([_/300 + 1 for _ in [1728, 1560]]))
cmaps = ['viridis', 'jet', 'bwr', 'plasma']
for i in range(2):
    for j in range(2):
        ax = axs[i][j]
        cmap = cmaps[i*2+j]
        img = brain_plot(v, vmax=1, vmin=0, cmap=cmap)
        ax.imshow(img)
        ax.axis('off')
        ax.set_title(cmap)
plt.show()
```
```{code-cell}python
:tags: ["remove-cell"]
from myst_nb import glue
glue('different_cmaps', fig, display=False)
```

{{ gallery_link }}
