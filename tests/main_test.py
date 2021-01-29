from tistory_cmd import *

USAGE = """USAGE:
    # 블로그 정보 보기
    tistory_cmd info
    
    # 카테고리 목록 보기
    tistory_cmd category
    
    # 글쓰기
    tistory_cmd post <category_id> <제목> <태그>"""


def main():
    if len(sys.argv) < 2:
        print(USAGE, file=sys.stderr)
        return

    command = sys.argv[1]
    auth = Auth()

    blog = Blog()
    if command == 'info':
        blog.info()
    elif command == 'category':
        blog.category_list()
    elif command == 'post':
        blog.category_list()
    else:
        print(USAGE, file=sys.stderr)
        return

main()