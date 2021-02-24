import asyncio
import time
from collections import deque

from telethon.tl.functions.channels import LeaveChannelRequest

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd("(leave|bye|kickme)$"))
async def leave(e):
    if e.fwd_from:
        return
    if e.is_private:
        await friday.tr_engine(event, "`I Can't Do That.`")
        return
    await friday.tr_engine(event, f"My Master {bot.me.first_name} Wishes To Leave This Chat, So Bye.")
    await e.client.kick_participant(e.chat_id, bot.me.id)


@friday.on(friday_on_cmd(";__;$"))
async def fun(e):
    if e.fwd_from:
        return
    t = ";__;"
    for j in range(10):
        t = t[:-1] + "_;"
        await friday.tr_engine(event, t)


@friday.on(friday_on_cmd("yo$"))
async def Ooo(e):
    if e.fwd_from:
        return
    t = "yo"
    for j in range(15):
        t = t[:-1] + "oo"
        await friday.tr_engine(event, t)


@friday.on(friday_on_cmd("Oof$"))
async def Oof(e):
    if e.fwd_from:
        return
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await friday.tr_engine(event, t)


@friday.on(friday_on_cmd("ccry$"))
async def cry(e):
    if e.fwd_from:
        return
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await friday.tr_engine(event, "(;´༎ຶД༎ຶ)")


@friday.on(friday_on_cmd("fap$"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🍆✊🏻💦"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await friday.tr_engine(event, "".join(deq))
        deq.rotate(1)


CMD_HELP.update({"leave": "Leave a Chat"})
CMD_HELP.update({"cry": "Cry"})
CMD_HELP.update({"fap": "Faking orgasm"})
