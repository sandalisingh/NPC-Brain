import numpy as np
from States import ActionStates, Range, PersonalityIndex, index_to_range_value, index_to_range_key, get_action, get_personality

class ActionGenerator:

    def __init__(self):
        # Initialize Q-table
        self.no_of_personality_states = 5    # OCEAN personality model
        self.no_of_ranges_of_personality_states = 3  # 3 ranges for each personality states (0-3, 4-7, 8-10)
        self.no_of_emotional_states = 28  # 10 emotional states
        self.no_of_action_states = 10  # 10 action states

        # initialize Q table
        # 5 ocean personality * 3 ranges (0-3,4-7,8-10) * 10 emotional states * 10 FROM action states * 10 TO action states
        self.Q = np.random.random((self.no_of_personality_states, self.no_of_ranges_of_personality_states, self.no_of_emotional_states, self.no_of_action_states, self.no_of_action_states))  # Initialize Q-table with zeros
        # print("Initializing Q table with shape : ", self.Q.size)

        # Parameters
        self.alpha = 0.1  # Learning rate
        self.gamma = 0.9  # Discount factor
        self.epsilon = 0.1  # Exploration rate

    def calculate_reward(self, personality_vector, current_action, next_action):
        reward = 0
        
        # Define all possible transitions and their associated rewards
        transitions = {
            # Unfavorable transitions
            (ActionStates.Patrolling, ActionStates.Attacking): -1,
            (ActionStates.Attacking, ActionStates.Fleeing): -1,
            (ActionStates.Celebrating, ActionStates.Resting): -1,
            (ActionStates.Helping, ActionStates.Attacking): -1,
            (ActionStates.Following, ActionStates.Fleeing): -1,
            # Favorable transitions
            (ActionStates.Interacting, ActionStates.Helping): 1,
            (ActionStates.Interacting, ActionStates.Celebrating): 1,
            (ActionStates.Fleeing, ActionStates.Resting): 1,
            (ActionStates.Fleeing, ActionStates.Interacting): 1,
            (ActionStates.Searching, ActionStates.Interacting): 1,
            (ActionStates.Searching, ActionStates.Patrolling): 1,
            (ActionStates.Attacking, ActionStates.Resting): 1,
            (ActionStates.Attacking, ActionStates.Interacting): 1,
            # Add more transitions as needed
        }

        # Check if the current and next actions correspond to a defined transition
        transition_key = (current_action, next_action)
        if transition_key in transitions:
            reward = transitions[transition_key]

        print("Transition Reward = ", reward)

        # preferable action states for each personality
        personality_preferences = {
            PersonalityIndex.Openness.value: {
                Range.High: (ActionStates.Interacting, ActionStates.Celebrating),
                Range.Medium: (),
                Range.Low: (ActionStates.Resting, ActionStates.Following, ActionStates.Patrolling),
            },
            PersonalityIndex.Conscientiousness.value: {
                Range.High: (ActionStates.Patrolling, ActionStates.Following, ActionStates.Helping),
                Range.Medium: (),
                Range.Low: (ActionStates.Resting, ActionStates.Celebrating, ActionStates.Interacting),
            },
            PersonalityIndex.Extraversion.value: {
                Range.High: (ActionStates.Interacting, ActionStates.Celebrating, ActionStates.Following),
                Range.Medium: (),
                Range.Low: (ActionStates.Resting, ActionStates.Searching, ActionStates.Patrolling),
            },
            PersonalityIndex.Agreeableness.value: {
                Range.High: (ActionStates.Helping, ActionStates.Interacting, ActionStates.Celebrating),
                Range.Medium: (),
                Range.Low: (ActionStates.Attacking, ActionStates.Patrolling, ActionStates.Searching),
            },
            PersonalityIndex.Neuroticism.value: {
                Range.High: (ActionStates.Resting, ActionStates.Fleeing, ActionStates.Interacting),
                Range.Medium: (),
                Range.Low: (ActionStates.Patrolling, ActionStates.Attacking, ActionStates.Celebrating),
            },
        }

        # Check if next_action is one of the preferred actions for each personality trait
        for trait, preferences in personality_preferences.items():
            # print("Personality_vector["+str(trait)+"] = "+str(personality_vector[trait]))
            index = index_to_range_key(personality_vector[trait])
            # print("Mapping - trait:"+str(trait)+" to index:"+str(index))
            if next_action in preferences[index]:
                reward += 1

        print("Preference Reward = ", reward)
        
        # Normalize the total reward to the range [-1, 1]
        max_reward = max(reward for reward in transitions.values()) + len(personality_preferences)  # Add maximum additional reward
        min_reward = min(reward for reward in transitions.values())
        if max_reward != min_reward:
            normalized_reward = 2 * (reward - min_reward) / (max_reward - min_reward) - 1
        else:
            normalized_reward = 0  # Handle the case where all rewards are the same

        print("Normalised Reward = ", reward)

        return normalized_reward

    def action_generator(self, personality_vector, emotional_state_index, previous_action_state_index) :
        # Choose action based on epsilon-greedy policy
        if np.random.rand() < self.epsilon: 
            final_action_state_index = np.random.randint(self.no_of_action_states)  # Choose random action
            print("Random final action state index = ", final_action_state_index)
        else:
            # initialize an array for 10 action states with value 1
            q_val_array = np.ones(10)

            for i in (0,4):     # 5 ocean personalities
                for j in (0,9) :    # 10 action states
                    # Q value of jTH action state = product of Q value of the jTH action state of each ocean personality
                    
                    personality_index = index_to_range_value(personality_vector[i])

                    # print("i - ", i)
                    # print("Personality index - ", personality_index)
                    # print("Emotional state index - ", emotional_state_index)
                    # print("Prev axn state index - ", previous_action_state_index)
                    # print("j - ", j)
                    q_val_array[j] *= self.Q[i][personality_index][emotional_state_index.value][previous_action_state_index.value][j]
            
            # select action state with max q value
            final_action_state_index = np.argmax(q_val_array)  # gives the index of that action state
            print("Final action state index = ", final_action_state_index)

        return final_action_state_index

    def get_dominant_personality(self, personality_vector) :
        dominant_personality_index = np.argmax(personality_vector)
        print("Dominant Personality = ", dominant_personality_index)
        return dominant_personality_index

    def q_learning(self, personality_vector, current_state, next_action_state):
        print("\nStarting with Q Learning ...")

        # Define current and next states
        print("Personality Vector:", personality_vector)
        print("Current State:", current_state)
        print("Next Action State:", get_action(next_action_state))

        # Execute action and observe reward
        reward = self.calculate_reward(personality_vector, current_state[1].value, next_action_state)
        print("Reward:", reward)

        # Update Q-value using Q-learning update rule
        # for dominant personality
        dominant_personality_index = self.get_dominant_personality(personality_vector)
        q_range_index = index_to_range_value(personality_vector[dominant_personality_index])
        print("Dominant Personality :", get_personality(dominant_personality_index))
        print("Q Range Index:", q_range_index)

        q_current = self.Q[dominant_personality_index][q_range_index][current_state[0].value][current_state[1].value][next_action_state]
        max_q_next = np.max(self.Q[dominant_personality_index][q_range_index][current_state[0].value][next_action_state])
        print("Q-value for current state-action pair:", q_current)
        print("Max Q-value for next state:", max_q_next)

        updated_q_value = (1 - self.alpha) * q_current + self.alpha * (reward + self.gamma * max_q_next)
        print("Updated Q-value:", updated_q_value)

        self.Q[dominant_personality_index][q_range_index][current_state[0].value][current_state[1].value][next_action_state] = updated_q_value

        # Q table for 
        q_table_slice = self.Q[dominant_personality_index][q_range_index][current_state[0].value]
        print("Q table slice:")
        print(q_table_slice)
