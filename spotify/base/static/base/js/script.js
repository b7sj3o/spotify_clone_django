const dropdownTrigger = document.querySelector(".dropdown-trigger");
const dropdownMenu = document.querySelector(".dropdown-menu__profile");

dropdownTrigger.addEventListener("click", function() {
  dropdownMenu.classList.toggle("show");
});

document.addEventListener("click", function(event) {
  if (event.target.closest(".dropdown-trigger") || event.target.closest(".dropdown-menu__profile")) {
    return;
  }

  if (dropdownMenu.classList.contains("show")) {
    dropdownMenu.classList.remove("show");
  }
});

document.addEventListener("keydown", function(event) {
    if (event.key === "Escape") {
    if (dropdownMenu.classList.contains("show")) {
      dropdownMenu.classList.remove("show");
    }
  }
});


