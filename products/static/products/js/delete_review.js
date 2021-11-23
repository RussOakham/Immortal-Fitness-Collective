$(document).on("click", ".confirm-delete", function () {
  $("#confirmDeleteModalReview").attr("review-id", $(this).attr("id"));
});

$(document).on("click", "#confirmDeleteButtonModalReview", function () {
  var review = $("#confirmDeleteButtonModalReview")
    .closest(".modal")
    .attr("review-id");
  window.location = $("#".concat(review)).attr("href");
});
