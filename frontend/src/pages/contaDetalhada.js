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
    const [ano, setAno] = useState(date.getFullYear());


    const [receitas, setReceitas]  = useState(JSON.parse(localStorage.getItem('incomes')))
    const [despesas, setDespesas] = useState(JSON.parse(localStorage.getItem('expenses')))
    const accounts = JSON.parse(localStorage.getItem('accounts'))
    const categories = JSON.parse(localStorage.getItem('categories'))
    const user = JSON.parse(localStorage.getItem('cpf'))

    useEffect(()=> {
        let mesAux = mes + 1
        let anoAux = ano
        
        if(mesAux == 13){
            mesAux = 1
            anoAux += 1
        }

        api.get(
            `/expense/${user}/${ano}-${mes}-01/${anoAux}-${mesAux}-01`
            ).then(info => {
            setDespesas(info.data.Expenses)
        })

        api.get(
            `/income/${user}/${ano}-${mes}-01/${anoAux}-${mesAux}-01`
            ).then(info => {
            setReceitas(info.data.Incomes)
        })
    }, [mes, ano])


    function handleMesAnterior(){
        if (mes == 1){
            setMes(12); 
            setAno(ano - 1);
        }
        
        else
            setMes(mes - 1);
    } 
    
    function handleMesSucessor(){
        if(mes == 12){
            setMes(1);
            setAno(ano + 1);
        }
        
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
                                <h5>{meses[mes - 1]}</h5>
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
                                    <p>R$ {e.Value}</p>    
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
                                <p>R$ {e.Value}</p>    
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