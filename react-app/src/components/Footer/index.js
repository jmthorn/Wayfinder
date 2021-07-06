import React from 'react';
import Github from '../../images/25231.png'
import LinkedIn from '../../images/linkedin-1.png'

import './footer.css'


const Footer = () => {


  return (
    <div id="footer-container">
        <div className="footer-icons">
            <a href="https://github.com/jmthorn" className="github_logo">
                <img src={Github} alt="logo"/>
            </a>
            <a href="https://www.linkedin.com/in/jessica-thornton-00615989/" className="github_logo">
                <img src={LinkedIn} alt="logo"/>
            </a>
        </div>
        <a href="https://jmthorn.github.io/Portfolio/" className="built-by">
            <h2>BUILT BY: JESSICA THORNTON</h2>
        </a>
        <div className="footer-description">
            <p> This itinerary builder was built as a week-long project for a rigorous 1000+ hour software engineering bootcamp. Images and content sourced from Conde Nast Traveler.</p>
        </div>
    </div>
  );
}

export default Footer;