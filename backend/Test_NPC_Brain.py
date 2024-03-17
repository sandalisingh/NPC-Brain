from NPC_Brain import NPC_Brain

personality_vector = [1,2,3,4,5]

environemnt = input("Environment = ")

NPC = NPC_Brain(personality_vector, environemnt)

emoji = NPC.get_emoji()
emotion = NPC.get_current_emotion_state()
action = NPC.get_current_action_state()
print("BOT - emoji = ", emoji)
print("BOT - emotion = ", emotion)
print("BOT - action = ", action)

while(True):
    chat = input("Chat = ")
    reply = NPC.generate_reply(chat)
    emoji = NPC.get_emoji()
    emotion = NPC.get_current_emotion_state()
    action = NPC.get_current_action_state()
    print("BOT - response = ", reply)
    print("BOT - emoji = ", emoji)
    print("BOT - emotion = ", emotion)
    print("BOT - action = ", action)