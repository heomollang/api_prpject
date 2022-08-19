#setup.py 파일있으면 pip로 설치가능
from setuptools  import setup   

setup(

    name = 'myapi', # 이  이름으로 패키지가 설치됨
    version = '0.0.1'  # major번호(엄청난 변화), mid번호 (기능수정이 많이 생겼을 떄), minor번호 (버그나 수정사항이 일어났을 떄 하나씩 올림)
    description = 'my api lib'
    url = 'https://github.com/heomollang/api_prpject.git'
    author = 'heomollang',
    author_email= 'heo09134@gmail.com',
    packages = ['my_api'],
    install_requires = [
        'requests'
    ] #의존이 있는 패키지 모듈 나열 ... 

)
