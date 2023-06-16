import "./insertTransaction.css";
import "./globalPopUp.css";
import { useState, useEffect } from "react";
import api from "../../services/api"


function InsertTransaction({ display, setDisplay, type, setType, setUpdate, fontesDePagamento, user, categories}){
    const [valor, setValor] = useState(0.0);
    const [data, setData] = useState("");
    const [descricao, setDescricao] = useState("");
    const [fontePagamento, setFontePagamento] = useState(fontesDePagamento[0]?.Id)
    const [categoria, setCategoria] = useState('')

    const criaTransacao = () => {
        console.log(
            {
                "user":{
                    "cpf": user.user_id
                },
                "transaction": {
                    "description": descricao,
                    "value": parseFloat(valor),
                    "reference_date": data,
                    "id_account": fontePagamento,
                    "id_category": categoria,
                    "type":  type == 'despesa' ? 2 : 1,
                    "expense_type": 1
            }}
        )

        setUpdate(true)

        api.post('/transaction/', {
            "user":{
                "cpf": user.user_id
            },
            "transaction": {
                "description": descricao,
                "value": valor,
                "reference_date": data,
                "id_account": fontePagamento,
                "id_category": categoria,
                "type":  type == 'despesa' ? 2 : 1,
                "expense_type": 1
            }}).then((res) => {
                console.log(res)
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
                        <input type="text" className="pop_up_input" placeholder="R$0.00" 
                            onChange={(e)=>{
                                setValor(e.target.value)                                
                                }}/>
                        <input className="pop_up_input" placeholder="Data"
                            onChange={(e)=>{setData(e.target.value)}}/>
                        <input className="pop_up_input" placeholder="Descrição"
                            onChange={(e)=>{setDescricao(e.target.value)}}/>
                        <div className="grid pop_up_input_group_line">
                            <select className="pop_up_input" placeholder="Fonte de Pagamento"
                                onChange={(e)=>{setFontePagamento(e.target.value)}}>
                                    {fontesDePagamento.map( e => {
                                        return(
                                            <option  key={e.Id} value={e.Id}>{e.Name}</option>
                                        )
                                     
                                    })}
                            
                            </select>
                            <select cypress_teste='placeCategory' className="pop_up_input" placeholder="Categoria"
                                onChange={(e)=>{setCategoria(e.target.value)}}>
                                    {categories.map( e => {
                                        return(
                                            <option key={e.Id} value={e.Id}>{e.Name}</option>
                                        )
                                    
                                    })}
                            
                            </select>
                        </div>
                    </div>
                    <div className="pop_up_button_group">
                        <button className="botao_voltar" onClick={() => setDisplay('none')}>Voltar</button>
                        <button className="botao_confirmar" onClick={() => criaTransacao()}>Criar</button>
                    </div>

                </div>
            </div>
        </div>
        
    )
}

export default InsertTransaction;