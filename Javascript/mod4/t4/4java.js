document.addEventListener('DOMContentLoaded', function() {
  const searchForm = document.getElementById('searchForm');
  const resultsContainer = document.getElementById('results');

  searchForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const query = document.getElementById('query').value.trim();
    if (query === '') {
      alert('Kerro sarjan nimi.');
      return;
    }

    const apiUrl = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`;

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Yhteys ei mennyt läpi');
        }
        return response.json();
      })
      .then(data => {
        // Clear previous results
        resultsContainer.innerHTML = '';

        data.forEach(result => {
          const tvShow = result.show;
          const article = document.createElement('article');

          const heading = document.createElement('h2');
          heading.textContent = tvShow.name;
          article.appendChild(heading);

          const link = document.createElement('a');
          link.href = tvShow.url;
          link.textContent = 'Details';
          link.target = '_blank';
          article.appendChild(link);

          const img = document.createElement('img');
          img.src = tvShow.image ? tvShow.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';
          img.alt = tvShow.name;
          article.appendChild(img);

          const summaryDiv = document.createElement('div');
          summaryDiv.innerHTML = tvShow.summary;
          article.appendChild(summaryDiv);

          resultsContainer.appendChild(article);
        });
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  });
});
