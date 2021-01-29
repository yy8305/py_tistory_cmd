from . import config
import requests, json


class Tis_blog_post:
    def __init__(self):
        self.output_type = 'json'
        print('blog init')

    # 블로그 정보 출력
    def info(self):
        """
            GET https://www.tistory.com/apis/blog/info?
            access_token={access-token}
            &output={output-type}

            응답
            id: 사용자 로그인 아이디
            userId: 사용자 id
            blogs
                url: 티스토리 기본 url
                secondaryUrl: 독립도메인 url
                title: 블로그 타이틀
                description: 블로그 설명
                default: 대표블로그 여부 (Y/N)
                blogIconUrl: 블로그 아이콘 URL
                faviconUrl: 파비콘 URL
                profileThumbnailImageUrl: 대표이미지 썸네일 URL
                profileImageUrl: 대표이미지 URL
                blogId: 블로그 아이디
                nickname: 블로그에서의 닉네임
                role: 블로그 권한
                statistics: 블로그 컨텐츠 개수
                post: 글 수
                comment: 댓글 수
                trackback: 트랙백 수
                guestbook: 방명록 수
                invitation: 초대장 수
        """
        url = 'https://www.tistory.com/apis/blog/info'
        data = {'access_token': config.config['access_token'], 'output': self.output_type}
        res = requests.get(url, params=data)
        print(res.url)
        if res.status_code == 200:
            print(json.dumps(res.json(), indent=4, ensure_ascii=False))

        else:
            print(json.dumps(res.json(), indent=4, ensure_ascii=False))

    # 블로그의 카테고리 리스트 얻기
    def category_list(self):
        """
        GET https://www.tistory.com/apis/category/list?
        access_token={access-token}
        &output={output-type}
        &blogName={blog-name}

        blogName: Blog 이름
        """
        url = 'https://www.tistory.com/apis/category/list'
        data = {'access_token': config.config['access_token'], 'output': self.output_type, 'blogName': config.config['blog_name']}
        res = requests.get(url, params=data)

        if res.status_code == 200:
            print('==================category list==================')
            print('[ID] = [카테고리명]')
            print('-------------------------------------------------')
            categories = res.json()["tistory"]["item"]["categories"]
            for category in categories:
                print(category["id"] + " = " + category["label"])
        else:
            print(json.dumps(res.json(), indent=4, ensure_ascii=False))

    # 블로그에 글쓰기
    def post_write(self, category_id, title, content, tag):
        url = 'https://www.tistory.com/apis/post/write'
        visibility = 3
        published = ''
        slogan = ''
        acceptComment = 1
        password = ''
        '''
        blogName: Blog Name (필수)
        title: 글 제목 (필수)
        content: 글 내용
        visibility: 발행상태 (0: 비공개 - 기본값, 1: 보호, 3: 발행)
        category: 카테고리 아이디 (기본값: 0)
        published: 발행시간 (TIMESTAMP 이며 미래의 시간을 넣을 경우 예약. 기본값: 현재시간)
        slogan: 문자 주소
        tag: 태그 (',' 로 구분)
        acceptComment: 댓글 허용 (0, 1 - 기본값)
        password: 보호글 비밀번호
        '''
        data = {'access_token': config.config['access_token'], 'output': self.output_type, 'blogName': config.config['blog_name'], 'title': title,
                'content': content, 'visibility': visibility, 'category': category_id, 'published': published,
                'slogan': slogan, 'tag': tag, 'acceptComment': acceptComment, 'password': password}
        res = requests.post(url, data=data)
        print(res.url)
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.json())