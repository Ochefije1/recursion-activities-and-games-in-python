# # Player 1
# file = open('day_11\comments.txt', 'a')
# file.write(['player1'], ["name" "John", "score" 100])

# # Player 2
# player2 = {
#     "name": "Wisdom",
#     "score": 100
  
# }

# # Reading the players
# print("Player 1: ", player1)
# print("Player 2: ", player2)

# file = open('day_11\comments.txt', 'a')
# file.write('this is the second line of this text\n')
# file.close()
# file = open('day_11\comments.txt', 'r')
# print(file.read())

# players = [
#     {'name': 'Ayo', 'score':0, 'trials':0},
#     {'name': 'Aliyu', 'score':0, 'trials':0},
#     ]

# with open('score.txt', 'a') as score
# content = score.read()
# for player in players:
#     for name, score, trial in players.items():
        # player_record = f"{name[1]}'/{score[1]}/ {trial[1]}\n'



import uuid
import datetime
import paystack

paystack_api_key = 'pk_test_7e0bf57d99c4466e68fe890ace6c22b7027f168d3'

class BankAccount:
    def __init__(self, name, email, password):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = password
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(('deposit', amount, datetime.datetime.now()))

    def transfer(self, to_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            to_account.balance += amount
            self.transactions.append(('transfer', amount, datetime.datetime.now()))
            to_account.transactions.append(('receive', amount, datetime.datetime.now()))
            return True
        else:
            return False

    def view_transactions(self):
        return self.transactions

    def check_balance(self):
        return self.balance

class BankApplication:
    def __init__(self):
        self.accounts = []

    def register(self, name, email, password):
        account = BankAccount(name, email, password)
        self.accounts.append(account)
        return account

    def login(self, email, password):
        for account in self.accounts:
            if account.email == email and account.password == password:
                return account
        return None

    def mock_transaction(self, amount, recipient):
        paystack.initialize(paystack_api_key)
        transaction = paystack.Transaction.initialize(
            amount=amount*100,
            email=recipient.email,
            reference=str(uuid.uuid4())
        )
        if transaction['status']:
            return True
        else:
            return False

if __name__ == '__main__':
    bank = BankApplication()

    while True:
        print('1. Register')
        print('2. Login')
        print('3. Deposit')
        print('4. Transfer')
        print('5. View Transaction History')
        print('6. Check Balance')
        print('7. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Enter your name: ')
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            account = bank.register(name, email, password)
            print(f'Your account ID is: {account.id}')

        elif choice == '2':
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            account = bank.login(email, password)
            if account:
                print(f'Welcome, {account.name}!')
            else:
                print('Invalid email or password')

        elif choice == '3':
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            account = bank.login(email, password)
            if account:
                amount = float(input('Enter the amount to deposit: '))
                account.deposit(amount)
                print(f'Deposit successful. Your new balance is: {account.check_balance()}')
            else:
                print('Invalid email or password')

        elif choice == '4':
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            account = bank.login(email, password)
            if account:
                recipient_email = input('Enter the recipient email: ')
                recipient = bank.login(recipient_email, '')
                if recipient:
                    amount = float(input('Enter the amount to transfer: '))
                    if account.transfer(recipient, amount):
                        print(f'Transfer successful. Your new balance is: {account.check_balance()}')
