import React, { useState } from 'react';
import { Modal } from '../../context/modal';
import CreateDestinationForm from './createdestinationform';


function CreateDestinationModal({cityId}) {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button onClick={() => setShowModal(true)} type="button" id="add-dest-button">+</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <CreateDestinationForm cityId={cityId} />
        </Modal>
      )}
    </>
  );
}

export default CreateDestinationModal;