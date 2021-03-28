
#    Copyright (C) 2020-2021 by @InukaAsith & @Mr_Dark_Prince
#    This programme is a part of DaisyX (TG bot) project
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#    Kang with the credits

import emoji
import requests
url = "https://iamai.p.rapidapi.com/ask"
from SaitamaRobot import OWNER_ID
from SaitamaRobot import pbot as daisyx
from pyrogram import filters
import asyncio, os
from SaitamaRobot.utils.pluginhelp import admins_only
BOT_ID = 1649439508

daisy_chats = []

# AI Chat (C) 2020-2021 by @InukaAsith & @Mr_Dark_Prince

@daisyx.on_message(filters.command("chatbot") & ~filters.edited)
@admins_only
async def hmm(_, message):
    global daisy_chats
    if len(message.command) != 2:
        await message.reply_text("I only recognize `/chatbot on` and /chatbot `off only`")
        return
    status = message.text.split(None, 1)[1] 
    chat_id = message.chat.id
    if status == "ON" or status == "on" or status == "On":
        if chat_id not in daisy_chats:
            daisy_chats.append(message.chat.id)
            text = "Chatbot Enabled Reply To Any Message" \
                   + " Of Mine To Get A Reply"
            await message.reply_text(text)
            return
        await message.reply_text("ChatBot Is Already Enabled.")
        return

    elif status == "OFF" or status == "off" or status == "Off":
        if chat_id in daisy_chats:
            daisy_chats.remove(chat_id)
            await message.reply_text("AI chat Disabled!")
            return
        await message.reply_text("AI Chat Is Already Disabled.")
        return
    
    else:
        await message.reply_text("I only recognize `/chatbot on` and /chatbot `off only`")



@daisyx.on_message(filters.text & filters.reply & ~filters.bot &
        ~filters.via_bot & ~filters.forwarded,group=2)
async def hmm(client,message):
  if message.chat.id not in daisy_chats:
    return
  if message.reply_to_message.from_user.id != BOT_ID:
    return
  test = message.text
  if test.startswith("/"):
    return
  test = emoji.demojize(test.strip())

# Kang with the credits bitches @InukaASiTH

  try:
    test = test.replace('mizu', 'Jessica')
  except:
    return
  r = ('\n    \"consent\": true,\n    \"ip\": \"::1\",\n    \"question\": \"{}\"\n').format(test)
  k = f"({r})"
  new_string = k.replace("(", "{")
  lol = new_string.replace(")","}")
  payload = lol
  headers = {
      'content-type': "application/json",
      'x-forwarded-for': "<user's ip>",
      'x-rapidapi-key': "33b8b1a671msh1c579ad878d8881p173811jsn6e5d3337e4fc",
      'x-rapidapi-host': "iamai.p.rapidapi.com"
      }
 
  response = requests.request("POST", url, data=payload, headers=headers)
  lodu = response.json()
  result = (lodu['message']['text'])
  if 'My name is Jessica' in result:
   pro = result
   pro = pro.replace('My name is Jessica','My name is Mizu.')
  if "Thergiakis Eftichios" in result:
   pro = result
   pro = pro.replace('Thergiakis Eftichios','@ImJanindu')
  if "Out of all ninja turtle" in result or "Mizuki is dead as fuck." in result:
   pro = "I'm at your service ask anthing sir?"
   try:
      await daisyx.send_chat_action(message.chat.id, "typing")
      await message.reply_text(pro)
   except CFError as e:
           print(e)
  elif "ann" in result:
   pro = "My name is Mizu."
   try:
      await daisyx.send_chat_action(message.chat.id, "typing")
      await message.reply_text(pro)
   except CFError as e:
           print(e)
  else:
    try:
      await daisyx.send_chat_action(message.chat.id, "typing")
      await message.reply_text(result)
    except CFError as e:
           print(e)
  

@daisyx.on_message(filters.text & filters.private & filters.reply &
        ~filters.via_bot & ~filters.forwarded & ~filters.bot)
