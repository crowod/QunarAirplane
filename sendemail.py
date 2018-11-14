import smtplib
from email.mime.text import MIMEText
from config import *


class SendMali(object):
    def __init__(self):
        self.mail_host = ''
        self.mail_user = ''
        self.mail_pass = ''
        self.sender = ''
        self.receivers = ['']

    def send(self, flights):
        """

        :type flights: list
        """
        message = ''
        for flight in flights:
            if 'pre' not in flight:
                message += '航班代码：' + str(
                    flight.get('airCode')
                ) + ', 航班公司: ' + flight.get('name') + ', 时间：' + str(
                    flight.get('depTime')
                ) + '-' + str(flight.get('arrTime')) + ', 最低价格: ' + str(
                    flight.get('minPrice')
                ) + ', 机场信息: ' + flight.get('depAirport') + '-' + flight.get(
                    'depTerminal') + ' -> ' + flight.get(
                        'arrAirport') + '-' + flight.get(
                            'arrTerminal') + ', 飞机信息: ' + flight.get(
                                'planeFullType') + ', 餐饮:' + flight.get(
                                    'mealDesc')
            else:
                message += '转机航班:\n' + '航班代码：' + str(
                    flight.get('pre').get('airCode')
                ) + ', 航班公司: ' + flight.get('pre').get('name') + ', 时间：' + str(
                    flight.get('pre').get('depTime')) + '-' + str(
                        flight.get('pre').get('arrTime')) + ', 最低价格: ' + str(
                            flight.get('minPrice')
                        ) + ', 机场信息: ' + flight.get('pre').get(
                            'depAirport') + '-' + flight.get('pre').get(
                                'depTerminal'
                            ) + ' -> ' + flight.get('pre').get(
                                'arrAirport') + '-' + flight.get('pre').get(
                                    'arrTerminal'
                                ) + ', 飞机信息: ' + flight.get('pre').get(
                                    'planeFullType'
                                ) + ', 餐饮: ' + flight.get('pre').get(
                                    'mealDesc'
                                ) + '\n>>>>>>转机>>>>>>\n' + '航班代码：' + str(
                                    flight.get('post').get('airCode')
                                ) + ', 航班公司: ' + flight.get('post').get(
                                    'name') + ', 时间：' + str(
                                        flight.get('post').get('depTime')
                                    ) + '-' + str(
                                        flight.get('post').get('arrTime')
                                    ) + ', 最低价格: ' + str(
                                        flight.get('minPrice')
                                    ) + ', 机场信息: ' + flight.get('post').get(
                                        'depAirport'
                                    ) + ' - ' + flight.get('post').get(
                                        'depTerminal'
                                    ) + ' -> ' + flight.get('post').get(
                                        'arrAirport'
                                    ) + '-' + flight.get('post').get(
                                        'arrTerminal'
                                    ) + ', 飞机信息: ' + flight.get(
                                        'post').get('planeFullType'
                                                    ) + ', 餐饮: ' + flight.get(
                                                        'post').get('mealDesc')
            message += '\n-----------------分割线-------------------------\n'
        message = MIMEText(message, 'plain', 'utf-8')
        # 邮件主题
        message[
            'Subject'] = '机票信息 ' + searchDepartureAirport + '-' + searchArrivalAirport + ' ' + searchDepartureTime
        # 发送方信息
        message['From'] = self.sender
        # 接受方信息
        message['To'] = self.receivers[0]

        # 登录并发送邮件
        try:
            smtp_obj = smtplib.SMTP_SSL(self.mail_host, 465)

            # 登录到服务器
            smtp_obj.login(self.mail_user, self.mail_pass)
            # 发送
            smtp_obj.sendmail(self.sender, self.receivers, message.as_string())
            # 退出
            smtp_obj.quit()
            print('success')
        except smtplib.SMTPException as e:
            print('error', e)  # 打印错误
