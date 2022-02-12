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

# Use different types of surface

By default `brain_plot` uses the `inflated` surface.
This can be changed to the `pial`, `white`, or `midthickness` (average of `pial` and `white`) surface using the `surf_type` parameter.

```{glue:} different_surfaces
```

```{code-cell}python
import numpy as np
from brainplotlib import brain_plot
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
v = rng.random((1175, ))
```
```{code-cell}python
:tags: ["remove-output"]
fig, axs = plt.subplots(2, 2, dpi=300, figsize=([_/300 + 1 for _ in [1728, 1560]]))
surf_types = ['inflated', 'midthickness', 'pial', 'white']
for i in range(2):
    for j in range(2):
        ax = axs[i][j]
        surf_type = surf_types[i*2+j]
        img = brain_plot(v, vmax=1, vmin=0, cmap='rainbow', surf_type=surf_type)
        ax.imshow(img)
        ax.axis('off')
        ax.set_title(f'{surf_type} surface')
plt.show()
```
```{code-cell}python
:tags: ["remove-cell"]
from myst_nb import glue
glue('different_surfaces', fig, display=False)
```

{{ gallery_link }}