async def inuka(client,message):
  test = message.text
  if test.startswith("/"):
     return
  test = emoji.demojize(test.strip())
  if "mizu" in test or 'Mizu' in test:
    try:
      test = test.replace('mizu', 'Jessica')
    except:
      test = test.replace('Mizu', 'Jessica')
  r = ('\n    \"consent\": true,\n    \"ip\": \"::1\",\n    \"question\": \"{}\"\n').format(test)
  k = f"({r})"
  new_string = k.replace("(", "{")
  lol = new_string.replace(")","}")
  payload = lol
  headers = {
    'content-type': "application/json",
    'x-forwarded-for': "<user's ip>",
    'x-rapidapi-key': "33b8b1a671msh1c579ad878d8881p173811jsn6e5d3337e4fc",
    'x-rapidapi-host': "iamai.p.rapidapi.com"
    }

  response = requests.request("POST", url, data=payload, headers=headers)
  lodu = response.json()
  result = (lodu['message']['text'])
  if 'My name is Jessica' in result:
   pro = result
   pro = pro.replace('My name is Jessica','My name is Mizu.')
  if "Thergiakis Eftichios" in result:
   pro = result
   pro = pro.replace('Thergiakis Eftichios','@ImJanindu')
  if "Mizuki is dead as fuck." in result:
   pro = "I'm at your service ask anthing sir?"
   try:
      await daisyx.send_chat_action(message.chat.id, "typing")
      await message.reply_text(pro)
   except CFError as e:
           print(e)
  elif "ann" in result:
   pro = "My name is Mizu."
   try:
      await daisyx.send_chat_action(message.chat.id, "typing")
      await message.reply_text(pro)
   except CFError as e:
           print(e)
  else:
    try:
      await daisyx.send_chat_action(message.chat.id, "typing")
      await message.reply_text(result)
    except CFError as e:
           print(e)

@daisyx.on_message(filters.regex("Mizu|mizu|MizuX|mizux") & ~filters.bot &
        ~filters.via_bot & ~filters.forwarded & ~filters.reply & ~filters.private)
async def inuka(client,message):
  test = str(message.text)
  test = emoji.demojize(test.strip())
  if "mizu" in test or 'Mizu' in test:
    try:
      test = test.replace('mizu', 'Jessica')
    except:
      test = test.replace('Mizu', 'Jessica')
    r = ('\n    \"consent\": true,\n    \"ip\": \"::1\",\n    \"question\": \"{}\"\n').format(test)
    k = f"({r})"
    new_string = k.replace("(", "{")
    lol = new_string.replace(")","}")
    payload = lol
    headers = {
      'content-type': "application/json",
      'x-forwarded-for': "<user's ip>",
      'x-rapidapi-key': "33b8b1a671msh1c579ad878d8881p173811jsn6e5d3337e4fc",
      'x-rapidapi-host': "iamai.p.rapidapi.com"
      }

    response = requests.request("POST", url, data=payload, headers=headers)
    lodu = response.json()
    result = (lodu['message']['text'])
    if 'My name is Jessica' in result:
     pro = result
     pro = pro.replace('My name is Jessica','My name is Mizu.')
    if "Thergiakis Eftichios" in result:
     pro = result
     pro = pro.replace('Thergiakis Eftichios','@ImJanindu')
    if "Out of all ninja turtle" in result or "Mizuki is dead as fuck." in result:
     pro = "I'm at your service ask anthing sir?"
     try:
        await daisyx.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
     except CFError as e:
             print(e)
    elif "ann" in result:
     pro = "My name is Mizu."
     try:
        await daisyx.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
     except CFError as e:
             print(e)
    else:
      try:
        await daisyx.send_chat_action(message.chat.id, "typing")
        await message.reply_text(result)
      except CFError as e:
             print(e)


__help__ = """
*Chatbot* allows Mizu to talk and provides a more interactive group chat experience.

*Admins only cmds:*
 • `/chatbot on`*:* Enables Chatbot mode in the chat.
 • `/chatbot off`*:* Disables Chatbot mode in the chat.

Reports bugs at @ImJanindu

*Powered by Mizu AI* from @InfinityJE

 • Turn on chat bot and reply to any message of Mizu to start chat with her!
 • Also you can chat with Mizu in groups by putting the word Mizu in messages you send to the group.

The word *Mizu* use to get attention of Mizu, then bot will reply to you.

Note: Chatbot is only works in groups.
"""

__mod_name__ = "Mizu Chat"
