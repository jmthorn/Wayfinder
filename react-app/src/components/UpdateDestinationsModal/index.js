import React, { useState } from 'react';
import { Modal } from '../../context/modal';
import UpdateDestinationsForm from './updatedestinationsform';


function UpdateDestinationsModal({destination}) {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button  onClick={() => setShowModal(true)} type="button" id="dest-edit-button">EDIT DESTINATION</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <UpdateDestinationsForm destination={destination}/>
        </Modal>
      )}
    </>
  );
}

export default UpdateDestinationsModal;