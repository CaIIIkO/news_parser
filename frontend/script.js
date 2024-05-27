document.addEventListener('DOMContentLoaded', function () {
    const getNewsForm = document.getElementById('getNewsForm');
    const getNewsByCategoryForm = document.getElementById('getNewsByCategoryForm');
    const getRandomNewsButton = document.getElementById('getRandomNewsButton');
    const getLastNewsButton = document.getElementById('getLastNewsButton');
    const newsResults = document.getElementById('newsResults');

    function displayNews(news) {
        newsResults.innerHTML = '';
        if (news.length === 0) {
            newsResults.innerHTML = '<p>Нет новостей для отображения</p>';
            return;
        }
        news.forEach(item => {
            const newsItem = document.createElement('div');
            newsItem.className = 'news-item';
            newsItem.innerHTML = `
                <h3>${item.text}</h3>
                <p>${item.time} | ${item.category}</p>
                <a href="${item.link}" target="_blank">Читать полностью</a>
            `;
            newsResults.appendChild(newsItem);
        });
    }

    function displayError(error) {
        newsResults.innerHTML = `<p style="color: red;">Ошибка: ${error.message}</p>`;
    }

    getNewsForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const day = document.getElementById('day').value;
        const month = document.getElementById('month').value;
        const year = document.getElementById('year').value;
        const quantity = document.getElementById('quantity').value;

        fetch(`http://localhost:8002/news/?day=${day}&month=${month}&quantity=${quantity}&year=${year}`)
            .then(response => response.json())
            .then(data => displayNews(data.news))
            .catch(error => displayError(error));
    });

    getNewsByCategoryForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const day = document.getElementById('dayCategory').value;
        const month = document.getElementById('monthCategory').value;
        const year = document.getElementById('yearCategory').value;
        const category = document.getElementById('category').value;
        const quantity = document.getElementById('quantityCategory').value;

        fetch(`http://localhost:8002/news/${category}?day=${day}&month=${month}&quantity=${quantity}&year=${year}`)
            .then(response => response.json())
            .then(data => displayNews(data.news))
            .catch(error => displayError(error));
    });

    getRandomNewsButton.addEventListener('click', function () {
        fetch('http://localhost:8002/news/last')
            .then(response => response.json())
            .then(data => displayNews([data]))
            .catch(error => displayError(error));
    });

    getLastNewsButton.addEventListener('click', function () {
        fetch('http://localhost:8002/news/random')
            .then(response => response.json())
            .then(data => displayNews([data]))
            .catch(error => displayError(error));
    });
});
