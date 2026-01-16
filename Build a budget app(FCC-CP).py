class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def check_funds(self,amount):
        acc_balance = 0
        for leader in self.ledger:
            acc_balance += leader['amount']
        if acc_balance >= amount:
            return True
        else:
            return False

    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': float(amount), 'description': description})

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': - float(amount), 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        acc_balance = 0
        for leader in self.ledger:
            acc_balance += leader['amount']
        return acc_balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.ledger.append({'amount': - float(amount), 'description': f'Transfer to {other_category.name}'})
            other_category.ledger.append({'amount': float(amount), 'description': f'Transfer from {self.name}'})
            return True
        else:
            return False

    def __str__(self):
        calc = round((30 - len(self.name)) / 2)
        top_line = '*' * calc + self.name + '*' * (30 - calc - len(self.name))
        mid_line = ''
        bottom_line = ''
        for ledger in self.ledger:
            len_d = len(str(ledger['description']))
            if len_d <= 23:
                mid_line += str(ledger['description']) + ' ' * (23 - len_d)
            else:
                mid_line += str(ledger['description'][:23])
            amount = int(ledger['amount'])
            len_am = len(str(amount))
            mid_line += ' ' * (4 - len_am) + f"{ledger['amount']:.2f}" + '\n'
            bottom_line = 'Total: ' + f"{self.get_balance():.2f}"
        return top_line + '\n' +  mid_line + bottom_line


def create_spend_chart(categories):
    title_part = 'Percentage spent by category'
    # percentage calculations
    category_list = []
    category_percentage_list = []
    names_list = []
    for category in categories:
        category_spend = 0
        for leader in category.ledger:
            if leader['amount'] < 0:
                category_spend += - leader['amount']
        category_list.append(category_spend)
        names_list.append(category.name)
    full_spend = 0
    for category_spend in category_list:
        full_spend += category_spend
    for category_spend in category_list:
        category_percentage_list.append((int(category_spend / full_spend * 10 ) * 10 ))
    # middle part output
    percentages = ['100',' 90',' 80',' 70',' 60',' 50',' 40',' 30',' 20',' 10','  0']
    middle_part = ''
    for pers in percentages:
        per_part = ''
        for index, category_percentage in enumerate(category_percentage_list):
            if category_percentage >= int(pers):
                per_part += 'o  '
            else:
                per_part += '   '
        if pers != percentages[-1]:
            middle_part += f'{pers}| {per_part}\n'
        else:
            middle_part += f'{pers}| {per_part}'
    # dash output
    dash_part = '    ' + '---' * len(category_percentage_list) + '-'
    # names output
    name_part = ''
    longest_name = ''
    # makes all names same length
    for name in names_list:
        if len(name) > len(longest_name):
            longest_name = name
    for index,name in enumerate(names_list):
        if len(name) < len(longest_name):
            names_list[index] += ' ' * (len(longest_name) - len(name))
    # final output
    for letter in range(len(longest_name)): # line
        name_part += '     '
        for name in names_list: # letter
            name_part += f'{name[letter]}  '
        if letter != len(longest_name) -1:
            name_part += '\n'
    return title_part + '\n' + middle_part + '\n' + dash_part + '\n' + name_part





food = Category('food')
go = Category('go')
clothing = Category('clothing')
go.deposit(500, 'deposit')
food.deposit(900, 'deposit')
food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
go.withdraw(136.77, 'milk, cereal, eggs, bacon, bread')
clothing.deposit(700, 'deposit')
clothing.withdraw(250, 'deposit')
print(food)
print(create_spend_chart([food,go,clothing]))