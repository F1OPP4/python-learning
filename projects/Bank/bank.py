class BankAccount:
    def __init__(self, owner, balance, id):
        if balance < 0:
            raise ValueError('умный самый?')
        self.owner = owner
        self.balance = balance
        self.id = id

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('А хуй тебе')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('А хуй тебе')
        if amount > self.balance:
            raise ValueError('Недостаточно средств')
        self.balance -= amount

    def get_info(self):
        return f"ID: {self.id}, Владелец: {self.owner}, Баланс: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = []
        self.next_id = 1

    def add_account(self, owner, balance):
        account = BankAccount(owner, balance, self.next_id)
        self.accounts.append(account)
        self.next_id += 1
        return account

    def get_account(self, account_id):
        for account in self.accounts:
            if account.id == account_id:
                return account
        raise ValueError("Аккаунт не найден")

    def transfer(self, from_id, to_id, amount):
        if from_id == to_id:
            raise ValueError('а ещё че хочешь')
        from_account = self.get_account(from_id)
        to_account = self.get_account(to_id)
        from_account.withdraw(amount)
        to_account.deposit(amount)

    def get_accounts_sorted_by_balance(self):
        return sorted(
            self.accounts,
            key=lambda account: account.balance,
            reverse=True
        )

    def get_total_balance(self):
        s = 0
        for account in self.accounts:
            s += account.balance
        return s
