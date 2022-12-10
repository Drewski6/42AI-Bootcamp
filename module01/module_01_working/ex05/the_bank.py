# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
from account import Account

class CorruptionError(Exception):
    """
    debug error class
    """
    def __init__(self, errno, message):
        self.message = message
        self.errno = errno

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
        # ccheck = True # using for debugging so I can see errors returned
        ccheck = self.__corruption_check(new_account)
        if ccheck is not True:
            # print(ccheck) # for debugging error message if wanted
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

        # left off here last thing to do


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
        status = False
        while status is not True:
            status = self.__corruption_check(account)
            if isinstance(status, CorruptionError):
                if self.__fix_account_issue(status, account) is False:
                    return False    # will receive false from __fix_account_issue
                                    # if error is encountered while fixing.
        return True

    def __corruption_check(self, account):
        """
        Checks if an account is corrupt or not.

        :param account: Account that is in the Bank's account list
        :returns:       True if account is not corrupted
                        CorruptionError object if account is corrupt or an error was encountered.
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
            return corr
            #return False # use when finished
        return True

    def __corr_even_attr_check(self, account):
        if len(dir(account)) % 2:
            raise CorruptionError(10, "even number of attributes")

    def __corr_attr_b_check(self, account):
        for item in dir(account):
            if str(item)[0] == 'b':
                raise CorruptionError(11, "attr starts with B")

    def __corr_attr_zip_addr(self, account):
        dir_lst = dir(account)
        for item in dir_lst:
            if "zip" in item:
                return
            if "addr" in item:
                return
        raise CorruptionError(12, "No attribute starting with either 'zip' or 'addr'")

    def __corr_name_type(self, account):
        if hasattr(account, "name") is False:
            raise CorruptionError(13, "account does not have attribute 'name'")
        if isinstance(account.name, str) is False:
            raise CorruptionError(14, "name attribute is not a string")

    def __corr_id_type(self, account):
        if hasattr(account, "id") is False:
            raise CorruptionError(15, "account does not have attribute 'id'")
        if isinstance(account.id, int) is False:
            raise CorruptionError(16, "id attribute is not an int")

    def __corr_value_type(self, account):
        if hasattr(account, "value") is False:
            raise CorruptionError(17, "account does not have attribute 'value'")
        if isinstance(account.value, int) or isinstance(account.value, float):
            return
        raise CorruptionError(18, "value attribute is not an int or float")

    def __fix_account_issue(self, error, account, debug=False):
        result = False
        if isinstance(error, CorruptionError) is False:
            return result
        if error.errno == 10:
            result = self.__errno_10_fix(account, debug)
        elif error.errno == 11:
            result = self.__errno_11_fix(account, debug)
        elif error.errno == 12:
            result = self.__errno_12_fix(account, debug)
        # elif error.errno == 13:
        #     result = self.__errno_13_fix(account, debug)
        # elif error.errno == 14:
        #     result = self.__errno_14_fix(account, debug)
        elif error.errno == 15:
            result = self.__errno_15_fix(account, debug)
        elif error.errno == 16:
            result = self.__errno_16_fix(account, debug)
        elif error.errno == 17:
            result = self.__errno_17_fix(account, debug)
        elif error.errno == 18:
            result = self.__errno_18_fix(account, debug)
        return result

    def __errno_10_fix(self, account, debug):
        if debug:
            print("in __errno_10_fix")
        if "odd_setter" in dir(account):
            delattr(account, "odd_setter")
        else:
            setattr(account, "odd_setter", 0)
        return True

    def __errno_11_fix(self, account, debug):
        if debug:
            print("in __errno_11_fix")
        for item in dir(account):
            if item[0] == 'b':
                delattr(account, item)
        return True

    def __errno_12_fix(self, account, debug):
        if debug:
            print("in __errno_12_fix")
        account.address = "Need customer address."
        return True

    # Error not fixable
    # def __errno_13_fix(self, account, debug):
    #     if debug:
    #         print("in __errno_13_fix")
    #     return True

    # Error not fixable
    # def __errno_14_fix(self, account, debug):
    #     if debug:
    #         print("in __errno_14_fix")
    #     return True

    def __errno_15_fix(self, account, debug):
        if debug:
            print("in __errno_15_fix")
        try:
            setattr(account, "id", account.ID_COUNT)
        except AttributeError:
            return False
        return True

    def __errno_16_fix(self, account, debug):
        if debug:
            print("in __errno_16_fix")
        try:
            account.id = int(account.id)
        except ValueError:
            return False
        return True

    def __errno_17_fix(self, account, debug):
        if debug:
            print("in __errno_17_fix")
        try:
            setattr(account, "value", 0)
        except AttributeError:
            return False
        return True

    def __errno_18_fix(self, account, debug):
        if debug:
            print("in __errno_18_fix")
        try:
            account.value = float(account.value)
        except ValueError:
            try:
                account.value = int(account.value)
            except ValueError:
                return False
        return True
