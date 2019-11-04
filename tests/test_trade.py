import unittest
from app import Account, Trade, Position, setDB
from app import InsufficientFundsError, InsufficientSharesError, NoSuchTickerError
from schema import schema
from tests.config import DBPATH


class TestTrade(unittest.TestCase):

    @classmethod 
    def setUpClass(cls):
        schema(DBPATH)
        setDB(DBPATH)


    @classmethod
    def tearDownClass(cls):
        # called once when all the tests in this file are done
        # os.remove(DBPATH)
        pass


    def setUp(self):
        # called once before EACH test method
        with sqlite3.connect(Account.dbpath) as conn:
            cur = conn.cursor()
            DELETESQL = "DELETE FROM trades;"
            cur.execute(DELETESQL)
            #joe = Account(first="Joe", last="Smith", account_num="00000009", balance=100.0, pin="0009")
            #joe.save()
            #self.joe_id = joe.id


    def tearDown(self):
        # called once after EACH test method
        pass

    def test_dummy(self):
        self.assertTrue(True)


    