import "./insertTransaction.css";
import "./globalPopUp.css";
import { useState, useEffect } from "react";
import api from "../../services/api"


function InsertTransaction({ display, setDisplay, type, setType, setUpdate }){
    var fontes = JSON.parse(localStorage.getItem('accounts')?localStorage.getItem('accounts') : '[]');

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

    const [valor, setValor] = useState(0.0);
    const [data, setData] = useState("");
    const [descricao, setDescricao] = useState("");
    const [fontePagamento, setFontePagamento] = useState(fontesDePagamento[0].id)
    const [categoria, setCategoria] = useState('')

    const user = JSON.parse(localStorage.cpf)

    const [categorias, setCategorias] = useState([])


    useEffect(() => {

        fetch(`http://localhost:8000/category/${user}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        })
            .then((resp) => resp.json())
            .then((data) => {
                setCategorias(data.Categories)

            })
            .catch((error) => console.log(error))

    }, [])

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
                                    {fontes.map( e => {
                                        return(
                                            <option  key={e.Id} value={e.Id}>{e.Name}</option>
                                        )
                                     
                                    })}
                            
                            </select>
                            <select className="pop_up_input" placeholder="Categoria"
                                onChange={(e)=>{setCategoria(e.target.value)}}>
                                    {categorias.map( e => {
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