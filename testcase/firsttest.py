import unittest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

    def test_0001title(self):
        print("0001")

        current_activity = self.driver.current_activity
        if current_activity == "com.ctrip.ibu.myctrip.main.module.home.IBUHomeActivity":
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'new user page 3 title')]")))
                print("new user page 3 title")
                titleText = self.driver.find_element_by_accessibility_id("new user page 3 title").get_attribute("text")
                subtitleText = self.driver.find_element_by_accessibility_id("new user page 3 desc").get_attribute("text")
                subscribeBtn = self.driver.find_element_by_accessibility_id("new user page ok button").get_attribute("text")
                notsubscribeBtn = self.driver.find_element_by_accessibility_id("new user page not button").get_attribute("text")

                self.assertEqual(titleText, "빠를수록 저렴한, 얼리버드 특가 혜택")
                self.assertEqual(subtitleText, "알림 기능을 사용할까요?")
                self.assertEqual(subscribeBtn, "확인")
                self.assertEqual(notsubscribeBtn, "나중에")

            except TimeoutException:
                print("new user page 0 title")
                skipBtn = self.driver.find_element_by_accessibility_id("new user page skip button")
                firstText = self.driver.find_element_by_accessibility_id("new user page 0 title").get_attribute("text")
                nextText = self.driver.find_element_by_id("ctrip.english:id/nextText").get_attribute("text")
                nextBtn = self.driver.find_element_by_accessibility_id("new user page next button").get_attribute("clickable")
                pager = self.driver.find_element_by_id("ctrip.english:id/pager")

                self.assertEqual(skipBtn.get_attribute("text"), "건너뛰기")
                self.assertTrue(skipBtn.get_attribute("clickable"))
                self.assertEqual(firstText, "트립닷컴이 알려주는 할인 항공편 및 호텔 특가 소식")
                self.assertEqual(nextText, "다음")
                self.assertTrue(nextBtn)
                self.assertTrue(pager.get_attribute("scrollable"))

    def test_0002title(self):
        print("test2")
        self.assertEqual(True, True)  # add assertion here

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
