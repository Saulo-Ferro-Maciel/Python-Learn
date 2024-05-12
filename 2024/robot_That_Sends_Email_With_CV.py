import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import tkinter as tk
from tkinter import filedialog
import re
import os

def enviar_email(email_destinatario, assunto, corpo_email, file_path_anexo):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_destinatario):
        print("Endereço de e-mail inválido!")
        return

    msg = MIMEMultipart()
    msg['Subject'] = assunto
    msg['From'] = 'COLOQUE AQUI O SEU EMAIL'
    msg['To'] = email_destinatario
    password = 'COLOQUE AQUI A SENHA DO GOOGLE'
    
    msg.attach(MIMEText(corpo_email, 'html'))

    if file_path_anexo:
        filename = os.path.basename(file_path_anexo)
        with open(file_path_anexo, 'rb') as attachment:
            part = MIMEApplication(attachment.read(), Name=filename)
        part['Content-Disposition'] = f'attachment; filename="{filename}"'
        msg.attach(part)

    with smtplib.SMTP('smtp.gmail.com: 587') as s:
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado com anexo' if file_path_anexo else 'Email enviado sem anexo')

def selecionar_arquivos():
    root = tk.Tk()
    root.withdraw()

    file_path_html = filedialog.askopenfilename(title="Selecione o arquivo HTML", filetypes=[("HTML files", "*.html")])

    if file_path_html:
        file_path_anexo = filedialog.askopenfilename(
            title="Selecione o arquivo para anexar",
            filetypes=[
                ("All files", "*.*")
            ]
        )

        email_destinatario = entry_email.get()
        assunto = entry_assunto.get()
        if assunto and email_destinatario:
            with open(file_path_html, "r") as file:
                corpo_email = file.read()
            enviar_email(email_destinatario, assunto, corpo_email, file_path_anexo)
        
        root.destroy()

def validar_email():
    selecionar_arquivos()

root = tk.Tk()
root.title("Enviar E-mail")
root.geometry("400x220")

label_email = tk.Label(root, text="Digite o e-mail do destinatário:")
label_email.pack(pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.pack(pady=5)

label_assunto = tk.Label(root, text="Digite o assunto do e-mail:")
label_assunto.pack(pady=5)
entry_assunto = tk.Entry(root, width=30)
entry_assunto.pack(pady=5)

btn_enviar = tk.Button(root, text="Enviar E-mail", command=validar_email)
btn_enviar.pack(pady=10)

root.mainloop()
