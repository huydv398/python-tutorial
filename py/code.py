import shodan
import requests
import telebot
import re
import json
import config
import sys
import ipaddress # Check ip

API_Key=config.TOKEN
bot = telebot.TeleBot(API_Key)
api = shodan.Shodan(config.API_SHODAN) 

# Reply hướng dẫn
@bot.message_handler(commands=["start"])
def send_welcome(message):
    """
    Hàm mô tả các hướng dẫn để thao tác với bot trên telegram
    """
    bot.reply_to(message, "Nhập vào /port <IP> để xem port. VD: /port 8.8.8.8"+ '\n\n', parse_mode='Markdown')
def list_port(ipaddr):

    ipinfo= api.host(ipaddr)
    info = ipinfo['data']
    info_port = 'Port \t Protocol \t Service'
    try:
        for data in info:
            port = str(data['port'])
            service = str(data['_shodan']['module'])
            protocol = str(data['transport'])
            inf_output = port + " : \t " +protocol+'\t'+ service 
            info_port = info_port +'\n'+ inf_output
    except:
            info_port = 'Lỗi port'
    return info_port  

if __name__ == "__main__":
    # Tạo lệnh check port 
    @bot.message_handler(commands=["port"])
    def check_port(message):
        IP = message.text[6:]
        try:
            if ipaddress.ip_address(IP).is_private == False :
                # print('Ip Public')
                port = list_port(IP)
                string_port  = str(port)
                send_message = bot.reply_to(message, IP + ' is IP Public' +'\n'+string_port, parse_mode='Markdown')
            elif ipaddress.ip_address(IP).is_private == True :

                # print('Ip Private')
                send_message = bot.reply_to(message, IP + 'is IP Private', parse_mode='Markdown')
        except:
            # print('sai cu phap')
            end_message = bot.reply_to(message, 'Sai cú pháp. ' + IP + ': không phải là một địa chỉ IP', parse_mode='')
            # send_message = bot.reply_to(message, IP + e , parse_mode='')


    bot.polling()

