import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {getDestination, updateDestination} from '../../store/destinations';
import { getTrips } from '../../store/trips';
import Geocode from "react-geocode";
import { useHistory } from 'react-router';
import { Link, useParams, Route } from 'react-router-dom';




function EventDetails({selectedEvent}) { 
    


  return (
   <>
      <h2 className="modal-title">{selectedEvent.name}</h2>
      <div className="modal-line"></div>
      <div id="events-detail-image">
          <img src={selectedEvent.image_url} alt="selectedEvent"></img>
      </div>
      <div className="modal-form"></div>
    </>
  );
}

export default EventDetails;