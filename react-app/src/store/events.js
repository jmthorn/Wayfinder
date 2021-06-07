const SET_EVENTS = "events/GET_EVENTS"
const ADD_EVENT = "events/ADD_EVENT"
const UPDATE_EVENT = "events/UPDATE_EVENT"
const DELETE_EVENT = "events/DELETE_EVENTS"

const setEvents = (events) => ({ 
    type: SET_EVENTS,
    payload: events
})

const addEvent = (event) => ({ 
    type: ADD_EVENT,
    payload: event
})

const update = (event) => ({ 
    type: UPDATE_EVENT,
    payload: event
})

const remove = (event) => ({ 
    type: DELETE_EVENT,
    payload: event
})

export const getEvents = (trip_id) => async(dispatch) => { 
    const response = await fetch(`/api/events/${trip_id}`)

    const data = await response.json();

    if(data.errors) { 
        return data;
    }
    dispatch(setEvents(data))
    return {}
}

export const createEvent = (trip_id, default_destination_id, custom_destination_id) => async(dispatch) => { 
    const response = await fetch(`/api/events/`, { 
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            trip_id, 
            default_destination_id,
            custom_destination_id
        })
    })
    const data = await response.json();
    if(data.errors) { 
        return data;
    }
    dispatch(addEvent(data))
    return {}
}

export const updateEvent = (event_id, order, start, end) => async(dispatch) => { 
    const response = await fetch(`/api/events/${event_id}`, { 
        method: 'PUT',
        headers: { 
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            event_id,
            order,
            start,
            end
        })
    })
    const data = await response.json()
    if(data.errors) { 
        return data;
    }
    dispatch(update(data))
    return {}
}

export const removeEvent = (event_id) => async(dispatch) => { 
    const response = await fetch(`/api/events/${event_id}`, { 
        method: 'DELETE',
        headers: { 
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            event_id
        })
    })
    const data = await response.json()
    if(data.errors) { 
        return data
    }
    dispatch(remove(data))
    return {}
}


const initialState = {}


export default function reducer(state=initialState, action)  { 
    let newState = {}
    switch (action.type) { 
        case SET_EVENTS:
            newState = {...state}
            for(let i=0; i < (action.payload.events).length; i++) {
                newState[action.payload.events[i].id] = action.payload.events[i]
            }
            return newState
        case ADD_EVENT: 
            newState = {...state}
            newState[action.payload.event.id] = action.payload.event
            return newState
        case UPDATE_EVENT: 
            newState = {...state}
            newState[action.payload.event.id] = action.payload.event
            return newState
        case DELETE_EVENT: 
            newState = {...state}
            delete newState[action.payload.event.id]
            return newState
        default:
            return state;
    }
}