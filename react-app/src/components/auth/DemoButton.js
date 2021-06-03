import React from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { login } from '../../store/session';

function DemoButton() {
    const dispatch = useDispatch();
  const history = useHistory();

  const handleClick = async (e) => {
    e.preventDefault();

    await dispatch(login('demo@aa.io', 'password'));
    history.push('/');
  }

  return (
    <button className="auth-button" onClick={handleClick} type='submit' id='demo-btn'>DEMO</button>
  )
}

export default DemoButton;