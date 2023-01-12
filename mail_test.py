import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# мои либы
from myMails import mail1
from acc_keys import mail_keys

# получаем пароль от аккаунта почты
mail = mail_keys('Sashaklivsovpechka@gmail.com')

# от кого, кому, тема сообщения
msg = MIMEMultipart('alternative')
msg['Subject'] = "Тест рассылки"
msg['From'] = 'Sashaklivsovpechka@gmail.com'
msg['To'] = "elenaklivtsova@icloud.com"

# запасной текст и основное сообщение
text = 'oh, something went wrong!'
html = mail1()

# записываем сообщение + текст в переменные
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# добавляем сообщение + текст
msg.attach(part1)
msg.attach(part2)

# выбираем сервер для отправки + порт (587 - стандарт, редко 465 )
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# просто надо
smtpObj.ehlo()

# используем шифрование
smtpObj.starttls()

# входим
smtpObj.login('Sashaklivsovpechka@gmail.com', mail)

# отправляем
smtpObj.sendmail("Sashaklivsovpechka@gmail.com","elenaklivtsova@icloud.com", msg.as_string())

# выходим
smtpObj.quit()

