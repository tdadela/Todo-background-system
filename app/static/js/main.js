function hideElement(id) {
  var x = document.getElementById(id);
  x.style.display = "none";
}

function finishTask(id) {
  hideElement(id);
  fetch("/finish/" + id);
}

function deleteTask(id) {
  hideElement(id);
  fetch("/delete/" + id);
}
