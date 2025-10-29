
def proverb(*input_data ,  qualifier=None):
    result = []
    if not input_data:
        return result
    qualifier =  f"{qualifier} "  if qualifier else ""
    first_word, *rest = input_data
    if rest:
      
        for current_word, next_word in zip(input_data, input_data[1:]):
            result.append(f"For want of a {current_word} the {next_word} was lost.")

    result.append(f"And all for the want of a {qualifier}{first_word}.")
    return result
