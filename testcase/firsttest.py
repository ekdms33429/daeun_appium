import time
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

    #New User 앱 최초 실행 > 안내 팝업
    def test_0001newuserpage(self):
        print("0001")
        titleText_list = ['트립닷컴이 알려주는 할인 항공편 및 호텔 특가 소식', '신속한 고객센터, 30초 이내 응답률로 안심 여행!',
                      '리워드 전용 혜택으로 더욱 알뜰하게', '빠를수록 저렴한, 얼리버드 특가 혜택']
        current_activity = self.driver.current_activity
        if current_activity == "com.ctrip.ibu.myctrip.main.module.home.IBUHomeActivity":
            try:
                page = self.driver.find_element_by_accessibility_id("new user page 0 title")
                if (page.is_displayed()):
                    #WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, "new user page 0 title")))
                    print("new user page 0 title")
                    print("len: ", len(titleText_list))
                    for i in range(0, len(titleText_list)-1):
                        skipBtn = self.driver.find_element_by_accessibility_id("new user page skip button")
                        title = "new user page "+str(i)+" title"
                        print("i: ", i, " title: ", title)
                        titleText = self.driver.find_element_by_accessibility_id(title).get_attribute(
                            "text")
                        nextText = self.driver.find_element_by_id("nextText").get_attribute("text")
                        nextBtn = self.driver.find_element_by_accessibility_id("new user page next button")
                        pager = self.driver.find_element_by_id("pager")

                        self.assertEqual(skipBtn.get_attribute("text"), "건너뛰기")
                        self.assertTrue(skipBtn.get_attribute("clickable"))
                        print(titleText_list[i])
                        self.assertEqual(titleText, titleText_list[i])
                        self.assertEqual(nextText, "다음")
                        self.assertTrue(nextBtn.get_attribute("clickable"))
                        self.assertTrue(pager.get_attribute("scrollable"))

                        nextBtn.click()
                        self.driver.save_screenshot('../capimg/screencap.png')

            except TimeoutException:
                print("TimeoutException")
                #assert False

            except NoSuchElementException:
                print("NoSuchElementException")
                #assert False

            finally:
                print("new user page 3 title")
                titleText3 = self.driver.find_element_by_accessibility_id("new user page 3 title").get_attribute("text")
                subtitleText = self.driver.find_element_by_accessibility_id("new user page 3 desc").get_attribute(
                    "text")
                subscribeBtn = self.driver.find_element_by_accessibility_id("new user page ok button")
                notsubscribeBtn = self.driver.find_element_by_accessibility_id("new user page not button")

                self.assertEqual(titleText3, titleText_list[3])
                self.assertEqual(subtitleText, "알림 기능을 사용할까요?")
                self.assertEqual(subscribeBtn.get_attribute("text"), "확인")
                self.assertEqual(notsubscribeBtn.get_attribute("text"), "나중에")

                subscribeBtn.click()

                """#팝업
                content = self.driver.find_element_by_id("ctrip.english:id/contentCard")
                if (content.is_displayed()):
                    self.driver.save_screenshot('screencap.png')
                    # image comparison
                    closeBtn = self.driver.find_element_by_id("ctrip.english:id/closeIcon")
                    closeBtn.click()
                    # 홈화면 진입
                else:
                    pass"""

    #홈화면 > 하단 바 - My 계정 > 팝업 - 종료 > 로그인/회원가입
    def test_0002logintype(self):
        print("0002")
        #Pre-Condition
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "account page tab button")))
            self.driver.find_element_by_accessibility_id("account page tab button").click()
            cardtext1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[1]").get_attribute("text")
            cardtext2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]").get_attribute("text")
            cardbtn = self.driver.find_element_by_id("ctrip.english:id/btn_upgrade")

            self.assertEqual(cardtext1, "트립닷컴 회원이면 최대 50% 할인혜택이?")
            self.assertEqual(cardtext2, "회원가입까지 딱 한 단계! 지금 가입하고 회원전용 시크릿 특가 확인하세요.")
            self.assertEqual(cardbtn.get_attribute("text"), "로그인/회원가입")

            self.driver.find_element_by_id("ctrip.english:id/iv_dialog_close").click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.ID, "ctrip.english:id/unlogin_tvSignIn"))

            #Test Precedure
            self.driver.find_element_by_id("ctrip.english:id/unlogin_tvSignIn").click()
            if self.driver.current_activity == "com.ctrip.ibu.account.module.login.LoginTypeActivity":
                loginbtn = self.driver.find_element_by_accessibility_id("mainlogin_login_btn")
                self.assertEqual(loginbtn.get_attribute("text"), "이메일 또는 휴대폰 번호로 로그인하기")
                loginbtn.click()
            else:
                assert False

        except TimeoutException:
            print("TimeoutException")
            assert False

        except NoSuchElementException:
            print("NoSuchElementException")
            assert False
    """
    def test_0003login(self):
        if self.driver.current_activity == "com.ctrip.ibu.account.module.login.LoginActivity":
    """

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        #time.sleep(600)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
