def solution(my_string):
    my_string = ((((my_string.replace("a", "")).replace("i", "")).replace('u', "")).replace('e', "")).replace('o', "")
    return my_string