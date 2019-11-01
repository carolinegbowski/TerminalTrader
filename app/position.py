import sqlite3
from .config import DBPATH
from . import account
from . import trade


class Position:

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
    def delete_all(cls):
        """ delete all rows from this table """
        pass

    @classmethod
    def from_id(cls):
        """ return an object of this class for the given database row id """
        pass

    @classmethod
    def all(cls):
        """ return a list of every row of this table as objects of this class """
        pass

    def __repr__(self):
        """ return a string representing this object """
        # this is a good default __repr__
        return f"<{type(self).__name__} {self.__dict__}>"
    
    def value(self):
        """ look up the current price and return that * number of shares """
        pass

    @classmethod
    def all_from_account_id(cls, account_id):
        """ return every Position object for a given account_id that has more than
        0 shares """
        pass

    @classmethod
    def from_account_id_and_ticker(cls, account_id, ticker):
        """ return the Position object for a given account_id and ticker symbol
        if there is no such position, return a new object with zero shares """
        pass

    def get_account(self):
        """ return the Account object associated with this object """
        return account.Account.from_id(self.account_id)
    
    def get_trades(self):
        """ return the Trades associated with this object """
        return trade.Trade.all_from_account_id_and_ticker(self.account_id, self.ticker)