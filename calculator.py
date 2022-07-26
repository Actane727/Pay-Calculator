#!/bin/python3

def hourly():
    global h_wage
    h_wage = input('How much do you make an hour? ')
    ot_question = input('Do you work overtime? [Y]es or [N]o ').lower()
    if str(ot_question) == 'y':
        global ot
        ot = input('How much overtime do you work a week? ')
        dt_question = input('Do you work any double time days? [Y]es or [N]o ').lower()
        if str(dt_question) == 'y':
            global dt
            dt = input('How much doubletime do you work a week? ')
        elif str(dt_question) == 'n':
            dt = 0
        else:
            print('That is not a [Y]es or [N]o')
    elif str(ot_question) == 'n':
        h_hours = input('How many hours do you work each week? ')
        if float(h_hours) <= 40:
            ot = 0
            dt = 0
        elif float(h_hours) > 40:
             ot = float(h_hours) - 40
             h_hours = 40
             dt = 0  
    else: print('That is not a [Y]es or [N]o')

def salary():
    global s_year
    s_year = input('How much do you make per year? [Do not use commas] ')
    global s_days
    s_days = input('How many days do you work a week? ')
    global s_even
    s_even = input('Do you work the same amount of hours every day? [Y]es or [N]o ').lower()
    if s_even == 'y':
        global s_hours
        s_hours = input('How many hours a day do you work? ')
    elif s_even == 'n':
        global s_week
        s_week = input('How many hours a week do you work? ')
    s_vaca = input('Do you get vacation time? ').lower()
    if s_vaca == 'y':
        global s_vweeks
        s_vweeks = input('How many weeks of vacation do you get? ')
    else:
        print("That's too bad. You need to negotiate better!")
        s_vweeks = '0'
        
def math_s():
    if s_even == 'y':
        global week_hours
        week_hours = float(s_days) * float(s_hours)
    elif s_even == 'n':
        week_hours = s_week
    work_weeks = 52 - float(s_vweeks)
    week_pay = format(round(float(s_year) / work_weeks, 2), '.2f')
    month_pay = format(round(4 * float(week_pay), 2), '.2f')
    hour_pay = format(round(float(week_pay) / float(week_hours), 2), '.2f')
    print('\nYou make $' + month_pay + ' per month.')
    print('You make $' + week_pay + ' per week.')
    print('You make $' + hour_pay + ' per hour, without overtime.\n')
    
def hb_math():
    if float(week_hours) > 40:
        ot_hours = float(week_hours) - 40
        hb_hour = format(round((float(s_year) /52) / ((ot_hours * 1.5) + 40), 2), '.2f')
        print('\nYou only make $' + hb_hour + ' per hour when you figure overtime!\n')
    else: print('You are lucky and do not work overtime!')

def heartbreak():
    hb = input('Do you want some heartbreak? [Y]es or [N]o ').lower()
    if str(hb) == 'y':
        hb_math()
    elif str(hb) == 'n':
        print("Good thing, because its very sad. :'(\n")

def math_h():
    reg_total = round((float(h_wage) * 40), 2)
    ot_total = format(round(float(h_wage) * 1.5 * float(ot), 2), '.2f')
    dt_total = format(round(float(h_wage) * 2.0 * float(dt), 2), '.2f')
    week_wage = format(round(float(reg_total) + float(ot_total) + float(dt_total), 2), '.2f')
    month_wage = format(round(4 * float(week_wage), 2), '.2f')
    year_wage = format(round(52 * float(week_wage), 2), '.2f')
    print("\nYou make $" + week_wage + " per week.")
    print('You make $' + month_wage + ' per month')
    print('You make $' + year_wage + ' per year\n')
    print('You make $' + ot_total + ' in overtime per week!')
    print('You make $' + dt_total + ' in doubletime per week!\n')

def main():
    print('****Welcome to My Pay Calculator!****\nI will help you find out how much you get paid.\nI even show you how much you might be missing out on!\n')
    type = input('Are you [H]ourly or [S]alary? ').lower()
    if str(type) == "s":
        salary()
        math_s()
        heartbreak()
    elif str(type) == "h":
        hourly()
        math_h()
    else: print("Please type 'h' for hourly or 's' for salary.")
       

while True:
    main() 