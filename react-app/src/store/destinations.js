// constants
const SET_DESTINATIONS = "destinations/GET_DESTINATIONS";
const SET_DESTINATION = "destinations/GET_DESTINATION";
const ADD_DESTINATION = "destinations/ADD_DESTINATION";
const UPDATE_DESTINATION = "destinations/UPDATE_DESTINATION";
const DELETE_DESTINATION = "destinations/DELETE_DESTINATION";

const setDestinations = (destinations) => ({
    type: SET_DESTINATIONS,
    payload: destinations
});

const setDestination = (destination) => ({
    type: SET_DESTINATION,
    payload: destination
});

const addDestination = (destination) => ({
    type: ADD_DESTINATION,
    payload: destination
});

const update = (destination) => ({
    type: UPDATE_DESTINATION,
    payload: destination
});

const remove = (destination) => ({
    type: DELETE_DESTINATION,
    payload: destination
});


//   get all destinations for one city
  export const getDestinations = (cityId) => async (dispatch)  => {
    const response = await fetch(`/api/destinations/${cityId}`)

    const data = await response.json();
    if (data.errors) {
        return data;
    }
    dispatch(setDestinations(data))
    return {};
  }


//   get one destination
  export const getDestination = (destinationName) => async (dispatch)  => {
    const response = await fetch(`/api/destinations/destination/${destinationName}`)

    const data = await response.json();
    if (data.errors) {
        return data;
    }
    dispatch(setDestination(data))
    return {};
  }

//   create  destination
  export const createDestination = (cityId, image_url, address, name, lat, lng, duration, description) => async (dispatch)  => {
    const response = await fetch(`/api/destinations/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            cityId,
            image_url,
            address,
            name,
            lat,
            lng,
            duration,
            description
        }),
    });

    const data = await response.json();
    if (data.errors) {
        return data;
    }
    dispatch(addDestination(data))
    return {};
  }

//   update  destination
  export const updateDestination = (
          destinationId,
          city_id,
          description,
          image_url,
          address, 
          duration, 
          lat,
          lng,
          name) => async (dispatch)  => {
    const response = await fetch(`/api/destinations/${destinationId}>`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          destinationId,
          city_id,
          description,
          image_url,
          address, 
          duration, 
          lat,
          lng,
          name
        }),
    });

    const data = await response.json();
    if (data.errors) {
        return data;
    }
    dispatch(update(data))
    return {};
  }



//   delete Destination
  export const deleteDestination= (destinationId) => async (dispatch)  => {
    const response = await fetch(`/api/destinations/${destinationId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            destinationId,
        
        }),
    });
    const data = await response.json();
    if (data.errors) {
        return data;
    }
    dispatch(remove(data))
    return {};
  }


const initialState = { destinations:null, destination:null};


export default function reducer(state=initialState, action) {
    switch (action.type) {
        case SET_DESTINATIONS:
            return {...state, destinations: action.payload}
        case SET_DESTINATION:
            return {...state, destination: action.payload}
        case ADD_DESTINATION:
            return {...state, destinations: action.payload}
        case UPDATE_DESTINATION:
            return {...state, destinations: {custom_destinations: [...action.payload.custom_destinations], default_destinations: [...action.payload.default_destinations]}, destination: action.payload.destination}
        case DELETE_DESTINATION:
            return {...state, destinations: action.payload}
        default:
            return state;
    }
}
