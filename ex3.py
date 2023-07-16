# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

total_cash = 0
count = 0

def print_balance():
    print(f'На балансе {total_cash} рублей')

def percents_for_third():
    global total_cash
    global count
    if count == 3:
        total_cash += total_cash * 0.03
        count = 0
    else:
        count += 1

def replenish(money):
    global total_cash
    if money % 50 == 0:
        total_cash += money
        percents_for_third()
        print_balance()

def withdraw(money):
    global total_cash
    if money % 50 == 0:
        percent = money * 0.015
        if percent < 30:
            percent = 30
        if percent > 600:
            percent = 600
        if total_cash < (money + percent):
            print("недостаточно средств")
        else:
            total_cash -= (money + percent)
            percents_for_third()
            print_balance()

def out():
    quit()

while True:
    input_menu = input('Введите номер операции: \n 1.Внести деньги\n 2.Снять деньги\n 3.Выйти\n')
    if input_menu == '1':
        money = int(input('Введите сумму для внесения: '))
        replenish(money)
    elif input_menu == '2':
        money = int(input('Введите сумму для снятия: '))
        withdraw(money)
    else:
        out()