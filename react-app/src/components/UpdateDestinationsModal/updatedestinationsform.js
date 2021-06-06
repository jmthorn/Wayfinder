import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {updateDestination} from '../../store/destinations';
import { getTrips } from '../../store/trips';
import Geocode from "react-geocode";
import { useHistory } from 'react-router';



function UpdateDestinationsForm({destination}) {

  const [name, setName] = useState(destination.name);
  const [address, setAddress] = useState(destination.address);
  const [image_url, setImageURL] = useState(destination.image_url);
  const [duration, setDuration] = useState(destination.duration);
  const [description, setDescription] = useState(destination.description);
  const [apiKey, setApiKey] = useState('');
  const [lat, setLat] = useState(destination.lat)
  const [lng, setLng] = useState(destination.lng)
  const [update, setUpdate] = useState("UPDATE TRIP")
  const trips = useSelector(state => state.trips)
  const tripsarr = Object.values(trips)
  const filteredtrips = tripsarr.filter((trip) => trip.city_id === destination.city_id)
  const dispatch = useDispatch();
  const [errors, setErrors] = useState([]);
  const city_id =  destination.city_id;     
  const destinationId = destination.id;
  const history = useHistory()

  useEffect(() => {
  (async()=> {
    const res = await fetch('/api/retrieve_api/');
    const { apiKey } = await res.json();
    setApiKey(apiKey);
    })()
  })


  useEffect(() => { 
      dispatch(getTrips())
  }, [])

  const handleSubmit = async(e) => {
    e.preventDefault();

    apiKey && Geocode.setApiKey(apiKey);
    let res = await Geocode.fromAddress(address)
    let { lat, lng } = res.results[0].geometry.location;
    setLat(lat)
    setLng(lng)

    let new_errors = [];
    if(!image_url || !address || !name || !duration || !description) { 
        new_errors.push("Your destination is missing data!")
    }

    setErrors(new_errors)
    if (errors.length == 0) {
      setUpdate("UPDATED!")
      dispatch(updateDestination(
          destinationId,
          city_id,
          description,
          image_url,
          address, 
          duration, 
          lat,
          lng,
          name
      ))

      return history.push(`/destinations/${city_id}/${name.split(" ").join("_")}`)
    }
  };  


  return (
   <>
      <h2 className="modal-title">Update Your Destination</h2>
      <div className="modal-line"></div>
      <div className="modal-form">
          <form onSubmit={(e) => handleSubmit(e)}>
            {errors && errors?.map((error) => (
                <div className="modal-error">{error}</div>
                )
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
                <label htmlFor="image_url">Image URL</label>
                <input
                    className="create-trip-input"
                    name="image_url"
                    type="text"
                    value={image_url}
                    onChange={(e) => setImageURL(e.target.value)}
                />
            </div>
            <button className="modal-button create-trip-btn" type="submit">{update}</button>
          </form>
      </div>
    </>
  );
}

export default UpdateDestinationsForm;