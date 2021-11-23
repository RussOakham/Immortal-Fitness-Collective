$(document).on("click", ".confirm-delete", function () {
  $("#confirmDeleteModal").attr("review-id", $(this).attr("id"));
});

$(document).on("click", "#confirmDeleteButtonModal", function () {
  var review = $("#confirmDeleteButtonModal")
    .closest(".modal")
    .attr("review-id");
  window.location = $("#".concat(review)).attr("href");
});
