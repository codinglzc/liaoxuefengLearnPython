# coding=utf-8

"""
SMTP是发送邮件的协议。
Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
Python对SMTP支持有smtplib和email两个模块：
email负责构造邮件，smtplib负责发送邮件。
"""

from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((
        Header(name, 'utf-8').encode(),
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

# 构造一个最简单的纯文本邮件：
# 注意，构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
# msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')

# 发送HTML邮件
html = """
    <html>
    <body>
    <h3>记得填写 Q & A 系统哦！</h3>
    <p>点击 <a href="http://grid.hust.edu.cn/qa/index.jsp">QA 系统</a> ...</p>
    </body>
    </html>
"""
msg = MIMEText(html, 'html', 'utf-8')

# 输入Email地址和口令：
from_addr = '822688424@qq.com'
password = 'gbcvgbmsseeobfdd'
# 输入SMTP服务器地址：
smtp_server = 'smtp.qq.com'
# 输入收件人地址：
# to_addr = '515568924@qq.com'
# to_addr = '1179903972@qq.com'
to_addrs = [
    # '515568924@qq.com',
    # '1179903972@qq.com',
    'codemasterlc@126.com',
    'codinglzc@gmail.com',
]

msg['From'] = _format_addr(u'南六218实验室机器人 <%s>' % from_addr)
# msg['From'] = _format_addr(u'南六218实验室机器人')
msg['To'] = _format_addr(u'实验室成员 <%s>' % to_addrs)
msg['Subject'] = Header(u'来自南六218实验室的温馨提示：QA系统提醒', 'utf-8').encode()

# server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)  # 打印和SMTP服务器交互的所有信息
server.login(from_addr, password)  # 登录SMTP服务器
server.sendmail(from_addr, to_addrs, msg.as_string())
server.quit()
