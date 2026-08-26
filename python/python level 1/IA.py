respotas = {f"ola" or "oi" or "bom dia" or  "boa tarde" or "boa noite": "olá, {login} como possa ajudar?"}.lower()

login = input("qual seu nome?: ")
print(f"Olá, {login}! Bem-vindo ao sistema, como posso te ajudar?")