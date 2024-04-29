'use strict';
const picArray = [
    {
        title: 'Title 1',
        caption: 'Caption 1',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis sodales enim eget leo condimentum vulputate. Sed lacinia consectetur fermentum. Vestibulum lobortis purus id nisi mattis posuere. Praesent sagittis justo quis nibh ullamcorper, eget elementum lorem consectetur. Pellentesque eu consequat justo, eu sodales eros.',
        image: {
            large: 'img/pic1.jpg',
            medium: 'thumbnails/pic1.jpg',
        },
    },
    {
        title: 'Title 2',
        caption: 'Caption 2',
        description: 'Donec dignissim tincidunt nisl, non scelerisque massa pharetra ut. Sed vel velit ante. Aenean quis viverra magna. Praesent eget cursus urna. Ut rhoncus interdum dolor non tincidunt. Sed vehicula consequat facilisis. Pellentesque pulvinar sem nisl, ac vestibulum erat rhoncus id. Vestibulum tincidunt sapien eu ipsum tincidunt pulvinar. ',
        image: {
            large: 'img/pic2.jpg',
            medium: 'thumbnails/pic2.jpg',
        },
    },
    // Add rest of the code here
];

document.addEventListener('DOMContentLoaded', function() {
    // Get the section element to append articles
    const articlesSection = document.getElementById('articles');

    picArray.forEach(pic => {
        const article = document.createElement('article');
        article.classList.add('card');

        const heading = document.createElement('h2');
        heading.textContent = pic.title;

        const figure = document.createElement('figure');

        // Create image
        const image = document.createElement('img');
        image.src = pic.image.medium;
        image.alt = pic.title;

        const figcaption = document.createElement('figcaption');
        figcaption.textContent = pic.caption;

        const description = document.createElement('p');
        description.textContent = pic.description;

        figure.appendChild(image);
        figure.appendChild(figcaption);
        article.appendChild(heading);
        article.appendChild(figure);
        article.appendChild(description);
        articlesSection.appendChild(article);
    });
});
