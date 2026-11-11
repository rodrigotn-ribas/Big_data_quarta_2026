import re 

def validar_email(email: str) -> bool:
    padrao = re.compile(r"^\w+([\.-]?\w)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")

    return bool(padrao.match(email))

def response_email(email_list: list) -> None:
    for e in email_list:
        if validar_email(e):
            print(f"'{e}' é um email válido")
        else:
            print(f"'{e}' não é um email válido")

        

email_list = [
    "luiz@gmail.com.br",
    "notvalid@.com",
    "email_bot0.com"
]

response_email(email_list)