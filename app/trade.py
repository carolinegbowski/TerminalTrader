import sqlite3
import time  # time.time() => floating point unix time stamp for right now
from .config import DBPATH
from . import account
from . import position
from . import errs

def get_current_price(ticker):
    """ return the current price of a given ticker. can raise NoSuchTickerError or
    ConnectionError """
    raise errs.NoSuchTickerError


class Trade:

    dbpath = DBPATH

    @classmethod
    def setDB(cls, dbpath):
        cls.dbpath = dbpath

    def __init__(self, **kwargs):
        """ sets each field from kwargs """
        pass

    def save(self):
        """ inserts or updates depending on id's value """
        pass

    def _insert(self):
        """ inserts a new row into the database and sets self.id """
        pass

    def _update(self):
        """ updates the row with id=self.id with this objects current values"""
        pass

    def delete(self):
        """ deletes row with id=self.id from db and sets self.id to None """
        pass

    @classmethod
    def from_id(cls):
        """ return an object of this class for the given database row id """
        pass

    @classmethod
    def all(cls):
        """ return a list of every row of this table as objects of this class """
        pass

    @classmethod
    def delete_all(cls):
        """ delete all rows from this table """
        pass

    @classmethod
    def all_from_account_id(cls, account_id):
        """ return a list of Trade objects for all of a given account's trades """
        pass

    @classmethod
    def all_from_account_id_and_ticker(cls, account_id, ticker):
        """ return a list of Trade object for all of a given accounts trades
        for a given ticker symbol """
        pass

    def get_account(self):
        """ return the Account object for this trade """
        return account.Account.from_id(self.account_id)
    
    def get_position(self):
        """ return the Position object for this trade """
        return position.Position.from_account_id_and_ticker(self.account_id, self.ticker)

    def __repr__(self):
        """ return a string representing this object """
        # this is a good default __repr__
        return f"<{type(self).__name__} {self.__dict__}>"