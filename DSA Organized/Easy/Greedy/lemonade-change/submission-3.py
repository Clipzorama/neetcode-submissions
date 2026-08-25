class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10 and five > 0:
                five -= 1
                ten += 1
            elif bill == 20:
                if five >= 3:
                    five -= 3
                elif five > 0 and ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    return False
            else:
                return False

        return True