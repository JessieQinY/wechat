from pathlib import Path
from multiprocessing import Process
from wxpy import *
from src.tasks.notes import send_note, set_note

cache_path = Path(__file__).parent / 'cache'
bot = Bot(cache_path=cache_path / 'wxpy.pkl')

help_message = '''
设置提醒：时间，消息
设置提醒：2019-10-01-08，起床啦
'''


@bot.register()
def distribute_messages(msg):
    message = msg.text.lower()
    if 'help' in message:
        return help_message

    if '设置提醒' in message:
        return set_note(f'{msg.chat}，{msg.text}')

    return 'got your message'


@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    if '咸鱼少女' in msg.text.lower():
        new_friend = bot.accept_friend(msg.card)
        new_friend.send('你好，我是咸鱼少女，很高兴认识你!')
        new_friend.send('输入"help"，获取帮助信息')


def main():
    alert = Process(name='send_note', target=send_note, args=(bot,))
    alert.start()


if __name__ == '__main__':
    main()
