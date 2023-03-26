// Get the heart element
const heart = document.querySelector('.heart');

// Add a click event listener to the heart
heart.addEventListener('click', () => {
    // Get the card element
    const card = heart.closest('.card');

    // Create a new container element
    const container = document.createElement('div');
    container.classList.add('container');

    // Clone the card element and append it to the container
    const clonedCard = card.cloneNode(true);
    container.appendChild(clonedCard);

    // Create a new XHR object
    const xhr = new XMLHttpRequest();

    // Define the destination URL and HTTP method
    const url = 'save-wishlist.php';
    const method = 'POST';

    // Set the request header
    xhr.setRequestHeader('Content-Type', 'application/json');

    // Define the request body as JSON
    const data = {
        cardHtml: container.innerHTML
    };

    // Convert the data to a JSON string
    const jsonData = JSON.stringify(data);

    // Send the request
    xhr.open(method, url);
    xhr.send(jsonData);
});


