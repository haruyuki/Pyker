# encoding: utf-8
# Poker Game
# ------------------------------ IMPORTS ------------------------------
import random
import time
# from myfile import *
# ------------------------------ DEFINITIONS ------------------------------


def space_check(num):  # Code to reverse printing 10 on top and bottom of card
    if num == '10':
        return ''
    else:
        return ' '

# ------------------------------ VARIABLES ------------------------------
cards = ['A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦',
         '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦',
         'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣',
         '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣',
         'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥',
         '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥',
         'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠',
         '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠']

invalid = []  # Cards that have already been drawn
hand = []  # Cards in user's hand
ai_hand = []  # Cards in AI's hand
dealt = 0  # Amount of times dealt

# Top card outline
c1_top = c2_top = c3_top = c4_top = c5_top = '┌─────────┐'

# Middle card outline
c1_middle = c2_middle = c3_middle = c4_middle = c5_middle = '│'

# Bottom card outline
c1_bottom = c2_bottom = c3_bottom = c4_bottom = c5_bottom = '└─────────┘'

# First card suit sections
c1_sect1 = c1_sect2 = c1_sect3 = c1_sect4 = c1_sect5 = c1_sect6 = c1_sect7 = c1_sect8 = c1_sect9 = c1_sect10 = c1_sect11 = c1_sect12 = c1_sect13 = c1_sect14 = c1_sect15 = ' '

# Second card suit sections
c2_sect1 = c2_sect2 = c2_sect3 = c2_sect4 = c2_sect5 = c2_sect6 = c2_sect7 = c2_sect8 = c2_sect9 = c2_sect10 = c2_sect11 = c2_sect12 = c2_sect13 = c2_sect14 = c2_sect15 = ' '

# Third card suit sections
c3_sect1 = c3_sect2 = c3_sect3 = c3_sect4 = c3_sect5 = c3_sect6 = c3_sect7 = c3_sect8 = c3_sect9 = c3_sect10 = c3_sect11 = c3_sect12 = c3_sect13 = c3_sect14 = c3_sect15 = ' '

# Fourth card suit sections
c4_sect1 = c4_sect2 = c4_sect3 = c4_sect4 = c4_sect5 = c4_sect6 = c4_sect7 = c4_sect8 = c4_sect9 = c4_sect10 = c4_sect11 = c4_sect12 = c4_sect13 = c4_sect14 = c4_sect15 = ' '

# Fifth card suit sections
c5_sect1 = c5_sect2 = c5_sect3 = c5_sect4 = c5_sect5 = c5_sect6 = c5_sect7 = c5_sect8 = c5_sect9 = c5_sect10 = c5_sect11 = c5_sect12 = c5_sect13 = c5_sect14 = c5_sect15 = ' '

# ------------------------------ CODE ------------------------------
print('Welcome to Poker!')
print('Choose AI difficulty:')
print('1) Easy')
print('2) Medium')
print('3) Hard')
while True:  # While user hasn't chosen a difficulty
    user_ai = input('> ')
    try:
        user_ai = int(user_ai)
        break
    except ValueError:  # If input isn't a number
        print('Choose the AI difficulty number.')
if user_ai == 1:
    ai_difficulty = 1
    print('You have selected Easy.')
elif user_ai == 2:
    ai_difficulty = 2
    print('You have selected Medium.')
elif user_ai == 3:
    ai_difficulty = 3
    print('You have selected Hard.')
# time.sleep(1.5)

while dealt < 5:  # While 5 cards haven't been dealt to the user and AI
    card_gen = random.randint(0, 51)  # Generate a random card for the user
    ai_card_gen = random.randint(0, 51)  # Generate a random card for the AI
    while True:
        if card_gen in invalid:
            card_gen = random.randint(0, 51)
        elif ai_card_gen in invalid:  # If generated card has already been drawn
            ai_card_gen = random.randint(0, 51)
        elif card_gen == ai_card_gen:  # If user and AI draw the same card
            card_gen = random.randint(0, 51)
            ai_card_gen = random.randint(0, 51)
        else:
            break
    invalid.append(card_gen)  # Add user drawn card to invalid list
    invalid.append(ai_card_gen)  # Add AI drwan card to invalid list
    hand.append(cards[card_gen])  # Add drawn card to user's hand
    ai_hand.append(cards[ai_card_gen])  # Add drawn card to AI's hand
    dealt += 1
