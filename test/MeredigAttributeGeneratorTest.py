import unittest
import pandas as pd
from CompositionEntry import CompositionEntry
from ElementFractionAttributeGenerator import ElementFractionAttributeGenerator
from MeredigAttributeGenerator import MeredigAttributeGenerator
from ValenceShellAttributeGenerator import ValenceShellAttributeGenerator
import numpy.testing as np_tst

class MeredigAttributeGeneratorTest(unittest.TestCase):
    def test_attribute_generator(self):
        # Make a list of CompositionEntry's.
        entries = [CompositionEntry(composition="FeO")]

        # Make generators.
        eg = ElementFractionAttributeGenerator()
        mg = MeredigAttributeGenerator()
        vg = ValenceShellAttributeGenerator()

        # Generate features.
        f1 = eg.generate_features(entries)
        f2 = mg.generate_features(entries, lookup_path="../lookup-data/")
        f3 = vg.generate_features(entries, lookup_path="../lookup-data/")

        # Final results.
        features = pd.concat([f1, f2, f3], axis=1)

        # Test results.
        self.assertEquals(129, len(features.columns))
        self.assertEquals(129, features.values[0].size)

        self.assertEquals(0.5, features.values[0][25])
        self.assertEquals(0.5, features.values[0][7])
        np_tst.assert_array_almost_equal([35.92, 12.0, 3.0, 18, 17, 66, 99,
                                          1.61, 2.635, 2, 2, 3, 0, 2.0 / 7.0,
                                          2.0 / 7.0, 3.0 / 7.0, 0],
                                         features.values[0][112:], decimal=2)