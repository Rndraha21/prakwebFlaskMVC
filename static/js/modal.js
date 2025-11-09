const detailBtn1 = document.getElementById("detail-proyek-1");
const detailBtn2 = document.getElementById("detail-proyek-2");
const closeIcon = document.querySelectorAll(".close-icon");

const modal1 = document.getElementById("modal-proyek-1");
const modal2 = document.getElementById("modal-proyek-2");

detailBtn1.addEventListener("click", () => {
  modal1.style.display = "flex";
});

detailBtn2.addEventListener("click", () => {
  modal2.style.display = "flex";
});

function closeModal(modal) {
  const container = modal.querySelector(".modal-container");
  container.classList.add("closing");

  container.addEventListener(
    "animationend",
    () => {
      modal.style.display = "none";
      container.classList.remove("closing");
    },
    { once: true }
  );
}

closeIcon.forEach((icon) => {
  icon.addEventListener("click", (e) => {
    e.preventDefault();
    closeModal(modal1);
    closeModal(modal2);
  });
});

window.onclick = (e) => {
  if (e.target === modal1) closeModal(modal1);
  if (e.target === modal2) closeModal(modal2);
};
