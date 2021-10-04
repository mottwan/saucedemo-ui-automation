import os
import sys
sys.path.append(sys.path[0] + "/...")

from unittest import TestLoader, TestSuite, TextTestRunner
from tests.test_purchase_flow import TestPurchaseFlow

if __name__ == "__main__":
    test_loader = TestLoader()
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(TestPurchaseFlow),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
