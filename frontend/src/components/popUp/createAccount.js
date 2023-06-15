import "./insertTransaction.css";
import "./globalPopUp.css";
import "./createAccount.css"
import { CheckBox } from "@mui/icons-material";
import { useState, useEffect } from "react";
import api from "../../services/api"

function CreateAccount({ display, setDisplay, user }){
    const [check, setCheck] = useState(false)
    const [cor, setCor] = useState("");
    const [taxa, setTaxa] = useState(0);
    const [saldo, setSaldo] = useState(0);
    const [nome, setNome] = useState("");
    const [descricao, setDescricao] = useState("");

    const handleCheck = () => {
        check ? setCheck(false) : setCheck(true);
    }

    function criaConta (nome, descricao, cor, taxa, user){
        api.post(
            `/account/`, {
                headers: {
                    'Content-Type': "application/json"
                },
                data:{
                    'name': nome,
                    'description': descricao,
                    'color': cor,
                    'fees': taxa,
                    'user_cpf': user
                }
            }
            ).then(info => {
                console.log(info)
                const conta = info
                if(saldo != 0){
                    const date = new Date()
                    api.post('/transaction/', {
                        "user":{
                            "cpf": user
                        },
                        "transaction": {
                            "description": "Correção de Saldo Inicial",
                            "value": saldo,
                            "reference_date": date.getFullYear() + '-' + date.getMonth() + '-' + date.getDay(),
                            "id_account": conta,
                            "id_category": 1, // TODO CORRIGIR CATEGORIA
                            "type":  2,
                            "expense_type": 1
                        }}).then((res) => {
                            console.log(res)
                        window.location.reload();
                    }).catch((err) => {
                        console.error(err);
                    })
                }
        })


    }

    return(
        <div className="block insert_transaction_modal" style={{ 'display': display }}>
            <div className="flex insert_transaction_center">
                <div className="grid pop_up_container">
                    <div className="create_account_title"><h1>Criar Conta</h1></div>
                    <div className="grid create_account_input_group">
                        <input className="pop_up_input" placeholder="Nome" onChange={(e)=>setNome(e.target.value)}></input>
                        <div className="grid pop_up_input_group_line">
                            <input className="pop_up_input" placeholder="Descrição Opcional" onChange={(e)=>setDescricao(e.target.value)}></input>
                            <input className="pop_up_input" placeholder="Cor" onChange={(e)=>setCor(e.target.value)}></input>
                        </div>
                        <div className="create_account_line_checkbox">
                            <p>É cartão de crédito?</p>
                            <input type="checkbox" checked={check} onChange = {handleCheck} color="#7A631D"/>
                        </div>
                        <input className="pop_up_input" placeholder="Saldo Inicial" onChange={(e)=>setSaldo(e.target.value)}></input>
                    </div>
                    <div className="pop_up_button_group">
                        <button className="botao_voltar" onClick={() => setDisplay('none')}>Voltar</button>
                        <button className="botao_confirmar" onClick={()=>criaConta(
                            nome,
                            descricao,
                            cor,
                            taxa,
                            user,
                            saldo
                        )}>Criar</button>
                    </div>

                </div>
            </div>
        </div>
    )
}

export default CreateAccount;