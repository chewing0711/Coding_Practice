def solution(keyinput, board):
    x = 0
    y = 0
    
    for i in keyinput :
        if i == "left" :
            x -= 1
        elif i == "right" :
            x += 1
        elif i == "up" :
            y += 1
        else :
            y -= 1
            
            
        if x >= board[0] // 2 :
            x = board[0] // 2
        elif x <= -(board[0] // 2) :
            x = -(board[0] // 2)
            
        if y >= board[1] // 2 :
            y = board[1] // 2
        elif y <= -(board[1] // 2) :
            y = -(board[1] // 2)
            
        print(f"{i}, {x}, {y}")
            
    return x, y