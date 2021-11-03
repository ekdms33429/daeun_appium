import unittest
from appium import webdriver

from android.desired_capabilities import get_desired_capabilities

class FirstTest(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        self.dc = get_desired_capabilities("eribank.apk")
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    def test_something(self):
        print("test")
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
