import random

def generator(input_str, sep=" ", option=None):
    """
    Splits the text according to sep value and yield the substrings.
    option indications if a cation is perfoemed to the substrings before it is yielded.
    """
    try:
        assert (isinstance(input_str, str))
    except AssertionError:
        print("ERROR")
        return
    word_lst = [""]
    i = 0
    for char in input_str:
        if char == sep:
            i = i + 1
            word_lst.append("")
            continue
        word_lst[i] = word_lst[i] + char
    i = 0
    while (option == "unique" and i < len(list(dict.fromkeys(word_lst)))):
        yield (list(dict.fromkeys(word_lst))[i])
        i = i + 1
    i = 0
    if (option == "shuffle" and i < len(word_lst)):
        for n in range(random.randint(5, 99)):
            newlist1 = word_lst[:int(len(word_lst)/2)]
            newlist2 = word_lst[int(len(word_lst)/2):]
            word_lst = [item for sublist in zip(newlist1, newlist2) for item in sublist]
    while (option == "shuffle" and i < len(word_lst)):
        yield (word_lst[i])
        i = i + 1
    i = 0
    while (option == "ordered" and i < len(word_lst)):
        yield (sorted(word_lst)[i])
        i = i + 1
    
test_string = "This is a dank and dope string. a string. yo hi"
for item in generator(test_string, option="shuffle"):
    print(item)