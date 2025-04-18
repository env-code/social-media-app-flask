import { AuthProvider }    from './context/AuthContext';
import { ThemeProvider }   from './context/ThemeContext';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header              from './components/layout/Header';
import HomePage            from './pages/HomePage.jsx';
import LoginPage           from './pages/LoginPage';
import './index.css';
import './App.css';

function App() {
  return (
    <AuthProvider>
      <ThemeProvider>
        <Router future={{ v7_startTransition: true, v7_relativeSplatPath: true }}>
          <Header />
          <main>
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/login" element={<LoginPage />} />
            </Routes>
          </main>
        </Router>
      </ThemeProvider>
    </AuthProvider>
  );
}

export default App;
