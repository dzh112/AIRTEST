import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendMail(object):
    def __init__(self, username, passwd, recv, title, content, email_host, test_report, port=25):
        self.username = username
        self.passwd = passwd
        self.recv = recv
        self.title = title
        self.test_report = test_report
        self.content = content
        self.file = self.new_report()
        self.email_host = email_host
        self.port = port

    def send_mail(self):
        msg = MIMEMultipart()
        # 发送内容的对象
        if self.file:  # 处理附件的
            att = MIMEApplication(open(self.file, 'rb').read())
            att.add_header('Content-Disposition', 'attachment', filename=self.file)
            msg.attach(att)
        msg.attach(MIMEText(self.content))  # 邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = self.recv  # 接收者账号列表
        self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        # 发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
        except Exception as e:
            print('出错了。。', e)
        else:
            print('发送成功！')
        self.smtp.quit()

    def new_report(self):
        lists = os.listdir(self.test_report)
        print(lists)
        lists.sort(key=lambda fn: os.path.getmtime(self.test_report + "\\" + fn))
        print(lists)
        file_new = os.path.join(self.test_report, lists[-1])
        print(file_new)
        return file_new

if __name__ == '__main__':
    m = SendMail(
        email_host='mail.yozosoft.com',
        username='dzh', passwd='user1057',
        recv='dzh@yozosoft.com',
        title='测试完成',
        content="手机电量: %s" % os.popen("adb shell dumpsys battery |findstr level").readline().split()[1].strip(),
        test_report=r'F:\AIRTEST\reports'
    )
    m.send_mail()

