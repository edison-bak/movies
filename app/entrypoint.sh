#!/bin/sh

# 환경 변수 $DATABASE가 "postgres"인 경우에만 아래의 명령을 수행.
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
# nc 명령어를 사용하여 PostgreSQL 데이터베이스의 호스트($SQL_HOST)와 
# 포트($SQL_PORT)가 사용 가능해질 때까지 대기
    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done
# PostgreSQL이 시작되었음을 출력
    echo "PostgreSQL started"
fi
# manage.py의 (환경설정) 데이터베이스를 비우는 명령입니다. 이 명령을 실행하면 데이터베이스의 모든 테이블이 삭제되고 초기화
python manage.py flush --no-input
# Django 어플리케이션의 manage.py의 마이그레이션을 수행
python manage.py migrate

# exec "$@"은 현재 스크립트를 종료하고 전달된 명령을 실행
exec "$@"