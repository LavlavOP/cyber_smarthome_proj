// document.addEventListener('DOMContentLoaded', async function() {
// Define a mapping from character IDs to numeric IDs
const idMapping = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'oven': 5,
    'microwave': 6,
    'dishwasher': 7,
    'diningLight': 8,
    'p': 9,
};
// }
document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('input[type="checkbox"][id]');

    // Fetch initial light states and update checkboxes accordingly
    fetch('/lights')
        .then(response => response.json())
        .then(data => {
            // Iterate over each checkbox and set the checked state based on the server data
            checkboxes.forEach(checkbox => {
                const lightId = checkbox.id;
                const newlightId = idMapping[lightId] || null; // Fallback to null if the ID doesn't exist in the mapping
                if (data.hasOwnProperty(newlightId)) {
                    checkbox.checked = data[newlightId];
                }
            });
        })
        .catch(error => console.error('Error fetching initial light states:', error));

    // Set up event listeners for toggling lights
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            const lightId = checkbox.id;
            const newlightId = idMapping[lightId] || null; // Fallback to null if the ID doesn't exist in the mapping
            console.log(newlightId)
            const endpoint = `/lights/${newlightId}/toggle`;

            fetch(endpoint, {
                method: 'POST',
            })
                .then(response => response.json())
                .then(data => {
                    // Ensure the checkbox reflects the state from the server
                    // if (data.hasOwnProperty(lightId)) {
                    //     checkbox.checked = data[lightId];
                    // } else {
                    //     console.error('Response does not contain the expected light ID:', newlightId);
                    // }
                })
                .catch(error => {
                    console.error('Error toggling light state:', error);
                    // Revert the checkbox state in case of an error
                    checkbox.checked = !checkbox.checked;
                });
        });
    });
});


function livingRoomShowHide() {
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
    const livingRoomId = document.getElementById('livingRoomId');
    const kitchenId = document.getElementById('kitchenId');
    livingRoomId.style.display = 'none';
    kitchenId.style.display = '';

    document.getElementById('kitchenbut').classList.add('active');

    if (document.getElementById('livinbut').classList.contains('active')) {
        document.getElementById('livinbut').classList.remove('active');
    }
}

async function logout() {
    await fetch(`/users/logout`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        window.location.href = "/site/login"; // Redirect on success
    })
    .catch(error => console.error('Error:', error));
}
