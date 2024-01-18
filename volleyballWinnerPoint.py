#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 18:45:38 2022

@author: onursemitosun
"""

name_first= input("Enter The Name of First Team:")
sets_first= int(input("Enter The Sets Won by First Team:"))
name_second= input("Enter The Name of Second Team:")
sets_second= int(input("Enter The Sets Won by Second Team:"))
sets_total= sets_first+sets_second 

if sets_total<5 and sets_first<sets_second:
    winner=name_second
    loser=name_first
    print(f"Winner Team is {winner} The Points Earned: 3 \nLoser Team is {loser} The Points Earned: 0")

if sets_total<5 and sets_first>sets_second:
    winner=name_first
    loser=name_second
    print(f"Winner Team is {winner} The Points Earned: 3 \nLoser Team is {loser} The Points Earned: 0")

if sets_total==5 and sets_first<sets_second:
    winner=name_second
    loser=name_first
    print(f"Winner Team is {winner} The Points Earned: 2 \nLoser Team is {loser} The Points Earned: 1")

if sets_total==5 and sets_first>sets_second:
    winner=name_first
    loser=name_second
    print(f"Winner Team is {winner} The Points Earned: 2 \nLoser Team is {loser} The Points Earned: 1")