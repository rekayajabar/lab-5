
## CS Lab 4 Week 5
## Program 
## Name Rekaya
## Email rjznp@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed

from random import randint

def play_again()->bool:
    play = input("Do you want to play again? ==> ").lower()
    options = ["n","y","no","yes"]
    if play not in options:
        print("\nYou must enter Y/YES/N/NO to continue. Please try again")
        return play_again()
    if (play=="yes" or play=="y"):
        return True
     

def get_wager(bank:int)->int:
    chips = int(input("How many chips do you want to wager? ==> "))
    if(chips < 1):
        print("The wager amount must be greater than 0. Please enter again.")
        return get_wager(bank)
    elif (chips>bank):
        print("The wager amount cannot be greater than how much you have.",bank)
        return get_wager(bank)
    return chips


def get_slot_results()->tuple:
    reel1 = randint(0,9)
    reel2 = randint(0,9)
    reel3 = randint(0,9)
    return reel1,reel2,reel3

def get_matches(reela,reelb,reelc)->int:
    if (reela==reelb==reelc):
        return 3
    elif (reela==reelb or reela==reelc or reelb==reelc):
        return 2
    return 0

def get_bank()->int:
    chips = int(input("How many chips do you want to start with? ==> "))
    if (chips<1):
        print("Too low a value, you can only choose 1 - 100 chips")
        return get_bank()
    elif (chips>100):
        print("Too high a value, you can only choose 1 - 100 chips")
        return get_bank()
    return chips

def get_payout(wager,matches):
    if matches==3:
        return wager*10
    elif matches==2:
        return wager*5
    return wager*-1

if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        start_chips = bank
        most = bank
        count = 0

        while True:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            count = count+1
            if most<bank:
                most = bank
            if bank <1:
                break
            
           
        print("You lost all", start_chips, "in", count, "spins")
        print("The most chips you had was", 0)
        playing = play_again()

import lab05 as lab05
import unittest
from unittest.mock import patch
from io import StringIO

class TestLabFunctions(unittest.TestCase):

    def test_play_again_returns_True(self):

        user_input = ["YeS"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.play_again()
                self.assertTrue(results, "When input is yes the function should return True")

    def test_play_again_returns_False_with_N_or_NO(self):

        user_input = ["nO"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.play_again()
                self.assertFalse(results, "When input is No play_again should return False")

    def test_play_again_warns_user_with_bad_input(self):

        user_input = ["incorrect", "nO"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.play_again()
                self.assertFalse(results, "When input is no the play_again should return False")
                l = es
        self.assertIn("try again", l.getvalue().lower(), "Bad input should be followed with an error with at least Please Try again in it.")
        

    def test_play_again_works_with_multiple_bad_inputs(self):

        user_input = ["chiefs", "incorrect", "nO"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.play_again()
                self.assertFalse(results, "play_again should return False when given 2 incorrect inputs and then no")

    def test_get_wager_returns_wager_amount(self):

        user_input = ["30"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.get_wager(200)
                self.assertEqual(30, results, "getWager should return 30 when the user enters 30")


    def test_get_wager_returns_wager_amount_after_negative(self):

        user_input = ["-5", "45"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.get_wager(200)
                self.assertEqual(45, results, "getWager should return 45 when the user enters -5, 30")

    def test_get_wager_returns_wager_amount_after_negative(self):

        user_input = ["-5", "45"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.get_wager(200)
                self.assertEqual(45, results, "getWager should return 45 when the user enters -5, 30")
                l = es

    def test_get_wager_returns_wager_amount_after_too_high_value(self):

        user_input = ["105", "22"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.get_wager(30)
                self.assertEqual(22, results, "getWager should return 22 when the user enters 105, 22, and the bank is less than 105")
                l = es


    def test_get_slot_results_returns_a_tuple_of_integers(self):

        results = lab05.get_slot_results()
        self.assertIsInstance(results, tuple, "get_slot_results should return a tuple")
        self.assertEqual(3, len(results), "get_slot_results shoudl return 3 items")
        self.assertIsInstance(results[0], int, "Item at index 0 was not an integer")
        self.assertIsInstance(results[1], int, "Item at index 1 was not an integer")
        self.assertIsInstance(results[2], int, "Item at index 2 was not an integer")


    def test_get_matches_returns_correct_number_of_matches(self):

        results = lab05.get_matches(3, 3, 3)
        self.assertEqual(3, results, "get_matches returns 3 when given 3 matching values")
        results = lab05.get_matches(4, 4, 4)
        self.assertEqual(3, results, "get_matches returns 3 when given 3 matching values")
        results = lab05.get_matches(4, 4, 5)
        self.assertEqual(2, results, "get_matches returns 2 when given 2 matching values")
        results = lab05.get_matches(8, 4, 4)
        self.assertEqual(2, results, "get_matches returns 2 when given 2 matching values")
        results = lab05.get_matches(8, 4, 8)
        self.assertEqual(2, results, "get_matches returns 2 when given 2 matching values")
        results = lab05.get_matches(8, 4, 3)
        self.assertEqual(0, results, "get_matches returns 0 when given 0 matching values")


    def test_get_payout_returns_correct_results(self):

        results = lab05.get_payout(3, 0)
        self.assertEqual(-3, results, "get_payout returns -3 when given 3 and no matches.")
        results = lab05.get_payout(2, 3)
        self.assertEqual(18, results, "get_payout returns 8 when given 2 and 3 matches.")
        results = lab05.get_payout(5, 2)
        self.assertEqual(10, results, "get_payout returns 10 when given 5 and 2 matches.")


if __name__ == "__main__":
    __unittest = True
    unittest.main()
