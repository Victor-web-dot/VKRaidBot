# Первоначальная настройка
pip install cx_freeze vk_api requests
# Запуск
Для начала откройте RaidBotSource.py в редакторе кода(в любом поддерживающем .py файлы)
В строке vk_session = vk_api.VkApi(token='') меж одинарных кавычек пропишите токен который взят с vkhost.github.io или любого другого сайта. Имейте ввиду что бот страничный и ему нужен токен вашей страницы для Kate Mobile иначе работать он не будет.
После добавления токена в файл запустите RaidBotSource.py в CMD или Терминале. Пропишите cd и после этого путь к файлу с ботом. Затем пропишите python ./RaidBotSource.py
После ввода пароля пригласите в нужную беседу страничку токен от которой вы использовали в боте. И пропишите в чат команду Начать или /start.  И в чатике начнется полная дурка :3.
Если вк выдаст капчу то бот по идее должен попросить ее у вас.
# Сборка в .exe файл
Пропишите в CMD cd и путь к файлу setup.py. Как только вы это сделали пропишите python ./setup.py build.
В директории файла с ботом и setup.py появится папка build в которой будет находится исполняемый файл с названием файла бота.
Запускать .exe файл точно также как скрипт. Только пишете просто путь к файлу без python. Если у вас до этого не было токена в файле с ботом то в .exe он не заработает.


И ДА Я ЗНАЮ ЧТО СКРИПТ ДОХУЯ ПРОСТОЙ И ЕГО МОЖЕТ ПОВТОРИТЬ КАЖДЫЙ НО СУКА НЕ ПРОСТО ТАК Я ЕГО ВЫЛОЖИЛ? Я ЕГО ВЫЛОЖИЛ ДЛЯ ЛЕНИВЫХ ЖОП КОТОРЫМ ЛЕНЬ СВОЙ ДЕЛАТЬ.



