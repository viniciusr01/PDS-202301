import "./insertTransaction.css";
import "./globalPopUp.css";
import "./createAccount.css"
import { CheckBox } from "@mui/icons-material";
import { useState, useEffect } from "react";
import api from "../../services/api"

function CreateAccount({ display, setDisplay }){
    const [valor, setValor] = useState("");
    const [data, setData] = useState("");
    
    const [fontePagamento, setFontePagamento] = useState("")
    const [categoria, setCategoria] = useState("")
    const [check, setCheck] = useState(false)



    const [nome, setNome] = useState("");
    const [descricao, setDescricao] = useState("");

    const handleCheck = () => {
        check ? setCheck(false) : setCheck(true);
    }

    // const criaConta = ({
    //     valor,
    //     data,
    //     descricao,
    //     fontePagamento,
    //     categoria
    // }) => {
    //     api.post('/transaction', {
    //         "user":{
    //             "cpf": JSON.parse(localStorage.user).user_id
    //         },
    //         "transaction": {
    //             "description": descricao,
    //             "value": valor,
    //             "reference_date": data,
    //             "id_category": categoria,
    //             "type": ""
    //         }

    //     }).then((res) => {
    //         window.location.reload();
    //     }).catch((err) => {
    //         console.error(err);
    //     })
    // }

    function criaConta (valor, data, descricao, fontePagamento, categoria){
        console.log(valor, data, descricao, fontePagamento, categoria)

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
                            <input className="pop_up_input" placeholder="Cor"></input>
                        </div>
                        <div className="create_account_line_checkbox">
                            <p>É cartão de crédito?</p>
                            <input type="checkbox" checked={check} onChange = {handleCheck} color="#7A631D"/>
                        </div>
                        <input className="pop_up_input" placeholder="Saldo Inicial"></input>
                    </div>
                    <div className="pop_up_button_group">
                        <button className="botao_voltar" onClick={() => setDisplay('none')}>Voltar</button>
                        <button className="botao_confirmar" onClick={()=>criaConta(
                            valor,
                            data,
                            descricao,
                            fontePagamento,
                            categoria
                        )}>Criar</button>
                    </div>

                </div>
            </div>
        </div>
    )
}

export default CreateAccount;