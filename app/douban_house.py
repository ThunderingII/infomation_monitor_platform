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
        login_data = data_util.pre_process(login_respone, data_util.ResponseType.html)

        img_tag = login_data.find('img', id='captcha_image')
        if img_tag == None:
            print('登陆成功')
        else:
            print(img_tag.get('src'))

    html = pfs.get('https://www.douban.com/group/').text
    data = data_util.pre_process(html, data_util.ResponseType.html)
    tags = data.find_all('a', class_='title')

    print(tags)

    pfs.persistence()
