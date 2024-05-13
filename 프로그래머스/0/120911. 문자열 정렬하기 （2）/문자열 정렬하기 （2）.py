def solution(my_string):
    my_string = sorted(my_string.lower())
            
    return ''.join(i for i in my_string)