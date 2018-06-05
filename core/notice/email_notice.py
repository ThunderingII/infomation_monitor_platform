from email.mime.text import MIMEText
import smtplib
from email.header import Header


class Email(object):
    def __init__(self, smtp_server, user_email_address, password, port=25):
        self.smtp_server = smtp_server
        self.user_email_address = user_email_address
        self.password = password
        self.port = port

    def sent_email(self, content, to_addr):
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = 'IMP<%s>' % self.user_email_address
        message['To'] = 'IMP_rec<%s>' % to_addr

        subject = '信监平台：' + content
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.smtp_server, self.port)  # 25 为 SMTP 端口号
            smtpObj.login(self.user_email_address, self.password)
            smtpObj.sendmail('<%s>' % self.user_email_address, '<%s>' % to_addr, message.as_string())
            print("邮件发送成功")
        except Exception as e:
            print('>' * 40 + str(e))



