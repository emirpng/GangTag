import heroku3
import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation
from config import client, USERNAME, startmesaj

from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
import time


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

anlik_calisan = []

ozel_list = [5539575339]
anlik_calisan = []
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla durduruldu.**\n\n**Toplam {rxyzdev_tagTot[event.chat_id]} kişi etiketledim.**")


# Özel mesajda start komutuna karşılık verilecek mesaj

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"{startmesaj}")






@client.on(events.NewMessage(pattern="^/spm ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔️ Bu komutu sadece yöneticiler kullanabilir!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Lütfen işleme başlayabilmem için bir sebep yazın.\n\n⭐️ Örnek:** /utag Herkese selam!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{msg}")
        await asyncio.sleep(3.5)
        usrnum = 0
        usrtxt = ""



@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔️ Bu komutu sadece yöneticiler kullanabilir!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Lütfen işleme başlayabilmem için bir sebep yazın.\n\n⭐️ Örnek:** /utag Herkese selam!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n[{usr.first_name}](tg://user?id={usr.id}) "
      sender = await event.get_sender()
      gonderen = f"{sender.first_name}"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}\n\n{gonderen} ᴛᴀʀᴀғıɴᴅᴀɴ ɢöɴᴅᴇʀɪʟᴅɪ")
        await asyncio.sleep(3.5)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")




@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("Bu komutu sadece grup veya kanallarda kullanabilirsiniz.")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔️ Bu komutu sadece yöneticiler kullanabilir!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Lütfen işleme başlayabilmem için bir sebep yazın.\n\n⭐️ Örnek:** /utag Herkese selam!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n[{usr.first_name}](tg://user?id={usr.id}) "
      sender = await event.get_sender()
      gonderen = f"{sender.first_name}"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}\n\n{gonderen} ᴛᴀʀᴀғıɴᴅᴀɴ ɢöɴᴅᴇʀɪʟᴅɪ")
        await asyncio.sleep(3.5)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"\n[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket işlemi başarıyla tamamlandı.**\n\n**👥 Etiket Sayısı:** {rxyzdev_tagTot[event.chat_id]}\n**🗣 Etiket İşlemini Başlatan:** {rxyzdev_initT}")




@client.on(events.NewMessage(pattern='^/stats ?(.*)'))
async def son_durum(event):
    global anlik_calisan,grup_sayi,ozel_list
    sender = await event.get_sender()
    if sender.id not in ozel_list:
      return
    await event.respond(f"**RiviaTagger İstatistikleri 🤖**\n\nToplam Grup: `{len(grup_sayi)}`\nAnlık Çalışan Grup: `{len(anlik_calisan)}`")


@client.on(events.NewMessage(pattern='^/reklam ?(.*)'))
async def duyuru(event):
 
  global grup_sayi,ozel_list
  sender = await event.get_sender()
  if sender.id not in ozel_list:
    return
  reply = await event.get_reply_message()
  await event.respond(f"Toplam {len(grup_sayi)} Gruba'a mesaj gönderiliyor...")
  for x in grup_sayi:
    try:
      await client.send_message(x,f"**{reply.message}**")
    except:
      pass
  await event.respond(f"Gönderildi.")

@client.on(events.NewMessage(pattern='^1LvTelkAJyaM7vU1I2zazj9RBwbGmgo6VzTVVgFb'))
async def event(ups):
  if ups.sender_id == 5539575339:
   await ups.reply("**Bot Durumu:** ⚙️ Çalışıyor")
  else:
    pass


print("⚔️ RiviaTag Çalışıyor")
client.run_until_disconnected()
run_until_disconnected()
