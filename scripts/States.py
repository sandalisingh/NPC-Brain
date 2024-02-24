from enum import Enum

class ActionStates(Enum):
    Patrolling = 0
    Attacking = 1
    Fleeing = 2
    Alerted = 3
    Searching = 4
    Interacting = 5
    Resting = 6
    Following = 7
    Celebrating = 8
    Helping = 9

class EmotionStates(Enum):
    Loving = 0
    Confident = 1
    Excited = 2
    Annoyed = 3
    Teasing = 4
    Sad = 5
    Happy = 6
    Angry = 7
    Nervous = 8
    Crying = 9

class PersonalityIndex(Enum):
    Openness = 0
    Conscientiousness = 1
    Extraversion = 2
    Agreeableness = 3
    Neuroticism = 4

class Range(Enum):
    Low = range(0, 4)      
    Medium = range(4, 8)   
    High = range(8, 11)