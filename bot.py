from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Para corrigir um bug da atual versao
from spacy.cli import download

download("en_core_web_sm") 

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot("Bot_teste", tagger_language=ENGSM)

conversa = [
    "Ola",
    "E aí, tranquilo?",
    "Tranquilo",
    "Como vai?",
    "Ah, eu estou bem",
    "O que voce e?",
    "Eu sou um bot",
    "Irado",
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)

while True:
    mensagem = input("Converse com o chatbot:")
    if mensagem == "parar":
        break
    resposta = chatbot.get_response(mensagem)
    print(resposta)