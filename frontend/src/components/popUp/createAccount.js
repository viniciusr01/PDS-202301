import "./insertTransaction.css";
import "./globalPopUp.css";
import "./createAccount.css"
import { CheckBox } from "@mui/icons-material";
import { useState, useEffect } from "react";
import api from "../../services/api"

function CreateAccount({ display, setDisplay }){
    const [valor, setValor] = useState("");
    const [data, setData] = useState("");
    const [descricao, setDescricao] = useState("");
    const [fontePagamento, setFontePagamento] = useState("")
    const [categoria, setCategoria] = useState("")
    const criaConta = ({
        valor,
        data,
        descricao,
        fontePagamento,
        categoria
    }) => {
        api.post('/transaction', {
            user_id: JSON.parse(localStorage.user).user_id,
            valor,
            data,
            descricao,
            fontePagamento,
            categoria
        }).then((res) => {
            window.location.reload();
        }).catch((err) => {
            console.error(err);
        })
    }

    return(
        <div className="block insert_transaction_modal" style={{ 'display': display }}>
            <div className="flex insert_transaction_center">
                <div className="grid pop_up_container">
                    <div className="create_account_title"><h1>Criar Conta</h1></div>
                    <div className="grid create_account_input_group">
                        <input className="pop_up_input" placeholder="Nome"></input>
                        <div className="grid pop_up_input_group_line

        ">
                            <input className="pop_up_input" placeholder="Descrição Opcional"></input>
                            <input className="pop_up_input" placeholder="Cor"></input>
                        </div>
                        <div className="create_account_line_checkbox">
                            É cartão de crédito?
                            <CheckBox/>
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