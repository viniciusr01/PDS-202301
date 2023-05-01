<div align="center">
  
<p>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Logo_UFMG.png/320px-Logo_UFMG.png" alt="alt text" width="210" height="82">
</p>

<p> <h2> MoneyHive BackEnd - Documentação </h2> </p>

  
| [Inicializar](#Inicializar) | [Serviços](#Serviços) | [Tecnologias](#tecnologias) | [Features](#features) |
| - | - | - | - |
</div>

# MoneyHive

## Inicializar
Para iniciar a aplicação deve-se seguir os seguintes passos:
1. Baixar as dependências presentes no arquivo backend/requirements.txt, através do comando:
```bash
pip install > /backend/requirements.txt
```
2. Iniciar o arquivo backend/app.py, através do comando:
```bash
python3 /backend/app.py
```

## Serviços
* **MakeTransaction:** Espera receber os dados de uma transação, seja ela de débito ou crédito, referente a uma conta ou a 
um cartão de crédito e salva esses dados no banco.
  * **Rota:** {base}/transaction/
  * **Header:** ['Content-Type']: 'application/json'  
  * **Body:** 
```json
{
    "user":{
        "cpf": "int"
    },
    "transaction": {
        "description": "str",
        "value": "float",
        "reference_date": "date xx/xx/xxxx",
        "id_category": "int",
        "type": "enum {Income = 1, Expense = 2}"
    }
}
```
