// frontend/src/components/LoginFormModal/index.js
import React, { useState } from 'react';
import { Modal } from '../../context/modal';
import CreateTripForm from './createtripform';


function CreateTripModal({cityId}) {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button onClick={() => setShowModal(true)} type="button" className="add-button">+</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <CreateTripForm cityId={cityId} />
        </Modal>
      )}
    </>
  );
}

export default CreateTripModal;