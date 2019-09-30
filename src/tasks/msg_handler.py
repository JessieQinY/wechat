from pathlib import Path
from wxpy import *
from .notes import set_note



print('before')




def help_message():
    text = '''
    输入"set note"， 设置提醒;
    输入任意问题，与机器人问答；
    '''
    return text


# embed()
bot.join()
print('bot process finished')
