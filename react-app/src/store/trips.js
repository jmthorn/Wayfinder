// constants
const SET_TRIPS = "trips/SET_TRIPS";
const ADD_TRIP = "trips/ADD_TRIP";

const setTrips = (trips) => ({
    type: SET_TRIPS,
    payload: trips
});

const addTrip = (trip) => ({
    type: ADD_TRIP,
    payload: trip
});

//   get all trips
  export const getTrips = () => async (dispatch)  => {
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
      console.log("HELLOOOO", chosenCityId, startDate, endDate)
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
    console.log("DATAAAAA",data)
    dispatch(addTrip(data))
    return {};
  }

const initialState = { trips: null};


export default function reducer(state=initialState, action) {
    let newState = {}
    switch (action.type) {
        case SET_TRIPS:
            newState = {...state}
            for (const trip in action.payload) { 
                newState[trip.id] = trip
            }
            return newState
        case ADD_TRIP : 
            newState = {...state}
            newState[action.payload.trip.id] = action.payload.trip
            return newState
        default:
            return state;
    }
}
