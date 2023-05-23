import './App.css';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Home from './pages/home';
import Principal from './pages/principal'



function App() {
  return (

    <Router>
      <div className="AppContainer">
      

        <Routes>
          <Route path="/" index element={<Home/>}></Route>
          <Route path="/main" index element={<Principal/>}></Route>


        </Routes>

      </div>

    </Router>
    
  );
}

export default App;
