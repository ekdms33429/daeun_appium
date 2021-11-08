import unittest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

from android.desired_capabilities import get_desired_capabilities
#https://hungc.tistory.com/82


class TestFirst(unittest.TestCase):
    dc = {}
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.dc = get_desired_capabilities("ctrip.english_7.42.2.apk")
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", cls.dc)
        print("lm setUpClass")

    def setUp(self) -> None:
        print("lm setUp")

    def test_0001title(self):
        print("0001")
        try:
            current_activity = self.driver.current_activity
            if current_activity == "com.ctrip.ibu.myctrip.main.module.home.IBUHomeActivity":
                skipBtn = self.driver.find_element_by_accessibility_id("new user page skip button")
                firstText = self.driver.find_element_by_accessibility_id("new user page 0 title").get_attribute("text")
                nextText = self.driver.find_element("ctrip.english:id/nextText").get_attribute("text")
                nextBtn = self.driver.find_element_by_accessibility_id("new user page next button").get_attribute("clickable")
                pager = self.driver.find_element("ctrip.english:id/pager")

                print(pager.get_attribute("xpath"))

                self.assertEqual(skipBtn.get_attribute("text"), "건너뛰기")
                self.assertTrue(skipBtn.get_attribute("clickable"))
                self.assertEqual(firstText, "트립닷컴이 알려주는 할인 항공편 및 호텔 특가 소식")
                self.assertEqual(nextText, "다음")
                self.assertTrue(nextBtn)
                self.assertTrue(pager.get_attribute("scrollable"))


        except NoSuchElementException:
            self.assertTrue(False)
        #self.assertTrue(is_alert_exist(self.driver))

    def test_0002title(self):
        print("test2")
        """        
        titleText = self.driver.find_element_by_accessibility_id("new user page 3 title").get_attribute("text")
        subtitleText = self.driver.find_element_by_accessibility_id("new user page 3 desc").get_attribute("text")
        subscribeBtn = self.driver.find_element_by_accessibility_id("new user page ok button").get_attribute("text")
        notsubscribeBtn = self.driver.find_element_by_accessibility_id("new user page not button").get_attribute("text")

        self.assertEqual(titleText, "빠를수록 저렴한, 얼리버드 특가 혜택")
        self.assertEqual(subtitleText, "알림 기능을 사용할까요?")
        self.assertEqual(subscribeBtn, "확인")
        self.assertEqual(notsubscribeBtn, "나중에")
        """

    def test_something(self):
        print("test3")
        self.assertEqual(True, True)  # add assertion here

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")


if __name__ == '__main__':
    unittest.main()
