# -*- coding: utf-8 -*-

import sys
import unittest
from PyQt4.QtGui import QApplication
import SearchBarTests, ViewEntryDialogTests


if __name__ == "__main__":
    app = QApplication(sys.argv)
    suite = unittest.TestLoader().loadTestsFromTestCase(SearchBarTests.SearchBarTests)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(ViewEntryDialogTests.ViewEntryDialogTests)
    fullSuite = unittest.TestSuite([suite, suite2])
    runner=unittest.TextTestRunner(verbosity=1)
    runner.run(fullSuite)



