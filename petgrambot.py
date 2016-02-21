import sys
import time
import telepot
import pygame


class YourBot(telepot.Bot):
    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if(content_type == 'voice' and chat_type == ('private' or 'group')):
            self.sendMessage(chat_id, "Thanks for sending me a voice note!")
            self.downloadFile(msg['voice']['file_id'], '/.')
            #pygame.mixer.init()
            #pygame.mixer.music.load()
            #pygame.mixer.music.play()
            #while pygame.mixer.music.get_busy() == True:
            #    continue


#TOKEN = sys.argv[1]  # get token from command-line

bot = YourBot('187480658:AAGGKZhviajklIiYbAiBif71YUCOToE8-6g')
bot.notifyOnMessage()

# Keep the program running.
while 1:
    time.sleep(10)