hand.sort()  # Organise the user's cards

# Assigning card value and suit from user's cards
c1_num = hand[0][0]
c1_suit = hand[0][1]
c2_num = hand[1][0]
c2_suit = hand[1][1]
c3_num = hand[2][0]
c3_suit = hand[2][1]
c4_num = hand[3][0]
c4_suit = hand[3][1]
c5_num = hand[4][0]
c5_suit = hand[4][1]

# Setting T card value to 10
if c1_num == 'T':
    c1_num = '10'
if c2_num == 'T':
    c2_num = '10'
if c3_num == 'T':
    c3_num = '10'
if c4_num == 'T':
    c4_num = '10'
if c5_num == 'T':
    c5_num = '10'

# Setting card color to red if suit is diamonds or hearts
if c1_suit == '♦' or c1_suit == '♥':  # If first card is diamonds or hearts
    c1_suit = '\033[0;31m' + c1_suit + '\033[0;0m'
    c1_top = '\033[0;31m' + c1_top + '\033[0;0m'
    c1_middle = '\033[0;31m' + c1_middle + '\033[0;0m'
    c1_bottom = '\033[0;31m' + c1_bottom + '\033[0;0m'
if c2_suit == '♦' or c2_suit == '♥':  # If second card is diamonds or hearts
    c2_suit = '\033[0;31m' + c2_suit + '\033[0;0m'
    c2_top = '\033[0;31m' + c1_top + '\033[0;0m'
    c2_middle = '\033[0;31m' + c1_middle + '\033[0;0m'
    c2_bottom = '\033[0;31m' + c1_bottom + '\033[0;0m'
if c3_suit == '♦' or c3_suit == '♥':  # If third card is diamonds or hearts
    c3_suit = '\033[0;31m' + c3_suit + '\033[0;0m'
    c3_top = '\033[0;31m' + c1_top + '\033[0;0m'
    c3_middle = '\033[0;31m' + c1_middle + '\033[0;0m'
    c3_bottom = '\033[0;31m' + c1_bottom + '\033[0;0m'
if c4_suit == '♦' or c4_suit == '♥':  # If fourth card is diamonds or hearts
    c4_suit = '\033[0;31m' + c4_suit + '\033[0;0m'
    c4_top = '\033[0;31m' + c1_top + '\033[0;0m'
    c4_middle = '\033[0;31m' + c1_middle + '\033[0;0m'
    c4_bottom = '\033[0;31m' + c1_bottom + '\033[0;0m'
if c5_suit == '♦' or c5_suit == '♥':  # If fifth card is diamonds or hearts
    c5_suit = '\033[0;31m' + c5_suit + '\033[0;0m'
    c5_top = '\033[0;31m' + c1_top + '\033[0;0m'
    c5_middle = '\033[0;31m' + c1_middle + '\033[0;0m'
    c5_bottom = '\033[0;31m' + c1_bottom + '\033[0;0m'

# Setting card suit sections
# First card
if c1_num == 'A':  # If card value is Ace
    c1_sect8 = c1_suit
elif c1_num == '2':  # If card value is 2
    c1_sect2 = c1_sect14 = c1_suit
elif c1_num == '3':  # If card value is 3
    c1_sect2 = c1_sect8 = c1_sect14 = c1_suit
elif c1_num == '4':  # If card value is 4
    c1_sect1 = c1_sect3 = c1_sect13 = c1_sect15 = c1_suit
elif c1_num == '5':  # If card value is 5
    c1_sect1 = c1_sect3 = c1_sect8 = c1_sect13 = c1_sect15 = c1_suit
elif c1_num == '6':  # If card value is 6
    c1_sect1 = c1_sect3 = c1_sect7 = c1_sect9 = c1_sect13 = c1_sect15 = c1_suit
