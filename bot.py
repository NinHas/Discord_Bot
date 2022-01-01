import discord
import random
import json
from discord.ext import commands


client = commands.Bot(command_prefix = "!")

with open("C:\\Users\\dell\\Documents\\GitHub\\DiscordBot\\cursewords.json","r") as fileobj:
    jsonfile = json.loads(fileobj.read())
    cursewords = jsonfile["cursewords"]

with open('C:\\Users\\dell\\Documents\\GitHub\\Token\\Token_File.txt','r') as obj:
    Token_here = obj.read()


@client.event
async def on_ready():
    #await change_presence(activity = discord.Game(name = 'fortnut'))
    print(f"{client.user} is connected to the guild ")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.mention}, welcome to our Guild!')
    for channel in member.guild.channels:
        if (str(channel) == "voidmain"):
            await channel.send(f"{member.mention} has joined the guild.")

       
    
@client.event
async def on_member_remove(member):
    print(f"{member} has left the server")
    
    for channel in member.guild.channels:
        if (str(channel) == "voidmain"):
            await channel.send(f"{member.mention} has left the guild")

@client.command(aliases = ["Bot"])
async def _8ball(ctx,*question):
    responses =['Likely.',
                'Yes - Definitely',
                'Without a doubt',
                'My reply is no',
                'Very doubtful']   
    await ctx.send(random.choice(responses))   

@client.command()
async def clear(ctx,amount = 5):
    if amount == 0:

        await ctx.send(f"You cannot delete {amount} messages.\nPlease enter a proper number.")
    else:
        amount += 1
        await ctx.channel.purge(limit = amount)               

@client.command()
async def ping(ctx):
    await ctx.send(f"pong {round(client.latency *1000)}ms ")

@client.command()
async def marco(ctx):
    await ctx.send("polo")

@client.command()
async def hi(ctx):
    await ctx.send("Hello")    

@client.command()
async def kick(ctx,member : discord.Member,*,reason = None):
    await member.kick(reason = reason)
    
@client.command()
async def ban(ctx,member : discord.Member,*,reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"Banned : {member.mention}")


@client.command()
async def unban(ctx,*,member):
    banned_users = await ctx.guid.bans()
    member_name,member_descriminator = member.split("#")

    for banned_entry in banned_users:
        user = banned_entry.user

        if (member_name,member_descriminator) == (user.name,user.descriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"unbanned : {user.mention}")
            return        

@client.event
async def on_message(message):
    
    if (message.author == client.user):
        return

    if (message.content in cursewords):
        
        await message.channel.purge(limit = 1)
        await message.author.create_dm()
        await message.author.dm_channel.send(f"{message.author.name} that's a strike buddy")

    tbbt = ["My brain is better than everybody's",
            "That's my spot",
            "Bazinga PUNK ",
            "I'm not crazy ,my mother had me tested"]    

    if (message.content == 'tbbtquotes'):
        await message.channel.send(random.choice(tbbt))

    await client.process_commands(message)

@client.event
async def on_message_delete(message):        
        print(f"name:{message.author.name} \n message : {message.content}")







@client.command()
async def logout(ctx):
    await ctx.send("Bravo 6 going dark")
    await client.logout()




client.run(Token_here) 

