class Bank:
    """
    The Bank
    """
    def __init__(self):
        self.accounts = []
    
    def add(self, new_account):
        """
        Add new_account in the Bank\n
        @new_account:   Account() new account to append\n
        @return:        True if success, False if an error occured\n
        """
        self.accounts.append(new_account)

    def transfer(self, origin, dest, amount):
        """
        Perform the fund transfer\n
        @origin:    str(name) of the first account\n
        @dest:      str(name) of the destination account\n
        @amount:    float(amount) amount to transfer\n
        @return:    True if success, False if an error occured\n
        """

    def fix_account(self, name):
        """
        fix account associated to name if corrupted
        @name:      str(name) of the account
        @return:    True if sucess, False if an error occured
        """
        