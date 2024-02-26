// dashboard.js
function submitRating(button) {
    const shopId = button.closest('.shop-box').getAttribute('data-shop-id');
    const ratingForm = button.closest('.rating-form');
    const userRating = ratingForm.querySelector('input[name="rating"]').value;
    const userComment = ratingForm.querySelector('textarea[name="comment"]').value;

    // Send the rating data to the server using AJAX
    fetch('/submit_rating', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            shop_id: shopId,
            rating: userRating,
            comment: userComment,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Update the user's previous rating and comment
        const previousRatingDiv = button.closest('.shop-box').querySelector('.previous-rating');
        previousRatingDiv.querySelector('.user-rating').innerText = data.rating;
        previousRatingDiv.querySelector('.user-comment').innerText = data.comment;
    })
    .catch(error => console.error('Error:', error));
}

// Implement editRating and deleteRating functions similarly