elif c1_num == '7':  # If card value is 7
    c1_sect1 = c1_sect3 = c1_sect5 = c1_sect7 = c1_sect9 = c1_sect13 = c1_sect15 = c1_suit
elif c1_num == '8':  # If card value is 8
    c1_sect1 = c1_sect3 = c1_sect5 = c1_sect7 = c1_sect9 = c1_sect11 = c1_sect13 = c1_sect15 = c1_suit
elif c1_num == '9':  # If card value is 9
    c1_sect1 = c1_sect2 = c1_sect3 = c1_sect7 = c1_sect8 = c1_sect9 = c1_sect13 = c1_sect14 = c1_sect15 = c1_suit
elif c1_num == '10':  # If card value is 10
    c1_sect1 = c1_sect3 = c1_sect4 = c1_sect6 = c1_sect7 = c1_sect9 = c1_sect10 = c1_sect12 = c1_sect13 = c1_sect15 = c1_suit
elif c1_num == 'J':  # If card value is Jack
    c1_sect8 = c1_suit
elif c1_num == 'Q':  # If card value is Queen
    c1_sect8 = c1_suit
elif c1_num == 'K':  # If card value is King
    c1_sect8 = c1_suit

# Second card
if c2_num == 'A':  # If card value is Ace
    c2_sect8 = c2_suit
elif c2_num == '2':  # If card value is 2
    c2_sect2 = c2_sect14 = c2_suit
elif c2_num == '3':  # If card value is 3
    c2_sect2 = c2_sect8 = c2_sect14 = c2_suit
elif c2_num == '4':  # If card value is 4
    c2_sect1 = c2_sect3 = c2_sect13 = c2_sect15 = c2_suit
elif c2_num == '5':  # If card value is 5
    c2_sect1 = c2_sect3 = c2_sect8 = c2_sect13 = c2_sect15 = c2_suit
elif c2_num == '6':  # If card value is 6
    c2_sect1 = c2_sect3 = c2_sect7 = c2_sect9 = c2_sect13 = c2_sect15 = c2_suit
elif c2_num == '7':  # If card value is 7
    c2_sect1 = c2_sect3 = c2_sect5 = c2_sect7 = c2_sect9 = c2_sect13 = c2_sect15 = c2_suit
elif c2_num == '8':  # If card value is 8
    c2_sect1 = c2_sect3 = c2_sect5 = c2_sect7 = c2_sect9 = c2_sect11 = c2_sect13 = c2_sect15 = c2_suit
elif c2_num == '9':  # If card value is 9
    c2_sect1 = c2_sect2 = c2_sect3 = c2_sect7 = c2_sect8 = c2_sect9 = c2_sect13 = c2_sect14 = c2_sect15 = c2_suit
elif c2_num == '10':  # If card value is 10
    c2_sect1 = c2_sect3 = c2_sect4 = c2_sect6 = c2_sect7 = c2_sect9 = c2_sect10 = c2_sect12 = c2_sect13 = c2_sect15 = c2_suit
elif c2_num == 'J':  # If card value is Jack
    c2_sect8 = c2_suit
elif c2_num == 'Q':  # If card value is Queen
    c2_sect8 = c2_suit
elif c2_num == 'K':  # If card value is King
    c2_sect8 = c2_suit

# Third card
if c3_num == 'A':  # If card value is Ace
    c3_sect8 = c3_suit
elif c3_num == '2':  # If card value is 2
    c3_sect2 = c3_sect14 = c3_suit
elif c3_num == '3':  # If card value is 3
    c3_sect2 = c3_sect8 = c3_sect14 = c3_suit
elif c3_num == '4':  # If card value is 4
    c3_sect1 = c3_sect3 = c3_sect13 = c3_sect15 = c3_suit
elif c3_num == '5':  # If card value is 5
    c3_sect1 = c3_sect3 = c3_sect8 = c3_sect13 = c3_sect15 = c3_suit
elif c3_num == '6':  # If card value is 6
    c3_sect1 = c3_sect3 = c3_sect7 = c3_sect9 = c3_sect13 = c3_sect15 = c3_suit
elif c3_num == '7':  # If card value is 7
    c3_sect1 = c3_sect3 = c3_sect5 = c3_sect7 = c3_sect9 = c3_sect13 = c3_sect15 = c3_suit
