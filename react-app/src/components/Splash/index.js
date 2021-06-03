import React from 'react';
import SplashImage from '../../images/splash.jpg'
import { useHistory } from "react-router-dom";

import SplashGraphic from '../../images/Splash-Graphic.png'
import './splash.css'

const Splash = () => {

  const history = useHistory()

  const handleClick = () => { 
      history.push('/sign-up')
  }

  return (
    <div id="splash-page-container">
      <div id="splash-main-image">
        <div>Let's plan on it.</div>
        <button type="button" onClick={() => handleClick()}>SIGN UP</button>
      </div>
      <div id="splash-graphic">
        <img src={SplashGraphic}></img>
      </div>
    </div>
  );
}

export default Splash;