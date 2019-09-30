import time
from datetime import datetime
from pathlib import Path
from wxpy import Bot
from src.tasks.news import get_weekly_news, get_hellogit_news

note_file = Path(__file__).parent / 'note_list.txt'


def send_note(bot: Bot):
    while True:
        with open(note_file) as fp:
            all_notes = fp.readlines()
            for text in all_notes:
                note = text.split('，')
                name = note[0]
                alert_time = note[1]
                alert_msg = note[2]
                friend = bot.friends().search(name)[0]
                if _should_send(alert_time):
                    friend.send(alert_msg)
                    all_notes.remove(text)
            fp.write('\n'.join(all_notes))
        news = [get_weekly_news(), get_hellogit_news()]
        friend = bot.friends().search('秦')[0]
        for new in news:
            friend.send(f'news: {new}')
        time.sleep(60 * 59)


def _should_send(alert_time):
    alert_time = datetime.strptime(alert_time, '%Y-%m-%d-%H')
    current = datetime.now()
    if (current-alert_time).seconds < 60 * 60:
        return True
    return False


def set_note(text):
    try:
        with open(note_file, 'a') as fp:
            fp.write(text)
        return '设置成功'
    except Exception as e:
        return f'设置失败， {e}'


