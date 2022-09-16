配置文件config.ini

[Slave]
pophost = pop.sina.com
smtphost = smtp.sina.com
port = 25
username = XXX@sina.com
password = XXX

[Boss]
mail = XXX@qq.com
timelimit = 2

[Command]
shutdown=shutdown -f -s -t 100 -c closing...
dir=dir


[Open]
music = F:Masetti - Our Own Heaven.mp3
video = F:Jai Waetford - Shy.mp4
notepad = notepad
excutor.py

#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import win32api
from mccLog import mccLog

class executor(object):
    def __init__(self,commandDict,openDict):
        '''
        创建方法
        :param commandDict:
        :param openDict:
        '''
        self.mccLog = mccLog()
        self.commandDict = commandDict
        self.openDict = openDict
    def execute(self,exe,mailHelper):
        self.mailHelper = mailHelper
        subject = exe['subject']
        # self.mccLog.mccWriteLog(u'开始处理命令')
        print u'start to process'
        if subject !='pass':
            self.mailHelper.sendMail('pass','Slave')
            if subject in self.commandDict:
                # self.mccLog.mccWriteLog(u'执行命令！')
                print u'start command'
                try:
                    command = self.commandDict[subject]
                    os.system(command)
                    self.mailHelper.sendMail('Success','Boss')
                    # self.mccLog.mccWriteLog(u'执行命令成功！')
                    print u'command success'
                except Exception,e:
                    # self.mccLog.mccError(u'执行命令失败'+ str(e))
                    print 'command error'
                    self.mailHelper.sendMail('error','boss',e)
            elif subject in self.openDict:
                # self.mccLog.mccWriteLog(u'此时打开文件')
                print u'open the file now'
                try:
                    openFile = self.openDict[subject]
                    win32api.ShellExecute(0,'open',openFile,'','',1)
                    self.mailHelper.sendMail('Success','Boss')
                    # self.mccLog.mccWriteLog(u'打开文件成功！')
                    print u'open file success'
                except Exception,e:
                    # self.mccLog.mccError(u'打开文件失败！' + str(e))
                    print u'open file error'
                    self.mailHelper.sendMail('error','Boss',e)
            elif subject[:7].lower() =='sandbox':
                self.sandBox(subject[8:])
            else:
                self.mailHelper.sendMail('error','Boss','no such command!')

    def sandBox(self,code):
        name = code.split('$n$')[0]
        code = code.split('$n$')[1]
        codestr = '\n'.join(code.split('$c$'))
        codestr = codestr.replace('$',' ')
        with open(name,'a') as f:
            f.write(codestr)
        os.system('python' + name)
configReader.py

#-*-coding:utf-8-*-
import ConfigParser
import os,sys

class configReader(object):
    def __init__(self,configPath):
        configFile = os.path.join(sys.path[0],configPath)
        self.cReader = ConfigParser.ConfigParser()
        self.cReader.read(configFile)

    def readConfig(self,section,item):
        return self.cReader.get(section,item)

    def getDict(self,section):
        commandDict = {}#字典
        items = self.cReader.items(section)
        for key,value in items:
            commandDict[key] = value
        return commandDict
日志文件mccLog.py

#-*-coding:utf-8-*-
import logging
from datetime import datetime

class mccLog(object):
    def __init__(self):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(levelname)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename=datetime. now().strftime('%Y%m%d%H%M%S') + '.log',
            filemode='a'
        )

    def mccWriteLog(self,logContent):
            logging.info(logContent)

    def mccError(self,errorContent):
            logging.error(errorContent)
mailHelper.py

#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from email.mime.text import MIMEText
from configReader import configReader
from mccLog import mccLog
import poplib
import smtplib
import re

