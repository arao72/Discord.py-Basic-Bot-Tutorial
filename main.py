import discord
from discord.ext import commands

client = commands.AutoShardedBot(commands.when_mentioned_or("*"))

@client.event
async def on_ready():
  print("The bot is ready to be used!")

@client.command()
async def randomcommand(ctx):
  await ctx.send("This is a random command!")


client.run("TOKEN")
