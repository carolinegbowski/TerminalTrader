import sqlite3 
from app.config import DBPATH 

def schema(dbpath=DBPATH):
    """
    Create these tables

    account:
        id, username, password_hash, balance, first, last

    position:
        id, ticker, shares, account_id

    trade:
        id, ticker, volume, time, price, account_id
    """
    pass

if __name__ == "__main__":
    schema()
