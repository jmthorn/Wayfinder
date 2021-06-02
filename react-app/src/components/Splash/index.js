import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import {getCities} from '../../store/cities'
import './splash.css'

const Splash = () => {

  const dispatch = useDispatch()
  const cities = useSelector(state => state.cities.cities)
  console.log("CITIES ON FRONTEND", cities)

  useEffect(async() => { 
      await dispatch(getCities())
  }, [dispatch])

  const handleClick = (e) => { 
      console.log(e)
  }

  return (
    <div id="splash-container">
        <h1>THE PLACES</h1>
        <p>Where to next? Add a place to your trips.</p>
        <div className="splash-line"></div>
        <h3>All Travel Guides</h3>
        <div className="splash-line"></div>
        <div id="cities-container">
            {cities?.cities.map((city) => ( 
                <div className="city-container">
                    <div className="city-image-container">
                        <img src={city.image_url} alt="city_image"></img>
                    </div>
                    <div className="city-info">
                        <div className="city-name">
                            <div >{city.name}</div>
                            <div className="city-line"></div>
                        </div>
                        <button value={city.id} type="button" className="add-button" onClick={(e) => handleClick(e.target.value)}>+</button>
                    </div>
                </div>
            ))}
        </div>
    </div>
  );
}

export default Splash;