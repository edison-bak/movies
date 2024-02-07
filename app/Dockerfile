# 사용할 베이스 이미지를 지정합니다.
FROM python:3.11.6-slim-bullseye

# 작업 디렉토리를 설정합니다.
WORKDIR /usr/src/app

# 환경 변수 설정
# 요약: 배포 시나리오에 최적화하기 위해 파일 쓰기를 최소화하고 버퍼링 없이 즉시 출력을 보장
# Python이 디스크에 pyc 파일(바이트코드)을 쓰지 않도록 합니다. 1로 설정되면 Python이 
# 컴파일된 바이트코드 파일을 생성하지 않도록 하며, 이는 불필요한 파일 쓰기를 줄이고 성능을 향상
ENV PYTHONDONTWRITEBYTECODE 1
# Python에 대한 버퍼 없는 모드를 활성화하기 위해 1로 설정됩니다. 버퍼 없는 모드에서는 Python이 
# 표준 스트림(stdout 및 stderr)을 버퍼링하지 않으므로 즉시 출력
ENV PYTHONUNBUFFERED 1

# apt-get update: 패키지 목록을 최신 상태로 업데이트합니다.
# apt-get -y install netcat gcc postgresql: netcat, gcc, postgresql 패키지를 설치합니다. 
# -y 플래그는 설치 중에 나오는 확인 메시지에 'yes'로 대답하여 무인 설치를 가능케 합니다.
# apt-get clean: 불필요한 패키지 캐시 및 설치된 패키지의 내려받은 파일 등을 정리합니다.
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# pip 업그레이드
RUN pip install --upgrade pip
# requirements.txt 현재 디렉토리로 복사
COPY ./requirements.txt .
# 설치
RUN pip install -r requirements.txt

# entrypoint 스크립트를 현재 디렉토리로 복사하고 실행 권한을 부여합니다.
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
# chmod +x 명령어는 파일을 실행 가능한 권한으로 변경
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . .

# 컨테이너가 시작될 때 entrypoint.sh 먼저 실행
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]