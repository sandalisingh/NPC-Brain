import numpy as np

class ActionGenerator:

    def __init__(self):
        # Initialize Q-table
        self.no_of_personality_states = 5    # OCEAN personality model
        self.no_of_ranges_of_personality_states = 3  # 3 ranges for each personality states (0-3, 4-7, 8-10)
        self.no_of_emotional_states = 10  # 10 emotional states
        self.no_of_action_states = 10  # 10 action states

        # initialize Q table
        # 5 ocean personality * 3 ranges (0-3,4-7,8-10) * 10 emotional states * 10 FROM action states * 10 TO action states
        self.Q = np.random.random((no_of_personality_states, no_of_ranges_of_personality_states, no_of_emotional_states, no_of_action_states, no_of_action_states))  # Initialize Q-table with zeros

        # Parameters
        self.alpha = 0.1  # Learning rate
        self.gamma = 0.9  # Discount factor
        self.epsilon = 0.1  # Exploration rate

    # Define reward function (example)
    def calculate_reward(personality_vector, current_action, next_action):
        reward = 0
        
        # Assign rewards based on personality type and emotional state
        if personality_type == "Extraversion":
            if emotional_state == "Happy":
                if action_taken in ["Interacting", "Celebrating", "Following", "Helping"]:
                    reward += 1
                elif action_taken == "Attacking":
                    reward -= 1
            elif emotional_state == "Sad":
                if action_taken == "Resting":
                    reward += 1
                elif action_taken in ["Attacking", "Fleeing"]:
                    reward -= 1
            # Add more conditions for other emotional states and actions
            
        # Add rewards for other personality types

        reward /= 5
        print("Reward = ", reward)
        
        return reward

    def action_generator(self, personality_vector, emotional_state_index, previous_action_state_index) :
        # Choose action based on epsilon-greedy policy
        if np.random.rand() < epsilon: 
            final_action_state_index = np.random.randint(self.no_of_action_states)  # Choose random action
        else:
            # initialize an array for 10 action states with value 1
            q_val_array = np.ones(10)

            for i in (0,4):     # 5 ocean personalities
                for j in (0,9) :    # 10 action states
                    # Q value of jTH action state = product of Q value of the jTH action state of each ocean personality
                    q_val_array[j] *= Q[i][(personality_vector[i]/3)-1][emotional_state_index][previous_action_state_index][j]
            
            # select action state with max q value
            final_action_state_index = np.argmax(q_val_array)  # gives the index of that action state
            print("Final action state index = ", final_action_state_index)

        return final_action_state_index

    def q_learning(self, personality_vector, current_state, next_state) :
        # Define current and next states
        # current_state = (emotional_state_index, action_state_index)
        # next_state = (next_emotional_state_index, next_action_state_index)

        # Execute action and observe reward         ### DIALOGUE GENERATION !!!!!
        reward = self.calculate_reward(current_state[1], next_state[1])

        # Update Q-value using Q-learning update rule
        # for dominant personality !!!!
        self.Q[current_state][final_action_state_index] = (1 - alpha) * self.Q[current_state][final_action_state_index] + alpha * (reward + gamma * np.max(self.Q[next_state]))
