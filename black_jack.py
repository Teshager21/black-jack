
def create_card(size,type):
    return f'''
           ___
          |{size}  |
          | {type} |
          |__{size}|
          '''
def blackJack():
    HEARTS   = chr(9829) # Character 9829 is '♥'.
    DIAMONDS = chr(9830) # Character 9830 is '♦'.
    SPADES   = chr(9824) # Character 9824 is '♠'.
    CLUBS    = chr(9827) # Character 9827 is '♣'.
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
        The dealer stops hitting at 17.    
          ''')
    print(create_card('K',SPADES))
    print(create_card(1,HEARTS))
    
blackJack()