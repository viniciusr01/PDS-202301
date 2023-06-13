import './principal.css'
import axios from 'axios';


import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';

import InserTransaction from '../components/popUp/insertTransaction';
import CreateAccount from '../components/popUp/createAccount';
import CreateCategory from '../components/popUp/createCategory';

import Header from '../components/header';
import { PieChart, Pie, BarChart, CartesianGrid, XAxis, YAxis, Tooltip, Legend, Bar} from 'recharts';
import { useState, useEffect } from 'react';
import { useNavigate } from "react-router-dom";


function Principal(){

    const queryParameters = new URLSearchParams(window.location.search)
    
    if(queryParameters.get("cpf")){
        const cpf = queryParameters.get("cpf")
        localStorage.setItem("cpf",cpf)

        axios.get(`http://localhost:8000/user/${cpf}`)
        .then(info => {
                localStorage.setItem("name",info.data.User.name)
                localStorage.setItem("email",info.data.User.email)
                localStorage.setItem("accounts",info.data.Accounts)
            }
        )      
    }
    

    const data = [
        {
            'Receita': 2000,
            'Despesa': 1000
        }
    ]

    const user_accounts = {
        'saldo': 1000,
        'balanco': 1000,
        'receitas': 2000,
        'despesas': 1000
    }

    const data02 = [
        {
            'name': 'Lazer',
            'value': 300
        },
        {
            'name': 'Farmácia',
            'value': 50
        },
        {
            'name': 'Shopping',
            'value': 500
        }
    ]

    const criaModalDespesa = () => {
        setModalType('despesa');
        setModalTransacao('inline')
    }
    const criaModalReceita = () => {
        setModalType('receita');
        setModalTransacao('inline')
    }

    const [modalTransacao, setModalTransacao] = useState('none');
    const [modalConta, setModalConta] = useState('none');
    const [modalCategory, setModalCategory] = useState('none');
    const [modalType, setModalType] = useState('despesa');
    let navigate = useNavigate(); 

    return (
        <div className='grid principal_container'>
            <Header/>
            <InserTransaction display={ modalTransacao } setDisplay={setModalTransacao} type={modalType} setType={setModalType}/>
            <CreateAccount display={ modalConta } setDisplay={setModalConta}/>
            <CreateCategory display={ modalCategory } setDisplay={setModalCategory}/>
            <div className='grid principal_bloco_principal'>                
                <div></div>
                <div className='grid principal_bloco_principal_container'>
                    <div className='flex principal_botoes'>
                        <button className='botao_receita_despesa' onClick={criaModalReceita}>+Receita</button>
                        <button className='botao_receita_despesa' onClick={criaModalDespesa}>+Despesa</button>
                        <button className='botao_receita_despesa' onClick={() => setModalConta('inline')}>+Conta</button>
                        <button className='botao_receita_despesa' onClick={() => setModalCategory('inline')}>+Categoria</button>
                    </div>
                    <div className='grid principal_cards_menores'>
                        <div className='flex shadow principal_card_menor' onClick={() => navigate("/account")}>
                            <h5>Saldo Atual <ArrowForwardIosIcon/> </h5>
                            <p>{user_accounts.saldo}</p>
                        </div>
                        <div className='flex shadow principal_card_menor' onClick={() => navigate("/account")}>
                            <h5>Receitas <ArrowForwardIosIcon/> </h5>
                            <p>{user_accounts.receitas}</p>
                        </div>
                        <div className='flex shadow principal_card_menor' onClick={() => navigate("/account")}>
                            <h5>Despesas <ArrowForwardIosIcon/> </h5>
                            <p>{user_accounts.despesas}</p>
                        </div>
                        <div className='flex shadow principal_card_menor' onClick={() => navigate("/account")}>
                            <h5>Balanço <ArrowForwardIosIcon/> </h5>
                            <p>{user_accounts.balanco}</p>
                        </div>
                    </div>
                    <div>
                        <div className='grid principal_cards_maiores'>
                            <div>
                                <h5>Despesas por categoria</h5>
                                <div className='shadow principal_card_maior'>
                                    <div className='flex principal_card_maior_detalhes'>
                                        <PieChart width={300} height={250}>
                                            <Pie data={data02} dataKey="value" nameKey="name" cx="50%" cy="50%" innerRadius={60} outerRadius={80} fill="#F7BC0A" label />
                                        </PieChart>
                                        <p  onClick={() => navigate("/account")}>VER MAIS</p>
                                    </div>
                                </div>
                            </div>
                            <div>
                                <h5>Receitas por categoria</h5>
                                <div className='shadow principal_card_maior'>
                                    <div className='flex principal_card_maior_detalhes'>
                                        <PieChart width={300} height={250}>
                                            <Pie data={data02} dataKey="value" nameKey="name" cx="50%" cy="50%" innerRadius={60} outerRadius={80} fill="#F7BC0A" label />
                                        </PieChart>
                                        <p  onClick={() => navigate("/account")}>VER MAIS</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className='principal_card_extendido'>
                        <h5>Balanço Mensal</h5>
                        <div className='grid shadow principal_card_extendido_infos'>
                            <BarChart width={300} height={200} data={data}>
                                <CartesianGrid strokeDasharray="3 3" />
                                <YAxis />
                                <Tooltip />
                                <Legend />
                                <Bar dataKey="Receita" fill="#428D2F" />
                                <Bar dataKey="Despesa" fill="#BA0000" />
                            </BarChart>
                            <div className='grid principal_card_extendido_infos_texto'>
                                <div className='flex principal_card_extendido_infos_texto_linha'>
                                    <h5>Receitas</h5>
                                    <p style={{"color": "#428D2F"}}>{data[0].Receita}</p>
                                </div>
                                <div className='flex principal_card_extendido_infos_texto_linha'>
                                    <h5>Despeas</h5>
                                    <p style={{"color": "#BA0000"}}>{data[0].Despesa}</p>
                                </div>
                                <div className='flex principal_card_extendido_infos_texto_linha'>
                                    <h5>Balanço</h5>
                                    <p >{data[0].Receita - data[0].Despesa}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div></div>

            </div>

        </div>
    )
}

export default Principal;