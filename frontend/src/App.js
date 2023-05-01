import './App.css';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Home from './pages/home';



function App() {
  return (

    <Router>
      <div className="AppContainer">
      

        <Routes>
          <Route path="/" index element={<Home/>}></Route>


        </Routes>

      </div>

    </Router>
    
  );
}

export default App;
