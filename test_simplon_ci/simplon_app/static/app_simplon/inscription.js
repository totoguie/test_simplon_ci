const form = document.querySelector('.container');
        const popup = document.getElementById('popup');
        const closePopupBtn = document.getElementById('closePopupBtn');

        form.addEventListener('submit', function(event) {
            event.preventDefault();
            // Simulate an AJAX request or other server-side logic to check and save the data.
            // For this example, we'll just show the popup immediately.
            popup.style.display = 'block';
        });

        closePopupBtn.addEventListener('click', function() {
            popup.style.display = 'none';
        });