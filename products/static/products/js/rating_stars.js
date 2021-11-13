const productStars = document.querySelectorAll(".review-card__title-stars");

productStars.forEach(rating => {
    const ratingValue = parseInt(rating.dataset.value);

    let stars = '';

    for (let i = 1; i < 6; i++) {
        if (i <= ratingValue) {
            stars += `<i class="fas fa-star"></i>`;
        } else {
            stars += `<i class="far fa-star"></i>`;
        }
    }

    rating.innerHTML = stars;
});