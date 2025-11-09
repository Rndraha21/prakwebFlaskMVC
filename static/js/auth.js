const input = document.getElementById("password");
const visibleIcon = document.getElementById("visible");

let inVisible = true;

function visibility() {
  input.type = "text";
  visibleIcon.src = "images/icons/invisibility.svg";
  inVisible = false;
}

function invisibility() {
  input.type = "password";
  visibleIcon.src = "images/icons/visibility.svg";
  inVisible = true;
}

visibleIcon.addEventListener("click", () => {
  if (inVisible) {
    visibility();
  } else {
    invisibility();
  }
});

// handle timeout flash message
const flashMsg = document.getElementById("flash-msg-container")

if (flashMsg) {
  setTimeout(() => {
    flashMsg.style.display = "none"
  }, 3000);
}
