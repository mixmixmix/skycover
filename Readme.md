# Read me

Based on opencv tutorials, nothing fancy here..

This program uses Otsu thresholding (normal thresholding but with threshold based on image histogram assuming bi-modal distribution of pixel intensities). It works on the blue channel, as it has the best contrast between sky and other objects. Then it uses morphological erosion (expands black areas) to account for lost coverage due to fact that images are taken against the light source so edges are naturally overexposed.

![skycover](http://mixmixmix.github.io/static/skycover.png)
