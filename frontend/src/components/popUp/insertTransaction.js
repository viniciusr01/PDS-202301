import "./insertTransaction.css";
import "./globalPopUp.css";
import { useState } from "react";


function InsertTransaction(){
    const[select, setSelect] = useState("despesa")
    return(
        <div className="grid pop_up_container">
            <select className="insert_transaction_select" value={select} onChange={(e) => setSelect(e.target.value)}>
                <option value="despesa">Despesa</option>
                <option value="receita">Receita</option>
            </select>

            <div className="grid insert_transaction_input_group">
                <input className="pop_up_input" placeholder="R$0.00"></input>
                <input className="pop_up_input" placeholder="Data"></input>
                <input className="pop_up_input" placeholder="Descrição"></input>
                <div className="grid pop_up_input_group_line

">
                    <input className="pop_up_input" placeholder="Fonte de Pagamento"></input>
                    <input className="pop_up_input" placeholder="Categoria"></input>
                </div>
            </div>
            <div className="pop_up_button_group">
                <button className="botao_voltar">Voltar</button>
                <button className="botao_confirmar">Criar</button>
            </div>

        </div>
    )
}

export default InsertTransaction;