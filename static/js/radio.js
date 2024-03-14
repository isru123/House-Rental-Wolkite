function unclickRadio() {
    $("input:radio").prop("checked", false);
}
function clickRadio(inputElement) {
  $("#" + inputElement).prop("checked", true);
}
function removeActive() {
$(".card").removeClass("active");
}
function makeActive(element) {
$("#" + element + "-card").addClass("active");
}
$(document).ready(function () {
$('input:radio').change(function () {//Clicking input radio
  var radioClicked = $(this).attr('id');
  unclickRadio();
  removeActive();
  clickRadio(radioClicked);
  makeActive(radioClicked);
});
$(".card").click(function () {//Clicking the card
  var inputElement = $(this).find('input[type=radio]').attr('id');
  unclickRadio();
  removeActive();
  makeActive(inputElement);
  clickRadio(inputElement);
});
});