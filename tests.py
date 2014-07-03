# Copyright (c) 2014 Johnnie Walker
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import unittest
import math
import copy
from affinetransform import AffineTransform

class AffineTransformTest(unittest.TestCase):

    def test_translate(self):
        translation = (100, 200)
        t = AffineTransform()
        t.translate(translation[0], translation[1])
        p = t.transformPoint(0, 0)
        for i in range(0, len(p)):
            self.assertAlmostEqual(p[i], translation[i])

    def test_rotate(self):
        t = AffineTransform()
        t.rotate(-math.pi/2.0)
        s = t.transformSize(0.0, 2.0)
        self.assertAlmostEqual(round(s[0]), 2.0)
        self.assertAlmostEqual(round(s[1]), 0.0)

    def test_scale(self):
        t = AffineTransform()
        t.scale(4.0, 3.0)
        r = t.transformRect(0, 0, 1, 1)
        re = (0, 0, 4, 3)
        for i in range(0, len(r)):
            self.assertAlmostEqual(r[i], re[i])
            
    def test_multiply(self):
        t1 = AffineTransform()
        t1.rotate(math.pi/2.0)
        t2 = AffineTransform()
        t2.translate(2, 4)
        t3 = AffineTransform()
        t3.scale(3, 5)
        
        p = (20, 20)
        
        p1 = (p[0], p[1])
        p1 = t1.transformPoint(p1[0], p1[1])
        p1 = t2.transformPoint(p1[0], p1[1])
        p1 = t3.transformPoint(p1[0], p1[1])
        
        t4 = AffineTransform()
        t4.multiply(t1)
        t4.multiply(t2)
        t4.multiply(t3)
        
        p2 = t4.transformPoint(p[0], p[1])
        
        for i in range(0, len(p1)):
            self.assertAlmostEqual(p1[i], p2[i])        
        
    def test_invert(self):
        t = AffineTransform()
        t.rotate(-math.pi/2.0)
        t.scale(4.0, 3.0)
        t.translate(100, 100)
        p = t.transformPoint(0, 0)
        t.invert()
        p = t.transformPoint(p[0], p[1])
        for i in range(0, len(p)):
            self.assertAlmostEqual(p[i], 0)        
            
    def test_copy(self):
        t1 = AffineTransform()
        t1.scale(2, 3)
        t1.rotate(3)
        t2 = copy.copy(t1)
        self.assertEqual(t1.m, t2.m)
        self.assertEqual(t1, t2)
        
    def test_equality(self):
        t1 = AffineTransform()
        t1.scale(2, 3)
        t1.rotate(3)
        t2 = AffineTransform()
        t2.scale(2, 3)
        t2.rotate(3)
        self.assertTrue(t1 == t2)
        t3 = AffineTransform()
        t3.scale(4, 5)
        self.assertFalse(t2 == t3)
        self.assertFalse(t3 == None)        
        
if __name__ == '__main__':
    unittest.main()