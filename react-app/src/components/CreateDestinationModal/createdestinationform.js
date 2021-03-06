import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {createDestination} from '../../store/destinations'
import Geocode from "react-geocode";





function CreateDestinationForm({cityId}) {


  const [created, setCreated] = useState("CREATE DESTINATION")
  const cities = useSelector(state => state.cities.cities)
  const chosenCity = cities?.cities?.filter((city) => city.id === cityId)[0]
  const chosenCityId = chosenCity?.id
  const dispatch = useDispatch();
  const [error, setError] = useState("");
  const [name, setName] = useState("");
  const [address, setAddress] = useState("");
  const [image_url, setImage] = useState("");
  const [lat, setLat] = useState("");
  const [lng, setLng] = useState("");
  const [duration, setDuration] = useState("");
  const [description, setDescription] = useState("");
  const [apiKey, setApiKey] = useState('');

  useEffect(() => {
  (async()=> {
    const res = await fetch('/api/retrieve_api/');
    const { apiKey } = await res.json();
    setApiKey(apiKey);
    })()
  })


  const handleSubmit = async(e) => {
    e.preventDefault();

    if(!image_url || !address || !name || !duration || !description) { 
      setError("Your destination is missing data!")
    } else {
      // Geocode.setApiKey(process.env.REACT_APP_GOOGLE_MAPS_KEY);
      apiKey && Geocode.setApiKey(apiKey);
      let res = await Geocode.fromAddress(address)
      const { lat, lng } = res.results[0].geometry.location;
      setLat(lat)
      setLng(lng)
      setCreated("CREATED!")
      return dispatch(createDestination(cityId, image_url, address, name, lat, lng, duration, description))
    }
  };  


  return (
    <>
      <h2 className="modal-title">Create a Destination</h2>
      <div className="modal-line"></div>
      <div className="modal-form">
          <form onSubmit={(e) => handleSubmit(e)}>
            {error && (
              <div className="modal-error">{error}</div>
            )}
            <div className="create-trip-div">
                <label htmlFor="name">Name</label>
                <input
                    className="create-trip-input"
                    name="name"
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    />
            </div>
            <div className="create-trip-div">
                <label htmlFor="address">Address</label>
                <input
                    className="create-trip-input"
                    name="address"
                    type="text"
                    value={address}
                    onChange={(e) => setAddress(e.target.value)}
                    />
            </div>
            <div className="create-trip-div">
                <label htmlFor="description">Description</label>
                <input
                    className="create-trip-input"
                    name="description"
                    type="text"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    />
            </div>
            <div className="create-trip-div">
                <label htmlFor="duration">Duration</label>
                <input
                    className="create-trip-input"
                    name="duration"
                    type="text"
                    value={duration}
                    onChange={(e) => setDuration(e.target.value)}
                    />
            </div>
            <div className="create-trip-div">
                <label htmlFor="image_url">Image</label>
                <input
                    className="create-trip-input"
                    name="image_url"
                    type="file"
                    accept="image/*"
                    onChange={(e) => setImage(e.target.files[0])}
                />
            </div>
            <button className="modal-button create-trip-btn" type="submit">{created}</button>
          </form>
      </div>
    </>
  );
}

export default CreateDestinationForm;