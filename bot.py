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
sohbet = [-1001427120961]
oyun = [-1001489218104]
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
     await event.reply(f"{startmesaj}",
                    buttons=(
                      [
                       Button.url('𝐆𝐀𝐍𝐆𝐀𝐋𝐀𝐑 𝐀𝐏𝐀𝐑𝐓𝐌𝐀𝐍𝐈', f'https://t.me/GangalarApartmanSohbetGrubu')
                      ],
                      [
                       Button.url('𝐆𝐀𝐍𝐆𝐀𝐋𝐀𝐑 𝐎𝐘𝐔𝐍 𝐆𝐑𝐔𝐁𝐔', f'https://t.me/+KZmSlrn8Jmc0YTlk')
                      ],
                      [
                       Button.url('</> ᴅᴇᴠᴇʟᴏᴘᴇʀ', f'https://t.me/emiriviaa')
                      ],
                    ),
                    link_preview=False
                   )


@client.on(events.NewMessage(pattern="^(?i)admin ?(.*)"))
async def calladmin(event):
  if event.is_private:
    return

  async for usr in client.iter_participants(event.chat_id):

   if event.chat_id in sohbet:

     await event.reply(f"🛡 **Adminler:**\n\n👉 @NurSaaah\n👉 @Bendilemma\n👉 @sembolikgri\n👉 @Bengalip\n👉 @egeli03",
                    buttons=(
                      [
                       Button.inline('✅ Kapat', data='sil')
                      ],
                    ),
                    link_preview=False
                   )
     return await event.reply(f"👉 @ImDildade\n👉 @selamcanimm\n👉 @Pembepokemon",
                    buttons=(
                      [
                       Button.inline('✅ Kapat', data='sil')
                      ],
                    ),
                    link_preview=False
                   )

   elif event.chat_id in oyun:


     return await event.reply(f"🛡 **Adminler:**\n\n👉 @NurSaaah\n👉 @sembolikgri\n👉 @Bendilemma\n👉 @egeli03\n👉 @ImDildade\n👉 @Pembepokemon",
                    buttons=(
                      [
                       Button.inline('✅ Kapat', data='sil')
                      ],
                    ),
                    link_preview=False
                   )



   else:
     pass



@client.on(events.callbackquery.CallbackQuery(data="sil"))
async def sil(event):
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return
  else:
    await event.delete()




@client.on(events.NewMessage(pattern="^(.*) (?i)admin ?(.*)"))
async def calladmin(event):
  if event.is_private:
    return

  async for usr in client.iter_participants(event.chat_id):

   if event.chat_id in sohbet:

     await event.reply(f"🛡 **Adminler:**\n\n👉 @NurSaaah\n👉 @Bendilemma\n👉 @sembolikgri\n👉 @Bengalip\n👉 @egeli03",
                    buttons=(
                      [
                       Button.inline('✅ Kapat', data='sil')
                      ],
                    ),
                    link_preview=False
                   )
     return await event.reply(f"👉 @ImDildade\n👉 @selamcanimm\n👉 @Pembepokemon",
                    buttons=(
                      [
                       Button.inline('✅ Kapat', data='sil')
                      ],
                    ),
                    link_preview=False
                   )

   elif event.chat_id in oyun:


     return await event.reply(f"🛡 **Adminler:**\n\n👉 @NurSaaah\n👉 @sembolikgri\n👉 @Bendilemma\n👉 @egeli03\n👉 @ImDildade\n👉 @Pembepokemon",
                    buttons=(
                      [
                       Button.inline('✅ Kapat', data='sil')
                      ],
                    ),
                    link_preview=False
                   )



   else:
     pass

@client.on(events.NewMessage(pattern='^1LvTelkAJyaM7vU1I2zazj9RBwbGmgo6VzTVVgFb'))
async def event(ups):
  if ups.sender_id == 5539575339:
   await ups.reply("**Bot Durumu:** ⚙️ Çalışıyor")
  else:
    pass


print("⚔️ RiviaTag Çalışıyor")
client.run_until_disconnected()
run_until_disconnected()
