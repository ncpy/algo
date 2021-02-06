import random

money_in_machine = 100
user_credit = 50
play_credit = 10
no_of_free_play = 0
constant = 1
symbols = ["black", "white", "green", "yellow"]
no_of_slots = 4

def play(user_credit, money_in_machine, no_of_free_play):
    slots = []
    for i in range(no_of_slots):
        slots.append(random.choice(symbols))
    print(slots)


    if slots[0] == slots[1] == slots[2] == slots[3]:        # all is equal
         user_credit = user_credit + money_in_machine
         money_in_machine = 0
         return user_credit, money_in_machine

    def check_difference():
        for i in range(no_of_slots):
            for j in range(i+1, no_of_slots):
                if slots[i] == slots[j]:    # except (all diff and all same)
                    return False
        return True

    if check_difference() == True:    #if all is diff. which means check_difference() func. return TRUE
        user_credit = user_credit + money_in_machine/2
        money_in_machine = money_in_machine/2
        return user_credit, money_in_machine
    elif check_difference() == False:
        if money_in_machine >= 5*play_credit:
            user_credit = user_credit + 5*play_credit
            money_in_machine = money_in_machine - 5*play_credit
        else:
            no_of_free_play = no_of_free_play + int((5*play_credit - money_in_machine)/play_credit)
            user_credit = user_credit + money_in_machine
            money_in_machine = 0
            
            pass

        return user_credit, money_in_machine
            

    return user_credit, money_in_machine

#while True:
for i in range(20):
    if no_of_free_play > 0:
        constant = 0
        no_of_free_play -= 1
    else:
        constant = 1

    if user_credit >= play_credit*constant:
        print("\nbefore playing: ",user_credit, money_in_machine)

        user_credit = user_credit - play_credit
        money_in_machine = money_in_machine + play_credit
        print("playing..: ",user_credit, money_in_machine)

        user_credit, money_in_machine = play(user_credit, money_in_machine, no_of_free_play)
        print("after playing: ",user_credit, money_in_machine)
    else:
        print("User dont have enough money to play")
        break



# def check_all_unique(li):
#     for i in range(0,len(li)):
#         for j in range(i+1, len(li)):
#             if li[i] == li[j]: return False
#     return True 

# print(check_all_unique(["a", "r", "b", "b"]))
