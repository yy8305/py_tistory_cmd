from .auth import *
from .server import *


USAGE = """USAGE:
    tistory post

    tistory category <blog_name>
    tistory post <blog_name> <category_id> <file_path>"""

def main():
    if len(sys.argv) < 2:
        print(USAGE, file=sys.stderr)
        return

    command = sys.argv[1]
    auth = Auth()
    if command == 'login':
        print('login')
    elif command == 'post':
        print('post')
    else:
        print(USAGE, file=sys.stderr)
        return