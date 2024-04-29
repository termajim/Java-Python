document.addEventListener('DOMContentLoaded', function() {
  const searchForm = document.getElementById('searchForm');

  searchForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const query = document.getElementById('query').value.trim();
    if (query === '') {
      alert('Kerro sarjan nimi.');
      return;
    }

    const apiUrl = searchForm.getAttribute('action') + '?q=' + encodeURIComponent(query);

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
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  });
});