class mailHelper(object):
    CONFIGPATH = 'config.ini'

    def __init__(self):
        '''
        初始化邮件
        '''
        self.mccLog = mccLog()
        cfReader = configReader(self.CONFIGPATH)
        self.pophost = cfReader.readConfig('Slave','pophost')
        self.smtphost = cfReader.readConfig('Slave','smtphost')
        self.port = cfReader.readConfig('Slave','port')
        self.username = cfReader.readConfig('Slave','username')
        self.password = cfReader.readConfig('Slave','password')
        self.bossMail = cfReader.readConfig('Boss','mail')
        self.loginMail()
        self.configSlaveMail()

    def loginMail(self):
        '''
        验证登陆
        :return:
        '''
        self.mccLog.mccWriteLog('start to login the E-mail')
        print 'start to login e-mail'
        try:
            self.pp = poplib.POP3_SSL(self.pophost)
            self.pp.set_debuglevel(0)#可以为0也可以为1，为1时会显示出来
            self.pp.user(self.username)#复制
            self.pp.pass_(self.password)
            self.pp.list()#列出赋值
            print 'login successful!'
            self.mccLog.mccWriteLog('login the email successful!')
            print 'login the email successful!'
        except Exception,e:
            print 'Login failed!'
            self.mccLog.mccWriteLog('Login the email failed!')
            exit()

    def acceptMail(self):
        '''
        接收邮件
        :return:
        '''
        self.mccLog.mccWriteLog('Start crawling mail！')
        print 'Start crawling mail'
        try:
            ret = self.pp.list()
            mailBody = self.pp.retr(len(ret[1]))
            self.mccLog.mccWriteLog('Catch the message successfully')
            print 'Catch the message successfully'
            return mailBody
        except Exception,e:
            self.mccLog.mccError('Catch the message failed' + e)
            print 'Catch the message failed'
            return None

    def analysisMail(self,mailBody):
        '''
        正则分析邮件
        :param mailBody:
        :return:
        '''
        self.mccLog.mccWriteLog('Start crawling subject and sender')
        print 'Start crawling subject and sender'
        try:
            subject = re.search("Subject: (.*?)',",str(mailBody[1]).decode('utf-8'),re.S).group(1)
            print subject
            sender = re.search("'X-Sender: (.*?)',",str(mailBody[1]).decode('utf-8'),re.S).group(1)
            command = {'subject':subject,'sender':sender}
            self.mccLog.mccWriteLog("crawling subject and sender successful！")
            print 'crawling subject and sender successful'
            return command
        except Exception,e:
            self.mccLog.mccError("crawling subject and sender failed！" + e)
            print 'crawling subject and sender failed！'
            return None

    def sendMail(self,subject,receiver,body='Success'):
        '''
        发送邮件
        :param subject:
        :param receiver:
        :param body:
        :return:
        '''
        msg = MIMEText(body,'plain','utf-8')
        #中文需要参数utf-8，单字节字符不需要
        msg['Subject'] = subject
        msg['from'] = self.username
        self.mccLog.mccWriteLog('Start sending mail' + 'to' +receiver)
        print 'Start sending mail'
        if receiver == 'Slave':
            try:
                self.handle.sendmail(self.username,self.username,msg.as_string())
                self.mccLog.mccWriteLog('Send the message successfully')
                print 'Send the message successfully'
            except Exception,e:
                self.mccLog.mccError('Send the message failed' + e)
                print 'Send the message failed'
                return False
        elif receiver == 'Boss':
            try:
                self.handle.sendmail(self.username,self.bossMail,msg.as_string())
                self.mccLog.mccWriteLog('Send the message successfully')
                print 'Send the message successfully'
            except Exception,e:
                self.mccLog.mccError('Send the message failed！' + e)
                print 'Send the message failed!'
                return False

    def configSlaveMail(self):
        '''
        配置邮件
        :return:
        '''
        self.mccLog.mccWriteLog('Start configuring the mailbox')
        print 'Start configuring the mailbox'
        try:
            self.handle = smtplib.SMTP(self.smtphost, self.port)
            self.handle.login(self.username, self.password)
            self.mccLog.mccWriteLog('The mailbox configuration is successful')
            print 'The mailbox configuration is successful'
        except Exception, e:
            self.mccLog.mccError('The mailbox configuration is failed' + e)
            print 'The mailbox configuration is failed'
            exit()

#
# if __name__=='__main__':
#     mail = mailHelper()
#     body = mail.acceptMail()
#     print body
#     print mail.analysisMail(body)
#     mail.sendMail('OK','Slave')
weiChatControlComputer.py

#-*-coding:utf-8-*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import time
import sys
from mailHelper import mailHelper
from excutor import executor
from configReader import configReader

__Author__ = 'william'
__Verson__ = 0.5

reload(sys)
sys.setdefaultencoding('utf-8')

class MCC(object):
    CONFIGPATH = 'config.ini'
    KEY_COMMAND = 'Command'
    KEY_OPEN = 'Open'
    KEY_BOSS = 'Boss'
    KEY_TIMELIMIT = 'timelimit'#扫描时间的频率

    def __init__(self):
        self.mailHelper = mailHelper()
        self.configReader = configReader(self.CONFIGPATH)
        commandDict = self.configReader.getDict(self.KEY_COMMAND)
        openDict = self.configReader.getDict(self.KEY_OPEN)
        self.timeLimit = int(self.configReader.readConfig(self.KEY_BOSS,self.KEY_TIMELIMIT))
        self.excutor = executor(commandDict,openDict)
        self.toRun()

    def toRun(self):
        '''
        实现轮训操作
        :return:
        '''
        while True:
            self.mailHelper = mailHelper()
            self.run()
            time.sleep(self.timeLimit)

    def run(self):
        mailBody = self.mailHelper.acceptMail()
        if mailBody:
            exe = self.mailHelper.analysisMail(mailBody)
            if exe:
                self.excutor.execute(exe,self.mailHelper)


if __name__ == '__main__':
    mcc = MCC()