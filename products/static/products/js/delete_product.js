$(document).on("click", ".confirm-delete-product", function () {
  $("#confirmDeleteModalProduct").attr("product-id", $(this).attr("id"));
});

$(document).on("click", "#confirmDeleteButtonModalProduct", function () {
  var product = $("#confirmDeleteButtonModalProduct")
    .closest(".modal")
    .attr("product-id");
  window.location = $("#".concat(product)).attr("href");
});
