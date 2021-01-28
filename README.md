# 설정(config.json)
- blog_name : 블로그명 (https://[블로그명].tistory.com)
- app_id : 앱 id (아래 #수동 api 토큰 받는 법 -> 1번 에서 확인 가능)
- secret_key : 시크릿키 (아래 #수동 api 토큰 받는 법 -> 1번 에서 확인 가능)
- access_code : 접근 코드, 한번 접속하면 사라짐 (아래 #수동 api 토큰 받는 법 -> 2번 에서 확인 가능)
- access_token : 액세스 토큰  (아래 #수동 api 토큰 받는 법 -> 3번 에서 확인 가능)

# 모듈 다운로드
```python
pip install pyfiglet
```


# 수동 api 토큰 받는 법 (토큰 유지시간 = 1시간)
1. https://www.tistory.com/guide/api/manage/register 접속해서 앱등록 ( 앱등록후 앱관리에서 app id, secret key 확인 가능)
2. https://www.tistory.com/oauth/authorize?client_id=[App id]&redirect_uri=[앱등록에서 입력한 redirect url]&response_type=code&state=someValue 접속하면 코드 확인 가능
3. https://www.tistory.com/oauth/access_token?client_id=[App id]&client_secret=[Secret key]&redirect_uri=[앱등록에서 입력한 redirect url]&code=[2번에서 얻은 코드 값]&grant_type=authorization_code 해당 url 접속하여 access token 확인 가능
   - 2번에서 얻은 코드가 기간 만료시 아래 에러가 발생하는것 같습니다.

        ```
            This page contains the following errors:

            error on line 1 at column 1: Document is empty

            Below is a rendering of the page up to the first error.
        ```
   - 위 에러가 발생하더라도 3번 url에서 발생한 파라미터를 한번 확인해보시기 바랍니다
   
   - 에러 발생시 2번 내용 부터 다시 진행해 보시길 바랍니다.


# 참고 url
- 토큰 받아오기 
  - https://limsee.com/325
- python 예제 github
  - https://github.com/chandong83/tistory-api-example
- python 예제2 github (tistory helper)
  - https://github.com/adunStudio/TistoryHelper
- 입력 예제
  - https://kimmj.github.io/python/python-beautiful-cli/
- setup.py 설정
  - https://item4.blog/2015-11-21/Arguments-of-setuptools.setup/