elif c3_num == '8':  # If card value is 8
    c3_sect1 = c3_sect3 = c3_sect5 = c3_sect7 = c3_sect9 = c3_sect11 = c3_sect13 = c3_sect15 = c3_suit
elif c3_num == '9':  # If card value is 9
    c3_sect1 = c3_sect2 = c3_sect3 = c3_sect7 = c3_sect8 = c3_sect9 = c3_sect13 = c3_sect14 = c3_sect15 = c3_suit
elif c3_num == '10':  # If card value is 10
    c3_sect1 = c3_sect3 = c3_sect4 = c3_sect6 = c3_sect7 = c3_sect9 = c3_sect10 = c3_sect12 = c3_sect13 = c3_sect15 = c3_suit
elif c3_num == 'J':  # If card value is Jack
    c3_sect8 = c3_suit
elif c3_num == 'Q':  # If card value is Queen
    c3_sect8 = c3_suit
elif c3_num == 'K':  # If card value is King
    c3_sect8 = c3_suit

# Fourth card
if c4_num == 'A':  # If card value is Ace
    c4_sect8 = c4_suit
elif c4_num == '2':  # If card value is 2
    c4_sect2 = c4_sect14 = c4_suit
elif c4_num == '3':  # If card value is 3
    c4_sect2 = c4_sect8 = c4_sect14 = c4_suit
elif c4_num == '4':  # If card value is 4
    c4_sect1 = c4_sect3 = c4_sect13 = c4_sect15 = c4_suit
elif c4_num == '5':  # If card value is 5
    c4_sect1 = c4_sect3 = c4_sect8 = c4_sect13 = c4_sect15 = c4_suit
elif c4_num == '6':  # If card value is 6
    c4_sect1 = c4_sect3 = c4_sect7 = c4_sect9 = c4_sect13 = c4_sect15 = c4_suit
elif c4_num == '7':  # If card value is 7
    c4_sect1 = c4_sect3 = c4_sect5 = c4_sect7 = c4_sect9 = c4_sect13 = c4_sect15 = c4_suit
elif c4_num == '8':  # If card value is 8
    c4_sect1 = c4_sect3 = c4_sect5 = c4_sect7 = c4_sect9 = c4_sect11 = c4_sect13 = c4_sect15 = c4_suit
elif c4_num == '9':  # If card value is 9
    c4_sect1 = c4_sect2 = c4_sect3 = c4_sect7 = c4_sect8 = c4_sect9 = c4_sect13 = c4_sect14 = c4_sect15 = c4_suit
elif c4_num == '10':  # If card value is 10
    c4_sect1 = c4_sect3 = c4_sect4 = c4_sect6 = c4_sect7 = c4_sect9 = c4_sect10 = c4_sect12 = c4_sect13 = c4_sect15 = c4_suit
elif c4_num == 'J':  # If card value is Jack
    c4_sect8 = c4_suit
elif c4_num == 'Q':  # If card value is Queen
    c4_sect8 = c4_suit
elif c4_num == 'K':  # If card value is King
    c4_sect8 = c4_suit

# Fifth card
if c5_num == 'A':  # If card value is Ace
    c5_sect8 = c5_suit
elif c5_num == '2':  # If card value is 2
    c5_sect2 = c5_sect14 = c5_suit
elif c5_num == '3':  # If card value is 3
    c5_sect2 = c5_sect8 = c5_sect14 = c5_suit
elif c5_num == '4':  # If card value is 4
    c5_sect1 = c5_sect3 = c5_sect13 = c5_sect15 = c5_suit
elif c5_num == '5':  # If card value is 5
    c5_sect1 = c5_sect3 = c5_sect8 = c5_sect13 = c5_sect15 = c5_suit
elif c5_num == '6':  # If card value is 6
    c5_sect1 = c5_sect3 = c5_sect7 = c5_sect9 = c5_sect13 = c5_sect15 = c5_suit
elif c5_num == '7':  # If card value is 7
    c5_sect1 = c5_sect3 = c5_sect5 = c5_sect7 = c5_sect9 = c5_sect13 = c5_sect15 = c5_suit
