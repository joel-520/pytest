"""
使用python的zmail模块实现发送邮件
1.安装zmail库
    pip install zmail
    python -m pip install zmail
2.设置邮箱的授权码
3.发邮件
    1.编辑邮件内容
    2.填写发件人邮箱和授权码
    3.发送邮件
"""

import zmail

# 1.准备发送邮件的内容（字典格式）
# 注意subject少用测试或者test，邮箱会自动屏蔽，多了还会拉黑你。
mail_content = {
    "subject": "邮件主题",
    "content_text": "邮件内容,邮件正文",
    "attachments": "D:\data.csv"
}

# 2.使用发送邮件的账户和密码,密码是授权码
server = zmail.server("yuehaitao0208@163.com", "IJBDEOOWRHJRGLPE")

"""
说明：
关于邮客户端设置的POP3，SMTP，IMAP地址，
zmail模块都帮助我们设置好了
点击zmail.server()方法即可查看，如下：

def server(username: str, password: str,
           smtp_host: Optional[str] = None,
           smtp_port: Optional[int] = None,
           smtp_ssl: Optional[bool] = None,
           smtp_tls: Optional[bool] = None,
           pop_host: Optional[str] = None,
           pop_port: Optional[int] = None,
           pop_ssl: Optional[bool] = None,
           pop_tls: Optional[bool] = None,
           config: Optional[str] = None,
           timeout=60, debug=False, log: Optional[logging.Logger] = None,
           auto_add_from=True, auto_add_to=True) -> MailServer:

"""

# 3.发送邮件
# 参数：收件人，邮件内容
server.send_mail("770546904@qq.com", mail_content)

# 给多人发送邮件
# server.send_mail([收件人1, 收件人2], 邮件内容)
