import random
suits=('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()

deck=Deck()
deck.shuffle()

class Hand:
    def __init__(self,ranger):
        self.ranger=ranger
        self.hand=[]
        self.aces=0
        for x in range(2):
            self.hand.append(deck.deal_one())
    def append_card(self):
        self.hand.append(deck.deal_one())
    def summ(self):
        summ=0
        for x in self.hand:
            summ=summ+x.value
        for x in self.hand:
            if x.rank=='Ace':
                self.aces+=1
        while summ>21 and self.aces:
            summ-=10
            self.aces-=1
        return summ
    def change_ranger(self):
        self.ranger=0
    def __str__(self):
        list_of_cards=[]
        for x in self.hand:
            list_of_cards.append(x.rank + ' of ' + x.suit)
        return str(list_of_cards[self.ranger:])

class Chip:
    def __init__(self, amount=100, bet=0):
        self.amount=amount
        self.bet=bet
    def win_chip(self,winner):
        if winner=='PLAYER':
            self.amount=self.amount+self.bet
        if winner=='DEALER':
            self.amount=self.amount-self.bet
        if winner=='TIE':
            pass
        return self.amount
        

def win(player_sum,dealer_sum):
    if player_sum>21:
        print('Dealer has won!')
        return 'DEALER'
    elif dealer_sum>21:
        print('Player has won!')
        return 'PLAYER'
    elif player_sum>dealer_sum:
        print('Player has won!')
        return 'PLAYER'
    elif player_sum<dealer_sum:
        print('Dealer has won!')
        return 'DEALER'
    else:
        print("It'a a tie")
        return 'TIE'
     
amount='a'
while amount.isdigit()==False:
    amount=input('How much money do you have? ')
amount=int(amount)

def betting(amount):
    bet='b'
    while bet.isdigit()==False or int(bet)>amount:
        bet=input('How much do you wanna bet? ')
    bet=int(bet)
    return bet
 

game_on=True

while game_on:
    player=Hand(0)
    dealer=Hand(1)
    winner=0
    bet=betting(amount)
    chip=Chip(amount,bet)
    print('Cards on the table are: ')
    print(f'Player: {player}')
    print(f'Dealer: {dealer}')
    draw=True
    while draw==True:
        answer='a'
        while answer!='Y' and answer!='N': 
            answer=input('Do you wanna take another card? (Y/N) ')
        if answer=='Y':
            player.append_card()
            print(f"Player's cards are {player}")
            if player.summ()>21:
                print('Player has lost')
                winner='DEALER'
                break
            elif player.summ()==21:
                print('Player has won')
                winner='PLAYER'
                break
            else:
                pass
        elif answer=='N':
            draw=False
            break
    
    dealer.change_ranger()
    print(f"Dealer's cards are {dealer}")   
    if winner==0:
        while dealer.summ()<=17:
            dealer.append_card()
            print(f"Dealer's cards are {dealer}")

        winner=win(player.summ(),dealer.summ())
        
    amount=chip.win_chip(winner)
    print(f'Player has left {amount} dollars')

    answer2='f'
    while answer2!='Y' and answer2!='N': 
        answer=input('Do you wanna play another round? (Y/N) ')
        if answer=='Y':
            break
        if answer=='N':
            game_on=False
            break
    
