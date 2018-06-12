from core.util import config_util
from core.util import data_util
from core.util import time_util
from core.util import file_util
from core.session import platform_session
from core.notice import email_notice
import re

if __name__ == '__main__':
    cu = config_util.ConfigUtil('my_config.ini')
    pfs = platform_session.load_ps()
    if pfs is None:
        pfs = platform_session.IMP_Session()
        pfs.add_value('source', 'index_nav')
        pfs.add_value('form_email', cu.get('form_email'))
        pfs.add_value('form_password', cu.get('form_password'))
        login_respone = pfs.post('https://accounts.douban.com/login')
        file_util.write(login_respone.text, 'douban.html')
        login_data = data_util.pre_process(login_respone, data_util.ResponseType.html)

        img_tag = login_data.find('img', id='captcha_image')
        if img_tag == None:
            print('登陆成功')
        else:
            file_util.write(pfs.get(img_tag.get('src')).content, 'captcha_image.jpg', mode='wb')
            print(img_tag.get('src'))
            p = re.compile('=.+&')
            img_id = p.search(img_tag.get('src')).group(0)[1:-1]
            print(img_id)
            print(login_data.find_all('input', attrs={'type': 'hidden'}, value=True))
            ci = input('请输入验证码：')
            '''
            ck: dZjd
            source: None
            redir: https://www.douban.com
            form_email: reg@mmail.win
            form_password: zhanglin2014
            captcha-solution: respect
            captcha-id: 9qfsFkUFSQ6rXPtZfbH0Gqhk:en
            login: 登录
            '''
            pfs.add_value('source', 'index_nav')
            pfs.add_value('form_email', cu.get('form_email'))
            pfs.add_value('form_password', cu.get('form_password'))
            # pfs.add_value('ck', login_data.find('input', name='ck')['value'])
            pfs.add_value('captcha-solution', ci)
            pfs.add_value('captcha-id', img_id)
            pfs.add_value('login', '登录')
            login_respone = pfs.post('https://accounts.douban.com/login')
            login_data = data_util.pre_process(login_respone, data_util.ResponseType.html)

    html = pfs.get('https://www.douban.com/group/').text
    data = data_util.pre_process(html, data_util.ResponseType.html)
    tags = data.find_all('a', class_='title')

    print(tags)

    pfs.persistence()
