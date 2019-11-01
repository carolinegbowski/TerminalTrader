from . import view
from . import account
# a way to get around having to use the module name when avoiding
# circular import problems
Account = account.Account
# note: if you do not create any new Trade or Position objects but only
# get them as the return values from Account's methods, you do not need
# to import those classes directly. You only need to import the class
# if you need to call the constructor (t=Trade()) or call a class method

def run():
    view.welcome()
    
    while True:
        account = login_menu()
        if account is None:
            break
        main_menu(account)
    
    view.goodbye()

def login_menu():
    """ login, create account, or quit. return an Account object on successful login
    return None for quit """
    return None

def main_menu(account):
    from . import InsufficientFundsError, InsufficientSharesError, NoSuchTickerError
    """ check balance, deposit, withdraw, see positions, see trades, look up stock
    prices, buy, and sell. No return value. """
    pass