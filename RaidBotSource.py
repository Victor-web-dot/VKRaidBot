import time
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
botpass=input('Введите пароль: ')
if(botpass=='b523aqAPzE2JEgSUnQQ9MrwMDGbmpGwV'):
    print('Бот успешно разблокирован. Теперь пригласите страничку подключенную к нему в беседу и пропишите там команду: Начать')
    vk_session = vk_api.VkApi(token='')
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text == 'Начать' or event.text == '/start':
                if event.from_chat:
                    a=1
                    while(a<1000):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=0,
                            message='😀😁😂🤣😃😄😅😆😉😊😋😎😍😘😗😆😙😚☺🙂🤩🤗🤨🤔😐😑😶🙄😏😜🤐😔🤬😡😷😱😬😧🤤☹😳🤢🤢🤧😇😈😈👿🙀🤖👽💀☠👻😻😹😸😻🙊🙉🙈👩🧒👴👦👨‍⚕️👨‍🎓️👨‍🍳️👨‍✈️🧕👲👳‍♀️👳🤴🕵💂👩‍🎤️👨‍🎤️👩‍💻️👨‍💻️💆🙋‍♂️🧘🧗👯💆‍♂️🏃‍♀️🏃‍♀️🛌⛷🤸‍♂️🏋‍♀️🏄🚵🤹🤾🤼🤹🤾🏄💑💗🤚💅✋✋🖕👆👆☝👉👊🤟🙌✍🤞🖖👏👃👍🤙🤜🤝💕💝💦💨💥💣💤💌🧣👑💭🛍🎒👠👔💬🦒🐿🦉🐓🐓🐓🐓🐳🐚🐛🐌🦑🕸🦂🕷🕸💐💮🏵🦐🦕🐧🐤🍔🥕🥝🍳🍿🍄🍞🎏🎍🎍🎏🎏🏉🏉🏉🏒🏒🏑🎟🎟🎟🎎🎎🎑🏅🏅🏉🏸🏸🌏🌏🗺🗺🥌🥌🎴⛺⛲⛲⛩⛩🏯🏯🏯🏦♨🚆🎪🛸🌆🛩🛎🕠🕜🕡🕥🕠🕓🕒🚽🚽💺⛴🛋🌩🌛🌔🌕🌠🌞🌗🌤🌈🔉🔇📻🎹📢📯🎤🔌📜🔎🖲🔭📚💸🏷📰🕯📘📮✏🖋🖊📋✂📏📍⛏⚒💊🚹🚰🏧🚳🛃⚠🚷🔞🚯🔂🕎♈♒🔽🎦©❇✖📛🔆📳📴⃣🆓🔠💯🈺🉐🈹🈚🉑🈳🈴🔸🔷⬛🇦🇬🚩🏳‍🌈️🏃‍♀️😀😁😂🤣😃😄😅😆😉😊😋😎😍😘😗😆😙😚☺🙂🤩🤗🤨🤔😐😑😶🙄😏😜🤐😔🤬😡😷😱😬😧🤤☹😳🤢🤢🤧😇😈😈👿🙀🤖👽💀☠👻😻😹😸😻🙊🙉🙈👩🧒👴👦👨‍⚕️👨‍🎓️👨‍🍳️👨‍✈️🧕👲👳‍♀️👳🤴🕵💂👩‍🎤️👨‍🎤️👩‍💻️👨‍💻️💆🙋‍♂️🧘🧗👯💆‍♂️🏃‍♀️🏃‍♀️🛌⛷🤸‍♂️🏋‍♀️🏄🚵🤹🤾🤼🤹🤾🏄💑💗🤚💅✋✋🖕👆👆☝👉👊🤟🙌✍🤞🖖👏👃👍🤙🤜🤝💕💝💦💨💥💣💤💌🧣👑💭🛍🎒👠👔💬🦒🐿🦉🐓🐓🐓🐓🐳🐚🐛🐌🦑🕸🦂🕷🕸💐💮🏵🦐🦕🐧🐤🍔🥕🥝🍳🍿🍄🍞🎏🎍🎍🎏🎏🏉🏉🏉🏒🏒🏑🎟🎟🎟🎎🎎🎑🏅🏅🏉🏸🏸🌏🌏🗺🗺🥌🥌🎴⛺⛲⛲⛩⛩🏯🏯🏯🏦♨🚆🎪🛸🌆🛩🛎🕠🕜🕡🕥🕠🕓🕒🚽🚽💺⛴🛋🌩🌛🌔🌕🌠🌞🌗🌤🌈🔉🔇📻🎹📢📯🎤🔌📜🔎🖲🔭📚💸🏷📰🕯📘📮✏🖋🖊📋✂📏📍⛏⚒💊🚹🚰🏧🚳🛃⚠🚷🔞🚯🔂🕎♈♒🔽🎦©❇✖📛🔆📳📴⃣🆓🔠💯🈺🉐🈹🈚🉑🈳🈴🔸🔷⬛🇦🇬🚩🏳‍🌈️🏃‍♀️😀😁😂🤣😃😄😅😆😉😊😋😎😍😘😗😆😙😚☺🙂🤩🤗🤨🤔😐😑😶🙄😏😜🤐😔🤬😡😷😱😬😧🤤☹😳🤢🤢🤧😇😈😈👿🙀🤖👽💀☠👻😻😹😸😻🙊🙉🙈👩🧒👴👦👨‍⚕️👨‍🎓️👨‍🍳️👨‍✈️🧕👲👳‍♀️👳🤴🕵💂👩‍🎤️👨‍🎤️👩‍💻️👨‍💻️💆🙋‍♂️🧘🧗👯💆‍♂️🏃‍♀️🏃‍♀️🛌⛷🤸‍♂️🏋‍♀️🏄🚵🤹🤾🤼🤹🤾🏄💑💗🤚💅✋✋🖕👆👆☝👉👊🤟🙌✍🤞🖖👏👃👍🤙🤜🤝💕💝💦💨💥💣💤💌🧣👑💭🛍🎒👠👔💬🦒🐿🦉🐓🐓🐓🐓🐳🐚🐛🐌🦑🕸🦂🕷🕸💐💮🏵🦐🦕🐧🐤🍔🥕🥝🍳🍿🍄🍞🎏🎍🎍🎏🎏🏉🏉🏉🏒🏒🏑🎟🎟🎟🎎🎎🎑🏅🏅🏉🏸🏸🌏🌏🗺🗺🥌🥌🎴⛺⛲⛲⛩⛩🏯🏯🏯🏦♨🚆🎪🛸🌆🛩🛎🕠🕜🕡🕥🕠🕓🕒🚽🚽💺⛴🛋🌩🌛🌔🌕🌠🌞🌗🌤🌈🔉🔇📻🎹📢📯🎤🔌📜🔎🖲🔭📚💸🏷📰🕯📘📮✏🖋🖊📋✂📏📍⛏⚒💊🚹🚰🏧🚳🛃⚠🚷🔞🚯🔂🕎♈♒🔽🎦©❇✖📛🔆📳📴⃣🆓🔠💯🈺🉐🈹🈚🉑🈳🈴🔸🔷⬛🇦🇬🚩🏳‍🌈️🏃‍♀️'
                            )
                        time.sleep(0.9)
else:
    print('Бот заблокирован')
    
