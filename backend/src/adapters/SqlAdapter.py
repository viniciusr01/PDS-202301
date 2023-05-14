from src.domain.entities.BankAccount import BankAccount
from src.domain.entities.CreditCard import CreditCard
from src.domain.gates.ISql import ISql
from ..utils.ValidObject import ValidObject
import sqlite3
from datetime import date
from src.domain.entities.Income import Income
from src.domain.entities.Expense import Expense
from typing import Any


class SqlAdapter(ISql):
    def __init__(self) -> None:
        self.db = 'db/db'

    def AddExpense(self, user_cpf: str, expense: dict):
        if not ValidObject().make(expense, [
            "description", 
            "value", 
            "reference_date",
            "id_account", 
            "id_category",
            "id_bill"
        ]):
            raise Exception('''Some key is missing. The following keys are expected:
                description, value, reference_date, id_account, id_category, id_bill''')

        SQL_QUERY = f'''
            INSERT INTO income (description, value, reference_date, id_account, id_category)
            VALUES(
                {expense['description']},
                {expense['value']},
                {expense['reference_date']},
                {user_cpf},
                {expense['id_category']}
            )
        '''

        res = self.__execute__(SQL_QUERY)
        print(res)

    def AddIncome(self, user_cpf: str, income: dict):
        if not ValidObject().make(income, [
            "description", 
            "value", 
            "reference_date",
            "id_category"
        ]):
            raise Exception('''Some key is missing. The following keys are expected: 
                description, value, reference_date, id_account, id_category''')
        
        SQL_QUERY = f'''
            INSERT INTO income ("description", "value", "reference_date", "id_account", "id_category")
            VALUES(
                '{str(income['description'])}',
                '{str(income['value'])}',
                '{str(income['reference_date'])}',
                '{str(user_cpf)}',
                '{str(income['id_category'])}'
            )
        '''
        
        res = self.__execute__(SQL_QUERY)
        print(res)

    def RetrieveIncomeFromAccount(self, id_account: str, date: date) -> list[Income]:
        SQL_QUERY = f'''
            SELECT description, value, reference_date, id_category
            FROM income i
            WHERE i.id_account = '{id_account}'
            AND i.reference_date <= '{date}'
        '''
        incomes = self.__execute__(SQL_QUERY)
        print(incomes)

        res = []

        for description, value, reference_date, id_category in incomes:
            res.append(Income(
                description,
                value,
                reference_date,
                id_category,
            ))

        return res

    def RetrieveExpenseFromAccount(self, id_account: str | None = None, 
                                   id_bill: str | None = None, date: date = date.today()) -> list[Expense]:
        
        if(id_account is None):
            SQL_QUERY = f'''
                SELECT description, value, reference_date, id_category, id_account, id_bill
                FROM expense e
                WHERE e.id_bill = '{id_bill}'
            '''

        else:
            SQL_QUERY = f'''
                SELECT description, value, reference_date, id_category, id_account, id_bill
                FROM expense e
                WHERE e.id_account = '{id_account}'
                AND e.reference_date <= '{date}'
            '''
        expenses = self.__execute__(SQL_QUERY)
        print(expenses)

        res = []

        for description, value, reference_date, id_category, id_account, id_bill in expenses:
            res.append(Expense(
                description,
                value,
                reference_date,
                id_category,
                id_account = id_account,
                id_bill= id_bill
            ))

        return res

    def RetrieveAccountsFromUser(self, user_cpf: int) -> list[BankAccount]:
        SQL_QUERY = f'''
            SELECT id, name, description, id_bank, fees, color
            FROM account a
            WHERE a.cpf_user = '{user_cpf}'
        '''
        accounts = self.__execute__(SQL_QUERY)
        print(accounts)

        res = []

        for id, name, description, id_bank, fees, color in accounts:
            res.append(BankAccount(
                id,
                name, 
                description,
                id_bank,
                fees,
                color
            ))

        return res
    
    def RetrieveCreditCardsFromUser(self, user_cpf: int, date: date) -> list[CreditCard]:
        SQL_QUERY = f'''
            SELECT id, name, description, fees, color, number_closure, number_deadline
            FROM credit_card c
            WHERE c.cpf_user = '{user_cpf}'
        '''

        creditCards = self.__execute__(SQL_QUERY)
        print(creditCards)

        res = []

        for id, name, description, fees, color, number_closure, number_deadline in creditCards:
            GET_CURRENT_BILL = f'''
                select id
                from bill b
                where b.month_year = "{str(date.month) + '/' + str(date.year)}"
                and b.id_credit_card = "{str(id)}"
            '''
            current_bill = self.__execute__(GET_CURRENT_BILL)
            current_bill, = current_bill[0]

            res.append(CreditCard(
                id,
                name, 
                description,
                number_closure,
                number_deadline,
                current_bill,
                color,
                fees
            ))

        return res


    def __execute__(self, sql_query: str):
        self.__init_cursor__()
        res = self.__execute_query__(sql_query)
        self.__close_conection__()
        
        return res

    def __init_cursor__(self):
        try:
            sqliteConnection = sqlite3.connect(self.db)
            cursor = sqliteConnection.cursor()
            print("Database Successfully Connected to SQLite")

            self.sqliteConnection = sqliteConnection
            self.cursor = cursor
        
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
            
    def __execute_query__(self, query: str) -> list[Any]:
        try:
            if self.cursor:
                self.cursor.execute(query)
                self.sqliteConnection.commit()

                record = self.cursor.fetchall()
                
                self.cursor.close()

                return record

            else:
                raise sqlite3.Error("Cursor is not available")

        except sqlite3.Error as error:
            print("Error while executing query", error)
            raise error
            
    def __close_conection__(self):
        if self.sqliteConnection:
            self.sqliteConnection.close()
            print("The SQLite connection is closed")
    
    