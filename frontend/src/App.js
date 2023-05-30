import './App.css';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Home from './pages/home';
import Principal from './pages/principal'
import ContaDetalhada from './pages/contaDetalhada';



function App() {
  return (

    <Router>
      <div className="AppContainer">
      

        <Routes>
          <Route path="/" index element={<Home/>}></Route>
          <Route path="/main" index element={<Principal/>}></Route>
          <Route path="/account" index element={<ContaDetalhada/>}></Route>


        </Routes>

      </div>

    </Router>
    
  );
}

export default App;
