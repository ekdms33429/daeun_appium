import os
from typing import Any, Dict, Optional

def PATH(p: str) -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', p))

def get_desired_capabilities(app: Optional[str] = None) -> Dict[str, Any]:
    desired_caps: Dict[str, Any] = {
        "deviceName": "V30",
        "platformName": "Android",
        "automationName": "Uiautomator2",
        "udid": "LGMV300S6fa91a67",
    }

    if app is not None:
        #PC 내부에 있는 apk 사용 시 default 값: "C:\Users\사용자"
        local_pathtxt = PATH(os.path.join('../../Desktop', 'apk', app))

        #프로젝트 내부에 있는 apk 사용 시 default 값: "현재 프로젝트 경로"
        project_pathtxt = os.path.abspath(os.path.join(os.path.dirname(__file__), '../apps', app))

        #print("로컬 경로: ",local_pathtxt)
        #print("프로젝트 내 경로: ", project_pathtxt)

        desired_caps['app'] = local_pathtxt

    return desired_caps