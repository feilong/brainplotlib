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

# Example

```{code-cell}
import numpy as np
from brainplotlib import brain_plot

rng = np.random.default_rng(0)
v = rng.random((1175, ))

img, scale = brain_plot(v, vmax=1, vmin=0, cmap='viridis', return_scale=True)
```

```{code-cell}
:tags: [remove-input]
from myst_nb import glue
from PIL import Image
im = np.round(img * 255).astype(np.uint8)
glue('example', Image.fromarray(im), display=False)
```

```{code-cell}
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(img.shape[1] / 200, img.shape[0] / 200), dpi=200)
plt.imshow(img)
plt.axis('off')
cbar = plt.colorbar(scale, shrink=0.8, aspect=30)
plt.savefig('random_data_with_colorbar.png', bbox_inches='tight')
plt.show()
```

```{glue:} example
```

````{panels}
:column: col-4

```{glue:} example
```
---
2
---
3
---
4
````

{glue:}`example`
