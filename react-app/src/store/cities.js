// constants
const SET_CITIES = "cities/SET_CITIES";

const setCities = (cities) => ({
    type: SET_CITIES,
    payload: cities
});

  
  export const getCities = () => async (dispatch)  => {
    const response = await fetch('/api/cities/')

    const data = await response.json();
    if (data.errors) {
        return data;
    }
    console.log("DATA", data)
    dispatch(setCities(data))
    return {};
  }

const initialState = { cities: null };


export default function reducer(state=initialState, action) {
    switch (action.type) {
        case SET_CITIES:
            return {cities: action.payload}
        default:
            return state;
    }
}
