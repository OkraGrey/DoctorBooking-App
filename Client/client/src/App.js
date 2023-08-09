import './App.css';
import HomePage from './pages/HomePage';
import Login from './pages/Login';
import {BrowserRouter as Router ,Route,Routes} from 'react-router-dom'
import Header from './components/Header';
import { store } from './store';
import { Provider } from 'react-redux'
function App() {
  return (

    <Router>
      <Provider store={store}>
        <Header />
        <Routes>
          <Route Component={HomePage} path='/' exact />
          <Route Component={Login} path='/login'/>
        </Routes>

      </Provider>
    </Router>
  );
}

export default App;
