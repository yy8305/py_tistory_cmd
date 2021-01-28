import setuptools

# 실행 : python setup.py install
setuptools.setup(
    name="tistory_cmd", # 패키지 이름
    version="0.2", # 버전
    license='MIT', # 라이센스
    author="hongpark",  # 패키지 제작자 이름
    author_email="yy8305@naver.com",  # 패키지 제작자 이메일
    description="tistory command", # 패키지 요약 설명
    long_description=open('README.md',encoding='UTF8').read(),  # 패키지 긴설명
    url="https://github.com/yy8305/py_tistory_cmd",  # github url 등
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    entry_points={
        # 콘솔에서 해당 패키지 사용할경우
        'console_scripts': [
            'tistory_cmd=tistory_cmd.main:main',
        ],
    },
    # 다운로드 할 라이브러리
    install_requires=['pyfiglet >= 0.8']
)