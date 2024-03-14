from NPC_Brain import NPC_Brain

personality_vector = [1,2,3,4,5]

environemnt = input("Environment = ")

NPC = NPC_Brain(personality_vector, environemnt)

emotion = NPC.get_emoji()
action = NPC.get_current_action_state()
print("BOT - emotion = ", emotion)
print("BOT - action = ", action)

while(True):
    chat = input("Chat = ")
    reply = NPC.generate_reply(chat)
    emotion = NPC.get_emoji()
    action = NPC.get_current_action_state()
    print("BOT - response = ", reply)
    print("BOT - emotion = ", emotion)
    print("BOT - action = ", action)