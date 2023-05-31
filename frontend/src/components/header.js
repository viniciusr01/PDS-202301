import "./header.css"

import logo from '../img/logo.svg'
import { useNavigate } from "react-router-dom";


function Header(){
    let navigate = useNavigate(); 

    return(
    <div>
        <div className="header_container">
            <img onClick={() => navigate("/main")} className="header_logo" src={logo}></img>
        </div>
    </div>
    )
}

export default Header;