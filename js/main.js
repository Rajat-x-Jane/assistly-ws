(function () {
  "use strict";

  const navToggle = document.querySelector("[data-nav-toggle]");
  const navMenu = document.querySelector("[data-nav-menu]");
  const navLinks = document.querySelectorAll("[data-nav-link]");
  const currentPage = window.location.pathname.split("/").pop() || "index.html";

  navLinks.forEach((link) => {
    const href = link.getAttribute("href");
    const isBlogPage = currentPage.startsWith("blog") && href === "blog.html";
    if (href === currentPage || isBlogPage || (currentPage === "" && href === "index.html")) {
      link.classList.add("is-active");
      link.setAttribute("aria-current", "page");
    }
  });

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", () => {
      const isOpen = navMenu.classList.toggle("is-open");
      navToggle.classList.toggle("is-active", isOpen);
      navToggle.setAttribute("aria-expanded", String(isOpen));
      navToggle.setAttribute("aria-label", isOpen ? "Close navigation menu" : "Open navigation menu");
      document.body.classList.toggle("nav-open", isOpen);
    });

    navLinks.forEach((link) => {
      link.addEventListener("click", () => {
        navMenu.classList.remove("is-open");
        navToggle.classList.remove("is-active");
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.setAttribute("aria-label", "Open navigation menu");
        document.body.classList.remove("nav-open");
      });
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && navMenu.classList.contains("is-open")) {
        navMenu.classList.remove("is-open");
        navToggle.classList.remove("is-active");
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.setAttribute("aria-label", "Open navigation menu");
        document.body.classList.remove("nav-open");
        navToggle.focus();
      }
    });
  }

  const yearTargets = document.querySelectorAll("[data-year]");
  yearTargets.forEach((target) => {
    target.textContent = new Date().getFullYear();
  });

  const slider = document.querySelector("[data-hero-slider]");
  if (slider) {
    const slides = Array.from(slider.querySelectorAll("[data-slide]"));
    const dots = Array.from(slider.querySelectorAll("[data-slide-dot]"));
    const prevButton = slider.querySelector("[data-prev-slide]");
    const nextButton = slider.querySelector("[data-next-slide]");
    const intervalMs = 5000;
    let activeIndex = 0;
    let timer = null;

    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function showSlide(index) {
      activeIndex = (index + slides.length) % slides.length;

      slides.forEach((slide, slideIndex) => {
        const isActive = slideIndex === activeIndex;
        slide.classList.toggle("is-active", isActive);
        slide.setAttribute("aria-hidden", String(!isActive));
      });

      dots.forEach((dot, dotIndex) => {
        const isActive = dotIndex === activeIndex;
        dot.classList.toggle("is-active", isActive);
        dot.setAttribute("aria-selected", String(isActive));
      });
    }

    function startTimer() {
      if (prefersReducedMotion || timer) return;
      timer = window.setInterval(() => {
        showSlide(activeIndex + 1);
      }, intervalMs);
    }

    function stopTimer() {
      if (!timer) return;
      window.clearInterval(timer);
      timer = null;
    }

    prevButton?.addEventListener("click", () => {
      showSlide(activeIndex - 1);
      stopTimer();
      startTimer();
    });

    nextButton?.addEventListener("click", () => {
      showSlide(activeIndex + 1);
      stopTimer();
      startTimer();
    });

    dots.forEach((dot, dotIndex) => {
      dot.addEventListener("click", () => {
        showSlide(dotIndex);
        stopTimer();
        startTimer();
      });
    });

    slider.addEventListener("mouseenter", stopTimer);
    slider.addEventListener("mouseleave", startTimer);
    slider.addEventListener("focusin", stopTimer);
    slider.addEventListener("focusout", startTimer);

    showSlide(activeIndex);
    startTimer();
  }

  const revealTargets = document.querySelectorAll(".reveal");
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
      { threshold: 0.14 }
    );

    revealTargets.forEach((target) => observer.observe(target));
  } else {
    revealTargets.forEach((target) => target.classList.add("is-visible"));
  }

  const contactForm = document.querySelector("[data-contact-form]");
  const formStatus = document.querySelector("[data-form-status]");
  if (contactForm && formStatus) {
    contactForm.addEventListener("submit", () => {
      formStatus.textContent = "Opening your email app to send this inquiry.";
    });
  }
})();
