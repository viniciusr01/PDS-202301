import styles from './principal.module.css'
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';


import logo from '../img/logo.svg'
import LogoutIcon from '@mui/icons-material/Logout';
import simbolo from '../img/Simbolo.svg'


function Principal(){



    return (
        
        <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
             <Box sx={{ flexGrow: 1 }}>
                <Grid container spacing={1}>
                    <Grid container item spacing={3}>
                        <img className={styles.logo} src={logo}></img>
                                 
                    </Grid>

                    <Grid container item spacing={3}>
            
                            <div className={styles.div_buttons}>
                                <button className={styles.botao_receita_despesa} >+ Receita</button>
                                &ensp;
                                &ensp;
                                <button className={styles.botao_receita_despesa}>+ Despesa</button>
                            </div>
                       
                    </Grid>

                    

                    <Grid container item spacing={3}>
                        <div className={styles.texto}>

                        
                        </div>
                    </Grid>

                   
                    
                </Grid>
            
                </Box>           


        </Grid>
    )
}

export default Principal;