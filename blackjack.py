# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:01:14 2019

@author: evl005
"""

import random
RANK, SUIT = 0,1
def get_point(hand):
    result = 0
    ace_flag = False
    for card in hand:
        num = card[RANK]
        if num == 1:
            ace_flag = True
        if num > 10:
            num = 10
        
        result = result + num
    if ace_flag and result <= 11:
        result += 10
    return result
def print_player_hand(player_hand):
    print('プレイヤー(', get_point(player_hand), '):  ')
    for card in player_hand:
        print('[', card[SUIT], card[RANK], ']')
    print
    
def print_dealer_hand(dealer_hand, uncovered):
    if uncovered:
        print('ディーラー（', get_point(dealer_hand), '):   ')
    else:
        print('ディーラー（??）:   ')
    flag = True
    for card in dealer_hand:
        if flag or uncovered:
            print('[', card[SUIT], card[RANK], ']')
            flag = False
        else:
            print('[ * * ]')
            
    print()
    
def make_deck():
    suits = ['S','H','D','C']
    ranks = range(1,14)
    deck = [(x,y) for x in ranks for y in suits]
    random.shuffle(deck)
    return deck

def main():
    turn = 1
    player_money = 100
    #deck = make_deck()
    #print(deck)
    while(player_money > 0):
        print('ターン：', turn)
        print('所もち金：', player_money)
        player_hand = []
        dealer_hand = []
        deck = make_deck()
        bet = 10
        player_money -= bet
        for i in range(2):
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())
        #print(player_hand)
        print_player_hand(player_hand)
        #print(get_point(player_hand))
        #print(dealer_hand)
        print_dealer_hand(dealer_hand, False)
        #print(get_point(dealer_hand))
        while True:
            op = input('スタンド:1,ヒット：2,ダブル:3　>　')
            if op == '1':
                print('[プレイヤー:スタンド]')
                break;
            elif op == '2':
                print('[プレイヤー:ヒット]')
                player_hand.append(deck.pop())
                print_player_hand(player_hand)
            elif op == '3':
                print('[プレイヤー:ダブル]')
                if len(player_hand) == 2:
                    print('[プレイヤー：ダブル]')
                    player_money -= bet
                    bet += bet
                    player_hand.append(deck.pop())
                    print_player_hand(player_hand)
                    break
                else:
                    print('(ダブルはできません。　)')
            else:
                continue
            if get_point(player_hand) > 21:
                print('[ プレイヤーはバスとした！ ]')
                break
            
        turn += 1
        input('次のターンへ')
    print('ゲームオーバー')

if __name__ == '__main__':
    main()    
    