import "./insertTransaction.css";
import "./globalPopUp.css";
import { useState, useEffect } from "react";
import api from "../../services/api"


function InsertTransaction({ display, setDisplay, type, setType }){
    const [valor, setValor] = useState("");
    const [data, setData] = useState("");
    const [descricao, setDescricao] = useState("");
    const [fontePagamento, setFontePagamento] = useState("")
    const [categoria, setCategoria] = useState("")

    const criaTransacao = ({
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
            console.error(res);
            window.location.reload();
        }).catch((err) => {
            console.error(err);
        })
    }

    return(
        <div className="block insert_transaction_modal" style={{ 'display': display }}>
            <div className="flex insert_transaction_center">

                <div className="grid pop_up_container" >
                    <select className="insert_transaction_select" value={type} 
                        onChange={(e) => setType(e.target.value)}>
                        <option value="despesa">Despesa</option>
                        <option value="receita">Receita</option>
                    </select>

                    <div className="grid insert_transaction_input_group">
                        <input className="pop_up_input" placeholder="R$0.00" 
                            onChange={(e)=>{setValor(e.target.value)}}/>
                        <input className="pop_up_input" placeholder="Data"
                            onChange={(e)=>{setData(e.target.value)}}/>
                        <input className="pop_up_input" placeholder="Descrição"
                            onChange={(e)=>{setDescricao(e.target.value)}}/>
                        <div className="grid pop_up_input_group_line

        ">
                            <input className="pop_up_input" placeholder="Fonte de Pagamento"
                                onChange={(e)=>{setFontePagamento(e.target.value)}}/>
                            <input className="pop_up_input" placeholder="Categoria"
                                onChange={(e)=>{setCategoria(e.target.value)}}/>
                        </div>
                    </div>
                    <div className="pop_up_button_group">
                        <button className="botao_voltar" onClick={() => setDisplay('none')}>Voltar</button>
                        <button className="botao_confirmar" onClick={()=>criaTransacao(
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

export default InsertTransaction;