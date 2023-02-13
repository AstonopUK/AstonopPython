import discord
import requests
import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
guild = discord.Guild

@client.event
async def on_ready():
    print(f'MaxBot is online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        key = 'b8da507081cff89b56b3b1ce77b8560e'
        t_title = "Message" + datetime.datetime.now().strftime("%f") + datetime.datetime.now().strftime("%d") + datetime.datetime.now().strftime("%m") + datetime.datetime.now().strftime("%Y")
        login_data = {'api_dev_key': key,'api_user_name': 'astonop','api_user_password': 'Ellipsis1'}
        data = {'api_option': 'paste','api_dev_key':key,'api_paste_code':message.content,'api_paste_name':t_title,'api_paste_expire_date': None,'api_user_key': None,'api_paste_format': None}

        login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
        print("Login status: ", login.status_code if login.status_code != 200 else "OK/200")
        print("User token: ", login.text)
        data['api_user_key'] = login.text
         
        r = requests.post("https://pastebin.com/api/api_post.php", data=data)
        print("Paste send: ", r.status_code if r.status_code != 200 else "OK/200")
        print("Paste URL: ", r.text)
        await message.channel.send(r.text)
        
client.run('MTAzNzAwOTQzMDk1MDIwMzQxNQ.Gd1l7S.c_hRySoKTgIY0FKgLXrJTZsYi-9ah3AKSajy_A')

        #file_location = "C:\\BotLogs\\data" + datetime.datetime.now().strftime("%d") + datetime.datetime.now().strftime("%m") + datetime.datetime.now().strftime("%Y") + ".txt
        #file = open(file_location, "w")
        #file.writelines(message.content)
        #file.close()
