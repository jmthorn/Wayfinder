import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import User from "./components/User";
import Splash from "./components/Splash";
import { authenticate } from "./store/session";
import NavBar from "./components/NavBar";
import Itinerary from "./components/Itinerary";


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
          <Splash />
        </Route>
        {/* <ProtectedRoute path="/users/:userId" exact={true} >
          <User />
        </ProtectedRoute> */}
        <ProtectedRoute path={`/itinerary/:tripId`} exact={true}>
          <Itinerary />
        </ProtectedRoute>
        <ProtectedRoute path={`/cities/:cityId`} exact={true}>
          <Itinerary />
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
