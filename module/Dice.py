
import random

class Dice:
    def __init__(self, dice_number, side_number):
        if dice_number <= 30 and side_number <= 100:
            self.dice_number = dice_number
            self.side_number = side_number
            self.result_list =[]
            result_total = 0
            for dice in range (dice_number):
                result = random.randint(1, side_number)
                self.result_list.append(result)
                result_total += result
            self.result_total = result_total
        else:
            pass
    
    def __str__(self):
        return f"{self.dice_number} {self.side_number} {self.result_list} {self.result_total}"

class DND_Attirbute_Dice (Dice):
    def __init__(self):
        super().__init__(4,6)
        minimal = min(self.result_list)
        self.result_list.remove(minimal)
        self.result_total -= minimal
    def __str__(self):
        return super().__str__()


