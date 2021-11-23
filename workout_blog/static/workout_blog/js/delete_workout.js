$(document).on("click", ".confirm-delete-workout", function () {
  $("#confirmDeleteModalWorkout").attr("workout-id", $(this).attr("id"));
});

$(document).on("click", "#confirmDeleteButtonModalWorkout", function () {
  var workout = $("#confirmDeleteButtonModalWorkout")
    .closest(".modal")
    .attr("workout-id");
  window.location = $("#".concat(workout)).attr("href");
});
