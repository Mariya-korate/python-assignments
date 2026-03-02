loyalty_points = 0
class Loyalty:

    def __init__(self):
        pass
    def process_transactions(self, transactions: list[int]):
        global loyalty_points
        sum_trans = sum(transactions)
        def apply_bonus():
            global loyalty_points
            nonlocal sum_trans
            if sum_trans > 1000:
                sum_trans += 50
            loyalty_points += int((sum_trans) / 100)
            return sum_trans

        return apply_bonus()

customer1=Loyalty()
result=customer1.process_transactions([300,400])
print(result)
print(loyalty_points)


























