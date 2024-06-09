from asyncio import sleep

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import MessageDeleteForbidden, RPCError
from pyrogram.types import Message

from YukkiMusic import app
from YukkiMusic.utils.permissions import adminsOnly

@app.on_message(filters.command("purge") & filters.group)
@adminsOnly("can_delete_messages") 
async def purge(app: app, msg: Message):

    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(
            text="**ɪ ᴄᴀɴ'ᴛ ᴘᴜʀɢᴇ ᴍᴇssᴀɢᴇs ɪɴ ᴀ ʙᴀsɪᴄ ɢʀᴏᴜᴘ ᴍᴀᴋᴇ sᴜᴘᴇʀ ɢʀᴏᴜᴘ.**"
        )
        return

    if msg.reply_to_message:
        message_ids = list(range(msg.reply_to_message.id, msg.id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await app.delete_messages(
                    chat_id=msg.chat.id, message_ids=plist, revoke=True
                )

            await msg.delete()
        except MessageDeleteForbidden:
            await msg.reply_text(
                text="**ɪ ᴄᴀɴ'ᴛ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs. ᴛʜᴇ ᴍᴇssᴀɢᴇs ᴍᴀʏ ʙᴇ ᴛᴏᴏ ᴏʟᴅ, ɪ ᴍɪɢʜᴛ ɴᴏᴛ ʜᴀᴠᴇ ᴅᴇʟᴇᴛᴇ ʀɪɢʜᴛs, ᴏʀ ᴛʜɪs ᴍɪɢʜᴛ ɴᴏᴛ ʙᴇ ᴀ sᴜᴘᴇʀɢʀᴏᴜᴘ.**"
            )
            return

        except RPCError as ef:
            await msg.reply_text(
                text=f"**sᴏᴍᴇ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ, ʀᴇᴘᴏʀᴛ ɪᴛ ᴜsɪɴɢ** `/bug`<b>ᴇʀʀᴏʀ:</b> <code>{ef}</code>"
            )
        count_del_msg = len(message_ids)
        sumit = await msg.reply_text(text=f"ᴅᴇʟᴇᴛᴇᴅ <i>{count_del_msg}</i> ᴍᴇssᴀɢᴇs")
        await sleep(3)
        await sumit.delete()
        return
    await msg.reply_text("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴛᴀʀᴛ ᴘᴜʀɢᴇ !**")
    return

@app.on_message(filters.command("del"))
@adminsOnly("can_delete_messages") 
async def del_msg(app: app, msg: Message):
    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(
            text="**ɪ ᴄᴀɴ'ᴛ ᴘᴜʀɢᴇ ᴍᴇssᴀɢᴇs ɪɴ ᴀ ʙᴀsɪᴄ ɢʀᴏᴜᴘ ᴍᴀᴋᴇ sᴜᴘᴇʀ ɢʀᴏᴜᴘ.**"
        )
        return
    if msg.reply_to_message:
        await msg.delete()
        await app.delete_messages(
            chat_id=msg.chat.id,
            message_ids=msg.reply_to_message.id,
            revoke=True,
        )
    else:
        await msg.reply_text(text="**ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ.**")
        return


__MODULE__ = "Pᴜʀɢᴇ"
__HELP__ = """
**ᴘᴜʀɢᴇ & ᴅᴇʟᴇᴛᴇ:**

• /purge: ɪᴛ ɪs ᴜsᴇᴅ ᴛᴏ ᴘᴜʀɢᴇ ɪɴ ᴀ ɢʀᴏᴜᴘ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ᴀʙᴏᴠᴇ ɪᴛ.
• /del: ɪᴛ ɪs ᴜsᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sɪɴɢʟᴇ ᴍᴇssᴀɢᴇ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴛʜᴇ ᴍᴇssᴀɢᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ.
"""