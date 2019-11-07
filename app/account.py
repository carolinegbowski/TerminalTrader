import sqlite3
import bcrypt

"""
Circular Imports:

When file A imports B and B imports A, this can cause issues with the from x 
import y method of importing can raise errors. Inside the module we need to
use the position.Position way of naming the class but because of our imports
in __init__.py, code that uses this module does not need to worry about that.

from . import 

. means 'this folder in the module'
"""

from . import position
from . import trade
from . import errs
from .config import DBPATH

class Account:

    dbpath = DBPATH

    @classmethod
    def setDB(cls, dbpath):
        cls.dbpath = dbpath

    def __init__(self, **kwargs):
        """ sets each field from kwargs """
        self.id = kwargs.get("id")
        self.username = kwargs.get("username")
        self.password_hash = kwargs.get("password_hash")
        self.balance = kwargs.get("balance", 0.00)
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.email_address = kwargs.get("email_address")
        

    def save(self):
        """ inserts or updates depending on id's value """
        pass

    def _insert(self):
        """ inserts a new row into the database and sets self.id """
        with sqlite3.connect(self.dbpath) as connection: 
            cursor = connection.cursor()
            INSERTSQL = """INSERT INTO accounts(username, password_hash, balance, first_name, last_name, email_address) 
            VALUES (:username, :password_hash, :balance, :first_name, :last_name, :email_address); """
            values = {
                "username": self.username,
                "password_hash" : self.password_hash, 
                "balance" : self.balance, 
                "first_name" : self.first_name,
                "last_name" : self.last_name,
                "email_address" : self.email_address, 
            }
            try: 
                cursor.execute(INSERTSQL, values)
                self.id = cursor.lastrowid
            except sqlite3.IntegrityError:
                raise ValueError("ticker not set or a position for this ticker already exists")
        # every other starting here 
        pass

    def _update(self):
        """ updates the row with id=self.id with this objects current values"""
        pass

    def delete(self):
        """ deletes row with id=self.id from db and sets self.id to None """
        with sqlite3.connect(self.dbpath) as connection: 
            cursor = connection.cursor()
            DELETESQL = """ DELETE FROM accounts WHERE id=:id """
            cursor.execute(DELETESQL, {"id": self.id})
            self.id = None

    @classmethod
    def from_id(cls, id):
        """ return an object of this class for the given database row id """
        pass

    @classmethod
    def all(cls):
        """ return a list of every row of this table as objects of this class """
        with sqlite3.connect(cls.dbpath) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            SELECTSQL = "SELECT * FROM accounts;"
            cursor.execute(SELECTSQL)
            result = []
            for dictrow in cursor.fetchall():
                result.append(cls(**dictrow))
            return result

    @classmethod
    def delete_all(cls):
        """ delete all rows from this table """
        pass

    def __repr__(self):
        """ return a string representing this object """
        # this is a good default __repr__
        # Q: using the docs, can you figure out what this is doing?
        return f"<{type(self).__name__} {self.__dict__}>"

    def set_password_hash(self, password):
        """ hash the provided password and set self.password_hash """
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode(), salt)
        return self.password_hash

    @classmethod
    def login(cls, username, password):
        """ check search for username and check password, return an object of this 
        class if it matches, None otherwise """
        return None

    def get_position_for(self, ticker):
        """ return the Position object for this account's holdings in a given
        stock, return a new 0 share position if it does not exist.
        
        Why? To make buy simple, you always just get the current position and 
        add to it. """
        return position.Position.from_account_id_and_ticker(self.id, ticker)
    
    def get_positions(self):
        """ return all Position objects for this account with more than 0 shares """
        return position.Position.all_from_account_id(self.id)
    
    def get_trades_for(self, ticker):
        """ return all Trade objects for this account and a given ticker """
        return trade.Trade.all_from_account_id_and_ticker(self.id, ticker)
    
    def get_trades(self):
        """ return all Trades this account has made """
        return trade.Trade.all_from_account_id(self.id)
    
    def buy(self, ticker, volume):
        """ Create a trade and modify a position for this user, creating a buy. Can
        raise errs.InsufficientFundsError or errs.NoSuchTickerError """
        raise errs.NoSuchTickerError

    def sell(self, ticker, volume):
        """ Create a trade and modify a position for this user, creating a sell. Can
        raise errs.InsufficientSharesError or errs.NoSuchTickerError """
        # CAROLINE 
        try:
            
        except: 
            raise errs.NoSuchTickerError