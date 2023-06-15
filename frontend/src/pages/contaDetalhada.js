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

    const [select, setSelect] = useState();
    const [mes, setMes] = useState(date.getMonth() + 1);


    const receitas  = JSON.parse(localStorage.getItem('incomes'))
    const despesas = JSON.parse(localStorage.getItem('expenses'))
    const accounts = JSON.parse(localStorage.getItem('accounts'))
    const categories = JSON.parse(localStorage.getItem('categories'))


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

    receitas.forEach(element => {
        console.log(accounts)
        console.log(categories.find((category) => category.Id == element.Id_category)?.Name) 
    })

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
                                    <p>{e.Reference_date}</p>    
                                    <p>{e.Description}</p>    
                                    <p>{accounts.find((account) => account.Id == e.Id_account).Name}</p>    
                                    <p>{categories.find((category) => category.Id == e.Id_category)?.Name}</p>    
                                    <p>{e.Value}</p>    
                                </div> )
                            }
                        )
                        :
                        despesas.map(
                            e => { return(
                            <div className="conta_detalhada_linha">
                                <p>{e.Reference_date}</p>    
                                <p>{e.Description}</p>    
                                <p>{accounts.find((account) => account.Id == e.Id_account).Name}</p>    
                                <p>{categories.find((category) => category.Id == e.Id_category)?.Name}</p>    
                                <p>{e.Value}</p>    
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