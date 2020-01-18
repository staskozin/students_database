import unittest
from tests import student_group_test, student_test, str_convert_test

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(student_test))
suite.addTests(loader.loadTestsFromModule(student_group_test))
suite.addTests(loader.loadTestsFromModule(str_convert_test))

runner = unittest.TextTestRunner(verbosity=1)
runner.run(suite)
