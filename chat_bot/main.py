import vk_api
import vk_api.bot_longpoll
import random


class ChatBot:
    def __init__(self):
        self._security_key = "4e8dcdfd0b892022efaf5c7f006795a4880742339352863b374f3776a493e997e506549fc5dfe5371ed63"
        self._group_id = 209994312
        self.vk = vk_api.VkApi(token=self._security_key)
        self.vk_long_poller = vk_api.bot_longpoll.VkBotLongPoll(group_id=self._group_id, vk=self.vk)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.vk_long_poller.listen():
            if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
                print(event.message.text)
                self.api.messages.send(
                    message="Начнем с того что ты ПИЗДОГЛАЗОЕ мудило, "
                             "вот твоё ссаное сообщение: " + str(event.message.text),
                    peer_id=event.message.peer_id,
                    random_id=random.randint(0, 2 ** 20)
                )


if __name__ == "__main__":
    bot = ChatBot()
    bot.run()
