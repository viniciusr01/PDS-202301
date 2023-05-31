import "./contaDetalhada.css"
import Header from "../components/header";
import { useEffect, useState } from "react";

import ArrowBackIosIcon from '@mui/icons-material/ArrowBackIos';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';

import api from "../services/api";

const meses = [
    'JANEIRO',
    'FEVEREIRO',
    'MARÇO',
    'ABRIL',
    'MAIO',
    'JUNHO',
    'JULHO',
    'AGOSTO',
    'SETEMBRO',
    'OUTUBRO',
    'NOVEMBRO',
    'DEZEMBRO'
];

const transacoes = ()=>{
    return api.get('/transaction/', {
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
            return res;
    }).catch((err) => {
        console.error(err);
    })
} 

function ContaDetalhada(){
    const date = new Date();

    const [select, setSelect] = useState();
    const [mes, setMes] = useState(date.getMonth() + 1);
    const [despesas, setDespesa] = useState([
        {
            'Data': "18/12/2023",
            'Descrição': "Descrição válida",
            'Conta': 'Cartão de Crédito Nu',
            'Categoria': 'Lazer',
            'Valor': 'R$180,00'
        },
        {
            'Data': "18/12/2023",
            'Descrição': "Descrição válida",
            'Conta': 'Cartão de Crédito Nu',
            'Categoria': 'Lazer',
            'Valor': 'R$180,00'
        },
        {
            'Data': "18/12/2023",
            'Descrição': "Descrição válida",
            'Conta': 'Cartão de Crédito Nu',
            'Categoria': 'Lazer',
            'Valor': 'R$180,00'
        },
        {
            'Data': "18/12/2023",
            'Descrição': "Descrição válida",
            'Conta': 'Cartão de Crédito Nu',
            'Categoria': 'Lazer',
            'Valor': 'R$180,00'
        },
        {
            'Data': "18/12/2023",
            'Descrição': "Descrição válida",
            'Conta': 'Cartão de Crédito Nu',
            'Categoria': 'Lazer',
            'Valor': 'R$180,00'
        }
    ])

    const [receitas, setReceita] = useState([
        {
            'Data': "18/12/2023",
            'Descrição': "Descrição válida",
            'Conta': 'Santander',
            'Categoria': 'Lazer',
            'Valor': 'R$180,00'
        },
        {
            'Data': "18/12/2023",
            'Descrição': "Descrição válida",
            'Conta': 'Santander',
            'Categoria': 'Lazer',
            'Valor': 'R$180,00'
        },
        {
            'Data': "18/12/2023",
            'Descrição': "Descrição válida",
            'Conta': 'Santander',
            'Categoria': 'Lazer',
            'Valor': 'R$180,00'
        },
        {
            'Data': "18/12/2023",
            'Descrição': "Descrição válida",
            'Conta': 'Santander',
            'Categoria': 'Lazer',
            'Valor': 'R$180,00'
        },
        {
            'Data': "18/12/2023",
            'Descrição': "Descrição válida",
            'Conta': 'Santander',
            'Categoria': 'Lazer',
            'Valor': 'R$180,00'
        }
    ])

    useEffect(() => {
        // TODO: Conferir a rota e requisição
        api
          .get("/extract")
          .then((response) =>{
            setDespesa(response.data.despesas)
            setReceita(response.data.receitas)
            })
          .catch((err) => {
            console.error("ops! ocorreu um erro" + err);
          });
      }, [mes]);

    function handleMesAnterior(){
        if (mes == 0)
            setMes(11); 

        else
            setMes(mes - 1);
    } 
    
    function handleMesSucessor(){
        if(mes == 11)
            setMes(0);

        else 
            setMes(mes + 1);
    } 

    return(
        <div className="conta_detalhada_container">
            <Header />
            <div className="conta_detalhada_bloco_principal">
                <div></div>
                <div>
                    <select className="conta_detalhada_select" value={select} onChange={(e) => setSelect(e.target.value)}>
                        <option value="despesa">Despesa</option>
                        <option value="receita">Receita</option>
                    </select>

                    <div className="conta_detalhada_fatura">
                        <div className="conta_detalhada_linha">
                            <div></div>
                            <div></div>
                            <div className="conta_detalhada_fatura_titulo">
                                <button onClick={ () => handleMesAnterior()}>
                                    <ArrowBackIosIcon/>
                                </button>
                                <h5>{meses[mes]}</h5>
                                <button onClick={ () => handleMesSucessor()}>
                                    <ArrowForwardIosIcon/>
                                </button>
                            </div>
                            <div></div>
                            <div></div>
                        </div>
                        <div className="conta_detalhada_linha">
                            <h5>DATA</h5>
                            <h5>DESCRIÇÃO</h5>
                            <h5>CONTA</h5>
                            <h5>CATEGORIA</h5>
                            <h5>VALOR</h5>
                        </div>

                        {
                        select == 'receita'?
                        receitas.map(
                            e => { return(
                                <div className="conta_detalhada_linha">
                                    <p>{e.Data}</p>    
                                    <p>{e.Descrição}</p>    
                                    <p>{e.Conta}</p>    
                                    <p>{e.Categoria}</p>    
                                    <p>{e.Valor}</p>    
                                </div> )
                            }
                        )
                        :
                        despesas.map(
                            e => { return(
                            <div className="conta_detalhada_linha">
                                <p>{e.Data}</p>    
                                <p>{e.Descrição}</p>    
                                <p>{e.Conta}</p>    
                                <p>{e.Categoria}</p>    
                                <p>{e.Valor}</p>    
                            </div> )
                        })}
                    </div>

                </div>


                <div></div>

            </div>

        </div>
    )
}

export default ContaDetalhada;