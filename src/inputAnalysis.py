def number_finder(wordList):
    for word in wordList:
        if word.isdigit():
            return int(word)
        elif word in ["one", "first"]:
            return 1
        elif word == "second":
            return 2
    return 1


def input_breakdown(wordList):
    special_type_request = []
    special_types = [
        "normal",
        "fire",
        "fighting",
        "water",
        "flying",
        "grass",
        "poison",
        "electric",
        "ground",
        "psychic",
        "rock",
        "ice",
        "bug",
        "dragon",
        "ghost",
        "dark",
        "steel",
        "fairy",
    ]
    useless_words = ["me", "i", "am", "a", "is", "the"]
    quest_list = ["which", "what", "how", "tell", "do"]
    type_list = ["type", "kind"]
    best_list = ["best", "popular", "top"]
    number_list = ["number"]
    amount_list = ["many"]
    worst_list = ["worst", "last"]
    contains = {
        "quest": False,
        "types": False,
        "number": False,
        "amount": False,
        "best": False,
        "worst": False,
        "isa": False,
        "special_type": False,
        "all_pokemon": False,
    }

    for word in reversed(wordList):
        if word in special_types:
            contains["special_type"] = True
            special_type_request.append(word.capitalize())
            wordList.remove(word)
        elif word in quest_list:
            contains["quest"] = True
            wordList.remove(word)
        elif word in type_list:
            contains["types"] = True
            wordList.remove(word)
        elif word in number_list:
            contains["number"] = True
            wordList.remove(word)
        elif word in amount_list:
            contains["amount"] = True
            wordList.remove(word)
        elif word in best_list:
            contains["best"] = True
            wordList.remove(word)
        elif word in worst_list:
            contains["worst"] = True
            wordList.remove(word)
        elif word in useless_words:
            wordList.remove(word)

    if "all" in wordList:
        all_pokemon = True
        wordList.remove("all")
    elif "is" in wordList and ("a" in wordList or "an" in wordList):
        isa = True
        wordList.remove("is")
        wordList.remove("a" if "a" in wordList else "an")
    elif ("is" in wordList or "are" in wordList) and "there" in wordList:
        all_pokemon = True
        wordList.remove("is" if "is" in wordList else "are")
        wordList.remove("there")

    req_number = number_finder(wordList)
    output_info = [contains["quest"], contains["isa"], wordList]
    info_list_pokemon = [
        contains["types"],
        contains["amount"],
        contains["best"],
        contains["worst"],
        contains["special_type"],
        special_type_request,
        req_number,
        wordList,
        contains["all_pokemon"],
        contains["number"],
    ]

    return [info_list_pokemon, output_info]
