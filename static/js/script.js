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

// Animasi
const revealElements = document.querySelectorAll(".reveal-element");

const observerOptions = {
  root: null,
  rootMargin: "0px",
  threshold: 0.1,
};

const revealObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("is-visible");

      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

revealElements.forEach((element) => {
  revealObserver.observe(element);
});
