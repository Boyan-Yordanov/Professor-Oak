import re


def input_function(question):
    cleaned_question = re.sub(
        r"[!?.]", "", question.lower()
    )  # Remove unwanted characters
    input_word_list = cleaned_question.split()  # Split cleaned question into a list
    original_word_list = question.rsplit()  # Split original question into a list
    return [input_word_list, original_word_list]
