import unittest
from appium import webdriver

class MyTestCase(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        self.dc['app'] = "C:\\Users\\ekdms\\Desktop\\apk\\eribank.apk"
        self.dc['appActivity'] = ".LoginActivity"
        self.dc['platformName'] = "Android"
        self.dc['deviceName'] = "V30"
        self.dc['udid'] = "LGMV300S6fa91a67"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    def test_something(self):
        print("test")
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
