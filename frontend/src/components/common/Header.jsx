import React from 'react';
import { NavLink } from 'react-router-dom';
import { Moon, Sun, Bell, MessageSquare, UserCircle, PlusSquare,Home } from 'lucide-react';
import './Header.css';
import { useTheme } from '../../hooks/useTheme.jsx';

const Header = () => {
  const { theme, toggleTheme } = useTheme();

  return (
    <header className="header">
      <div className="header-container">
        <div className="logo">
          <NavLink to="/">e.on</NavLink>
        </div>
        
        <nav className="nav">
          <ul className="nav-list">
            <li className="nav-item">
              <NavLink to="/" className={({ isActive }) => isActive ? 'active' : ''}>
                <Home size={20}/>
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink to="/create-post" className={({ isActive }) => isActive ? 'active' : ''}>
                <PlusSquare size={20} />
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink to="/notifications" className={({ isActive }) => isActive ? 'active' : ''}>
                <Bell size={20} />
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink to="/messages" className={({ isActive }) => isActive ? 'active' : ''}>
                <MessageSquare size={20} />
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink to="/profile" className={({ isActive }) => isActive ? 'active' : ''}>
                <UserCircle size={20} />
              </NavLink>
            </li>
          </ul>
        </nav>
        
        <button className="theme-toggle" onClick={toggleTheme} aria-label="Toggle theme">
          {theme === 'light' ? <Moon size={20} /> : <Sun size={20} />}
        </button>
      </div>
    </header>
  );
};

export default Header;