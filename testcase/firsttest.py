import unittest
from appium import webdriver

from android.desired_capabilities import get_desired_capabilities

#https://hungc.tistory.com/82
class TestFirst(unittest.TestCase):
    dc = {}
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.dc = get_desired_capabilities("eribank.apk")
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", cls.dc)
        print("lm setUpClass")

    def setUp(self) -> None:
        print("lm setUp")

    def test_0001title(self):
        from android.test_helper import is_alert_exist
        print("0001")
        self.assertFalse(is_alert_exist(self.driver))


    def test_0002title(self):
        print("test2")

    def test_something(self):
        print("test3")
        self.assertEqual(True, True)  # add assertion here

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

if __name__ == '__main__':
    unittest.main()
