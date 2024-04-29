'use strict';
const names = ['John', 'Paul', 'Jones'];

document.addEventListener('DOMContentLoaded', function() {
    const targetElement = document.getElementById('target');
    let htmlContent = '';

    for (const name of names) {
        htmlContent += `<li>${name}</li>`;
    }

    targetElement.innerHTML = htmlContent;
});
