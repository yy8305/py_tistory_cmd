# tistorycmd
- markdown 형식으로 작성된 파일을 html 형식으로 변환하여 티스토리에 업로드 해줍니다.  

[![PyPI - Version](https://img.shields.io/pypi/v/tistorycmd?style=for-the-badge)](https://pypi.org/project/tistorycmd)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/tistorycmd?label=DOWNLOADS&style=for-the-badge)](https://pypi.org/project/tistorycmd)

# 설치
```
# 파일로 다운로드시
python setup.py install

# pip로 다운로드 하기
pip install tistorycmd
```

# 사용법
```
CMD, 터미널 창에서 실행

# 블로그 정보 보기
tistorycmd info

# 카테고리 목록 보기
tistorycmd category

# 글쓰기
tistorycmd post <제목> <내용|파일경로> <category_id> <태그>
```

# 사용시 주의사항
- 이미지는 아래 형태대로 쓰셔야하며 한줄마다 쓰시면 자동으로 업로드 됩니다.
    ```
    ![screenshot1](./screenshot.png)
    ``` 
- 이미지 경로가 url(http://~)이 들어간경우는 파일이 업로드되지 않고 해당 url로 해서 내용이 적용됩니다.

- 이미지가 업로드 된경우 마크다운 파일 내용에 이미지가 업로드된 url이 자동으로 들어갑니다. 

- 글쓰기, 수정 시 해당 글들은 자동으로 발행됩니다.

# 기타 모듈 다운로드
```python
pip install pyfiglet

pip install mistune (anaconda의 경우 설치 되어있습니다.)
```

# tistorycmd 모듈 사용시
```python
from tistorycmd import *

auth = Auth()  # 로그인, oauth, 토큰 관련 클래스
blog = Blog()  # 글쓰기, 블로그 관련 클래스

blog.info() #블로그 정보 불러오기

# 나머지는 소스 참고
```

# 설정(config.json)
- blog_name : 블로그명 (https://[블로그명].tistory.com)
  
- app_id : 앱 id (아래 #수동 api 토큰 받는 법 -> 1번 에서 확인 가능)
  
- secret_key : 시크릿키 (아래 #수동 api 토큰 받는 법 -> 1번 에서 확인 가능)
  
- access_code : 접근 코드, 한번 접속하면 사라짐 (아래 #수동 api 토큰 받는 법 -> 2번 에서 확인 가능)
  
- access_token : 액세스 토큰  (아래 #수동 api 토큰 받는 법 -> 3번 에서 확인 가능)

# 수동 api 토큰 받는 법
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


