
import requests
from .models import TeleSettings


def sendTelegram(tg_name, tg_phone, ip):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_msg)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        a = text.find('{')
        b = text.find('}')
        c = text.rfind('{')
        d = text.rfind('}')

        part_1 = text[0:a]
        part_2 = text[b+1:c]
        part_3 = text[d:-1]

        text_slice = ip + part_1 + tg_name + part_2 + tg_phone + part_3
        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slice
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print('False!')
            elif req.status_code == 500:
                print('Server')
            else:
                print('Great Job')
    else:
        pass
