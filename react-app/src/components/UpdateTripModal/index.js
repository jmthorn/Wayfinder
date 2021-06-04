// frontend/src/components/LoginFormModal/index.js
import React, { useState } from 'react';
import { Modal } from '../../context/modal';
import UpdateTripForm from './updatetripform';


function UpdateTripModal({tripId}) {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button onClick={() => setShowModal(true)} type="button" className="add-button">...</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <UpdateTripForm tripId={tripId} />
        </Modal>
      )}
    </>
  );
}

export default UpdateTripModal;