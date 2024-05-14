// document.addEventListener('DOMContentLoaded', async function() {

// }
document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"][id]');

    // Fetch and update the initial state for all checkboxes from the server
    checkboxes.forEach(checkbox => {
        fetchCheckboxState(checkbox.id);
    });

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const checkboxId = checkbox.id;
            const newState = checkbox.checked ? 'on' : 'off';

            // Send the new state to the server
            fetch('/update-checkbox-state', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ checkboxId: checkboxId, state: newState })
            })
            .then(response => response.json())
            .then(data => {
                // Ensure the checkbox is updated based on the server's response
                updateCheckboxState(checkbox, data.state);
            })
            .catch(error => console.error('Error updating checkbox state:', error));
        });
    });

    function fetchCheckboxState(checkboxId) {
        fetch(`/get-checkbox-state/${checkboxId}`)
        .then(response => response.json())
        .then(data => {
            const checkbox = document.querySelector(`input[id="${checkboxId}"]`);
            if (checkbox) {
                updateCheckboxState(checkbox, data.state);
            }
        })
        .catch(error => console.error('Error fetching checkbox state:', error));
    }

    function updateCheckboxState(checkbox, state) {
        checkbox.checked = state === 'on';
    }
});


function livingroomShowHide() {
    document.getElementById('livingRoomId').style.display = '';
    document.getElementById('kitchenId').style.display = 'none';

    if (!document.getElementById('livinbut').classList.contains('active')) {
        document.getElementById('livinbut').classList.add('active');
    }
        
    if (document.getElementById('kitchenbut').classList.contains('active')) {
        document.getElementById('kitchenbut').classList.remove('active');
    }
}

function kitchenShowHide() {
    const livinbtu = document.getElementById('livingRoomId');
    const kitchenbtu = document.getElementById('kitchenId');
    livinbtu.style.display = 'none';
    kitchenbtu.style.display = '';

    document.getElementById('kitchenbut').classList.add('active');

    if (document.getElementById('livinbut').classList.contains('active')) {
        document.getElementById('livinbut').classList.remove('active');
    }   
}