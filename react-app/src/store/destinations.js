// constants
const SET_DESTINATIONS = "destinations/GET_DESTINATIONS";
const SET_DESTINATION = "destinations/GET_DESTINATION";

const setDestinations = (destinations) => ({
    type: SET_DESTINATIONS,
    payload: destinations
});

const setDestination = (destination) => ({
    type: SET_DESTINATION,
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

const initialState = { destinations:null, destination:null};


export default function reducer(state=initialState, action) {
    switch (action.type) {
        case SET_DESTINATIONS:
            return {...state, destinations: action.payload}
        case SET_DESTINATION:
            return {...state, destination: action.payload}
        default:
            return state;
    }
}
