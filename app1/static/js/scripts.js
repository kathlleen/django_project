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

    document.addEventListener('DOMContentLoaded', function() {
        const cartBtn = document.getElementById('cart-btn');
        const cartModal = document.getElementById('cartModal');
        const closeModal = document.getElementById('closeModal');

        // Открытие модального окна при клике на кнопку корзины
        cartBtn.addEventListener('click', function() {
            cartModal.style.display = 'block';
        });

        // Закрытие модального окна при клике на кнопку закрытия
        closeModal.addEventListener('click', function() {
            cartModal.style.display = 'none';
        });

        // Закрытие модального окна при клике вне области модального окна
        window.addEventListener('click', function(event) {
            if (event.target === cartModal) {
                cartModal.style.display = 'none';
            }
        });
    });
