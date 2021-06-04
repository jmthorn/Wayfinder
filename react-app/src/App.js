import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import LoginForm from "./components/auth/Login";
import SignUpForm from "./components/auth/Signup";
import ProtectedRoute from "./components/auth/ProtectedRoute";
// import User from "./components/User";
import Cities from "./components/Cities";
import Splash from "./components/Splash";
import Destinations from "./components/Destinations";
import { authenticate } from "./store/session";
import NavBar from "./components/NavBar";
import Itinerary from "./components/Itinerary";
import Footer from "./components/Footer";
import Trips from "./components/Trips";


function App() {
  const user = useSelector(state => state.session.user)
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, []);

  if (!loaded) {
    return null;
  }

  let sessionlink;
  if(user) { 
    sessionlink =(
        <Cities />
    )
  }else { 
    sessionlink =(
        <Splash />
    )
  }


  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <Route path="/" exact={true} >
          {sessionlink}
        </Route>
        {/* <ProtectedRoute path="/users/:userId" exact={true} >
          <User />
        </ProtectedRoute> */}
        <ProtectedRoute path={[`/destinations/:cityId`, "/destinations/:cityId/:destinationName"]} exact={true}>
          <Destinations />
        </ProtectedRoute>
        <ProtectedRoute path={`/itinerary/:tripId`} exact={true}>
          <Itinerary />
        </ProtectedRoute>
        <ProtectedRoute path={`/mytrips`} exact={true}>
          <Trips />
        </ProtectedRoute>
      </Switch>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
