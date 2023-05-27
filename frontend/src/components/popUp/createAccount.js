import "./insertTransaction.css";
import "./globalPopUp.css";
import "./createAccount.css"
import { CheckBox } from "@mui/icons-material";

function CreateAccount(){
    return(
        <div className="grid pop_up_container">
            <div className="create_account_title"><h1>Criar Conta</h1></div>
            <div className="grid create_account_input_group">
                <input className="pop_up_input" placeholder="Nome"></input>
                <div className="grid pop_up_input_group_line

">
                    <input className="pop_up_input" placeholder="Descrição Opcional"></input>
                    <input className="pop_up_input" placeholder="Cor"></input>
                </div>
                <div className="create_account_line_checkbox">
                    É cartão de crédito?
                    <CheckBox/>
                </div>
                <input className="pop_up_input" placeholder="Saldo Inicial"></input>
            </div>
            <div className="pop_up_button_group">
                <button className="botao_voltar">Voltar</button>
                <button className="botao_confirmar">Criar</button>
            </div>

        </div>
    )
}

export default CreateAccount;