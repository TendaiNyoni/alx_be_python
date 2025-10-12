from volume_cuboid import *
import unittest

class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2),8)
        self.asserAlmostEqual(cuboid_volume(1),1)
        self.assertAlmostEqual(cuboid_volume(0),0)

    def test_input_value(self):
        self.assertRaises(SyntaxError, IndentationError, ModuleNotFoundError, cuboid_volume, True)
