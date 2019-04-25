# Read me

Based on opencv tutorials, nothing fancy here..

This program uses Otsu thresholding (adapitve based on histogram assuming bi-modal distribution of pixel intensities) on blue channel to generate a black and white image. The blue channel has the best contrast between sky and other objects. Then it uses morphological erosion (expands black areas) to account for lost coverage due to fact that images are taken against the light source so edges are naturally overexposed.

