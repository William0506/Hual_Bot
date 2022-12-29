from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import src.TextCommands.joke as joke
import src.TextCommands.ping as ping
import src.TextCommands.greeting as greeting
import src.TextCommands.help as help
import src.TextCommands.author as author
import src.TextCommands.me as me
import src.TextCommands.echo as echo
import time
import requests

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code
#-----------------------------------
app = Flask(__name__)
# LINE BOT info
line_bot_api = LineBotApi('AwrIea2C6+iwl9Cf9ed7vTw51e3T038DWMV/10zX8eSB1KMtGynvmmfRb4kJQlASoWWN3JZr4TCfs/4dP0+yG2HWSkxGe9bMRjoJaHMALLn0lYpD21gtiADZ3thJhHRB47py1GQT9kkruEadiR2PQQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('896c99a3e5d6e6a2df6be995cba98f56')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# Message event
@handler.add(MessageEvent)
def handle_message(event):
    #開始
    time1 = time.time()
    
    #資訊
    token = event.reply_token
    token_notify = 'DE60rfYceaSZVLL8QglgTrR6PTbj54VVkdU0wQAIpnE'
    UserId = event.source.user_id
    profile = line_bot_api.get_profile(UserId)
    print(profile)
    #文字處理
    if event.message.type == "text":
        message = event.message.text
        prefix="/"
        command = str(message[len(prefix):]).split(" ")[0]
    
        #指令處理
        text_commands = ["joke","ping","g","echo"]
        flex_commands = ["help","author","me"]
        
        #檢查前綴字
        if message.startswith(prefix) and text_commands.count(command) != 0 and flex_commands.count(command) == 0:
            #text
            print(command)
            
            text = None
            
            text = joke.joke(command=command)
            
            if not text:
                text = ping.ping(time1=time1,command=command)
            
            if not text:
                text = greeting.g(command=command,user_name=profile.display_name)
                
            if not text:
                text = echo.echo(command=command,content=str(message[len(prefix):]).split(" ")[1])
            
            if text != None:
                text_msg = TextSendMessage(text=text)
                line_bot_api.reply_message(token,text_msg)
                lineNotifyMessage(token_notify,"/"+command)
            
        elif message.startswith(prefix) and flex_commands.count(command) != 0:
            # flex
            print(command)
            
            flex = None
            
            flex = help.help(command=command)
            
            if not flex:
                flex = author.author(command=command)
            
            if not flex:
                flex = me.me(command=command,displayName=profile.display_name,pictureUrl=profile.picture_url,statusMessage=profile.status_message)
            
            if flex != None:
                line_bot_api.reply_message(token,FlexSendMessage('flex',flex))
                lineNotifyMessage(token_notify,"/"+command)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)