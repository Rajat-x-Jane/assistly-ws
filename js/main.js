(function () {
  const header = document.querySelector("[data-header]");
  const navToggle = document.querySelector("[data-nav-toggle]");
  const navMenu = document.querySelector("[data-nav-menu]");
  const backTop = document.querySelector("[data-back-top]");
  const contactForm = document.querySelector("[data-contact-form]");

  const setScrolledState = () => {
    if (header) {
      header.classList.toggle("is-scrolled", window.scrollY > 12);
    }
    if (backTop) {
      backTop.classList.toggle("is-visible", window.scrollY > 520);
    }
  };

  setScrolledState();
  window.addEventListener("scroll", setScrolledState, { passive: true });

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", () => {
      const isOpen = navMenu.classList.toggle("is-open");
      navToggle.classList.toggle("is-open", isOpen);
      navToggle.setAttribute("aria-expanded", String(isOpen));
      navToggle.setAttribute("aria-label", isOpen ? "Close menu" : "Open menu");
      document.body.classList.toggle("nav-open", isOpen);
    });

    navMenu.addEventListener("click", (event) => {
      const link = event.target.closest("a");
      if (!link) return;
      navMenu.classList.remove("is-open");
      navToggle.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
      navToggle.setAttribute("aria-label", "Open menu");
      document.body.classList.remove("nav-open");
    });
  }

  const currentFile = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".primary-nav a[href]").forEach((link) => {
    const linkFile = link.getAttribute("href").split("#")[0];
    if (linkFile === currentFile) {
      link.classList.add("is-active");
      link.setAttribute("aria-current", "page");
    }
  });

  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (event) => {
      const target = document.querySelector(link.getAttribute("href"));
      if (!target) return;
      event.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  if (backTop) {
    backTop.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.16, rootMargin: "0px 0px -40px 0px" }
    );

    document.querySelectorAll(".reveal").forEach((item) => observer.observe(item));
  } else {
    document.querySelectorAll(".reveal").forEach((item) => item.classList.add("is-visible"));
  }

  if (contactForm) {
    contactForm.addEventListener("submit", (event) => {
      event.preventDefault();
      if (!contactForm.checkValidity()) {
        contactForm.reportValidity();
        return;
      }

      const formData = new FormData(contactForm);
      const name = String(formData.get("name") || "").trim();
      const business = String(formData.get("business") || "").trim();
      const service = String(formData.get("service") || "").trim();
      const note = String(formData.get("message") || "").trim();

      const lines = [
        "Hi Assistly WS, I want to start a project for my business. Please guide me.",
        name ? "Name: " + name : "",
        business ? "Business: " + business : "",
        service ? "Service: " + service : "",
        note ? "Project note: " + note : ""
      ].filter(Boolean);

      const url = "https://wa.me/918059134416?text=" + encodeURIComponent(lines.join("\n"));
      window.open(url, "_blank", "noopener");
    });
  }
})();
