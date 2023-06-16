import "./insertTransaction.css";
import "./globalPopUp.css";
import "./createAccount.css"
import { useState, useEffect } from "react";


function CreateCategory({ display, setDisplay }){
    const [nome, setNome] = useState("");
    const [descricao, setDescricao] = useState("");
    const [cor, setCor] = useState("");


    const user = JSON.parse(localStorage.getItem('cpf'));

    function criaCategoria(nome, descricao, cor){


       const dataToSend = {
            "category":
            {
                "name": nome,
                "user_cpf": user,
                "description": descricao, 
                "color": cor
            }
       }

       fetch('http://localhost:8000/category/',{
            method:'POST',
            headers:{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dataToSend),
       })
       .then( res =>  window.location.reload())
       .catch((err) => {
            console.error(err);
       })
    }

    return(
        <div className="block insert_transaction_modal" style={{ 'display': display }}>
            <div className="flex insert_transaction_center">
                <div className="grid pop_up_container">
                    <div className="create_account_title"><h1>Criar Categoria</h1></div>
                    <div className="grid create_account_input_group">
                        <input cypress_teste='nome' className="pop_up_input" placeholder="Nome" onChange={(e)=>setNome(e.target.value)}></input>
                        <input cypress_teste='descricao'className="pop_up_input" placeholder="Descrição (Opcional)"onChange={(e)=>setDescricao(e.target.value)}></input>
                        <input cypress_teste='cor' className="pop_up_input" placeholder="Cor" onChange={(e)=>setCor(e.target.value)}></input>
                    </div>
                    <div className="pop_up_button_group">
                        <button className="botao_voltar" onClick={() => setDisplay('none')}>Voltar</button>
                        <button cypress_teste='buttonConfirmar' className="botao_confirmar" onClick={() => criaCategoria(nome, descricao, cor)}>Criar</button>
                    </div>

                </div>
            </div>
        </div>
    )

}

export default CreateCategory;