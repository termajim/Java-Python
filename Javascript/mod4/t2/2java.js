document.addEventListener('DOMContentLoaded', function() {
  const searchForm = document.getElementById('searchForm');

  searchForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const query = document.getElementById('query').value.trim();
    if (query === '') {
      alert('Kerro sarjan nimi.');
      return;
    }

    // Constructing the API URL with the query parameter
    const apiUrl = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`;

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Yhteys ei mennyt läpi');
        }
        return response.json();
      })
      .then(data => {
        console.log('Hakemuksen tulokset:');
        console.log(data);
        // Print search results to the console
        data.forEach(result => {
          console.log('Show:', result.show.name);
          console.log('Rating:', result.show.rating.average);
          console.log('Genres:', result.show.genres.join(', '));
          console.log('Summary:', result.show.summary);
          console.log('-------------------------');
        });
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  });
});
