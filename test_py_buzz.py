import unittest
import py_buzz

class TestPyBuzz(unittest.TestCase):

    def test_a_normal_number(self):
        pyBuzz = py_buzz.PyBuzz(100)
        assert pyBuzz.check(1) == 1
        
    def test_number_divisible_by_three_should_return_py(self):
        pyBuzz = py_buzz.PyBuzz(3)
        assert pyBuzz.check(3) == 'Py'

    def test_number_divisible_by_five_should_return_buzz(self):
        pyBuzz = py_buzz.PyBuzz(5)
        self.assertEquals(pyBuzz.check(5), 'Buzz')

    def test_number_divisible_by_both_three_and_five_should_return_pybuzz(self):
        pyBuzz = py_buzz.PyBuzz(15)
        self.assertEquals(pyBuzz.check(15), 'PyBuzz')