document.addEventListener('DOMContentLoaded', function() {
    const themeButton = document.getElementById('themeChange');
    const titleText = document.querySelector('.funny-title');
    const funnyButton = document.querySelector('.funny-button')
    const body = document.body;

    // Функция для переключения темы
    function toggleTheme() {
        if (body.classList.contains('dark-theme')) {
            body.classList.remove('dark-theme');
            body.classList.add('light-theme');
            titleText.textContent = '😄 Enter Your Details! 🦄'
            funnyButton.textContent = "🚀 Let's Go!"
            localStorage.setItem('theme', 'light-theme');
        } else {
            body.classList.remove('light-theme');
            body.classList.add('dark-theme');
            titleText.textContent = '👻 Enter Your Details! 🕸'
            funnyButton.textContent = "🕷 Let's Go!"
            localStorage.setItem('theme', 'dark-theme');
        }
    }

    themeButton.addEventListener('click', toggleTheme);
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        body.classList.remove('light-theme', 'dark-theme');
        body.classList.add(savedTheme);

        if (savedTheme === 'dark-theme') {
            titleText.textContent = '👻 Enter Your Details! 🕸'
            funnyButton.textContent = "🕷 Let's Go!"
        } else {
            titleText.textContent = '😄 Enter Your Details! 🦄'
            funnyButton.textContent = "🚀 Let's Go!"
        }
    } else {
        body.classList.add('light-theme');
        themeButton.textContent = 'Switch Theme (Light)';
    }
});
