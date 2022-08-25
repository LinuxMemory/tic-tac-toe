def winner_function(list):
    if list[0] == list[1] and list[1] == list[2]:
        return True
    elif list[3] == list[4] and list[4] == list[5]:
        return True
    elif list[6] == list[7] and list[7] == list[8]:
        return True
    elif list[0] == list[3] and list[3] == list[6]:
        return True
    elif list[1] == list[4] and list[4] == list[7]:
        return True
    elif list[2] == list[5] and list[5] == list[8]:
        return True
    elif list[0] == list[4] and list[4] == list[8]:
        return True
    elif list[2] == list[4] and list[4] == list[6]:
        return True
    else:
        return False



def show_board(list):
    list1 = []
    for j in list:
        list1.append(j)
        if len(list1) == 3:
            print("{} {} {}\n".format(list1[0], list1[1], list1[2]))
        elif len(list1) == 6:
            print("{} {} {}\n".format(list1[3], list1[4], list1[5]))
        elif len(list1) == 9:
            print("{} {} {}\n".format(list1[6], list1[7], list1[8]))
        else:
            continue



def count_x_o(list4):
    list_x = []
    list_o = []
    for j in list4:
        if j == 'X':
            list_x.append(j)
        elif j == 'O':
            list_o.append(j)
    if len(list_x) > len(list_o):
        print("Player 1 won the game")
    else:
        print("Player 2 won the game")



def user_variants(list):
    add = True
    while add:
        player1 = int(input("Player1 enter the value from wihtin  {} \n".format(list)))
        if player1 in list:
            list[player1-1] = "X"
            break
        else:
            add = False
    if winner_function(list) == True:
        count_x_o(list)
        return list
    else:
        while add:
            player2 = int(input("Player2 enter the value wihtin {} \n".format(list)))
            if player2 in list:
                list[player2-1] = "O"
                break
            else:
                add = True
    if winner_function(list) == True:
        count_x_o(list)
    return list
    
    
    
#user_variants(['X', 'O', 3, 'X', 'O', 6, 7, 8, 9])


list3 = []
b = True
while b:
    if len(list3) == 0:
        list3 = user_variants([1, 2, 3, 4, 5, 6, 7, 8, 9])
        show_board(list3)
    else:
        list3 = user_variants(list3)
        show_board(list3)
        if winner_function(list3) == True:
            break