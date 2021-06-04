// constants
const SET_TRIPS = "trips/SET_TRIPS";
const ADD_TRIP = "trips/ADD_TRIP";
const UPDATE_TRIP = "trips/UPDATE_TRIP";
const DELETE_TRIP = "trips/DELETE_TRIP";

const setTrips = (trips) => ({
    type: SET_TRIPS,
    payload: trips
});

const addTrip = (trip) => ({
    type: ADD_TRIP,
    payload: trip
});

const update = (trip) => ({
    type: ADD_TRIP,
    payload: trip
});

const remove = (trip) => ({
    type: DELETE_TRIP,
    payload: trip
});

//   get all trips
  export const getTrips = () => async (dispatch)  => {
      console.log("HELLO!!")
    const response = await fetch('/api/trips/')

    const data = await response.json();
    if (data.errors) {
        return data;
    }
    dispatch(setTrips(data))
    return {};
  }

//   create Trip
  export const createTrip = (chosenCityId, startDate, endDate) => async (dispatch)  => {
    const response = await fetch(`/api/trips/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            chosenCityId,
            startDate,
            endDate
        }),
    });
    const data = await response.json();
    if (data.errors) {
        return data;
    }
    dispatch(addTrip(data))
    return {};
  }

//   update Trip
  export const updateTrip = (chosenTripId, startDate, endDate) => async (dispatch)  => {
    const response = await fetch(`/api/trips/${chosenTripId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            chosenTripId,
            startDate,
            endDate
        }),
    });
    const data = await response.json();
    if (data.errors) {
        return data;
    }
    dispatch(update(data))
    return {};
  }

//   delete Trip
  export const deleteTrip = (chosenTripId) => async (dispatch)  => {
    const response = await fetch(`/api/trips/${chosenTripId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            chosenTripId,
        }),
    });
    const data = await response.json();
    if (data.errors) {
        return data;
    }
    dispatch(remove(data))
    return {};
  }

const initialState = { trips: null};


export default function reducer(state=initialState, action) {
    let newState = {}
    switch (action.type) {
        case SET_TRIPS:
            newState = {...state}
            for (let i=0; i < (action.payload.trips).length; i++) { 
                newState[action.payload.trips[i].id] = action.payload.trips[i]
            }
            return newState
        case ADD_TRIP : 
            newState = {...state}
            newState[action.payload.trip.id] = action.payload.trip
            return newState
        case UPDATE_TRIP : 
            newState = {...state}
            newState[action.payload.trip.id] = action.payload.trip
            return newState
        case DELETE_TRIP : 
            newState = {...state}
            delete newState[action.payload.trip.id]
            return newState
        default:
            return state;
    }
}
