// Yang ini bagian yang ytta aja:)
const nav = document.getElementById("mainNavbar");
const breadCrumb = document.getElementById("mainBreadcrumb");
const breadCrumbTitle = document.getElementById("breadTitle");
const containerNav = document.getElementById("container-Navitem");
const pageId = document.body.dataset.pageId;

let lastScrollY = window.scrollY;

if (pageId === "home") {
  window.addEventListener("scroll", () => {
    if (lastScrollY > 100) {
      nav.classList.remove("fixed-top");
      breadCrumbTitle.classList.add("show");
      breadCrumbTitle.classList.remove("hidden");
      breadCrumb.classList.add("fixed-top");
      breadCrumb.style.fontSize = "20px";
      breadCrumb.style.padding = "1rem 2rem";
      breadCrumb.style.border = "none";
      breadCrumb.style.background = "var(--bg-dark)";
      breadCrumb.style.alignSelf = "center";
      breadCrumb.style.borderBottom = "1px solid var(--bg-tertiary)";
      breadCrumb.style.borderRadius = "0%";
      breadCrumb.style.fontFamily = "Verdana";
      containerNav.style.justifyContent = "center";
    } else {
      nav.classList.add("fixed-top");
      breadCrumbTitle.classList.remove("show");
      breadCrumbTitle.classList.add("hidden");
      breadCrumb.classList.remove("fixed-top");
      breadCrumb.style.background = "none";
      breadCrumb.style.fontSize = "16px";
      breadCrumb.style.padding = "1rem 1rem";
      breadCrumb.style.borderLeft = "4px solid var(--bg-tertiary)";
      breadCrumb.style.borderBottom = "1px solid var(--bg-tertiary)";
      breadCrumb.style.borderRadius = "12px";
      breadCrumb.style.fontFamily = "sans-serif";
      containerNav.style.justifyContent = "start";
    }

    lastScrollY = window.scrollY;
  });
}

// wkwk nerapin ilmu aja ini mah:)
const datetime = () => {
  let now = new Date();
  let hours = now.getHours();
  let minute = now.getMinutes();
  let second = now.getSeconds();

  const addZero = (num) => {
    if (num < 10) {
      return "0" + num;
    }

    return num;
  };

  hours = addZero(hours);
  minute = addZero(minute);
  second = addZero(second);

  const stringTime = `${hours}:${minute}:${second}`;
  document.getElementById("datetime").innerHTML = stringTime;
};

setInterval(datetime, 1000);
datetime();

const flasMsg = document.getElementById("flash-msg-container");

if (flasMsg) {
  setTimeout(() => {
    flasMsg.style.display = "none";
  }, 3000);
}

// Handle submit, atau prevent default yang ngereload halaman
const contactForm = document.getElementById("contact-form");

contactForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const nameEl = document.getElementById("name");
  const emailEl = document.getElementById("email");
  const textareaEl = document.getElementById("message");

  const name = nameEl.value;
  const email = emailEl.value;
  const message = textareaEl.value;

  const response = await fetch("/proses-data", {
    method: "POST",
    headers: {
      "Content-Type": "application/json; charset=utf-8",
    },
    body: JSON.stringify({ name, email, message }),
  });

  const data = await response.json();

  const msgEl = document.getElementById("msg");
  msgEl.textContent = data.msg;

  setTimeout(() => {
    msgEl.textContent = "";
  }, 5000);

  nameEl.value = "";
  emailEl.value = "";
  textareaEl.value = "";
});

const submitBtn = document.getElementById("submit-btn");
contactForm.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    contactForm.requestSubmit();
  }
});
