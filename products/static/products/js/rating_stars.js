const productStars = document.querySelectorAll(".review-card__title-stars");

productStars.forEach(rating => {
    const ratingValue = parseInt(rating.dataset.value);
    const ratingStar = ratingValue;

    let stars = '';

    for (let i = 1; i < 6; i++) {
        if (i <= ratingStar) {
            stars += `<i class="fas fa-star"></i>`;
        } else {
            stars += `<i class="far fa-star"></i>`;
        }
    }

    rating.innerHTML = stars;
});