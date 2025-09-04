import os
import smtplib
from dotenv import load_dotenv

load_dotenv ()

login=os.getenv('login')
password=os.getenv('password')


adress_recipient='ggella1@yandex.ru'
Letter_subject='Приглашение'
site_name='https://dvmn.org/profession-ref-progra'
friend_name='Fedor'
sender_name='Elena'


letter='''\
From: {0}
To: {1}
Subject: {2}
Content-Type: text/plain; charset="UTF-8";

Привет, {4}, {5} приглашает тебя на сайт {3}!

{3} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {3}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {3}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.

'''.format(login, adress_recipient, Letter_subject, site_name, friend_name, sender_name)

letter=letter.encode('UTF-8')

server=smtplib.SMTP_SSL('smtp.yandex.ru', 465)


server.login(login, password)
server.sendmail(login, adress_recipient, letter)
server.quit()

