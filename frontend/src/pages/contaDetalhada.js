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

function ContaDetalhada(){
    const date = new Date();
    const user = {'user_id': "15899451742"}

    const [select, setSelect] = useState();
    const [mes, setMes] = useState(date.getMonth() + 1);
    const [despesas, setDespesa] = useState([])

    const [receitas, setReceita] = useState([])


    const incomes = () => {
        return api.post('/income/'+ user.user_id, {
            'initial_date': '2023-'+ (mes) + '-01',
            'end_date': '2023-'+ (mes+1) + '-01'
        
        }).then((res) => {
                setReceita(res.data.Incomes);
        }).catch((err) => {
            console.error(err);
        })
    }

    const expenses = () => {
        return api.post('/expense/' + user.user_id, {
            'initial_date': '2023-'+ (mes) + '-01',
            'end_date': '2023-'+ (mes+1) + '-01'
        
        }).then((res) => {
                setDespesa(res.data.Expenses);
        }).catch((err) => {
            console.error(err);
        })
    } 

    useEffect(() => {
        
        expenses();
        incomes();
        console.log(receitas)
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