
from telethon import events
from telethon.errors import ChatAdminRequiredError


@borg.on(events.MessageDeleted)
async def handler(event):
    me = await event.client.get_me()
    me_id = me.id
    grup = await event.client.get_entity(event.chat_id)
    group_ismi = grup.title

    try:
        if event and event.chat_id != me_id:

            events = await event.client.get_admin_log(event.chat_id, delete=True)
            user = await event.client.get_entity(events[0].user_id)
            ismi = user.first_name
            # if user.username is not None:
            #     k_adi = user.username
            silinen_msg = events[0].old.message
            kullanici = f"[{ismi}](tg://user?id={user.id})"
            msg = f"**{group_ismi} Grubundan Silinen Mesaj\n\n**"\
                f"**Silen Kişi:** __{kullanici}__\n\n**Silinen Mesaj:** __{silinen_msg}__"

            if events[0].old.media is not None:

                medya = events[0].old.media
                msg = f"**{group_ismi} Grubundan Silinen Medya\n\n**"\
                    f"**Silen Kişi:** __{kullanici}__\n\n"

                await event.client.send_message(
                    entity=-1001220834298,
                    message=msg,
                    file=medya,
                    force_document=False
                )
            else:

                await event.client.send_message(
                    entity=-1001220834298,
                    message=msg
                )
    except ChatAdminRequiredError:
        return
