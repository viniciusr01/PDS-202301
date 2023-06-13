<div align="center">
  
<p>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Logo_UFMG.png/320px-Logo_UFMG.png" alt="alt text" width="210" height="82">
</p>

<p> <h2> MoneyHive BackEnd - Documentação </h2> </p>

  
| [Arquitetura](#Arquitetura) | [Adapters e Portas](#Adapters e Portas) | [Exemplos de Codigo](#Exemplos de Codigo) | [Features](#features) |
| - | - | - | - |
</div>

# MoneyHive


## Arquitetura
A primeira camada da Arquitetura que comunica com o cliente, é a camada de blueprint, ela funciona como um controller validando as informações passadas. Após as informações validadas através de uma injeção de depedência, o blueprint chama o service que irá executar a funcionalidade. Essa injeção de depedência é feita passando o construtor do adapter que será utilizado dentro do service como argumento do construtor do próprio service. Dentro do service, não há conhecimento da implementação da interface a qual ele se relaciona, apenas dos métodos que existem nela. 


## Adapters e Portas
Adapters: camada do blueprint, SQLadapter.
Portas: ISQL, TransactionFacturies, CategoryFactories, além de DTOs utilizados para apresentar a resposta para o cliente: RetrieveExpensesDTO, RetrieveExtractDTO, RettrieveIncomesDTO, TransactionDTO, RetrieveUseAccountDTO.



## Exemplos de Codigo
```python

transaction.route('/', methods = ['POST'])
@cross_origin()
def CreateTransaction():
    try:
        if request.headers['Content-Type'] != 'application/json':
                current_app.logger.debug(request.headers['Content-Type'])
                return jsonify(msg=('Header Error'))

        data = request.get_json()

        return jsonify(MakeTransaction(SqlAdapter()).make(TransactionFactory().make(obj=data['transaction'])))


    except TypeError as e:
        return jsonify(str(e)), 400
         

    except Exception as e:
        print(e.with_traceback, e.args)
        return "An internal error occurred. Please, try again later.", 500
```

```python
class MakeTransaction:
    def _init_(self, db: ISql) -> None:
        self.db = db

    def make(self, transaction: Transaction) -> str:
        if transaction.type == TransactionType.Expense: # type: ignore
            print("Adding an expense... ")
            for i in range(0, transaction.number_of_installments): # type: ignore
                print("Adding an expense installment")
                self.db.AddExpense({
                    "description": transaction.description + f" {i + 1}/{transaction.number_of_installments}", #type: ignore
                    "value": transaction.value / transaction.number_of_installments, # type: ignore
                    "reference_date": transaction.reference_date + relativedelta(months=i),
                    "id_account": transaction.id_account,  # type: ignore
                    "id_category": transaction.id_category,
                    "id_credit_card": transaction.id_credit_card, # type: ignore
                    "is_recurrency": transaction.is_recurrency, # type: ignore
                    "end_date": transaction.end_date # type: ignore
                })
                print("installment added.")

            return "The expense was successfully added."

        if transaction.type == TransactionType.Income: # type: ignore
            print("Adding an income... ")
            self.db.AddIncome({
                "description": transaction.description, 
                "value": transaction.value, 
                "reference_date": transaction.reference_date,
                "id_category": transaction.id_category,
                "id_account": transaction.id_account #type: ignore
            })
        
            return "The income was successfully added."
        
        raise Exception("Something went wrong...")
        
```
