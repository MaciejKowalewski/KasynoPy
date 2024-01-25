import random
import time
import math
import os


class Game:
    def __init__(self, n=4, empty_char=" ", coins=None, percentage_of_win=10):
        if coins is None:
            coins = [1, 2, 5]
        self.randomArray = []
        self.n = int(n)
        self.ec = empty_char
        self.coins = coins
        self.pow = float(percentage_of_win)

    def calculate_prize(self):
        return math.pow(10, self.n - 3) * self.pow

    def insert_coin(self):
        coin = input(f"Wrzuć monetę ({str([coin for coin in self.coins])[1:-1]}): ")
        if coin.isnumeric():
            coin = int(coin)
            if coin in self.coins:
                return coin
            else:
                print("Nieprawidłowy nominał!")
                return 0
        else:
            print("To nie jest moneta!")
            return 0

    def fill_randomArray(self):
        self.randomArray = [self.ec for _ in range(0, self.n)]

    def do_u_want_to_play_again(self):
        answer = input("Chcesz jeszcze zagrać? (t/n): \n")
        if answer == 't':
            self.fill_randomArray()
            return False
        else:
            return True

    def is_win(self):
        check_num = self.randomArray[0]
        for num in range(1, self.n):
            if check_num != self.randomArray[num]:
                return False
        return True

    def show_randomArray(self):
        arrStr = ''
        for num in range(0, self.n):
            arrStr += str(self.randomArray[num]) + ','
        print(f'[{arrStr[:-1]}]')

    def drawing_numbers(self):
        time.sleep(0)
        for num in range(0, self.n):
            self.randomArray[num] = random.randint(0, 9)
            self.show_randomArray()
            time.sleep(0)
        return self.randomArray

    def lets_play(self):
        self.fill_randomArray()
        income = 0
        num_of_wins = 0
        while 1:
            os.system('cls')
            print(f"Do wygrania {self.calculate_prize()}zł!!!")
            coins = self.insert_coin()
            income += coins
            for i in range(0, coins):
                print(f"Gra numer {i + 1} z {coins}")
                self.show_randomArray()
                self.drawing_numbers()
                if self.is_win():
                    num_of_wins += 1
                    print(f"Wygrałeś {self.calculate_prize()}zł!!! \n")
                else:
                    print("Przegrałeś! \n")
                self.fill_randomArray()
            if self.do_u_want_to_play_again():
                break
        profit = income - num_of_wins * self.calculate_prize()
        Expected_profit = income - (income * self.pow) / 100
        print(f"Zarobek kasyna {profit}zł. Liczba wygranych to {num_of_wins}. Oczekiwana wartość zarobku wynosi {Expected_profit}zł.")
        return self.randomArray


gra = Game()
gra.lets_play()
