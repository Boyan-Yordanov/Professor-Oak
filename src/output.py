def output(info_list, original_input, extra_info, pokemon, more_info):
    if not original_input:
        return "What does this have to do with Pokemon"

    if pokemon:
        return "Thats everything I found:\n" + ",\n".join(info_list) + "."

    if extra_info[4]:
        if extra_info[1]:
            return f"There is/are {len(info_list)} {extra_info[5]} type pokemon"
        elif extra_info[2]:
            return f"These are the top {extra_info[5]} Pokemon: {', '.join(info_list)}"
        elif extra_info[3]:
            return (
                f"These are the worst {extra_info[5]} Pokemon: {', '.join(info_list)}"
            )
        else:
            return f"{', '.join(info_list)} is/are {extra_info[5]} type pokemon"

    if extra_info[0]:
        return f"A {original_input[-1]}'s type is/are {', '.join(info_list)}"

    if extra_info[1] and extra_info[8]:
        return f"there are {info_list[0]-1}"

    if not pokemon:
        if len(info_list) == 0:
            return ""
        result = (
            " ".join(str(more_info[2][i]) for i in range(2, len(more_info[2])))
            + f" {more_info[2][1]} "
        )
        result += ", ".join(info_list) + "."
        return result

    return "Sorry kid could you ask me in a different way"
