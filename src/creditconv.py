#!/usr/bin/env python3

def credit_to_eur(amount):
    credit_in_eur = amount / 1.867
    return credit_in_eur

def eur_to_credit(amount):
    eur_in_credit = amount * 1.867
    return eur_to_credit

def credit_to_usd(amount):
    credit_in_eur = amount / 1.867
    credit_in_usd = credit_in_eur * 0.92
    return credit_in_usd

def usd_in_credit(amount):
    eur_in_credit = amount * 1.867
    usd_to_credit = eur_to_credit * 0.92
    return usd_in_credit
