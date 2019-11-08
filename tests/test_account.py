import bcrypt
import sqlite3
import unittest
from app import Account, Trade, Position, setDB
from app import InsufficientFundsError, InsufficientSharesError, NoSuchTickerError
from schema import schema
from tests.config import DBPATH


class TestAccount(unittest.TestCase):

    @classmethod 
    def setUpClass(cls):
        schema(DBPATH)
        setDB(DBPATH)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        with sqlite3.connect(DBPATH) as connection:
            cursor = connection.cursor()
            DELETESQL = "DELETE FROM accounts;"
            cursor.execute(DELETESQL)
    
    def tearDown(self):
        pass

    def test_dummy(self):
        self.assertTrue(True)
    
    def testSaveInsert(self):
        caroline = Account(username="cg16" , password_hash="password" , balance=10000, 
        first_name="Caroline", last_name="Grabowski", email="caroline.gbowksi@gmail.com")
        caroline.save()
        self.assertIsNotNone(caroline.id, "save should set an id value for new input")
        with sqlite3.connect(DBPATH) as connection:
            cursor = connection.cursor()
            SQL = "SELECT * FROM accounts WHERE username='cg16';"
            cursor.execute(SQL)
            rows = cursor.fetchall()
            self.assertEqual(len(rows), 1, "save should create 1 new row in the database")

    def testSaveUpdate(self):
        caroline = Account(username="cg16" , password_hash="password" , balance=10000, 
        first_name="Caroline", last_name="Grabowski", email="caroline.gbowksi@gmail.com")
        caroline.save()
        caroline_id = caroline.id
        caroline2 = Account.from_id(caroline_id)
        caroline2.username = "cgrabow16"
        caroline2.balance = 20000
        caroline2.first_name = "Caro"
        caroline2.last_name = "Grabo"
        caroline2.save()
        self.assertEqual(caroline2.id, caroline_id, "update should not change ID number")

        caroline3 = Account.from_id(caroline_id)
        self.assertEqual(caroline3.username, "cgrabow16", "update should update username")
        self.assertEqual(caroline3.balance, 20000 , "update should update balance")
        self.assertEqual(caroline3.first_name, "Caro" , "update should update name")
        self.assertEqual(caroline3.last_name, "Grabo" , "update should update name")

    def testDelete(self):
        caroline = Account(username="cg16" , password_hash="password" , balance=10000, 
        first_name="Caroline", last_name="Grabowski", email="caroline.gbowksi@gmail.com")
        caroline.save()
        alex = Account(username="alex16" , password_hash="password" , balance=20000, 
        first_name="Alex", last_name="C", email="alexc@gmail.com")
        alex.save()
        caroline.delete()
        with sqlite3.connect(DBPATH) as connection: 
            cursor = connection.cursor()
            SQL = "SELECT * FROM ACCOUNTS WHERE balance=10000;"
            cursor.execute(SQL)
            rows = cursor.fetchall()
            self.assertEqual(len(rows), 0, "delete should delete 1 row in the table")

    def testDeleteAll(self):
        caroline = Account(username="cg16" , password_hash="password" , balance=10000, 
        first_name="Caroline", last_name="Grabowski", email="caroline.gbowksi@gmail.com")
        caroline.save()
        alex = Account(username="alex16" , password_hash="password" , balance=20000, 
        first_name="Alex", last_name="C", email="alexc@gmail.com")
        alex.save()
        Account.delete_all()
        with sqlite3.connect(DBPATH) as connection: 
            cursor = connection.cursor()
            SQL = "SELECT * FROM ACCOUNTS;"
            cursor.execute(SQL)
            rows = cursor.fetchall()
            self.assertEqual(len(rows), 0, "delete all should delete all rows in the table")

    def testFromId(self):
        caroline = Account(username="cg16" , password_hash="password" , balance=10000, 
        first_name="Caroline", last_name="Grabowski", email="caroline.gbowksi@gmail.com")
        caroline.save()
        caroline_id = caroline.id
        caroline2 = Account.from_id(caroline_id)
        self.assertEqual(caroline2.first_name, "Caroline")
        alex = Account.from_id(10340923950399)
        self.assertIsNone(alex, "from_id returns None for nonexistent row")

    def testAll(self):
        caroline = Account(username="cg16" , password_hash="password" , balance=10000, 
        first_name="Caroline", last_name="Grabowski", email="caroline.gbowksi@gmail.com")
        caroline.save()
        alex = Account(username="alex16" , password_hash="password" , balance=20000, 
        first_name="Alex", last_name="C", email="alexc@gmail.com")
        alex.save()

        all_data = Account.all()
        # self.assertEqual(len(all_data), 2, "all data should return all rows of data")
        self.assertEqual(all_data[0].first_name, "Caroline", "all function should return all account data")
        self.assertEqual(all_data[1].first_name, "Alex", "all function should return all account data")

    def testPasswordHash(self):
        caroline = Account(username="cg16" , balance=10000, 
        first_name="Caroline", last_name="Grabowski", email="caroline.gbowksi@gmail.com")
        caroline.save()
        caroline.set_password_hash("password")

        # HERE TEST LOGIN WITH instance caroline username & SAME PASSWORD

        salt = bcrypt.gensalt()
        test_password_hash = bcrypt.hashpw("password".encode(), salt)

        self.assertEqual(test_password_hash, caroline.password_hash, "set password hash should set self.hashed_password to encrypted password")

