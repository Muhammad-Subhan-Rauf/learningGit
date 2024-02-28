#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the scientific name for the process of plants making their own food?", "Photosynthesis"),
        ("What is the unit of measurement for electrical resistance?", "Ohm"),
        ("Which gas do plants absorb during photosynthesis?", "Carbon dioxide"),
        ("What is the study of the earth's physical structure and substance called?", "Geology"),
        ("What is the name of the smallest unit of matter?", "Atom"),
        ],
    "History": [
        ("Who was the first President of the United States?", "George Washington"),
        ("Which ancient civilization built the pyramids at Giza?", "Ancient Egyptians"),
        ("What was the main cause of the French Revolution?", "Social inequality and economic hardship"),
        ("Who wrote the 'The Communist Manifesto'?", "Karl Marx and Friedrich Engels"),
        ("What year did World War I begin?", "1914"),
        ]
    }


hints = {
    "Science": [
        ("Hint: This process involves plants using sunlight to produce their own food.", "Photosynthesis"),
        ("Hint: Named after the German physicist who formulated Ohm's Law.", "Ohm"),
        ("Hint: Humans exhale this gas, which plants absorb to produce oxygen.", "Carbon dioxide"),
        ("Hint: This field of science studies rocks, minerals, and the Earth's structure.", "Geology"),
        ("Hint: These are the building blocks of all matter.", "Atom"),
        ],
    "History": [
        ("Hint: He is often referred to as the 'Father of His Country'.", "George Washington"),
        ("Hint: This civilization flourished along the banks of the Nile River.", "Ancient Egyptians"),
        ("Hint: This revolution was fueled by the ideals of liberty, equality, and fraternity.", "French Revolution"),
        ("Hint: This influential political pamphlet advocates for a classless society.", "The Communist Manifesto"),
        ("Hint: It's the year when the assassination of Archduke Franz Ferdinand triggered the war.", "1914"),
        ]
}

#---------------------------------------
import random

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    #------------------------
    return random.choice(questions[category])
    
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    if player_answer == correct_answer:
        return True
    return False
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    for i in questions[category]:
        if i[0] == question:
            questions[category].remove(question)
        
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    #------------------------
    print(question)
    ch = input("Enter your Answer:  ")
    return ch

    # for i in questions:
    #     for j in questions[i]:
    #         if j[0] == question:
    #             answer = 

    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------




