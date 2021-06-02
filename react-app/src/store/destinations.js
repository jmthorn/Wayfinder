// constants
const SET_DESTINATIONS = "destinations/GET_DESTINATIONS";

const setDestinations = (destinations) => ({
    type: SET_DESTINATIONS,
    payload: destinations
});


//   get all destinations for one city
  export const getDestinations = (cityId) => async (dispatch)  => {
    console.log("HELLOOOO")
    const response = await fetch(`/api/destinations/${cityId}`)

    const data = await response.json();
    if (data.errors) {
        return data;
    }
    dispatch(setDestinations(data))
    return {};
  }

const initialState = { destinations:null };


export default function reducer(state=initialState, action) {
    switch (action.type) {
        case SET_DESTINATIONS:
            return {...initialState, destinations: action.payload}
        default:
            return state;
    }
}
