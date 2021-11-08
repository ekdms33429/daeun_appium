from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
현재 {package/activity}
adb shell dumpsys window | find "mCurrentFocus"
"""

# 팝업 알림(alert)가 떠있는지 확인
def is_alert_exist(webdriver):
    from selenium.common.exceptions import NoAlertPresentException
    try:
        webdriver.switch_to.alert
        return True

    except NoAlertPresentException:
        return False

#text와 동일한 toast 존재 여부 확인
def is_toast_exist(webdriver, text, timeout=2, poll_frequency=0.5):
    try:
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
        WebDriverWait(webdriver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
        return True
    except:
        return False

def find_element_by_tmpmatching(driver, thr, cap_path, tmp_img):
    #thr > 일치하는 정도 = 이정도 일치하면 True 처리됨
    #cap_path > 캡쳐본 저장 경로
    #tmp_img > 기획서 이미지 or 찾을 이미지 대상
    import cv2
    import numpy as np

    cap_img = cv2.imread(cap_path) #원본 이미지
    cap_imgray = cv2.cvtColor(cap_img, cv2.COLOR_BGR2GRAY) #원본 이미지
    template = cv2.imread(tmp_img, cv2.IMREAD_GRAYSCALE) # 템플릿 이미지, grayscale 이미지 사용
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(cap_imgray, template, cv2.TM_CCOEFF_NORMED)#템플릿 매칭 함수 matchTemplate(원본 이미지, 템플릿 이미지, 템플릿 매칭 플래그) / 이미지는 8비트의 단일 채널 이미지 사용
        #매칭 수식 TM_SQDIFF / TM_SQDIFF_NORMED / TM_CCORR / TM_CCORR_NORMED / TM_CCOEFF / TM_CCOEFF_NORMED
        #(W, H) 원본 이미지 크기 / (w, h) 템플릿 이미지 크기
        # 결과값은 32비트 단일 채널, (W-w+1, H-h+1) 배열의 크기
        # 템플릿 이미지로 비교하기 때문에 검출된 이미지 또한 템플릿 이미지와 동일한 크기

    loc = np.where(res >= thr) # (array_row, array_column) row = y, column = x

    for pt in zip(*loc[::-1]):
        cv2.rectangle(cap_img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    #일치하는 영역 중앙 좌표 Tap 동작
    TouchAction(driver).tap(x=pt[0] + w / 2, y=pt[1] + h / 2).perform()
