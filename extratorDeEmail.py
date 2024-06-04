# importa a biblioteca regex
import re

def extrair_emails(texto):
    #formato que estou me baseando do e-mail é xxxxxxx@xxxxx.com
    padrao_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    #usa um metodo re para verificar quais os padroes_email há no texto
    emails = re.findall(padrao_email, texto)
    #retorna os emails
    return emails