## -*- coding: utf-8 -*-
import vk_api, random, time, wikipedia
from vk_api.longpoll import VkLongPoll, VkEventType, VkMessageFlag

token1 = "9be2c0c01d2192faaa3e6006b576ca2f48d180e218915e25f6c306002d0f46a8d7bd7e67f0596d5a70171"

vk_session = vk_api.VkApi(token=token1)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender_me(id, text):
	vk.messages.send(user_id=id, message=text, random_id=0)

def sender_chat(id, text):
	vk.messages.send(chat_id=id, message=text, random_id=0)

wikipedia.set_lang("RU")

print('Бот запущен')
p_d_c = random.randint(0, 999999999)

as_89 = "негр"

sender_me(400484262, 'Бот запущен')

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        try:
            if event.from_user:
                id = event.user_id
                msg = event.text.lower()
                msgl = event.text
                te2xt = msg.split(' ')

                if id in [400484262]:

                    if "написать" in event.text.lower():
                        if te2xt[0] == "написать":
                            a = te2xt[1]
                            vk.messages.setActivity(peer_id=2000000000 + int(a), type="typing")
                            time.sleep(4)
                            sender_chat(int(a), msgl.split(" ", 2)[2])
                            sender_me(id, "Сообщение " + msgl.split(" ", 2)[2] + " <br>Отправлено в чат " + str(a))

            if event.from_chat:
                id = event.chat_id
                user = event.user_id
                msg = event.text.lower()
                msgl = event.text
                te2xt = msg.split(' ')
                a_time = event.timestamp

                if user in [585702599]:
                    g = 1

                else:
                    if as_89 in event.text.lower():
                        if str(p_d_c) in msg:
                            dw = 1

                        else:
                            dk_r_u1 = vk.users.get(user_ids=user, name_case='nom')
                            dk_r_n_11 = dk_r_u1[0]["first_name"]
                            dk_r_n_21 = dk_r_u1[0]["last_name"]
                            dk_r_n_f1 = dk_r_n_11 + ' ' + dk_r_n_21
                            dk_n_f_n1 = '[id' + str(user) + '|' + dk_r_n_f1 + ']'

                            c_time = time.ctime(a_time)
                            dk = dk_n_f_n1 + '<br>' + c_time + '<br>Ключ: ' + as_89 + '<br>Чат айди: ' + str(id) + '<br>Текст сообщения: ' + msgl + '<br>Протокол защиты: ' + str(p_d_c)

                            sender_me(400484262, dk)

                    if user in [400484262]:

                        if "написать" in event.text.lower():
                            if te2xt[0] == "написать":
                                msg_nm = msgl.split(" ", 1)[1]
                                vk.messages.setActivity(peer_id=2000000000 + id, type="typing")
                                time.sleep(4)
                                sender_chat(id, msg_nm)

                        if "чат айди" in event.text.lower():
                            sender_me(400484262, 'Чат айди: ' + str(id))

                    if "отклик" in event.text.lower():
                        otklik = time.time()
                        sender_chat(id, str(otklik) + ' мс')

                    if msg in ['random key']:
                        p_d_c = random.randint(0, 999999999)
                        sender_chat(id, 'Новый ключ протокола защиты установлен')

                    if "кнб" in event.text.lower():
                        kmb11 = msg.split(" ", 2)
                        kmb1 = kmb11[1]
                        kmb2 = ['камень', 'ножницы', 'бумага']
                        kmb3 = random.choice(kmb2)
                        if kmb1 == 'камень':
                            if kmb3 == 'камень':
                                sender_chat(id, 'Камень<br>Ничья!')
                            if kmb3 == 'ножницы':
                                sender_chat(id, 'Ножницы<br>Вы выйграли')
                            if kmb3 == 'бумага':
                                sender_chat(id, 'Бумага<br>Вы проиграли')
                                
                        if kmb1 == 'ножницы':
                            if kmb3 == 'ножницы':
                                sender_chat(id, 'Ножницы<br>Ничья!')
                            if kmb3 == 'камень':
                                sender_chat(id, 'Камень<br>Вы проиграли')
                            if kmb3 == 'бумага':
                                sender_chat(id, 'Бумага<br>Вы выйграли')

                        if kmb1 == 'бумага':
                            if kmb3 == 'бумага':
                                sender_chat(id, 'Бумага<br>Ничья!')
                            if kmb3 == 'ножницы':
                                sender_chat(id, 'Ножницы<br>Вы проиграли')
                            if kmb3 == 'камень':
                                sender_chat(id, 'Камень<br>Вы выйграли')

                    if "ключ" in event.text.lower():
                        as_89 = msg.split(" ", 1)[1]
                        sender_chat(id, 'Ключ longpoll.listen() ' + as_89 + ' успешно установлен')

                    if "вики" in event.text.lower():
                        qies3t_wiki = msg.replace("вики ", "")
                        try:
                            wiki_redsult = str(wikipedia.summary(qies3t_wiki))
                            sewnd_wiki = "Вот что я нашла: <br>" + wiki_redsult
                            sender_chat(id, f'' + sewnd_wiki)
                        except:
                            sender_chat(id, f'По вашему запросу ничего не найдено')
                    
                    if msg in ['орел и решка', 'монетка']:
                        o_and_r = ['Выпал орёл', 'Выпала решка']
                        r232313 = random.choice(o_and_r)
                        sender_chat(id, f'' + r232313)

                    if msg in ["кто онлайн"]:
                        f = vk.messages.getConversationMembers(peer_id=2000000000 + id, fields="online")
                        al = -1
                        sw_all = ""
                        try:
                            while True:
                                al = al + 1
                                sw1 = f["profiles"][al]["first_name"]
                                sw2 = f["profiles"][al]["last_name"]
                                sw3 = f["profiles"][al]["id"]
                                sw4 = f["profiles"][al]["online"]
                                if sw4 == 1:
                                    sw_al = "[id" + str(sw3) + "|" + sw1 + " " + sw2 + "]"
                                    sw_all += "<br>" + sw_al
                        except:
                            sender_chat(id, 'Пользователи онлайн:' + sw_all)

                    if "женя кто" in event.text.lower():
                        user_q_r = msgl.split(" ", 2)
                        userclfo = vk.messages.getConversationMembers(peer_id=2000000000 + id)
                        user_r_fef = userclfo["items"]
                        user_r_fef_l = random.choice(user_r_fef)
                        user_r_fef_l_o = user_r_fef_l["member_id"]

                        user_r_u = vk.users.get(user_ids=user_r_fef_l_o, name_case='nom')
                        user_r_n_1 = user_r_u[0]["first_name"]
                        user_r_n_2 = user_r_u[0]["last_name"]
                        user_r_n_f = user_r_n_1 + ' ' + user_r_n_2
                        user_n_f_n = '[id' + str(user_r_fef_l_o) + '|' + user_r_n_f + ']'

                        sender_chat(id, 'Я думаю ' + str(user_q_r[2]) + ' ' + user_n_f_n)

                    if "женя инфа" in event.text.lower():
                        infa_ra = random.randint(0, 100)
                        sender_chat(id, 'Я думаю это ' + str(infa_ra) + '%')

        except Exception as e:
            print(e)
            sender_me(400484262, str(e))