import React from "react";
import { useDispatch} from "react-redux";
import { useHistory } from 'react-router-dom'
import { logout } from "../../store/session";

const LogoutButton = () => {
  const dispatch = useDispatch();
  const history = useHistory()
  const onLogout = async (e) => {
    dispatch(logout());
    history.push('/')
  };

  return <button onClick={onLogout}>LOGOUT</button>;
};

export default LogoutButton;
