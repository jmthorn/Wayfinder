import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import Logo from '../../images/logo.png'
import { useSelector } from 'react-redux';
import './navbar.css'


const NavBar = () => {

  const user = useSelector(state => state.session.user)


  let sessionLinks;
    if (user) {
      sessionLinks = (
        <>
          <span className="nav-options">
            <li id="nav-home">
              <NavLink to="/" exact={true} activeClassName="active">
                Home
              </NavLink>
            </li>
            <li id="nav-portfolio">
              <NavLink to="/" exact={true}>
                Portfolio
              </NavLink>
            </li>
            <li id="nav-logout">
              <LogoutButton />
            </li>
          </span>
        </>
      );
    } else {
      sessionLinks = (
        <span className="nav-options">
          <li id="nav-login">
            <NavLink to="/login" exact={true} >
              LOG IN
            </NavLink>
          </li>
          <li id="nav-signup">
            <NavLink to="/sign-up" exact={true} >
              SIGN UP
            </NavLink>
          </li>
        </span>
      );
    }
  


  return (
    <nav>
      <ul id="nav-list">
        <li id="nav-home">
          <NavLink to="/" exact={true}>
            <img className="logo" src={Logo} alt="logo" />
          </NavLink>
        </li>
        {sessionLinks}
      </ul>
    </nav>
  );
}

export default NavBar;
