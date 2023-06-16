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
    const [balance, setBalance] = useState();
    const [incomes, setIncomes] = useState([]);
    const [expenses, setExpenses] = useState([]);
    const [dataGraphBar, setDataGraphBar] = useState([]);
    const [dataGraphCircle, setDataGraphCircle] = useState([]);
    const [fontesDePagamento, setFontesDePagamento] = useState([]);
    const [categories, setCategories] = useState([]);
    const [user, setUser] = useState();
    const [update, setUpdate] = useState(true);
    const queryParameters = new URLSearchParams(window.location.search)
    
    useEffect(()=>{
        var incomesAux = []
        var expensesAux = []

        if(update == false){
            incomesAux = JSON.parse(localStorage.getItem('incomes'))
            expensesAux = JSON.parse(localStorage.getItem('expenses'))

            setIncomes(incomesAux.reduce(
                (acc, currentValue) => acc + currentValue?.Value, 0
                ))
            setExpenses(expensesAux.reduce(
                (acc, currentValue) => acc + currentValue?.Value, 0
                ))

        } else {
            console.log("Buscando parâmetros do usuário no back...")
            const cpf = queryParameters.get("cpf") ? queryParameters.get("cpf") : localStorage.getItem("cpf") 
            
            setUser(cpf)
            localStorage.setItem("cpf", cpf)
    
            axios.get(`http://localhost:8000/user/${cpf}`)
                .then(info => {

                    console.log(info.data)

                    localStorage.setItem("name",info.data.User.name)
                    localStorage.setItem("email",info.data.User.email)
                    localStorage.setItem("accounts",JSON.stringify(info.data.Accounts))
                    localStorage.setItem("incomes",JSON.stringify(info.data.Incomes))
                    localStorage.setItem("expenses",JSON.stringify(info.data.Expenses))
                    localStorage.setItem("categories",JSON.stringify(info.data.Categories))
    
                    incomesAux = info.data.Incomes
                    expensesAux = info.data.Expenses
                    
                    setFontesDePagamento(info.data.Accounts);
                    setCategories(info.data.Categories);

                    setIncomes(incomesAux.reduce(
                        (acc, currentValue) => acc + currentValue?.Value, 0
                        ))
                    setExpenses(expensesAux.reduce(
                        (acc, currentValue) => acc + currentValue?.Value, 0
                        ))
                }
                
                ) 
            }
            


            setUpdate(false)
             
    }, [])

    useEffect(()=> {
        setBalance(incomes - expenses)
        setDataGraphBar(
            [
                {
                    'Receita': incomes,
                    'Despesa': expenses
                }
            ]
        )

        const incomesAux = JSON.parse(localStorage.getItem('incomes'))
        const expensesAux = JSON.parse(localStorage.getItem('expenses'))

        // TODO: CORRIGIR NAME DE CADA UM
        setDataGraphCircle({
            "Expenses": expensesAux.map((e) => e.Id_category).map((e) => ({
                'name': e,
                'value': expensesAux.filter((income) => income.Id_category === e).reduce((acc, currentValue) => acc + currentValue.Value, 0)
            })),
            
            "Incomes": incomesAux.map((e) => e.Id_category).map((e) => ({
                'name': e,
                'value': incomesAux.filter((income) => income.Id_category === e).reduce((acc, currentValue) => acc + currentValue.Value, 0)
            }))
        })

        // console.log(dataGraphCircle)
        // console.log(categories.find((category) => category.Id == 11)?.Name)


    }, [incomes, expenses])

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
            <InserTransaction display={ modalTransacao } setDisplay={setModalTransacao} type={modalType} setType={setModalType} setUpdate={setUpdate} fontesDePagamento={fontesDePagamento} user={user} categories={categories}/>
            <CreateAccount display={ modalConta } setDisplay={setModalConta} user={user}/>
            <CreateCategory display={ modalCategory } setDisplay={setModalCategory} user={user}/>
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
                            <p>R$ {balance}</p>
                        </div>
                        <div className='flex shadow principal_card_menor' onClick={() => navigate("/account")}>
                            <h5>Receitas <ArrowForwardIosIcon/> </h5>
                            <p>R$ {incomes}</p>
                        </div>
                        <div className='flex shadow principal_card_menor' onClick={() => navigate("/account")}>
                            <h5>Despesas <ArrowForwardIosIcon/> </h5>
                            <p>R$ {expenses}</p>
                        </div>
                        <div className='flex shadow principal_card_menor' onClick={() => navigate("/account")}>
                            <h5>Balanço <ArrowForwardIosIcon/> </h5>
                            <p>R$ {balance}</p>
                        </div>
                    </div>
                    <div>
                        <div className='grid principal_cards_maiores'>
                            <div>
                                <h5>Despesas por categoria</h5>
                                <div className='shadow principal_card_maior'>
                                    <div className='flex principal_card_maior_detalhes'>
                                        <PieChart width={300} height={250}>
                                            <Pie data={dataGraphCircle.Expenses} dataKey="value" nameKey="name" cx="50%" cy="50%" innerRadius={60} outerRadius={80} fill="#F7BC0A" label />
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
                                            <Pie data={dataGraphCircle.Incomes} dataKey="value" nameKey="name" cx="50%" cy="50%" innerRadius={60} outerRadius={80} fill="#F7BC0A" label />
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
                            <BarChart width={300} height={200} data={dataGraphBar}>
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
                                    <p style={{"color": "#428D2F"}}>R$ {dataGraphBar[0]?.Receita}</p>
                                </div>
                                <div className='flex principal_card_extendido_infos_texto_linha'>
                                    <h5>Despeas</h5>
                                    <p style={{"color": "#BA0000"}}>R$ {dataGraphBar[0]?.Despesa}</p>
                                </div>
                                <div className='flex principal_card_extendido_infos_texto_linha'>
                                    <h5>Balanço</h5>
                                    <p >R$ {dataGraphBar[0]?.Receita - dataGraphBar[0]?.Despesa}</p>
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