import React, { useState } from 'react';
import { Modal } from '../../context/modal';
import CreateEventForm from './createeventform';


function CreateEventModal({cityId}) {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button onClick={() => setShowModal(true)} type="button"  id="dest-button" >ADD TO TRIP</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <CreateEventForm cityId={cityId} />
        </Modal>
      )}
    </>
  );
}

export default CreateEventModal;