const menu = document.getElementById('menu');
const header_menu = document.querySelector('.header_menu');

menu.addEventListener('click', () => {
    header_menu.style.display = header_menu.style.display === 'block' ? 'none' : 'block';
})
