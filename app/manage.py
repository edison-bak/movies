# 장고의 다양한 명령어를 실행하기 위한 파일. 임의변경 X
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # Django의 설정 모듈을 환경 변수로 설정합니다. 이를 통해 Django가 프로젝트의 설정을 올바르게 로드
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leaderboard.settings")
    try:
        # Django의 관리 명령을 실행하는 역할을 합니다. 이 함수는 일반적으로 Django 프로젝트의 
        # 진입점 스크립트에서 호출되며, 커맨드 라인에서 입력한 명령을 해석하여 해당 명령을 실행
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Django 프로젝트의 관리 명령을 실행하는 함수입니다. 이 함수는 커맨드 라인에서 전달된 인자들을 받아서 해당 명령을 실행
    execute_from_command_line(sys.argv)

'''if __name__ == "__main__": 구문을 사용하지 않고 main() 함수를 호출하면, 스크립트가 모듈로 사용될 때에도 
main() 함수가 실행되어 버리게 됩니다. 이는 스크립트가 모듈로 사용될 때는 주로 함수나 클래스의 정의만 필요한데,
이들이 불필요하게 실행되는 것을 방지하기 위함'''
if __name__ == "__main__":
    main()
