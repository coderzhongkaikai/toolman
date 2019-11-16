from nonebot import on_command, CommandSession
from nonebot.typing import Context_T
import nonebot.helpers
import nonebot
from dfaMaster.app.test import check_sensitive
bot = nonebot.get_bot()
@bot.on_message('group')
async def handle_group_message(ctx: Context_T):
    text=""
    for i in ctx.get('message'):
        if i.type == 'text':
            text += i.data['text']

    ifDangerous = check_sensitive(text)
    try:
      pass
    except:
        print('dfa error')
        return
    if ifDangerous:
        text='危险言论'
        await nonebot.helpers.send(bot=bot, ctx=ctx, message=text)