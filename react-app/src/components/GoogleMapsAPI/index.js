import React from 'react';
import { Map, GoogleApiWrapper, Marker } from 'google-maps-react';


const mapStyles = {
  width: '100%',
  height: '200px',
};

export function MapContainer (props) {

    let { coordinate } = props
    
    return (
      <Map
        google={props.google}
        zoom={13}
        style={mapStyles}
        initialCenter={coordinate}
        center={coordinate}
        >
        <Marker
            key={coordinate?.lat}
            position={{lat: coordinate?.lat, lng: coordinate?.lng}} 
            // onClick={() => onClick2(coordinate.id)}
        />
        </Map>
    );
  
}

export default GoogleApiWrapper(
  (props) => ({
    apiKey: props.apiKey,
  }
))(MapContainer)