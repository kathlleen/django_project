document.querySelector('.filter-btn').addEventListener('click', function() {
    var dropdownContent = document.querySelector('.dropdown-content');
    dropdownContent.classList.toggle('show'); // Переключение класса "show"
});

document.addEventListener('click', function(event) {
    var dropdown = document.querySelector('.dropdown');
    if (!dropdown.contains(event.target)) {
        document.querySelector('.dropdown-content').classList.remove('show');
    }
});
