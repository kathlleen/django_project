document.addEventListener("DOMContentLoaded", function() {
    const dropbtn = document.querySelector('.dropbtn');
    const dropdownContent = document.querySelector('.dropdown-content');

    // При клике на кнопку dropdown открываем/закрываем меню
    dropbtn.addEventListener('click', function(event) {
        event.preventDefault();
        dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
    });

    // Закрываем меню при клике вне dropdown
    document.addEventListener('click', function(event) {
        if (!dropbtn.contains(event.target) && !dropdownContent.contains(event.target)) {
            dropdownContent.style.display = 'none';
        }
    });
});
