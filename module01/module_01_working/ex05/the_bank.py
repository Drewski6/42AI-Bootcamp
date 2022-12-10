# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
from account import Account

class CorruptionError(Exception):
    """
    debug error class
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class Bank:
    """
    The Bank
    """
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """
        Add new_account in the Bank
        @new_account:   Account() new account to append
        @return:        True if success, False if an error occured
        """
        try:
            assert (isinstance(new_account, Account)), "\
                new_account must be of class Account."
        except AssertionError:
            return False
        ccheck = True # using for debugging so I can see errors returned
        #ccheck = self.__corruption_check(new_account)
        if ccheck is not True:
            # print(ccheck) for debugging error message if wanted
            return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """
        Perform the fund transfer
        @origin:    str(name) of the first account
        @dest:      str(name) of the destination account
        @amount:    float(amount) amount to transfer
        @return:    True if success, False if an error occured
        """

    def fix_account(self, name):
        """
        fix account associated to name if corrupted
        @name:      str(name) of the account
        @return:    True if sucess, False if an error occured
        """
        assert isinstance(name, str), "\
            Please enter the string attribute for name of an account."
        account = None
        for item in self.accounts:
            try:
                if item.name == name:
                    account = item
            except AttributeError:
                continue
        if account is None:
            return False    # account with name not found
        status = self.__corruption_check(account)
        print(type(status))
        return status

    def debug_print_account_list(self):
        """
        prints full account list for debug
        """
        print([item.name for item in self.accounts])

    def __corruption_check(self, account):
        """
        Checks if an account is corrupt or not.

        :param account: Account that is in the Bank's account list
        :returns:       True if account is not corrupted
                        Error message if account is corrupt or an error was encountered.
        """
        assert isinstance(account, Account), "\
            corruption check can only be performed on Accounts"
        try:
            self.__corr_even_attr_check(account)
            self.__corr_attr_b_check(account)
            self.__corr_attr_zip_addr(account)
            self.__corr_name_type(account)
            self.__corr_id_type(account)
            self.__corr_value_type(account)
        except CorruptionError as corr:
            return corr.message
            #return False # use when finished
        return True

    def __corr_even_attr_check(self, account):
        if len(dir(account)) % 2:
            raise CorruptionError("even number of attributes")

    def __corr_attr_b_check(self, account):
        for item in dir(account):
            if str(item)[0] == 'b':
                raise CorruptionError("attr starts with B")

    def __corr_attr_zip_addr(self, account):
        dir_lst = dir(account)
        for item in dir_lst:
            if "zip" in item:
                return
            if "addr" in item:
                return
        raise CorruptionError("No attribute starting with either 'zip' or 'addr'")

    def __corr_name_type(self, account):
        if hasattr(account, "name") is False:
            raise CorruptionError("account does not have attribute 'name'")
        if isinstance(account.name, str) is False:
            raise CorruptionError("name attribute is not a string")

    def __corr_id_type(self, account):
        if hasattr(account, "id") is False:
            raise CorruptionError("account does not have attribute 'id'")
        if isinstance(account.id, int) is False:
            raise CorruptionError("id attribute is not an int")

    def __corr_value_type(self, account):
        if hasattr(account, "value") is False:
            raise CorruptionError("account does not have attribute 'value'")
        if isinstance(account.value, int) or isinstance(account.value, float):
            return
        raise CorruptionError("value attribute is not an int or float")
