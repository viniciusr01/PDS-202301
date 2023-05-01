import styles from './home.module.css'
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';


import logo from '../img/logo.svg'
import simbolo from '../img/Simbolo.svg'


function Home(){



    return (
        
        <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>

            
            <Box sx={{ flexGrow: 1 }}>
                <Grid container spacing={1}>
                    <Grid container item spacing={3}>
                        <img className={styles.logo} src={logo}></img>
                    </Grid>

                    <Grid container item spacing={3}>
                        <div className={styles.texto}>
                            <h1 className={styles.h1}> A <b>Colmeia</b> que te ajuda a  </h1>
                            <h1 className={styles.h1}> controlar seu <strong>dinheiro</strong>  </h1>
                            
                            <Button variant="contained">Cadastrar</Button>
                            &ensp;
                            &ensp;
                            <Button variant="outlined">Login</Button>

                        </div>
                    </Grid>

                    <Grid container item spacing={1}>
                        <img className={styles.simbolo} src={simbolo}></img>
                    </Grid>
                </Grid>
            </Box>
           


        </Grid>
    )
}

export default Home;