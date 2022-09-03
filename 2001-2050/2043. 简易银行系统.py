class Bank:

    def __init__(self, balance: List[int]):
        self.acct=balance
        self.size=len(balance)
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 <=self.size and account2 <=self.size and self.acct[account1-1]>=money:
            self.acct[account1-1]-=money
            self.acct[account2-1]+=money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account <=self.size:
            self.acct[account-1]+=money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if account <=self.size and self.acct[account-1]>=money:
            self.acct[account-1]-=money
            return True
        else:
            return False

