import random
def display_card(player):
    card=row1=row2=row3=row4=''
    # print('here',player)
    for p in player:
        size,type,open=p
        if open==False:
            size=type='#' 
        row1+=f' ___'
        row2+=f'\n|{size}  |'.strip()
        row3+=f'\n| {type} |'.strip()
        row4+=f'\n|__{size}|  '.strip()      
    print(row1+'\n'+row2+'\n'+row3+'\n'+row4)
def generateCard():
    HEARTS   = chr(9829) # Character 9829 is '♥'.
    DIAMONDS = chr(9830) # Character 9830 is '♦'.
    SPADES   = chr(9824) # Character 9824 is '♠'.
    CLUBS    = chr(9827) # Character 9827 is '♣'.
    CARDS=['A',2,3,4,5,6,7,8,9,'J','Q','K']
    TYPE=[ HEARTS,DIAMONDS,SPADES,CLUBS,]
    return [CARDS[ random.randint(0,11)],TYPE[random.randint(0,3)]]
def cardSum(player):
    values=[]
    for i in player:
        if type(i[0])!=str and 2<=i[0]<10:
            values.append(i[0])
        elif i[0].lower()=='a': 
            values.append(1)
        else: values.append(10)

    return sum(values)
def check_game_status(player,name):
    if cardSum(player)==21 : 
        print(f"{name} won!")
        return 'gameover'
    elif cardSum(player)>21:
        print(f"{name} Lost")
        return 'gameover'
    else: return 'gameon'


def blackJack():
    Money=5000
    print('''
      Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.  ''')
    print("You have $5000")
    dealer=[]
    player=[]
    d1=generateCard()
    d1.append(False)
    d2=generateCard()
    d2.append(True)
    p1= generateCard()
    p1.append(True)
    p2=generateCard()
    p2.append(True)
    dealer.extend([d1,d2])
    player.extend([p1,p2])
    bet=int(input(f'How much would you like to bet? 1-{Money}: \n'))
    # print('dealer',dealer)
    print("Dealer: ???")
    display_card(dealer)
    print("Player: ", cardSum(player))
    display_card(player)
    while True:
        move=input('(H)it, (S)tand, (D)ouble down\n').lower()
        if move=='h':
            p=generateCard()
            p.append(True)
            player.append(p)
            dealer[0][2]=True
            if cardSum(dealer)<17: 
                d=generateCard()
                d.append(True)
                dealer.append(d)
                
            print('dealer: ',cardSum(dealer))
            display_card(dealer)
            print("Player: ", cardSum(player))
            display_card(player)
            if check_game_status(dealer,'Dealer')=='gameover':
                    # print('Dealer Lost!')
                    break
            if check_game_status(player,'You')=='gameover':
                break
            else: continue
        elif move=='d':
            bet+=bet
            print("your current bet is: ", bet)
        elif move=='s': continue
        else: print('Please choose the right letter!')
blackJack()