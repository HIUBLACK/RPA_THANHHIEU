import os
import shutil
import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

folder_sql = './SQL'
folder_backup = './BackUp_SQL'
sender = 'hieu_2251220098@dau.edu.vn'
pas = 'rribxwyjheauwymr'  
receiver = 'thanhhieu27072004@gmail.com'


def send_email(subject, body):
    
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, pas)
        text = message.as_string()
        server.sendmail (sender, receiver, text)
        print(f"Thông báo đã được gửi đến {receiver}")
        server.quit()
    except Exception as e:
        print(f'Lỗi khi gửi email: {e}')

def backup_sql():
    try:
        if not os.path.exists(folder_backup):
            os.makedirs(folder_backup)
            
        sql = [f for f in os.listdir(folder_sql) if f.endswith('.sql') or f.endswith('.sqlite3')]
        
        for s in sql:
            i = os.path.join(folder_sql, s)
            o = os.path.join(folder_backup, s)
            shutil.copy2(i, o)  
            print(f'Đã backup file: {s}')
        send_email('Backup Database Thành công', 'Thầy rô đẹp trai')
        
    except Exception as e:
        send_email('Backup Database Thất bại', f'Lỗi khi backup database: {e}')

schedule.every().day.at("00:00").do(backup_sql)

print('Đang chạy...')

while True:
    schedule.run_pending()
    time.sleep(1)  
