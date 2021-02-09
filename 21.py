import random

deck=["Ah","2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","As","2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","Ad","2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ac","2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc"]
deckValue={"Ah":11,"2h":2,"3h":3,"4h":4,"5h":5,"6h":6,"7h":7,"8h":8,"9h":9,"10h":10,"Jh":10,"Qh":10,"Kh":10,"As":11,"2s":2,"3s":3,"4s":4,"5s":5,"6s":6,"7s":7,"8s":8,"9s":9,"10s":10,"Js":10,"Qs":10,"Ks":10,"Ad":11,"2d":2,"3d":3,"4d":4,"5d":5,"6d":6,"7d":7,"8d":8,"9d":9,"10d":10,"Jd":10,"Qd":10,"Kd":10,"Ac":11,"2c":2,"3c":3,"4c":4,"5c":5,"6c":6,"7c":7,"8c":8,"9c":9,"10c":10,"Jc":10,"Qc":10,"Kc":10}
limit_at_first = 21

#Shuffle the cards...
random.shuffle(deck)

#Player's Hand
print("Players' Hands:")
P1card1 = deck.pop(0)
P1card2 = deck.pop(0)
P2card1 = deck.pop(0)
P2card2 = deck.pop(0)

P1card1Value = deckValue[P1card1]
P1card2Value = deckValue[P1card2]
P1total = P1card1Value+P1card2Value

P2card1Value = deckValue[P2card1]
P2card2Value = deckValue[P2card2]
P2total = P2card1Value+P2card2Value


print("P1 1st Card: " + P1card1 + " - value: " + str(P1card1Value))
print("P1 2nd Card: " + P1card2 + " - value: " + str(P1card2Value))
print("---------------------------" + str(P1total))

print("\nP2 1st Card: " + P2card1 + " - value: " + str(P2card1Value))
print("P2 2nd Card: " + P2card2 + " - value: " + str(P2card2Value))
print("---------------------------" + str(P2total))

if P1total == 21:
    print("P1 won")
elif P2total == 21:
    print("P2 won")
else:       # which means no one go over 21,   
    def P2(P2total):
        def P2_stop(P2total):
            if 21 >= P2total > P1total:
                P1(P1total, P2total)

            elif P2total > 21:
                print("P2 lost, P1 win")
            
        def P2_playing(P2total):
            while P2total < 5:
                P2next = deck.pop(0)
                P2total = P2total + deckValue[P2next]
                print("P2 next Card: " + P2next + " - value: " + str(deckValue[P2next]))
                print("P2 Total", P2total)
                P2_stop(P2total)

        P2_playing(P2total)
        P2_stop(P2total)


    def P1(P1total, P2total):
        def P1_playing(P1total, P2total, limit_at_first):
            while P1total < limit_at_first:         #P1 playing...
                P1next = deck.pop(0)
                P1total += deckValue[P1next]
                print("\nP1 next Card: " + P1next + " - value: " + str(deckValue[P1next]))
                print("P1 Total", P1total)
                P1_stop(P1total, P2total)
                limit_at_first = 17

        def P1_stop(P1total, P2total):
            if 21 >= P1total >= 17:       # P1 stop P2's turn
                P2(P2total)

            elif P1total > 21 :
                print("P1 lost, P2 win")
        
        

        P1_playing(P1total, P2total, limit_at_first)
        P1_stop(P1total, P2total)
    
    P1(P1total, P2total)


# if blakjack == 21 

# if under blackjack
        # Sam start drawing cards
        # if Sam equals or over 17 ---> 
            # stop drawing card, 
            # and Dealer start drawing
            # if dealer has over Sam:
                # stop drawing 
                # if dealer over 21
                    # lost (Sam win)
        # if Sam over 21: 
            # ---> lose (Dealer win)