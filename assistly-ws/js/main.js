(function () {
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));
  const rupee = new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
    maximumFractionDigits: 0
  });

  function encodeMessage(message) {
    return encodeURIComponent(message.trim());
  }

  function whatsappLink(message) {
    return `https://wa.me/918059134416?text=${encodeMessage(message)}`;
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, (char) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      "\"": "&quot;",
      "'": "&#039;"
    }[char]));
  }

  function initHeader() {
    const header = $(".site-header");
    const progress = $(".scroll-progress");
    const toggle = $(".mobile-toggle");
    const mobilePanel = $("#mobilePanel");
    const megaButtons = $$("[data-mega-trigger]");

    const updateScroll = () => {
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - window.innerHeight;
      if (header) header.classList.toggle("is-scrolled", scrollTop > 10);
      if (progress) progress.style.width = height > 0 ? `${(scrollTop / height) * 100}%` : "0%";
    };

    updateScroll();
    window.addEventListener("scroll", updateScroll, { passive: true });

    if (toggle && mobilePanel) {
      toggle.addEventListener("click", () => {
        const isOpen = toggle.getAttribute("aria-expanded") === "true";
        toggle.setAttribute("aria-expanded", String(!isOpen));
        mobilePanel.classList.toggle("is-open", !isOpen);
        document.body.classList.toggle("menu-open", !isOpen);
      });
    }

    megaButtons.forEach((button) => {
      const target = document.getElementById(button.getAttribute("aria-controls"));
      if (!target) return;

      button.addEventListener("click", (event) => {
        event.preventDefault();
        const isOpen = button.getAttribute("aria-expanded") === "true";
        megaButtons.forEach((other) => {
          const otherTarget = document.getElementById(other.getAttribute("aria-controls"));
          other.setAttribute("aria-expanded", "false");
          if (otherTarget) otherTarget.classList.remove("is-open");
        });
        button.setAttribute("aria-expanded", String(!isOpen));
        target.classList.toggle("is-open", !isOpen);
      });
    });

    document.addEventListener("click", (event) => {
      if (event.target.closest("[data-mega-root]")) return;
      megaButtons.forEach((button) => {
        const target = document.getElementById(button.getAttribute("aria-controls"));
        button.setAttribute("aria-expanded", "false");
        if (target) target.classList.remove("is-open");
      });
    });

    document.addEventListener("keydown", (event) => {
      if (event.key !== "Escape") return;
      megaButtons.forEach((button) => {
        const target = document.getElementById(button.getAttribute("aria-controls"));
        button.setAttribute("aria-expanded", "false");
        if (target) target.classList.remove("is-open");
      });
      if (toggle && mobilePanel) {
        toggle.setAttribute("aria-expanded", "false");
        mobilePanel.classList.remove("is-open");
        document.body.classList.remove("menu-open");
      }
    });
  }

  function initReveal() {
    const items = $$(".reveal");
    if (!items.length) return;

    if (!("IntersectionObserver" in window)) {
      items.forEach((item) => item.classList.add("is-visible"));
      return;
    }

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

    items.forEach((item) => observer.observe(item));
  }

  function initHeroSlider() {
    const slider = $("[data-hero-slider]");
    if (!slider) return;

    const slides = $$("[data-hero-slide]", slider);
    const dots = $$("[data-hero-dot]", slider);
    const prev = $("[data-hero-prev]", slider);
    const next = $("[data-hero-next]", slider);
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const delay = 4500;
    let activeIndex = 0;
    let timer = null;

    const showSlide = (index) => {
      if (!slides.length) return;
      activeIndex = (index + slides.length) % slides.length;

      slides.forEach((slide, slideIndex) => {
        const isActive = slideIndex === activeIndex;
        slide.classList.toggle("is-active", isActive);
        slide.setAttribute("aria-hidden", String(!isActive));
      });

      dots.forEach((dot, dotIndex) => {
        const isActive = dotIndex === activeIndex;
        dot.classList.toggle("is-active", isActive);
        dot.setAttribute("aria-current", String(isActive));
      });
    };

    const stop = () => {
      if (!timer) return;
      window.clearInterval(timer);
      timer = null;
    };

    const start = () => {
      if (reduceMotion || slides.length < 2) return;
      stop();
      timer = window.setInterval(() => showSlide(activeIndex + 1), delay);
    };

    dots.forEach((dot, index) => {
      dot.addEventListener("click", () => {
        showSlide(index);
        start();
      });
    });

    if (prev) {
      prev.addEventListener("click", () => {
        showSlide(activeIndex - 1);
        start();
      });
    }

    if (next) {
      next.addEventListener("click", () => {
        showSlide(activeIndex + 1);
        start();
      });
    }

    slider.addEventListener("mouseenter", stop);
    slider.addEventListener("mouseleave", start);
    slider.addEventListener("focusin", stop);
    slider.addEventListener("focusout", start);

    document.addEventListener("visibilitychange", () => {
      if (document.hidden) stop();
      else start();
    });

    showSlide(0);
    start();
  }

  function initFaqs() {
    $$(".faq-question").forEach((button) => {
      const answer = document.getElementById(button.getAttribute("aria-controls"));
      if (!answer) return;

      button.addEventListener("click", () => {
        const isOpen = button.getAttribute("aria-expanded") === "true";
        button.setAttribute("aria-expanded", String(!isOpen));
        answer.classList.toggle("is-open", !isOpen);
      });
    });
  }

  function initBackToTop() {
    const button = $(".back-to-top");
    if (!button) return;

    const update = () => {
      button.classList.toggle("is-visible", window.scrollY > 700);
    };

    button.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
    window.addEventListener("scroll", update, { passive: true });
    update();
  }

  function initTimeline() {
    const timeline = $(".timeline");
    const fill = $(".timeline-fill");
    if (!timeline || !fill) return;

    const update = () => {
      const rect = timeline.getBoundingClientRect();
      const viewport = window.innerHeight;
      const progress = Math.min(1, Math.max(0, (viewport * 0.75 - rect.top) / rect.height));
      fill.style.height = `${Math.round(progress * 100)}%`;
    };

    update();
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
  }

  function initContactForm() {
    const form = $("[data-contact-form]");
    if (!form) return;

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const data = new FormData(form);
      const name = data.get("name") || "";
      const mobile = data.get("mobile") || "";
      const business = data.get("business") || "";
      const service = data.get("service") || "";
      const budget = data.get("budget") || "";
      const message = data.get("message") || "";

      const text = [
        "Hi Assistly WS, I want a free consultation.",
        `Name: ${name}`,
        `Mobile: ${mobile}`,
        `Business type: ${business}`,
        `Required service: ${service}`,
        `Budget: ${budget}`,
        `Message: ${message}`
      ].join("\n");

      window.open(whatsappLink(text), "_blank", "noopener,noreferrer");
    });
  }

  function numberValue(form, name, fallback = 0) {
    const value = Number(new FormData(form).get(name));
    return Number.isFinite(value) ? value : fallback;
  }

  function yes(form, name) {
    return new FormData(form).get(name) === "yes" || new FormData(form).get(name) === "on";
  }

  function showResult(form, html) {
    const result = $(".result-card", form.closest(".tool-shell") || document);
    if (!result) return;
    result.innerHTML = html;
  }

  function websiteCost(form) {
    const data = new FormData(form);
    const typeBase = {
      basic: 4999,
      business: 8999,
      ecommerce: 18999,
      custom: 24999
    };
    const designAdd = {
      simple: 0,
      premium: 3000,
      custom: 7000
    };
    const pages = Math.max(1, numberValue(form, "pages", 5));
    let low = typeBase[data.get("websiteType")] || 4999;
    low += Math.max(0, pages - 5) * 800;
    low += designAdd[data.get("designLevel")] || 0;
    if (yes(form, "contactForm")) low += 800;
    if (yes(form, "blog")) low += 1200;
    if (yes(form, "seo")) low += 1800;
    if (yes(form, "content")) low += pages * 450;
    if (data.get("urgency") === "fast") low *= 1.18;
    const high = low * 1.35;
    const packageName = low < 9000 ? "Starter Website" : low < 18000 ? "Growth Website" : "Custom Website";

    showResult(form, `
      <h3>Estimated website cost</h3>
      <div class="big-result">${rupee.format(low)} - ${rupee.format(high)}</div>
      <p class="muted">Suggested package: <strong>${packageName}</strong>. This is a planning estimate, not a final quote.</p>
      <a class="btn small" href="${whatsappLink("Hi Assistly WS, I used the website cost calculator. Please share an exact quote for my business website.")}" target="_blank" rel="noopener">Get exact quote on WhatsApp</a>
    `);
  }

  function gstLateFee(form) {
    const days = Math.max(0, numberValue(form, "days", 0));
    const tax = Math.max(0, numberValue(form, "taxAmount", 0));
    const nilReturn = yes(form, "nilReturn");
    const lateFeePerDay = nilReturn ? 20 : 50;
    const lateFee = days * lateFeePerDay;
    const interest = (tax * 0.18 * days) / 365;

    showResult(form, `
      <h3>Estimated late fee and interest</h3>
      <div class="big-result">${rupee.format(lateFee + interest)}</div>
      <p class="muted">Late fee estimate: ${rupee.format(lateFee)}. Interest estimate: ${rupee.format(interest)}. Actual rules may vary by return type and notifications.</p>
      <a class="btn small" href="${whatsappLink("Hi Assistly WS, I need help checking GST late fee and filing my return.")}" target="_blank" rel="noopener">Check GST return support</a>
    `);
  }

  function tdsCalculator(form) {
    const amount = Math.max(0, numberValue(form, "amount", 0));
    const rate = Math.max(0, numberValue(form, "rate", 10));
    const tds = (amount * rate) / 100;
    const net = amount - tds;

    showResult(form, `
      <h3>TDS estimate</h3>
      <div class="big-result">${rupee.format(tds)}</div>
      <p class="muted">Net payable after TDS: <strong>${rupee.format(net)}</strong>. Confirm section, PAN status, and threshold before deduction.</p>
      <a class="btn small" href="${whatsappLink("Hi Assistly WS, I need help with TDS/TCS return or TDS calculation.")}" target="_blank" rel="noopener">Ask for TDS help</a>
    `);
  }

  function adBudget(form) {
    const budget = Math.max(0, numberValue(form, "budget", 0));
    const metaShare = Math.max(0, Math.min(100, numberValue(form, "metaShare", 50)));
    const cpc = Math.max(1, numberValue(form, "cpc", 20));
    const conversionRate = Math.max(0.1, numberValue(form, "conversionRate", 3));
    const metaBudget = (budget * metaShare) / 100;
    const googleBudget = budget - metaBudget;
    const clicks = budget / cpc;
    const leads = clicks * (conversionRate / 100);

    showResult(form, `
      <h3>Planning estimate</h3>
      <div class="big-result">${rupee.format(budget / 30)} / day</div>
      <p class="muted">Meta Ads: ${rupee.format(metaBudget)}. Google Ads: ${rupee.format(googleBudget)}. Estimated clicks: ${Math.round(clicks)}. Possible enquiries at ${conversionRate}% conversion: ${Math.round(leads)}.</p>
      <a class="btn small" href="${whatsappLink("Hi Assistly WS, I used the ad budget calculator. Please help me plan Meta Ads or Google Ads.")}" target="_blank" rel="noopener">Plan my ads</a>
    `);
  }

  function profitMargin(form) {
    const revenue = Math.max(0, numberValue(form, "revenue", 0));
    const cost = Math.max(0, numberValue(form, "cost", 0));
    const extra = Math.max(0, numberValue(form, "extra", 0));
    const profit = revenue - cost - extra;
    const margin = revenue > 0 ? (profit / revenue) * 100 : 0;
    const markup = cost > 0 ? (profit / cost) * 100 : 0;

    showResult(form, `
      <h3>Profit result</h3>
      <div class="big-result">${rupee.format(profit)}</div>
      <p class="muted">Profit margin: <strong>${margin.toFixed(1)}%</strong>. Markup on cost: <strong>${markup.toFixed(1)}%</strong>.</p>
      <a class="btn small" href="${whatsappLink("Hi Assistly WS, I need help reviewing pricing, accounting, or profit margin for my business.")}" target="_blank" rel="noopener">Review my numbers</a>
    `);
  }

  function logoBrief(form) {
    const data = new FormData(form);
    const rawBrand = data.get("brand") || "Brand name";
    const brand = escapeHtml(rawBrand);
    const audience = escapeHtml(data.get("audience") || "target customers");
    const style = escapeHtml(data.get("style") || "clean and modern");
    const colors = escapeHtml(data.get("colors") || "open to suggestions");
    const notes = escapeHtml(data.get("notes") || "No extra notes");

    showResult(form, `
      <h3>Logo brief draft</h3>
      <div class="generated-box">
        <p><strong>Brand:</strong> ${brand}</p>
        <p><strong>Audience:</strong> ${audience}</p>
        <p><strong>Preferred style:</strong> ${style}</p>
        <p><strong>Color direction:</strong> ${colors}</p>
        <p><strong>Notes:</strong> ${notes}</p>
      </div>
      <a class="btn small" href="${whatsappLink(`Hi Assistly WS, I created this logo brief for ${rawBrand}. Please guide me on logo design and branding.`)}" target="_blank" rel="noopener">Send brief on WhatsApp</a>
    `);
  }

  function initChecklistTool(form) {
    const checks = $$("input[type='checkbox']", form);
    const output = $(".result-card", form.closest(".tool-shell") || document);
    const progress = $(".progress-track span", form);

    const update = () => {
      const done = checks.filter((check) => check.checked).length;
      const percent = checks.length ? Math.round((done / checks.length) * 100) : 0;
      if (progress) progress.style.width = `${percent}%`;
      if (output) {
        output.innerHTML = `
          <h3>Checklist progress</h3>
          <div class="big-result">${percent}% complete</div>
          <p class="muted">${done} of ${checks.length} SEO basics marked complete. Use this as a simple readiness check before deeper SEO work.</p>
        `;
      }
    };

    checks.forEach((check) => check.addEventListener("change", update));
    update();
  }

  function initTools() {
    const handlers = {
      "website-cost": websiteCost,
      "gst-late-fee": gstLateFee,
      "tds-calculator": tdsCalculator,
      "ad-budget": adBudget,
      "profit-margin": profitMargin,
      "logo-brief": logoBrief
    };

    $$("[data-tool-form]").forEach((form) => {
      const type = form.dataset.toolForm;
      if (type === "seo-checklist") {
        initChecklistTool(form);
        return;
      }

      const handler = handlers[type];
      if (!handler) return;
      form.addEventListener("submit", (event) => {
        event.preventDefault();
        handler(form);
      });
      handler(form);
    });
  }

  function initActiveNav() {
    const current = window.location.pathname.split("/").pop() || "index.html";
    $$(".nav-link, .mobile-panel a").forEach((link) => {
      const href = link.getAttribute("href") || "";
      if (href.endsWith(current)) link.classList.add("is-active");
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    initHeader();
    initReveal();
    initHeroSlider();
    initFaqs();
    initBackToTop();
    initTimeline();
    initContactForm();
    initTools();
    initActiveNav();
  });
})();
