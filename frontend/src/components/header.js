import "./header.css"

import logo from '../img/logo.svg'
import { useNavigate } from "react-router-dom";
import LogoutIcon from '@mui/icons-material/Logout';


function Header(){
    let navigate = useNavigate(); 
    
    function logout(){
        localStorage.clear();
        navigate('/');
    }
    
    return(
    <div>
        <div className="header_container">
            <div></div>
            <div className="grid header_bloco_main">
                <div></div>
                <div className="flex header_logo_div">
                    <img onClick={() => navigate("/main")} className="header_logo" src={logo}></img>
                </div>
                <div className="flex header_logout">
                    <LogoutIcon onClick={() => logout()} />
                </div>
            </div>
            <div></div>
        </div>
    </div>
    )
}

export default Header;