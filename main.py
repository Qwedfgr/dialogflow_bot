import logging
import dotenv
import os
import vk_bot
import tg_bot


def main():

    dotenv.load_dotenv()
    TOKEN_TG = os.environ["token_tg"]
    chat_id = os.environ["chat_id"]
    PROJECT_ID = os.environ['project_id']
    credential_path = u'C:/Users/Георгий/PycharmProjects/dialogflow/newagent-dqntos-1ae36c327db5.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    TOKEN_VK = os.environ["TOKEN_VK"]

    tg_bot.run_tg_bot(TOKEN_TG, PROJECT_ID)

    vk_bot.run_vk_bot(TOKEN_VK, PROJECT_ID)




if __name__ == '__main__':
    main()