elif c5_num == '8':  # If card value is 8
    c5_sect1 = c5_sect3 = c5_sect5 = c5_sect7 = c5_sect9 = c5_sect11 = c5_sect13 = c5_sect15 = c5_suit
elif c5_num == '9':  # If card value is 9
    c5_sect1 = c5_sect2 = c5_sect3 = c5_sect7 = c5_sect8 = c5_sect9 = c5_sect13 = c5_sect14 = c5_sect15 = c5_suit
elif c5_num == '10':  # If card value is 10
    c5_sect1 = c5_sect3 = c5_sect4 = c5_sect6 = c5_sect7 = c5_sect9 = c5_sect10 = c5_sect12 = c5_sect13 = c5_sect15 = c5_suit
elif c5_num == 'J':  # If card value is Jack
    c5_sect8 = c5_suit
elif c5_num == 'Q':  # If card value is Queen
    c5_sect8 = c5_suit
elif c5_num == 'K':  # If card value is King
    c5_sect8 = c5_suit

print('Your hand:')

# Card numbers
print('     1            2            3            4            5     ')
print('{}  {}  {}  {}  {}'.format(c1_top, c2_top, c3_top, c4_top, c5_top))  # Top card outline
print('{}{}{}       {}  {}{}{}       {}  {}{}{}       {}  {}{}{}       {}  {}{}{}       {}'.format(c1_middle, c1_num, space_check(c1_num), c1_middle, c2_middle, c2_num, space_check(c2_num), c2_middle, c3_middle, c3_num, space_check(c3_num), c3_middle, c4_middle, c4_num, space_check(c4_num), c4_middle, c5_middle, c5_num, space_check(c5_num), c5_middle))  # Top card numbers
print('{}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}'.format(c1_middle, c1_sect1, c1_sect2, c1_sect3, c1_middle, c2_middle, c2_sect1, c2_sect2, c2_sect3, c2_middle, c3_middle, c3_sect1, c3_sect2, c3_sect3, c3_middle, c4_middle, c4_sect1, c4_sect2, c4_sect3, c4_middle, c5_middle, c5_sect1, c5_sect2, c5_sect3, c5_middle))  # Card suit sections
print('{}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}'.format(c1_middle, c1_sect4, c1_sect5, c1_sect6, c1_middle, c2_middle, c2_sect4, c2_sect5, c2_sect6, c2_middle, c3_middle, c3_sect4, c3_sect5, c3_sect6, c3_middle, c4_middle, c4_sect4, c4_sect5, c4_sect6, c4_middle, c5_middle, c5_sect4, c5_sect5, c5_sect6, c5_middle))  # Card suit sections
print('{}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}'.format(c1_middle, c1_sect7, c1_sect8, c1_sect9, c1_middle, c2_middle, c2_sect7, c2_sect8, c2_sect9, c2_middle, c3_middle, c3_sect7, c3_sect8, c3_sect9, c3_middle, c4_middle, c4_sect7, c4_sect8, c4_sect9, c4_middle, c5_middle, c5_sect7, c5_sect8, c5_sect9, c5_middle))  # Card suit sections
print('{}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}'.format(c1_middle, c1_sect10, c1_sect11, c1_sect12, c1_middle, c2_middle, c2_sect10, c2_sect11, c2_sect12, c2_middle, c3_middle, c3_sect10, c3_sect11, c3_sect12, c3_middle, c4_middle, c4_sect10, c4_sect11, c4_sect12, c4_middle, c5_middle, c5_sect10, c5_sect11, c5_sect12, c5_middle))  # Card suit sections
print('{}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}  {}  {} {} {}  {}'.format(c1_middle, c1_sect13, c1_sect14, c1_sect15, c1_middle, c2_middle, c2_sect13, c2_sect14, c2_sect15, c2_middle, c3_middle, c3_sect13, c3_sect14, c3_sect15, c3_middle, c4_middle, c4_sect13, c4_sect14, c4_sect15, c4_middle, c5_middle, c5_sect13, c5_sect14, c5_sect15, c5_middle))  # Card suit sections
print('{}       {}{}{}  {}       {}{}{}  {}       {}{}{}  {}       {}{}{}  {}       {}{}{}'.format(c1_middle, space_check(c1_num), c1_num, c1_middle, c2_middle, space_check(c2_num), c2_num, c2_middle, c3_middle, space_check(c3_num), c3_num, c3_middle, c4_middle, space_check(c4_num), c4_num, c4_middle, c5_middle, space_check(c5_num), c5_num, c5_middle))  # Bottom card numbers
print('{}  {}  {}  {}  {}'.format(c1_bottom, c2_bottom, c3_bottom, c4_bottom, c5_bottom))  # Bottom card outline
print('Combinations:')
print('a) High Card: Highest value card.')
print('b) One Pair: Two cards of the same value.')
print('c) Two Pairs: Two different pairs.')
print('d) Three of a Kind: Three cards of the same value.')
print('e) Straight: All cards are consecutive values.')
print('f) Flush: All cards of the same suit.')
print('g) Full House: Three of a kind and a pair.')
print('h) Four of a Kind: Four cards of the same value.')
print('i) Straight Flush: All cards are consecutive values of same suit.')
print('j) Royal Flush: Ten, Jack, Queen, King, Ace, in same suit')
print()
print('Select cards and combination you would like to use. E.g \'1,3,4,5,h\'')
trim = ','
selected_cards = 0
card1 = card2 = card3 = card4 = card5 = ''
while True:  # While the correct cards and combination haven't been chosen
    while True:  # While selection can't be converted into an integer
        user_cards = input('> ')
        selection = list(user_cards)
        while trim in selection:
            selection.remove(trim)
        selection_combination = selection[-1:][0]
        selection_cards = selection[:-1]
        try:  # Trying to convert list into integer
            selection_cards = [int(x) for x in selection_cards]
            break
        except ValueError:
            print('One or more of your selection isn\'t a card!')
            user_cards = input('> ')
    for i in range(len(selection_cards)):
        if selection_cards[i] == 1:
            selected_cards += 1
        elif selection_cards[i] == 2:
            selected_cards += 1
        elif selection_cards[i] == 3:
            selected_cards += 1
        elif selection_cards[i] == 4:
            selected_cards += 1
        elif selection_cards[i] == 5:
            selected_cards += 1
    if selected_cards == 1:
        if selection_combination != 'a':
            print('You didn\'t select enough cards to use this combination!')
            selected_cards = 0
        else:
            card1 = hand[selection_cards[0]-1]
            break
    elif selected_cards == 2:
        if selection_combination != 'b':
            print('You didn\'t select enough cards to use this combination!')
            selected_cards = 0
        else:
            card1 = hand[selection_cards[0]-1]
            card2 = hand[selection_cards[1]-1]
            break
    elif selected_cards == 3:
        if selection_combination != 'd':
            print('You didn\'t select enough cards to use this combination!')
            selected_cards = 0
        else:
            card1 = hand[selection_cards[0]-1]
            card2 = hand[selection_cards[1]-1]
            card3 = hand[selection_cards[2]-1]
            break
    elif selected_cards == 4:
        if selection_combination != 'c' or selection_combination != 'h':
            print('You didn\'t select enough cards to use this combination!')
            selected_cards = 0
        else:
            card1 = hand[selection_cards[0]-1]
            card2 = hand[selection_cards[1]-1]
            card3 = hand[selection_cards[2]-1]
            card4 = hand[selection_cards[3]-1]
            break
    elif selected_cards == 5:
        if selection_combination != 'e' or selection_combination != 'f' or selection_combination != 'g' or selection_combination != 'i' or selection_combination != 'j':
            print('You didn\'t select enough cards to use this combination!')
            selected_cards = 0
        else:
            card1 = hand[selection_cards[0]-1]
            card2 = hand[selection_cards[1]-1]
            card3 = hand[selection_cards[2]-1]
            card4 = hand[selection_cards[3]-1]
            card5 = hand[selection_cards[4]-1]
            break
print(card1)
print(card2)
print(card3)
print(card4)
print(card5)
