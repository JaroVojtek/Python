import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertFalse(a,msg='A is not False')
        b = False
        self.assertFalse(b,'B is not False')

    def test_assertEqual(self):
        a = 'Test'
        b = 'Test'
        self.assertEqual(a,b,msg="A is not equal to B")


if __name__ == '__main__':
    unittest.main(verbosity=2)