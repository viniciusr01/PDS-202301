import "./insertTransaction.css";
import "./globalPopUp.css";
import { useState, useEffect } from "react";
import api from "../../services/api"


function InsertTransaction({ display, setDisplay, type, setType }){
    const fontesDePagamento = [
        {
            "name": "Santander",
            "id": "1",
            "color": "#FFFFFF"
        },
        {
            "name": "Nubank",
            "id": "2",
            "color": "#FFFFFF"
        },
        {
            "name": "Cartao Nu",
            "id": "3",
            "color": "#FFFFFF"
        }
    ]

    const categorias = [
        {
            "name": "Lazer",
            "id": "1",
            "color": "#FFFFFF"
        },
        {
            "name": "Saúde",
            "id": "2",
            "color": "#FFFFFF"
        },
        {
            "name": "Compras",
            "id": "3",
            "color": "#FFFFFF"
        }
    ]
    const [valor, setValor] = useState("");
    const [data, setData] = useState("");
    const [descricao, setDescricao] = useState("");
    const [fontePagamento, setFontePagamento] = useState(fontesDePagamento[0].id)
    const [categoria, setCategoria] = useState(categorias[0].id)

    // const user = JSON.parse(localStorage.user)
    const user = {"user_id": "15899451742"}

    const criaTransacao = () => {
        console.log(
            {
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
            }}
        )


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
                                console.log(valor)
                                
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
                                            <option value={e.id}>{e.name}</option>
                                        )
                                     
                                    })}
                            
                            </select>
                            <select className="pop_up_input" placeholder="Categoria"
                                onChange={(e)=>{setCategoria(e.target.value)}}>
                                    {categorias.map( e => {
                                        return(
                                            <option value={e.id}>{e.name}</option>
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