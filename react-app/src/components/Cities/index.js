import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import {getCities} from '../../store/cities'
import CreateTripModal from '../CreateTripModal';
import './cities.css'

const Cities = () => {

  const dispatch = useDispatch()
  const cities = useSelector(state => state.cities.cities)

  useEffect(() => { 
      dispatch(getCities())
  }, [dispatch])


  return (
    <div id="cities-page-container">
        <h1>THE PLACES</h1>
        <p>Where to next? Add a place to your trips.</p>
        <div className="cities-line"></div>
        <h3>All Travel Guides</h3>
        <div className="cities-line"></div>
        <div id="cities-container">
            {cities?.cities.map((city) => ( 
                <div key={city.id} className="city-container">
                    <Link to={`/destinations/${city.id}`}>
                        <div className="city-image-container">
                            <div className="city-image-info">
                                <button className="destinations-button">DESTINATIONS</button>
                            </div>
                            <img src={city.image_url} alt="city_image"></img>
                        </div>
                    </Link>
                    <div className="city-info">
                        <div className="city-name">
                            <div >{city.name}</div>
                            <div className="city-line"></div>
                        </div>
                        {/* <button value={city.id} type="button" className="add-button" onClick={(e) => handleClick(e.target.value)}>+</button> */}
                        <CreateTripModal cityId={city.id}/>                    
                    </div>
                </div>
            ))}
        </div>
    </div>
  );
}

export default Cities;