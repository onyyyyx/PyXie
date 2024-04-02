import interactions
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.config')
TOKEN=os.getenv('TOKEN')

bot = interactions.Client(token=TOKEN)
slash=interactions.slash_command

@bot.event
async def on_ready():
	print(f'\nLogged as {bot.user.name}\n')

@slash(name='test',description='Try the slash command')
async def test(ctx):
	await ctx.send('Hello World!')

@slash(name='ping',description='Ping the bot 🏓')
async def ping(ctx):
	embed=interactions.Embed(title='Pong! :ping_pong:',description=f'Latency: {round(bot.latency*1000)} ms',color=0x1593d8)
	await ctx.send(embed=embed)

bot.start()
