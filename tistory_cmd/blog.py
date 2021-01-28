from . import config
import requests, json


class Blog:
    def __init__(self):
        self.output_type = 'json'

    # 해당 블로그 정보 출력
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

    # 해당 블로그의 카테고리 리스트 얻기
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
            print(json.dumps(res.json(), indent=4, ensure_ascii=False))
        else:
            print(json.dumps(res.json(), indent=4, ensure_ascii=False))

