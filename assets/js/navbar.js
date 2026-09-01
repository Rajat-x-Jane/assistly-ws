(() => {
  document.documentElement.classList.add("reveal-ready");

  const contactConfig = {
    whatsappNumber: "918814030282",
    whatsappDisplay: "+91 88140 30282",
    email: "teamassistly@gmail.com",
  };

  const serviceLabels = {
    technology: "Technology",
    "brand-growth": "Brand & Growth",
    "business-compliance": "Business Compliance",
  };

  const stageLabels = {
    startup: "Startup",
    "small-business": "Small Business",
    "growing-business": "Growing Business",
  };

  const whatsappUrl = (message) =>
    `https://wa.me/${contactConfig.whatsappNumber}?text=${encodeURIComponent(message)}`;

  const mailtoUrl = (subject, body = "") => {
    const params = new URLSearchParams({ subject, body });
    return `mailto:${contactConfig.email}?${params.toString()}`;
  };

  const readableName = (name) =>
    name
      .replace(/[-_]/g, " ")
      .replace(/\b\w/g, (letter) => letter.toUpperCase());

  const headerMount = document.querySelector("[data-shell-header]");
  const footerMount = document.querySelector("[data-shell-footer]");

  if (headerMount) {
    headerMount.outerHTML = `
      <header class="site-header">
        <nav class="navbar container" aria-label="Main navigation">
          <a class="brand" href="/" aria-label="Assistly WS home">
            <span class="brand-mark"><img src="/assets/images/logo.png" alt="" width="38" height="38"></span>
            <span>Assistly WS</span>
          </a>
          <button class="nav-toggle" type="button" aria-label="Open navigation" aria-expanded="false" aria-controls="primary-navigation" data-nav-toggle>
            <span></span>
          </button>
          <div class="nav-panel" id="primary-navigation" data-nav-panel>
            <ul class="nav-primary" aria-label="Primary links">
              <li><a href="/" data-nav-link>Home</a></li>
              <li class="nav-services">
                <button class="mega-trigger" type="button" aria-expanded="false" aria-controls="services-menu" data-mega-toggle>Services</button>
                <div class="mega-panel" id="services-menu" data-mega-panel>
                  <div class="mega-grid">
                    <div class="mega-column">
                      <span class="mono-label">01 Technology</span>
                      <strong>Build the operating layer</strong>
                      <a href="/services/technology/">Website development</a>
                      <a href="/services/technology/">Apps and automation</a>
                      <a href="/services/technology/">E-commerce</a>
                      <a href="/services/technology/">UI and UX systems</a>
                      <a href="/services/technology/">View all -&gt;</a>
                    </div>
                    <div class="mega-column">
                      <span class="mono-label">02 Brand &amp; Growth</span>
                      <strong>Shape demand and trust</strong>
                      <a href="/services/brand-growth/">Brand identity</a>
                      <a href="/services/brand-growth/">SEO</a>
                      <a href="/services/brand-growth/">Marketing campaigns</a>
                      <a href="/services/brand-growth/">Packaging and creatives</a>
                      <a href="/services/brand-growth/">View all -&gt;</a>
                    </div>
                    <div class="mega-column">
                      <span class="mono-label">03 Compliance</span>
                      <strong>Keep the business in order</strong>
                      <a href="/services/business-compliance/">GST and tax assistance</a>
                      <a href="/services/business-compliance/">MCA filings</a>
                      <a href="/services/business-compliance/">MSME support</a>
                      <a href="/services/business-compliance/">Accounting coordination</a>
                      <a href="/services/business-compliance/">View all -&gt;</a>
                    </div>
                  </div>
                </div>
              </li>
              <li><a href="/solutions/" data-nav-link>Solutions</a></li>
              <li><a href="/work/" data-nav-link>Work</a></li>
              <li><a href="/about/" data-nav-link>About</a></li>
              <li><a href="/insights/" data-nav-link>Insights</a></li>
              <li><a href="/contact/" data-nav-link>Contact</a></li>
            </ul>
            <div class="nav-actions">
              <a class="schedule-link" href="/schedule/" data-nav-link>Schedule a Call</a>
              <a class="btn btn-primary nav-book" href="/book/" data-nav-link>Book a Service</a>
            </div>
          </div>
        </nav>
      </header>
    `;
  }

  if (footerMount) {
    footerMount.outerHTML = `
      <footer class="site-footer cornered">
        <div class="container footer-grid">
          <div>
            <a class="brand" href="/" aria-label="Assistly WS home">
              <span class="brand-mark"><img src="/assets/images/logo.png" alt="" width="38" height="38"></span>
              <span>Assistly WS</span>
            </a>
            <p>One business. One partner. Multiple solutions.</p>
          </div>
          <div>
            <h3>Services</h3>
            <nav class="footer-links" aria-label="Footer services">
              <a href="/services/technology/">Technology</a>
              <a href="/services/brand-growth/">Brand &amp; Growth</a>
              <a href="/services/business-compliance/">Business Compliance</a>
              <a href="/services/">All Services</a>
            </nav>
          </div>
          <div>
            <h3>Company</h3>
            <nav class="footer-links" aria-label="Footer company">
              <a href="/about/">About</a>
              <a href="/work/">Work</a>
              <a href="/insights/">Insights</a>
              <a href="/contact/">Contact</a>
            </nav>
          </div>
          <div>
            <h3>Start</h3>
            <nav class="footer-links" aria-label="Footer action links">
              <a href="/book/">Book a Service</a>
              <a href="/schedule/">Schedule a Call</a>
              <a href="/privacy/">Privacy</a>
              <a href="/terms/">Terms</a>
            </nav>
          </div>
        </div>
        <div class="container footer-bottom">
          <span>&copy; 2026 Assistly WS. All rights reserved.</span>
          <a href="/disclaimer/">Disclaimer</a>
        </div>
      </footer>
    `;
  }

  const buildBookMessage = (link) => {
    const href = link.getAttribute("href") || "/book/";
    let url;
    try {
      url = new URL(href, window.location.origin);
    } catch {
      url = new URL("/book/", window.location.origin);
    }

    const lines = ["Hi Assistly WS, I want to book a service."];
    const service = url.searchParams.get("service");
    const stage = url.searchParams.get("stage");
    const label = link.textContent.trim().replace(/\s+/g, " ");

    if (service && serviceLabels[service]) {
      lines.push(`Service: ${serviceLabels[service]}`);
    }
    if (stage && stageLabels[stage]) {
      lines.push(`Business stage: ${stageLabels[stage]}`);
    }
    if (label && !/^book a service$/i.test(label)) {
      lines.push(`Request: ${label}`);
    }
    lines.push(`Page: ${document.title}`);

    return lines.join("\n");
  };

  document.querySelectorAll('a[href="/book/"], a[href^="/book/?"]').forEach((link) => {
    link.href = whatsappUrl(buildBookMessage(link));
    link.target = "_blank";
    link.rel = "noopener";
  });

  const body = document.body;
  const navToggle = document.querySelector("[data-nav-toggle]");
  const navPanel = document.querySelector("[data-nav-panel]");
  const megaToggle = document.querySelector("[data-mega-toggle]");
  const megaPanel = document.querySelector("[data-mega-panel]");
  const navLinks = document.querySelectorAll("[data-nav-link]");

  const closeNav = () => {
    body.classList.remove("nav-open");
    navToggle?.setAttribute("aria-expanded", "false");
  };

  navToggle?.addEventListener("click", () => {
    const isOpen = body.classList.toggle("nav-open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });

  navLinks.forEach((link) => {
    link.addEventListener("click", closeNav);
  });

  megaToggle?.addEventListener("click", (event) => {
    event.preventDefault();
    const isOpen = megaPanel?.classList.toggle("is-open");
    megaToggle.setAttribute("aria-expanded", String(Boolean(isOpen)));
  });

  document.addEventListener("click", (event) => {
    if (!megaPanel || !megaToggle) return;
    if (event.target instanceof Node && !megaPanel.contains(event.target) && !megaToggle.contains(event.target)) {
      megaPanel.classList.remove("is-open");
      megaToggle.setAttribute("aria-expanded", "false");
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;
    closeNav();
    megaPanel?.classList.remove("is-open");
    megaToggle?.setAttribute("aria-expanded", "false");
  });

  const revealTargets = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window) {
    const revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.14 }
    );
    revealTargets.forEach((target) => revealObserver.observe(target));
  } else {
    revealTargets.forEach((target) => target.classList.add("is-visible"));
  }
  window.setTimeout(() => {
    revealTargets.forEach((target) => target.classList.add("is-visible"));
  }, 900);

  document.querySelectorAll("[data-faq]").forEach((faq) => {
    const button = faq.querySelector("[data-faq-button]");
    button?.addEventListener("click", () => {
      const isOpen = faq.classList.toggle("is-open");
      button.setAttribute("aria-expanded", String(isOpen));
    });
  });

  const bookingForm = document.querySelector("[data-booking-form]");
  if (bookingForm) {
    const serviceInputs = bookingForm.querySelectorAll('input[name="services"]');
    const budgetInputs = bookingForm.querySelectorAll('input[name="budget"]');
    const lockedSections = bookingForm.querySelectorAll("[data-progressive-section]");
    const status = bookingForm.querySelector("[data-form-status]");
    bookingForm.action = `mailto:${contactConfig.email}`;

    const params = new URLSearchParams(window.location.search);
    const requestedService = params.get("service");
    if (requestedService) {
      const firstMatchingService = Array.from(serviceInputs).find((input) => input.value === requestedService);
      if (firstMatchingService) {
        firstMatchingService.checked = true;
      }
    }

    const updateSections = () => {
      const hasService = Array.from(serviceInputs).some((input) => input.checked);
      lockedSections.forEach((section) => {
        section.classList.toggle("is-locked", !hasService);
        section.querySelectorAll("input, textarea, select").forEach((field) => {
          if (field instanceof HTMLInputElement || field instanceof HTMLTextAreaElement || field instanceof HTMLSelectElement) {
            field.disabled = !hasService;
          }
        });
      });
    };

    serviceInputs.forEach((input) => input.addEventListener("change", updateSections));
    budgetInputs.forEach((input) => input.addEventListener("change", () => {
      budgetInputs.forEach((item) => item.closest(".chip")?.classList.toggle("is-selected", item.checked));
    }));
    updateSections();

    bookingForm.addEventListener("submit", (event) => {
      event.preventDefault();

      if (!Array.from(serviceInputs).some((input) => input.checked)) {
        if (status) {
          status.textContent = "Please select at least one service before sending.";
        }
        return;
      }

      if (!bookingForm.checkValidity()) {
        bookingForm.reportValidity();
        return;
      }

      const message = buildFormMessage(bookingForm, "New service request");
      window.open(whatsappUrl(message), "_blank");
      if (status) {
        status.textContent = `WhatsApp opened for ${contactConfig.whatsappDisplay}. Email fallback: ${contactConfig.email}.`;
      }
    });
  }

  document.querySelectorAll("[data-contact-form]").forEach((form) => {
    const status = form.querySelector("[data-form-status]");
    form.action = `mailto:${contactConfig.email}`;
    form.addEventListener("submit", (event) => {
      event.preventDefault();

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      const message = buildFormMessage(form, "New enquiry");
      window.open(whatsappUrl(message), "_blank");
      if (status) {
        status.textContent = `WhatsApp opened for ${contactConfig.whatsappDisplay}. Email fallback: ${contactConfig.email}.`;
      }
    });
  });

  function buildFormMessage(form, title) {
    const groupedValues = new Map();

    Array.from(form.elements).forEach((control) => {
      if (!(control instanceof HTMLInputElement || control instanceof HTMLTextAreaElement || control instanceof HTMLSelectElement)) {
        return;
      }
      if (!control.name || control.disabled || ["button", "submit", "reset"].includes(control.type)) {
        return;
      }
      if ((control.type === "checkbox" || control.type === "radio") && !control.checked) {
        return;
      }

      const label = getControlLabel(control);
      const value = getControlValue(control);
      if (!value) return;

      const existingValues = groupedValues.get(label) || [];
      existingValues.push(value);
      groupedValues.set(label, existingValues);
    });

    const lines = [`${title} - Assistly WS`, ""];
    groupedValues.forEach((values, label) => {
      lines.push(`${label}: ${values.join(", ")}`);
    });
    lines.push(`Page: ${window.location.href}`);
    lines.push(`Email fallback: ${contactConfig.email}`);

    return lines.join("\n");
  }

  function getControlLabel(control) {
    if (control.name === "services") return "Services";
    if (control.name === "budget") return "Budget";

    const fieldLabel = control.closest(".field")?.querySelector(".field-label");
    if (fieldLabel?.textContent?.trim()) {
      return fieldLabel.textContent.trim();
    }

    return readableName(control.name);
  }

  function getControlValue(control) {
    if (control instanceof HTMLSelectElement) {
      return control.selectedOptions[0]?.textContent.trim() || control.value.trim();
    }

    if (control instanceof HTMLInputElement && (control.type === "checkbox" || control.type === "radio")) {
      return control.closest("label")?.textContent.trim() || control.value.trim();
    }

    return control.value.trim();
  }
})();
