// Tehdään dynaaminen lista
const listItems = [
    'First item',
    'Second item',
    'Third item'
];

const targetElement = document.getElementById('target');

listItems.forEach(itemText => {
    const listItem = document.createElement('li');
    listItem.textContent = itemText;
    targetElement.appendChild(listItem);
});

const secondListItem = targetElement.children[1];
secondListItem.classList.add('my-item');
