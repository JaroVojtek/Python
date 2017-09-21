import unittest

class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("*#" * 30)
        print("Class1 -> Class level setUP")
        print("*#" * 30)

    def setUp(self):
        print("Class1 -> setUP")

    def test_methodA(self):
        print("Running Class1 -> method A")

    def test_methodB(self):
        print("Running Class1 -> method B")

    def tearDown(self):
        print("Class1 -> tearDown")

    @classmethod
    def tearDownClass(self):
        print("*#" * 30)
        print("Class1 -> class level tearDown")
        print("*#" * 30)


if __name__=='__main__':
    if __name__ == '__main__':
        unittest.main(verbosity=2)


