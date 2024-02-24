import numpy as np

# Initialize Q-table
no_of_personality_states = 5    # OCEAN personality model
no_of_ranges_of_personality_states = 3  # 3 ranges for each personality states (0-3, 4-7, 8-10)
no_of_emotional_states = 10  # 10 emotional states
no_of_action_states = 10  # 10 action states

# initialize Q table
# 5 ocean personality * 3 ranges (0-3,4-7,8-10) * 10 emotional states * 10 FROM action states * 10 TO action states
Q = np.random.random((no_of_personality_states, no_of_ranges_of_personality_states, no_of_emotional_states, no_of_action_states, no_of_action_states))  # Initialize Q-table with zeros

# Parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor

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
    
    return reward

def action_generator(personality_vector, current_state) :
    # Choose action based on epsilon-greedy policy
    epsilon = 0.1  # Exploration rate
    if np.random.rand() < epsilon:
        final_action_state_index = np.random.randint(no_of_action_states)  # Choose random action
    else:
        final_action_state_index = np.argmax(Q[current_state])  # PROBABILITY MULTIPLICATION !!!!

    return final_action_state_index

def q_learning(personality_vector, current_state, next_state) :
    # Define current and next states
    # current_state = (emotional_state_index, action_state_index)
    # next_state = (next_emotional_state_index, next_action_state_index)

    # Execute action and observe reward         ### DIALOGUE GENERATION !!!!!
    reward = calculate_reward(current_state[1], next_state[1])

    # Update Q-value using Q-learning update rule
    # for dominant personality !!!!
    Q[current_state][final_action_state_index] = (1 - alpha) * Q[current_state][final_action_state_index] + alpha * (reward + gamma * np.max(Q[next_state]))
