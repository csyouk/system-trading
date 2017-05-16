원글은 [이곳](https://wikidocs.net/book/110)을 참고한다.

* 만약, 하다가 뭔가 안되면, [여기 참조](http://www.daishin.co.kr/ctx_kr/sc_customer/sg_notice/svc_notice/tujainfo_notice_web.html)
1. python 32-bit 용으로 돌려야 한다.(cpcybos util이 32bit용에 맞게 구현이 되어 있는듯?)
    - pycharm을 쓰는 경우, interpreter설정을 32bit에 맞게 해놓을 것.
2. COM(Component Object Model)을 파이썬에서 사용할 수 있도록 만들어 놓은 wrapper를 설치해야 함.
    - pip install pypiwin32
3. 개발을 할 때에는 cp cybo plus에 접속이 되어있는 상태여야 한다.

    