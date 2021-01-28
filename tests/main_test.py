from tistory_cmd import *

USAGE = """USAGE:
    tistory post

    tistory category <blog_name>
    tistory post <blog_name> <category_id> <file_path>"""


def main():
    command = 'category_list'
    auth = Auth()
    blog = Blog()
    if command == 'login':
        print('login')
    elif command == 'info':
        blog.info()
    elif command == 'category_list':
        blog.category_list()
    else:
        print(USAGE, file=sys.stderr)
        return


if __name__ == '__main__':
    main()