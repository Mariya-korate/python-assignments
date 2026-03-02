def withdraw(withdrawals):
    list_withdrawal = []
    current_balance = 1000
    i=0
    while i<len(withdrawals):
        if withdrawals[i] < current_balance:
            current_balance -= withdrawals[i]
            list_withdrawal.append(f"Withdrawn: {withdrawals[i]}")


        else:
            list_withdrawal.append(f"Insufficient funds for requested amount: {withdrawals[i]}")
        i=i+1

    list_withdrawal.append(f"Remaining Balance: {current_balance}")
    return list_withdrawal

withdrawals=[200,100,100,3000]
result=withdraw(withdrawals)
print(result)






