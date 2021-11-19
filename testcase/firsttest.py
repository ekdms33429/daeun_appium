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
        print("setUpClass")

    #New User: 앱 최초 실행 > 안내 팝업
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
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'account page tab button')]")))
            self.driver.find_element_by_accessibility_id("account page tab button").click()
            self.driver.implicitly_wait(5)
            cardtext1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[1]").get_attribute("text")
            cardtext2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]").get_attribute("text")
            cardbtn = self.driver.find_element_by_id("ctrip.english:id/btn_upgrade")

            self.assertEqual(cardtext1, "트립닷컴 회원이면 최대 50% 할인혜택이?")
            self.assertEqual(cardtext2, "회원가입까지 딱 한 단계! 지금 가입하고 회원전용 시크릿 특가 확인하세요.")
            self.assertEqual(cardbtn.get_attribute("text"), "로그인/회원가입")

            self.driver.find_element_by_id("ctrip.english:id/iv_dialog_close").click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "unlogin_tvSignIn")))

            #Test Precedure
            self.driver.find_element_by_id("ctrip.english:id/unlogin_tvSignIn").click()
            if self.driver.current_activity == "com.ctrip.ibu.account.module.login.LoginTypeActivity":
                loginbtn = self.driver.find_element_by_accessibility_id("mainlogin_login_btn")
                login_list = ["이메일 또는 휴대폰 번호로 로그인", "이메일 또는 휴대폰 번호로 로그인하기"]
                self.assertIn(loginbtn.get_attribute("text"), login_list)
                loginbtn.click()
            else:
                assert False

        except TimeoutException:
            print("TimeoutException")
            assert False

        except NoSuchElementException:
            print("NoSuchElementException")
            assert False

    #LoginActivity
    def test_0003login(self):
        print("0003")
        try:
            if self.driver.current_activity == "com.ctrip.ibu.account.module.login.LoginActivity":
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@text, '트립닷컴 로그인하기')]")))
                accountText = self.driver.find_element_by_accessibility_id("accountlogin_account_edt")
                pwText = self.driver.find_element_by_accessibility_id("accountlogin_password_edt")
                forgotpwText = self.driver.find_element_by_id("ctrip.english:id/forgot_password_text")
                loginBtn = self.driver.find_element_by_accessibility_id("test_login_sign_in")
                policyText = self.driver.find_element_by_id("ctrip.english:id/account_login_policy")

                self.assertEqual(accountText.get_attribute("text"), "이메일 주소/아이디/휴대전화")
                self.assertEqual(pwText.get_attribute("text"), "비밀번호")
                self.assertEqual(forgotpwText.get_attribute("text"), "비밀번호를 분실하셨나요?")
                self.assertEqual(loginBtn.get_attribute("text"), "로그인")
                self.assertEqual(policyText.get_attribute("text"), "계속 진행 시, 트립닷컴 예약 규정 및 개인정보 처리방침을 읽었으며 이에 동의합니다.")

                accountText.send_keys("ekdms33429@gmail.com")
                pwText.send_keys("!!!kde0818")
                loginBtn.click()

        except NoSuchElementException:
            assert False

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        #time.sleep(600)
        #cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
