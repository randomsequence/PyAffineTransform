PyAffineTransform
=================

A matrix class for affine transformations in Python

A transformation specifies how points in one coordinate system map to points in another coordinate system. An affine transformation is a special type of mapping that preserves parallel lines in a path but does not necessarily preserve lengths or angles. Scaling, rotation, and translation are the most commonly used manipulations supported by affine transforms, but skewing is also possible.

You can use PyAffineTransform to transform points, sizes and rectangles from one coordinate system to another.

Rotate a point 90º about the origin:

```python

import math
from affinetransform import AffineTransform

t = AffineTransform()
t.rotate(math.pi/2)

t.transformPoint(10, 20)

# (-20.0, 10.000000000000002)
```

Translate a rectangle:

```python
t = AffineTransform()
t.translate(100, 10)
t.transformRect(0, 0, 10, 20)
# (100.0, 10.0, 10.0, 20.0)
```

Scale a size:

```python
t = AffineTransform()
t.scale(4, 4)
t.transformSize(2, 2)
# (8.0, 8.0)
```

Concatenate transformations:

```python
t = AffineTransform()
t.rotate(math.pi)
t.translate(100, 10)
t.scale(4, 4)
t.transformPoint(0, 0)
# (-100.0, -9.999999999999988)
```

There are also methods to invert, multiply (concat), compare and copy transforms.
