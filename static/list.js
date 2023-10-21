function AddToList(user, p_id) {
    const morningCheckbox = document.querySelector('input[name="MorningD"]');
    const dayCheckbox = document.querySelector('input[name="DayD"]');
    const nightCheckbox = document.querySelector('input[name="NightD"]');
    const numDays = parseInt(document.getElementById('Daynum').innerText) || 0;

    // Check if the checkboxes are checked or not
    const isMorningChecked = morningCheckbox.checked;
    const isDayChecked = dayCheckbox.checked;
    const isNightChecked = nightCheckbox.checked;

    const intakes = [];
    if (isMorningChecked) intakes.push("Morning");
    if (isDayChecked) intakes.push("Day");
    if (isNightChecked) intakes.push("Night");

    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    // console.log('Intakes:', intakes);
    // console.log('NumDays:', numDays);
    // Prepare the data to be sent in the POST request
    const data = {
        user: user,
        p_id: p_id,
        intakes: intakes,
        numDays: numDays
    };
    // console.log("Data:", data)

    // Make a POST request to your server with CSRF token included
    fetch('/save_med_list/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken, // Include CSRF token for CSRF protection
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server if needed
        console.log(data);
    })
    .catch(error => {
        // Handle errors if the request fails
        console.error('Error:', error);
    });
}











// document.addEventListener('DOMContentLoaded', function () {
//     const medListForm = document.getElementById('medListForm');
//     const morningCheckbox = document.querySelector('input[name="Morning"]');
//     const dayCheckbox = document.querySelector('input[name="Day"]');
//     const nightCheckbox = document.querySelector('input[name="Night"]');
//     const numDays = parseInt(document.getElementById('num').innerText);
//     const user = '{{ user }}';


//     medListForm.addEventListener('submit', function (event) {
//         event.preventDefault();

//         const formData = new FormData();
//         formData.append('user', user);
//         formData.append('medicine_id', '{{ product_details.p_id }}');
//         formData.append('Morning', morningCheckbox.checked);
//         formData.append('Day', dayCheckbox.checked);
//         formData.append('Night', nightCheckbox.checked);
//         formData.append('number_of_days', numDays);
//         console.log(formData)
//         fetch('{% url "save_med_list" %}', {
//             method: 'POST',
//             body: formData,
//             headers: {
//                 'X-CSRFToken': '{{ csrf_token }}',
//             },
//         })
//             .then(response => response.json())
//             .then(data => {
//                 if (data.success) {
//                     medListForm.reset();
//                     document.getElementById('message').innerText = 'Medicine added to the list successfully!';
//                 } else {
//                     document.getElementById('message').innerText = 'Failed to add medicine to the list. Please try again.';
//                 }
//             })
//             .catch(error => {
//                 console.error('Error:', error);
//                 document.getElementById('message').innerText = 'An error occurred while processing your request. Please try again later.';
//             });
//     });
// });
