import re
import discord

# --------------
# Lista de palavras tóxicas
palavras_toxicas = [
    "cu", "merda", "puta", "idiota", "burro", "imbecil",
    "otário", "otária", "babaca", "vagabundo", "arrombado",
    "filho da puta", "viado", "bicha", "corno", "corna",
    "cuzão", "cuzona", "desgraçado", "desgraçada", "escroto",
    "escrota", "foda-se", "merdinha", "palhaço", "palhaça",
    "retardado", "retardada", "safado", "safada", "vagabunda",
    "traveco", "macaco", "macaca", "pica", "pika", "piroca",
    "buceta", "xana", "caralho", "crioulo", "criolo", "crioula", "criola",
]


def verificar_toxicidade_direta(texto):
    texto = texto.lower()
    for palavra in palavras_toxicas:
        if re.search(rf"\b{re.escape(palavra)}\b", texto):
            return True
    return False
# --------------


# --------------
# Eventos do bot
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # filtragem de toxicidade
    if verificar_toxicidade_direta(message.content):
        await message.delete()
        return  

    
    await bot.process_commands(message)
# --------------
bot.run(TOKEN)
