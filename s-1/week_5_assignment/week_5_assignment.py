def find_account_index(account_ids, account_id):
    for i in range(len(account_ids)):
        if account_ids[i] == account_id:
            return i
    return -1
    
def process_ledger(initial_accounts, initial_balances, transactions):
    c_accounts = initial_accounts[:]
    c_balance = initial_balances[:]
    c_t = transactions
    for sublist in c_t:
        if sublist[0] == 'OPEN':
            ind = find_account_index(c_accounts, sublist[1])
            if ind == -1:
                c_accounts.append(sublist[1])
                c_balance.append(sublist[2])
        elif sublist[0] == 'DEPOSIT':
            ind = find_account_index(c_accounts, sublist[1])
            if ind != -1: c_balance[ind] += sublist[2]
        else:
            ind = find_account_index(c_accounts, sublist[1])
            if ind != -1 and c_balance[ind] >= sublist[2]: c_balance[ind] -= sublist[2]
    final_account_ids_list = c_accounts
    final_account_balances_list = c_balance
    return final_account_ids_list, final_account_balances_list