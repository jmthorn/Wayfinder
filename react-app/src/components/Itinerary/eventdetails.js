import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {getDestination, updateDestination} from '../../store/destinations';
import { getTrips } from '../../store/trips';
import Geocode from "react-geocode";
import { useHistory } from 'react-router';
import { Link, useParams, Route } from 'react-router-dom';
import moment from 'moment'




function EventDetails({selectedEvent}) { 
    


  return (
   <>
      <div id="events-detail-image">
          <img src={selectedEvent.image_url} alt="selectedEvent"></img>
      </div>
      <h2 className="modal-title">{selectedEvent.name}</h2>
      <div className="modal-line"></div>
      <div className="modal-form"></div>
      <div className="modal-events-duration">Duration: {(selectedEvent.duration)/60} Hours</div>
      <div className="modal-events-time">{moment(selectedEvent.start).format("LT")} - {moment(selectedEvent.end).format("LT")}</div>
    </>
  );
}

export default EventDetails;