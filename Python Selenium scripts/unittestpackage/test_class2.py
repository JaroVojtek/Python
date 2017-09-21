import unittest

class TestClass2(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("*#" * 30)
        print("Class2 -> Class level setUP")
        print("*#" * 30)

    def setUp(self):
        print("Class2 -> setUP")

    def test_methodA(self):
        print("Running Class2 -> method A")

    def test_methodB(self):
        print("Running Class2 -> method B")

    def tearDown(self):
        print("Class2 -> tearDown")

    @classmethod
    def tearDownClass(self):
        print("*#" * 30)
        print("Class2 -> class level tearDown")
        print("*#" * 30)


if __name__=='__main__':
    if __name__ == '__main__':
        unittest.main(verbosity=2)


