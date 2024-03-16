from EmotionGenerator import EmotionGenerator
from ActionGenerator import ActionGenerator
# from DialogueGenerator import DialogueGenerator
from States import ActionStates

class NPC_Brain:
    def __init__(self, personality_vector=[1,2,3,4,5], environment="Resting", emotional_state=None, action_state=None):
        self.PERSONALITY_VECTOR = personality_vector
        self.EMOTION_GENERATOR = EmotionGenerator(self.PERSONALITY_VECTOR, environment)
        self.ACTION_GENERATOR = ActionGenerator()
        
        if emotional_state is None:
            self.EMOTIONAL_STATE = self.EMOTION_GENERATOR.get_emotion_state()
        else:
            self.EMOTIONAL_STATE = emotional_state

        if action_state is None:
            self.ACTION_STATE = self.ACTION_GENERATOR.generate_action(self.PERSONALITY_VECTOR, self.EMOTIONAL_STATE)
        else:
            self.ACTION_STATE = action_state

    def generate_reply(self, chat_text):
        prev_emotion_state = self.EMOTIONAL_STATE
        self.EMOTIONAL_STATE = self.EMOTION_GENERATOR.update_emotion(chat_text)
        prev_action_state = self.ACTION_STATE
        self.ACTION_STATE = self.ACTION_GENERATOR.generate_action(self.PERSONALITY_VECTOR, self.EMOTIONAL_STATE, self.ACTION_STATE)

        prev_state = [prev_emotion_state, prev_action_state]
        self.ACTION_GENERATOR.q_learning(self.PERSONALITY_VECTOR, prev_state, self.ACTION_STATE)
        return "Dummy text"

    def get_emoji(self):
        return self.EMOTION_GENERATOR.get_current_emotion_emoji()
    
    def get_current_emotion_state(self):
        return self.EMOTIONAL_STATE
    
    def get_current_action_state(self):
        return self.ACTION_STATE.name

    