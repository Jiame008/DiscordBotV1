import discord
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

#Comando de hola, dice hola
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}')

#Comando de bye, deberia decir bye
@bot.command()
async def bye(ctx):
    await ctx.send(f'\\U0001f642')

#Este evento repite cualquier mensaje puesto en el server
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        await message.channel.send(message.content)

#Token
bot.run("MTI4Mjg4MDI1ODY4ODY4NDExNQ.G5UXzp.88d7BYENDZlnqUSsi319yfDnUeVmEUxNPTUWl0")