import "./header.css"

import logo from '../img/logo.svg'
import { redirect } from "react-router-dom";


function Header(){
    return(
    <div>
        <div className="header_container">
            <img onClick={()=> redirect("/main")} className="header_logo" src={logo}></img>
        </div>
    </div>
    )
}

export default Header;