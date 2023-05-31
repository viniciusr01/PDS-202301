from src.domain.entities.BankAccount import BankAccount
from src.domain.entities.Bill import Bill
from src.domain.entities.Category import Category
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
        # TODO: COLOCAR ISSO NUMA VARIÁVEL DE AMBIENTE
        self.db = 'db/db'

    # TODO: CONFERIR SE AS CLASSES DENTRO DO ADAPTER PODEM RECEBER ENTIDADES AO INVÉS DE DICIONÁRIO (ACREDITO QUE POSSA)
    def AddExpense(self, expense: dict):
        if not ValidObject().make(expense, [
            "description", 
            "value", 
            "reference_date",
            "id_account", 
            "id_category",
            "id_credit_card",
            "is_recurrency",
            "end_date"
        ]):
            raise Exception('''Some key is missing. The following keys are expected:
                description, value, reference_date, id_account, id_category, id_bill, is_recurrency, end_date''')

        if expense['id_account'] != None:

            SQL_QUERY = f'''
                INSERT INTO expense (description, value, reference_date, id_account, id_category, is_recurrency, recurrency_end_date)
                VALUES(
                    '{expense['description']}',
                    '{expense['value']}',
                    '{expense['reference_date']}',
                    '{expense['id_account']}',
                    '{expense['id_category']}',
                    '{expense['is_recurrency']}',
                    '{expense['end_date']}'
                )
            '''

        else:
            bill = self.__GetBillByDate__(expense['id_credit_card'],expense['reference_date'])



            SQL_QUERY = f'''
                INSERT INTO expense (description, value, reference_date, id_bill, id_category, is_recurrency, recurrency_end_date)
                VALUES(
                    '{expense['description']}',
                    '{expense['value']}',
                    '{expense['reference_date']}',
                    '{ bill }',
                    '{expense['id_category']}',
                    '{expense['is_recurrency']}',
                    '{expense['end_date']}'
                )
            '''

        res = self.__execute__(SQL_QUERY)
        print(res)

    def AddIncome(self, income: dict):
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
                '{income['description']}',
                '{income['value']}',
                '{income['reference_date']}',
                '{income['id_account']}',
                '{income['id_category']}'
            )
        '''
        
        res = self.__execute__(SQL_QUERY)
        print(res)
    
    def AddCategory(self, category: dict):
        if not ValidObject().make(category, [
            "name",
            "description", 
            "user_cpf"
        ]):
            raise Exception('''Some key is missing. The following keys are expected: 
                name, description, user_cpf''')
        
        SQL_QUERY = f'''
            INSERT INTO category ("name", "description", "color", "cpf_user")
            VALUES(
                '{category['name']}',
                '{category['description']}',
                '{category['color']}',
                '{category['user_cpf']}'
            )
        '''

        res = self.__execute__(SQL_QUERY)
        print(res)
        

    def RetrieveIncomesFromAccount(self, id_account: str, initial_date: date, end_date: date = date.today()) -> list[Income]:
        SQL_QUERY = f'''
            SELECT description, value, reference_date, id_category
            FROM income i
            WHERE i.id_account = '{id_account}'
            AND i.reference_date <= '{end_date}'
            AND i.reference_date >= '{initial_date}'
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
                id_account
            ))

        return res

    def RetrieveExpensesFromAccount(self, id_account: str | None = None, 
                                    id_credit_card: str | None = None, 
                                    initial_date: date = date.today(), 
                                    end_date: date = date.today()) -> list[Expense]:
        
        if(id_credit_card is not None):
            bill = self.__GetBillByDate__(int(id_credit_card), initial_date)
            
            SQL_QUERY = f'''
                SELECT description, value, reference_date, id_category, id_account, id_bill
                FROM expense e
                WHERE e.id_bill = '{bill}'
                AND e.reference_date <= '{end_date}'
                AND e.reference_date >= '{initial_date}'
            '''

        else:
            SQL_QUERY = f'''
                SELECT description, value, reference_date, id_category, id_account, id_bill
                FROM expense e
                WHERE e.id_account = '{id_account}'
                AND e.reference_date <= '{end_date}'
                AND e.reference_date >= '{initial_date}'
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

    def RetrieveSumIncomeFromAccount(self, id_account: str, date: date = date.today()) -> float:
        GET_SUM_INCOME = f'''
            SELECT SUM(e.value) as value
            from income e 
            where id_account  = "{id_account}"
            and reference_date  <= "{ date }"
            group by (id_account)
            '''
        
        income = self.__execute__(GET_SUM_INCOME)
        if len(income) == 0:
            return 0.0

        income, = income[0]
        return income
        

    def RetrieveSumExpenseFromAccount(self, id_account: str | None = None, id_bill: str | None = None, date: date = date.today()) -> float:
        if(id_account is not None):
            GET_SUM_EXPENSE = f'''
                SELECT SUM(e.value) as value
                from expense e 
                where id_account  = "{id_account}"
                and reference_date  <= "{ date }"
                group by (id_account)
                '''
        else:
            GET_SUM_EXPENSE = f'''
                SELECT SUM(e.value) as value
                from expense e 
                where id_bill  = "{id_bill}"
                group by (id_bill)
                '''
            
        expense = self.__execute__(GET_SUM_EXPENSE)
        if len(expense) == 0:
            return 0.0

        expense, = expense[0]
        return expense

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
            bill_id = self.__GetBillByDate__(id, date)
            current_bill = Bill(
                bill_id,
                f"{date.month}/{date.year}",
            )

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
        
    def RetrieveCategoriesFromUser(self, user_cpf: int) -> list[Category]:
        SQL_QUERY = f'''
            SELECT name, description, color, cpf_user
            FROM category c
            WHERE c.cpf_user = '{user_cpf}'
        '''

        categories = self.__execute__(SQL_QUERY)
        print(categories)

        res = []

        for name, description, color, user_cpf in categories:
            aux = Category(
                name, 
                description,
                user_cpf,
                color
            )
            res.append(aux)

        return res


    #TO DO: Vinicius
    def CreateUser(self, cpf, name, email) -> None:
        
        SQL_QUERY = f'''
            INSERT INTO user ("cpf", "name", "email")
            VALUES(
                '{cpf}',
                '{name}',
                '{email}'
            )
        '''
        
        res = self.__execute__(SQL_QUERY)
        print(res)
    

    def GetUser(self, cpf) -> None:
        
        SQL_QUERY = f'''
            SELECT *
            FROM user as u
            WHERE u.cpf = '{cpf}'
        '''
        user = self.__execute__(SQL_QUERY)
        return user
        

    def __GetBillByDate__(self, credit_card_id: int, date: date):
        GET_CURRENT_BILL = f'''
                select id
                from bill b
                where b.month_year = "{str(date.month) + '/' + str(date.year)}"
                and b.id_credit_card = "{str(credit_card_id)}"
            '''
        
        current_bill = self.__execute__(GET_CURRENT_BILL)

        if len(current_bill) == 0:
            CREATE_BILL = f'''
                insert into bill (month_year, id_credit_card)
                values ("{str(date.month) + '/' + str(date.year)}", "{str(credit_card_id)}")        
                returning id
            '''
            current_bill = self.__execute__(CREATE_BILL)
        
        current_bill, = current_bill[0]
        return current_bill

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

                record = self.cursor.fetchall()
                
                self.sqliteConnection.commit()
                
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
    
    