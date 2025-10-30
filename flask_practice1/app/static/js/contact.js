const form = document.querySelector('form')
const messageElement = document.querySelector('.ok-message')
const loadingElement = document.querySelector('.loading')

function timeOut() {
    setTimeout(() => {
        messageElement.textContent = ''
    }, 10000);
}

form.addEventListener('submit', function(event) {
    event.preventDefault()

    loadingElement.style.display = 'block'

    fetch('/submit', {
        method: 'POST',
        body: new FormData(this)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        loadingElement.style.display = 'none'

        if (data.success) {
            messageElement.textContent = 'Your message has been sent successfully!'
            messageElement.style.color = 'green'
            timeOut()
        } else {
            messageElement.textContent = 'Error sending!'
            messageElement.style.color = 'red'
            timeOut()
        }
    })
    .catch((error) => {
        loadingElement.style.display = 'none'
        console.error('Error:', error)
        messageElement.textContent = 'Error!'
        messageElement.style.color = 'red'
        timeOut()
    })
})