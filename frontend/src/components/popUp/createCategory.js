import "./insertTransaction.css";
import "./globalPopUp.css";
import "./createAccount.css"
import { useState, useEffect } from "react";
import api from "../../services/api"

function CreateCategory({ display, setDisplay }){
    const [nome, setNome] = useState("");
    const [descricao, setDescricao] = useState("");
    const [cor, setCor] = useState("");

    const user = {'user_id': '15899451742'}

    // const user = JSON.parse(localStorage.getItem('user'));

    const criaCategoria = ({
        nome,
        descricao,
        cor
    }) => {
        api.post('/category', {
            user_id: user.user_id,
            descricao,
            nome,
            cor
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
                    <div className="create_account_title"><h1>Criar Categoria</h1></div>
                    <div className="grid create_account_input_group">
                        <input className="pop_up_input" placeholder="Nome" onChange={(e)=>setNome(e.target.value)}></input>
                        <input className="pop_up_input" placeholder="Descrição (Opcional)"onChange={(e)=>setDescricao(e.target.value)}></input>
                        <input className="pop_up_input" placeholder="Cor" onChange={(e)=>setCor(e.target.value)}></input>
                    </div>
                    <div className="pop_up_button_group">
                        <button className="botao_voltar" onClick={() => setDisplay('none')}>Voltar</button>
                        <button className="botao_confirmar" onClick={criaCategoria({nome, descricao, cor})}>Criar</button>
                    </div>

                </div>
            </div>
        </div>
    )

}

export default CreateCategory;