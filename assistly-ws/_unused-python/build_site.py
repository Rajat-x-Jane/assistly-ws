from __future__ import annotations

import html
import json
import os
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
DOMAIN = "https://assistlyws.in"
SITE_NAME = "Assistly WS"
TAGLINE = "Your Growth, Our Mission"
FOUNDER = "Rajat Tomar"
EMAIL = "teamassistly@gmail.com"
PHONE = "+91 8059134416"
WHATSAPP = "https://wa.me/918059134416"
LOCATION = "Sonipat / Delhi NCR, Haryana"
SERVICE_AREA = "India"
UPDATED = "2026-05-10"
UPDATED_LABEL = "May 10, 2026"


def esc(value: str) -> str:
    return html.escape(str(value), quote=True)


def page_url(path: str) -> str:
    if path == "index.html":
        return f"{DOMAIN}/"
    return f"{DOMAIN}/{path}"


def rel_link(current: str, target: str) -> str:
    current_dir = os.path.dirname(current) or "."
    return os.path.relpath(target, current_dir).replace("\\", "/")


def asset(current: str, target: str) -> str:
    return rel_link(current, target)


def wa(message: str) -> str:
    return f"{WHATSAPP}?text={quote(message)}"


def json_ld(data: dict) -> str:
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "</script>"


def icon(name: str = "spark") -> str:
    icons = {
        "web": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 5h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2Zm0 4v8h16V9H4Zm2-3v1h12V6H6Z"/></svg>',
        "doc": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6 2h9l5 5v15H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2Zm8 1.8V8h4.2L14 3.8ZM8 12h8v2H8v-2Zm0 4h8v2H8v-2Z"/></svg>',
        "calc": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M7 2h10a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2Zm0 4v4h10V6H7Zm1 7v2h2v-2H8Zm4 0v2h2v-2h-2Zm4 0v2h1v-2h-1Zm-8 4v2h2v-2H8Zm4 0v2h2v-2h-2Zm4 0v2h1v-2h-1Z"/></svg>',
        "web-calc": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 4h16a2 2 0 0 1 2 2v8H2V6a2 2 0 0 1 2-2Zm0 4v4h16V8H4Zm2 8h6v2H6v-2Zm0 3h4v2H6v-2Zm9-3h2v2h-2v-2Zm3 0h2v2h-2v-2Zm-3 3h2v2h-2v-2Zm3 0h2v2h-2v-2Z"/></svg>',
        "gst": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6 2h9l5 5v15H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2Zm8 1.8V8h4.2L14 3.8ZM8 11h8v2H8v-2Zm0 4h5v2H8v-2Zm8.5 0H19v2h-1.5v1.5h-2V17H14v-2h1.5v-1.5h2V15Z"/></svg>',
        "tds": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M5 3h14v18H5V3Zm3 4v2h8V7H8Zm0 4v2h5v-2H8Zm0 4v2h8v-2H8Zm8.8-3.8 1.4 1.4-5 5-1.4-1.4 5-5Zm-4.3.3a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm7 5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z"/></svg>',
        "ads": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 10v4h3l8 4V6l-8 4H4Zm14-2v8h2V8h-2ZM7 16H5l1 5h3l-2-5Z"/></svg>',
        "seo": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M10 3a7 7 0 0 1 5.65 11.13l4.61 4.61-1.52 1.52-4.61-4.61A7 7 0 1 1 10 3Zm0 2a5 5 0 1 0 0 10 5 5 0 0 0 0-10Zm2.9 3.8 1.2 1.2-4.2 4.2-2.2-2.2 1.2-1.2 1 1 3-3Z"/></svg>',
        "profit": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 19h16v2H4v-2Zm1-3.4 5.2-5.2 3.2 3.2L19 8v3.5h2V4.6h-6.9v2H17.6l-4.2 4.2-3.2-3.2-6.6 6.6L5 15.6Zm2-11.6h4v2H7v2H5V6a2 2 0 0 1 2-2Z"/></svg>',
        "brief": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M5 4h9l5 5v11H5V4Zm8 1.8V10h4.2L13 5.8ZM8 13h7v2H8v-2Zm0 4h5v2H8v-2Zm11-1 1 3 3 1-3 1-1 3-1-3-3-1 3-1 1-3Z"/></svg>',
        "brand": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2 14 8l6 2-6 2-2 6-2-6-6-2 6-2 2-6Zm-6 13h2v5H6v-5Zm5-1h2v6h-2v-6Zm5 2h2v4h-2v-4Z"/></svg>',
        "compliance": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2 20 5v6c0 5-3.4 9.5-8 11-4.6-1.5-8-6-8-11V5l8-3Zm-1 13.2 5-5-1.4-1.4-3.6 3.6-1.6-1.6L8 12.2l3 3Z"/></svg>',
        "accounting": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6 3h12a2 2 0 0 1 2 2v16H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2Zm2 4v3h8V7H8Zm0 6v2h2v-2H8Zm4 0v2h4v-2h-4Zm-4 4v2h2v-2H8Zm4 0v2h4v-2h-4Z"/></svg>',
        "registration": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 5h16v14H4V5Zm2 2v10h12V7H6Zm2 2h4v4H8V9Zm6 .5h3v2h-3v-2Zm0 3h3v2h-3v-2ZM8 15h7v1H8v-1Z"/></svg>',
        "growth": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="m4 17.6 5.4-5.4 3.4 3.4L20 8.4V13h2V5h-8v2h4.6l-5.8 5.8-3.4-3.4L2.6 16.2 4 17.6ZM4 20h16v2H4v-2Z"/></svg>',
        "support": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a8 8 0 0 1 8 8v3a4 4 0 0 1-4 4h-2v-2h2a2 2 0 0 0 2-2v-3a6 6 0 0 0-12 0v4H4v-4a8 8 0 0 1 8-8Zm-1 16h2v2h3v2h-5a2 2 0 0 1-2-2v-2h2Zm-5-6h2v5H6a3 3 0 0 1 0-6v1Zm12 0v-1a3 3 0 0 1 0 6h-2v-5h2Z"/></svg>',
        "spark": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="m12 2 1.8 6.2L20 10l-6.2 1.8L12 18l-1.8-6.2L4 10l6.2-1.8L12 2Zm7 13 1 3 3 1-3 1-1 3-1-3-3-1 3-1 1-3ZM5 14l.8 2.2L8 17l-2.2.8L5 20l-.8-2.2L2 17l2.2-.8L5 14Z"/></svg>',
    }
    return icons.get(name, icons["spark"])


def organization_schema() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": SITE_NAME,
        "url": DOMAIN,
        "slogan": TAGLINE,
        "email": EMAIL,
        "telephone": PHONE,
        "founder": {"@type": "Person", "name": FOUNDER},
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Sonipat",
            "addressRegion": "Haryana",
            "addressCountry": "IN",
        },
        "areaServed": {"@type": "Country", "name": "India"},
    }


def website_schema() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": SITE_NAME,
        "url": DOMAIN,
        "description": "Founder-led website, marketing, compliance, accounting support, free tools, and templates for Indian small businesses.",
        "publisher": {"@type": "Organization", "name": SITE_NAME},
    }


def breadcrumb_schema(items: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": index + 1,
                "name": name,
                "item": page_url(path),
            }
            for index, (name, path) in enumerate(items)
        ],
    }


def faq_schema(faqs: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faqs
        ],
    }


TOOLS = [
    {
        "slug": "website-cost-calculator",
        "name": "Website Cost Calculator",
        "kind": "website-cost",
        "title": "Website Cost Calculator India | Assistly WS",
        "meta": "Estimate website design cost in India based on pages, design level, SEO setup, content writing, blog, and delivery urgency.",
        "h1": "Website Cost Calculator for Indian Small Businesses",
        "short": "Estimate a practical website budget before you request a quote.",
        "summary": "A website cost calculator helps you plan a realistic budget by combining page count, design complexity, content, SEO setup, and delivery urgency.",
        "service": "services/website-design.html",
        "template": "templates/website-proposal-template.html",
        "blog": "blog/website-cost-india.html",
        "icon": "web-calc",
    },
    {
        "slug": "gst-late-fee-calculator",
        "name": "GST Late Fee Calculator",
        "kind": "gst-late-fee",
        "title": "GST Late Fee Calculator India | Assistly WS",
        "meta": "Estimate GST return late fee and interest for planning. Use this free GST calculator before speaking with a GST support provider.",
        "h1": "GST Late Fee Calculator",
        "short": "Check a planning estimate for delayed GST return filing.",
        "summary": "The GST late fee calculator gives a rough planning estimate for delayed return filing based on delay days, tax amount, and nil-return status.",
        "service": "services/gst-return-filing.html",
        "template": "templates/gst-invoice-format.html",
        "blog": "blog/gst-registration-guide.html",
        "icon": "gst",
    },
    {
        "slug": "tds-calculator",
        "name": "TDS Calculator",
        "kind": "tds-calculator",
        "title": "TDS Calculator India | Assistly WS",
        "meta": "Use this simple TDS calculator to estimate tax deduction amount and net payable before TDS/TCS return support.",
        "h1": "TDS Calculator",
        "short": "Estimate TDS deduction and net payable from a transaction amount.",
        "summary": "A TDS calculator helps you estimate deduction amount from a payment value and rate, but the correct section and threshold should still be checked.",
        "service": "services/tds-tcs-return.html",
        "template": "templates/service-agreement-format.html",
        "blog": "blog/gst-invoice-format-guide.html",
        "icon": "tds",
    },
    {
        "slug": "ad-budget-calculator",
        "name": "Ad Budget Calculator",
        "kind": "ad-budget",
        "title": "Ad Budget Calculator for Meta Ads and Google Ads | Assistly WS",
        "meta": "Plan monthly ad budget, daily spend, Meta and Google split, expected clicks, and possible enquiries using simple assumptions.",
        "h1": "Ad Budget Calculator",
        "short": "Plan a starting budget for Meta Ads and Google Ads.",
        "summary": "An ad budget calculator helps you split spend across Meta Ads and Google Ads and estimate clicks or enquiries using clear assumptions.",
        "service": "services/meta-ads.html",
        "template": "templates/social-media-calendar.html",
        "blog": "blog/google-ads-vs-meta-ads.html",
        "icon": "ads",
    },
    {
        "slug": "seo-checklist-tool",
        "name": "SEO Checklist Tool",
        "kind": "seo-checklist",
        "title": "SEO Checklist Tool for Small Business Websites | Assistly WS",
        "meta": "Use a free SEO checklist tool to review titles, meta descriptions, headings, speed, mobile layout, internal links, and local SEO basics.",
        "h1": "SEO Checklist Tool",
        "short": "Mark SEO basics complete before publishing or improving a website.",
        "summary": "An SEO checklist tool turns website optimization into a practical list covering search intent, page structure, content, speed, local signals, and tracking.",
        "service": "services/seo-services.html",
        "template": "templates/seo-checklist-pdf.html",
        "blog": "blog/seo-for-small-business.html",
        "icon": "seo",
    },
    {
        "slug": "profit-margin-calculator",
        "name": "Profit Margin Calculator",
        "kind": "profit-margin",
        "title": "Profit Margin Calculator India | Assistly WS",
        "meta": "Calculate profit, profit margin, and markup using revenue, cost, and extra expenses. Useful for pricing decisions.",
        "h1": "Profit Margin Calculator",
        "short": "Check profit margin before setting or revising pricing.",
        "summary": "A profit margin calculator compares selling price, cost, and expenses so you can see profit, margin percentage, and markup percentage.",
        "service": "services/accounting-support.html",
        "template": "templates/business-plan-template.html",
        "blog": "blog/local-business-marketing-guide.html",
        "icon": "profit",
    },
    {
        "slug": "logo-brief-generator",
        "name": "Logo Brief Generator",
        "kind": "logo-brief",
        "title": "Logo Brief Generator for Small Businesses | Assistly WS",
        "meta": "Create a simple logo design brief with brand name, audience, style, colors, and notes before starting logo design.",
        "h1": "Logo Brief Generator",
        "short": "Prepare a practical logo brief before starting design work.",
        "summary": "A logo brief generator helps a founder explain the business, audience, preferred style, color direction, and required usage clearly.",
        "service": "services/logo-design.html",
        "template": "templates/branding-brief-template.html",
        "blog": "blog/local-business-marketing-guide.html",
        "icon": "brief",
    },
]


TEMPLATES = [
    ("gst-invoice-format", "GST Invoice Format", "XLSX/PDF", "Create GST invoices with invoice number, GSTIN, buyer details, taxable value, tax rate, and total.", "services/gst-return-filing.html", "tools/gst-late-fee-calculator.html", "blog/gst-invoice-format-guide.html"),
    ("quotation-format", "Quotation Format", "DOCX/XLSX", "Send clear service or product quotations with scope, price, taxes, validity, and terms.", "services/website-design.html", "tools/profit-margin-calculator.html", "blog/business-website-checklist.html"),
    ("salary-slip-format", "Salary Slip Format", "XLSX/PDF", "Prepare salary slips with earnings, deductions, net salary, month, employee details, and employer details.", "services/accounting-support.html", "tools/tds-calculator.html", "blog/local-business-marketing-guide.html"),
    ("business-plan-template", "Business Plan Template", "DOCX", "Organize business idea, audience, offers, pricing, cost, marketing plan, and action steps.", "services/branding.html", "tools/profit-margin-calculator.html", "blog/local-business-marketing-guide.html"),
    ("website-proposal-template", "Website Proposal Template", "DOCX", "Document website scope, pages, timeline, technology, pricing, and responsibilities.", "services/website-design.html", "tools/website-cost-calculator.html", "blog/website-cost-india.html"),
    ("social-media-calendar", "Social Media Calendar", "XLSX", "Plan posts, captions, creatives, hashtags, offers, festivals, and publishing dates.", "services/social-media-marketing.html", "tools/ad-budget-calculator.html", "blog/google-ads-vs-meta-ads.html"),
    ("seo-checklist-pdf", "SEO Checklist PDF", "PDF", "Review SEO basics including titles, headings, speed, internal links, local SEO, and tracking.", "services/seo-services.html", "tools/seo-checklist-tool.html", "blog/seo-for-small-business.html"),
    ("branding-brief-template", "Branding Brief Template", "DOCX", "Capture audience, brand personality, colors, logo direction, competitors, and deliverables.", "services/branding.html", "tools/logo-brief-generator.html", "blog/local-business-marketing-guide.html"),
    ("client-onboarding-form", "Client Onboarding Form", "DOCX", "Collect client details, goals, access needs, references, budget, approvals, and timeline.", "services/website-design.html", "tools/website-cost-calculator.html", "blog/business-website-checklist.html"),
    ("service-agreement-format", "Service Agreement Format", "DOCX", "Outline scope, payments, revisions, ownership, timelines, cancellation, and communication terms.", "services/company-registration.html", "tools/tds-calculator.html", "blog/gst-registration-guide.html"),
]


BLOGS = [
    {
        "slug": "website-cost-india",
        "title": "Website Cost in India: Practical Guide for Small Businesses | Assistly WS",
        "meta": "Learn what affects website cost in India, from pages and design level to domain, hosting, content, SEO, and maintenance.",
        "h1": "Website Cost in India: A Practical Guide for Small Businesses",
        "short": "A basic business website in India often starts from a small fixed scope, while larger websites cost more because of extra pages, content, SEO, integrations, speed work, and maintenance needs.",
        "topic": "website cost",
        "service": "services/website-design.html",
        "tool": "tools/website-cost-calculator.html",
        "template": "templates/website-proposal-template.html",
    },
    {
        "slug": "gst-registration-guide",
        "title": "GST Registration Guide for Indian Small Businesses | Assistly WS",
        "meta": "Understand GST registration, GSTIN, documents, process, common mistakes, and when to get help.",
        "h1": "GST Registration Guide for Indian Small Businesses",
        "short": "GST registration helps an eligible business get a GSTIN, issue GST invoices, collect tax, claim input tax credit, and file GST returns as required.",
        "topic": "GST registration",
        "service": "services/gst-registration.html",
        "tool": "tools/gst-late-fee-calculator.html",
        "template": "templates/gst-invoice-format.html",
    },
    {
        "slug": "msme-registration-benefits",
        "title": "MSME Registration Benefits and Udyam Basics | Assistly WS",
        "meta": "Learn MSME/Udyam registration benefits, documents, process, and why small businesses should keep registration details accurate.",
        "h1": "MSME Registration Benefits for Small Businesses",
        "short": "MSME/Udyam registration gives eligible businesses a government recognition number and can help with schemes, loans, tenders, and business credibility.",
        "topic": "MSME registration",
        "service": "services/msme-registration.html",
        "tool": "tools/profit-margin-calculator.html",
        "template": "templates/business-plan-template.html",
    },
    {
        "slug": "google-ads-vs-meta-ads",
        "title": "Google Ads vs Meta Ads for Small Businesses | Assistly WS",
        "meta": "Compare Google Ads and Meta Ads for leads, awareness, local businesses, budget planning, and campaign selection.",
        "h1": "Google Ads vs Meta Ads: Which Should a Small Business Start With?",
        "short": "Google Ads usually captures existing search demand, while Meta Ads is useful for awareness, offers, retargeting, and visual discovery.",
        "topic": "Google Ads vs Meta Ads",
        "service": "services/google-ads.html",
        "tool": "tools/ad-budget-calculator.html",
        "template": "templates/social-media-calendar.html",
    },
    {
        "slug": "seo-for-small-business",
        "title": "SEO for Small Business Websites in India | Assistly WS",
        "meta": "A simple guide to SEO for small business websites, including page structure, local SEO, content, speed, and internal links.",
        "h1": "SEO for Small Business Websites",
        "short": "SEO for a small business starts with clear service pages, helpful content, fast mobile performance, local signals, and consistent updates.",
        "topic": "small business SEO",
        "service": "services/seo-services.html",
        "tool": "tools/seo-checklist-tool.html",
        "template": "templates/seo-checklist-pdf.html",
    },
    {
        "slug": "domain-and-hosting-guide",
        "title": "Domain and Hosting Guide for Indian Businesses | Assistly WS",
        "meta": "Learn how to choose a domain, hosting, SSL, email, backups, and basic setup for a small business website.",
        "h1": "Domain and Hosting Guide for Indian Businesses",
        "short": "A domain is your website address, while hosting is where the website files live. Both should be chosen for reliability, control, and easy renewal.",
        "topic": "domain and hosting",
        "service": "services/website-design.html",
        "tool": "tools/website-cost-calculator.html",
        "template": "templates/website-proposal-template.html",
    },
    {
        "slug": "static-website-vs-wordpress",
        "title": "Static Website vs WordPress: Which Is Better? | Assistly WS",
        "meta": "Compare static websites and WordPress websites for speed, editing, cost, maintenance, SEO, and small business use cases.",
        "h1": "Static Website vs WordPress Website",
        "short": "A static website is fast and simple when content changes are limited. WordPress is better when you need frequent edits, blog publishing, and admin control.",
        "topic": "static website vs WordPress",
        "service": "services/wordpress-website.html",
        "tool": "tools/website-cost-calculator.html",
        "template": "templates/website-proposal-template.html",
    },
    {
        "slug": "business-website-checklist",
        "title": "Business Website Checklist Before Launch | Assistly WS",
        "meta": "Use this business website checklist before launch to review pages, content, contact options, SEO, speed, and tracking.",
        "h1": "Business Website Checklist Before Launch",
        "short": "Before launching a business website, review the home page, service pages, contact details, WhatsApp links, SEO tags, mobile design, speed, and tracking setup.",
        "topic": "business website checklist",
        "service": "services/website-design.html",
        "tool": "tools/seo-checklist-tool.html",
        "template": "templates/client-onboarding-form.html",
    },
    {
        "slug": "gst-invoice-format-guide",
        "title": "GST Invoice Format Guide for Small Businesses | Assistly WS",
        "meta": "Understand GST invoice format, required fields, common mistakes, and how to keep invoices clear and compliant.",
        "h1": "GST Invoice Format Guide",
        "short": "A GST invoice generally includes supplier details, buyer details, GSTIN, invoice number, date, item details, HSN/SAC where applicable, taxable value, tax rate, and total amount.",
        "topic": "GST invoice format",
        "service": "services/gst-return-filing.html",
        "tool": "tools/gst-late-fee-calculator.html",
        "template": "templates/gst-invoice-format.html",
    },
    {
        "slug": "local-business-marketing-guide",
        "title": "Local Business Marketing Guide for India | Assistly WS",
        "meta": "Learn practical local business marketing steps for website, Google Business Profile, social media, offers, ads, and follow-up.",
        "h1": "Local Business Marketing Guide for India",
        "short": "Local marketing works best when your website, Google Business Profile, social pages, offers, reviews, WhatsApp follow-up, and basic ads all support the same customer journey.",
        "topic": "local business marketing",
        "service": "services/social-media-marketing.html",
        "tool": "tools/ad-budget-calculator.html",
        "template": "templates/social-media-calendar.html",
    },
]


SERVICES = [
    {
        "slug": "website-design",
        "name": "Website Design",
        "title": "Website Design Service in India for Small Businesses | Assistly WS",
        "meta": "Get a clean, mobile-friendly, SEO-ready business website with transparent pricing and founder-led support. Ideal for small businesses, startups, and service providers in India.",
        "h1": "Website Design Service for Indian Small Businesses",
        "quick": "Website design service helps small businesses create a professional online presence with mobile-friendly pages, clear service information, contact options, and basic SEO setup.",
        "price": "&#8377;4,999 onwards",
        "timeline": "5-7 days for a basic website",
        "best": "Local businesses, service providers, startups, consultants, and freelancers",
        "docs": ["Business name and contact details", "Service list and basic content", "Logo or brand colors if available", "Domain and hosting access if already purchased"],
        "gets": ["Responsive page design", "WhatsApp and contact CTAs", "Basic on-page SEO setup", "Speed-friendly static build or platform guidance"],
        "mistakes": ["Starting without a clear page list", "Using copied content from competitors", "Ignoring mobile layout", "Skipping contact and trust information"],
        "faqs": [
            ("How much does a website cost in India?", "A small business website can start from &#8377;4,999 onwards at Assistly WS, depending on pages, content, design level, SEO setup, and urgency."),
            ("Do I need hosting and domain?", "Yes, a live website needs a domain and hosting. I can guide you on options or work with your existing setup."),
            ("Can you write website content?", "Yes, basic content guidance and content writing can be included based on scope."),
            ("Is SEO included?", "Basic SEO structure is included. Deeper SEO work can be added as a separate service."),
            ("Can I update the website later?", "Yes. Static sites can be edited manually, while WordPress is better if you want admin-panel updates."),
        ],
        "tool": "tools/website-cost-calculator.html",
        "template": "templates/website-proposal-template.html",
        "blog": "blog/website-cost-india.html",
    },
    {
        "slug": "landing-page-design",
        "name": "Landing Page Design",
        "title": "Landing Page Design Service in India | Assistly WS",
        "meta": "Launch a focused landing page for leads, campaigns, offers, or service promotion with clean design, WhatsApp CTA, and basic SEO.",
        "h1": "Landing Page Design for Leads and Campaigns",
        "quick": "Landing page design creates one focused page for a single offer, service, product, or campaign so visitors understand the value and contact you quickly.",
        "price": "&#8377;2,999 onwards",
        "timeline": "3-5 days for a focused landing page",
        "best": "Ad campaigns, local offers, workshops, services, product launches, and appointment enquiries",
        "docs": ["Offer details", "Target audience", "Photos or product references", "CTA preference such as call, WhatsApp, or form"],
        "gets": ["Conversion-focused page structure", "Hero, benefits, process, FAQ, and CTA sections", "Mobile-first layout", "Basic tracking guidance"],
        "mistakes": ["Trying to sell too many offers on one page", "Weak headline", "No proof or clear process", "Slow-loading visuals"],
        "faqs": [
            ("Can a landing page work without a full website?", "Yes, a landing page can work for a specific campaign, but a full website is better for long-term credibility."),
            ("Can you connect it with ads?", "I can design it for Meta Ads or Google Ads traffic and guide the tracking setup."),
            ("Is content included?", "Basic content structure is included. Detailed copywriting can be added."),
            ("Can it collect leads?", "A static page can use WhatsApp CTAs or connect to Formspree, Google Forms, or another form tool later."),
            ("How fast can it go live?", "A simple landing page can usually be prepared in 3-5 days after content is clear."),
        ],
        "tool": "tools/ad-budget-calculator.html",
        "template": "templates/website-proposal-template.html",
        "blog": "blog/google-ads-vs-meta-ads.html",
    },
    {
        "slug": "wordpress-website",
        "name": "WordPress Website",
        "title": "WordPress Website Design Service in India | Assistly WS",
        "meta": "Get a WordPress website for blogs, business pages, service pages, and easier updates with founder-led setup guidance.",
        "h1": "WordPress Website Design Service",
        "quick": "A WordPress website is useful when you need a business website that can be updated through an admin dashboard, blog posts, plugins, and content management features.",
        "price": "&#8377;7,999 onwards",
        "timeline": "7-12 days depending on pages and plugins",
        "best": "Businesses that need blog publishing, admin editing, service pages, and future content updates",
        "docs": ["Domain and hosting access", "Logo and brand details", "Page list", "Plugin needs such as forms or SEO"],
        "gets": ["WordPress setup", "Theme customization", "Core pages and menu setup", "Basic SEO plugin setup"],
        "mistakes": ["Installing too many plugins", "Ignoring backups", "Using heavy themes", "Leaving default demo content live"],
        "faqs": [
            ("Is WordPress better than static HTML?", "WordPress is better for frequent updates and blog management. Static HTML is simpler and faster for fixed content."),
            ("Will I get admin access?", "Yes, you can get admin access with basic usage guidance."),
            ("Do you provide hosting?", "I can guide hosting selection. Hosting cost is separate unless included in a custom scope."),
            ("Can you migrate an old website?", "Migration can be reviewed after checking the current website."),
            ("Can WordPress be SEO-friendly?", "Yes, with clean structure, good hosting, optimized content, and basic SEO settings."),
        ],
        "tool": "tools/website-cost-calculator.html",
        "template": "templates/website-proposal-template.html",
        "blog": "blog/static-website-vs-wordpress.html",
    },
    {
        "slug": "shopify-store",
        "name": "Shopify Store",
        "title": "Shopify Store Setup Service in India | Assistly WS",
        "meta": "Set up a clean Shopify store for Indian small businesses with product pages, navigation, payment guidance, and launch checklist.",
        "h1": "Shopify Store Setup for Small Businesses",
        "quick": "Shopify store setup helps product businesses launch an online store with product listings, collections, payment guidance, shipping basics, and a polished storefront.",
        "price": "&#8377;12,999 onwards",
        "timeline": "10-18 days depending on products and setup",
        "best": "D2C brands, local product sellers, boutiques, handmade products, and catalog-based businesses",
        "docs": ["Product list and photos", "Pricing and SKU details", "Shipping policy", "Payment gateway details"],
        "gets": ["Theme setup", "Product and collection structure", "Basic store pages", "Launch checklist"],
        "mistakes": ["Uploading low-quality product photos", "Missing return policy", "No shipping clarity", "Launching without test orders"],
        "faqs": [
            ("Is Shopify good for small businesses?", "Shopify is good when you need a hosted ecommerce platform and can manage monthly app and platform costs."),
            ("Do you add products?", "Yes, product upload can be included based on quantity and scope."),
            ("Is payment setup included?", "I can guide payment setup, but approval depends on provider requirements."),
            ("Can Shopify rank on Google?", "Yes, but product content, speed, category structure, and SEO work matter."),
            ("Can I manage orders myself?", "Yes, Shopify is built for owner-managed order processing."),
        ],
        "tool": "tools/profit-margin-calculator.html",
        "template": "templates/business-plan-template.html",
        "blog": "blog/local-business-marketing-guide.html",
    },
    {
        "slug": "seo-services",
        "name": "SEO Services",
        "title": "SEO Services for Small Businesses in India | Assistly WS",
        "meta": "Get practical SEO support for small business websites, including keyword mapping, on-page SEO, content structure, local SEO, and technical basics.",
        "h1": "SEO Services for Small Businesses",
        "quick": "SEO service improves how a website is structured, written, connected, and understood by search engines so relevant customers can find it more easily over time.",
        "price": "&#8377;4,999 onwards per month",
        "timeline": "Initial setup in 7-10 days, ongoing improvement monthly",
        "best": "Service businesses, local businesses, websites with useful pages, and founders who want long-term organic visibility",
        "docs": ["Website access", "Target services and locations", "Competitor references", "Google Business Profile access if local"],
        "gets": ["Keyword and page mapping", "Title and meta improvements", "Internal linking guidance", "Local SEO basics"],
        "mistakes": ["Expecting certain ranking positions", "Publishing thin pages", "Ignoring local intent", "Not tracking enquiries"],
        "faqs": [
            ("Do you guarantee rankings?", "No. Honest SEO cannot guarantee rankings. I focus on practical improvements, content quality, and clear tracking."),
            ("How long does SEO take?", "SEO usually takes time. Basic fixes can be quick, but meaningful results often need consistent work."),
            ("Is SEO included with website design?", "Basic SEO setup is included in website work. Ongoing SEO is separate."),
            ("Do you write blogs?", "Blog planning and writing support can be included based on scope."),
            ("Can you help local SEO?", "Yes, local service pages and Google Business Profile basics can be reviewed."),
        ],
        "tool": "tools/seo-checklist-tool.html",
        "template": "templates/seo-checklist-pdf.html",
        "blog": "blog/seo-for-small-business.html",
    },
    {
        "slug": "social-media-marketing",
        "name": "Social Media Marketing",
        "title": "Social Media Marketing Support for Small Businesses | Assistly WS",
        "meta": "Get practical SMO and social media marketing support for content planning, post ideas, captions, profile cleanup, and campaigns.",
        "h1": "Social Media Marketing Support",
        "quick": "Social media marketing helps a business present offers, educate customers, stay visible, and support enquiries through consistent posts and clear calls to action.",
        "price": "&#8377;4,999 onwards per month",
        "timeline": "Plan in 3-5 days, ongoing monthly execution",
        "best": "Local businesses, service providers, early-stage brands, and founders who need simple content consistency",
        "docs": ["Business details", "Offer list", "Brand colors or references", "Photos or service examples"],
        "gets": ["Profile review", "Monthly content themes", "Caption and creative direction", "WhatsApp-friendly CTAs"],
        "mistakes": ["Posting randomly", "No offer clarity", "Using only festival posts", "Ignoring comment and DM follow-up"],
        "faqs": [
            ("Do you manage Instagram and Facebook?", "Support can include Instagram and Facebook content planning and profile improvement."),
            ("Do you design posts?", "Post design can be included in monthly packages depending on quantity."),
            ("Can social media bring leads?", "It can support enquiries, but leads depend on offer, audience, consistency, and follow-up."),
            ("Do I need ads too?", "Ads help when you need faster reach. Organic content supports credibility."),
            ("Can I start small?", "Yes, we can begin with a content calendar and profile cleanup."),
        ],
        "tool": "tools/ad-budget-calculator.html",
        "template": "templates/social-media-calendar.html",
        "blog": "blog/local-business-marketing-guide.html",
    },
    {
        "slug": "meta-ads",
        "name": "Meta Ads",
        "title": "Meta Ads Setup and Support in India | Assistly WS",
        "meta": "Plan and set up Meta Ads for Facebook and Instagram with clear campaign objective, landing page, budget, and tracking guidance.",
        "h1": "Meta Ads Support for Facebook and Instagram",
        "quick": "Meta Ads support helps you plan Facebook and Instagram campaigns for awareness, enquiries, offers, retargeting, and local reach with realistic budget guidance.",
        "price": "&#8377;3,999 onwards for setup",
        "timeline": "3-7 days after creatives and offer are ready",
        "best": "Local offers, visual products, service awareness, retargeting, and WhatsApp enquiry campaigns",
        "docs": ["Business Manager access", "Page and Instagram access", "Offer details", "Creative assets or references"],
        "gets": ["Campaign structure", "Audience and budget planning", "Ad copy guidance", "Landing page or WhatsApp CTA review"],
        "mistakes": ["Running ads without a clear offer", "Using weak creatives", "No follow-up process", "Expecting fixed lead counts"],
        "faqs": [
            ("Do you guarantee leads from Meta Ads?", "No. I help plan and set up campaigns honestly, but leads depend on offer, targeting, creative, budget, and follow-up."),
            ("Can ads run to WhatsApp?", "Yes, WhatsApp enquiry campaigns are possible when the offer and response process are clear."),
            ("What budget should I start with?", "Use the ad budget calculator for planning, then adjust based on objective and location."),
            ("Do you design creatives?", "Creative direction or design can be included based on scope."),
            ("Can you fix existing ads?", "Yes, I can review existing structure and suggest improvements."),
        ],
        "tool": "tools/ad-budget-calculator.html",
        "template": "templates/social-media-calendar.html",
        "blog": "blog/google-ads-vs-meta-ads.html",
    },
    {
        "slug": "google-ads",
        "name": "Google Ads",
        "title": "Google Ads Setup for Small Businesses in India | Assistly WS",
        "meta": "Get Google Ads setup support for search campaigns, keyword planning, landing pages, budget, and conversion-focused structure.",
        "h1": "Google Ads Setup for Small Businesses",
        "quick": "Google Ads support helps a business reach people already searching for services or products, using focused keywords, clear ads, and useful landing pages.",
        "price": "&#8377;4,999 onwards for setup",
        "timeline": "4-8 days after account and landing page are ready",
        "best": "Search-driven services, local businesses, high-intent enquiries, and businesses with clear landing pages",
        "docs": ["Google Ads access", "Website or landing page", "Target locations", "Service list and budget range"],
        "gets": ["Keyword and campaign structure", "Ad copy suggestions", "Budget planning", "Landing page review"],
        "mistakes": ["Broad keywords without control", "Sending traffic to a weak page", "No negative keywords", "Ignoring call and form tracking"],
        "faqs": [
            ("Is Google Ads better than Meta Ads?", "Google Ads is often stronger for high-intent searches. Meta Ads is useful for awareness and visual offers."),
            ("Do you guarantee enquiries?", "No. Ads can be planned carefully, but enquiries are never guaranteed."),
            ("Can you set up call ads?", "Call-focused campaigns can be reviewed based on service and location."),
            ("Do I need a landing page?", "A focused landing page usually improves campaign clarity and conversion chances."),
            ("What budget is needed?", "Budget depends on keyword competition, location, and goal. Start with a test budget and review data."),
        ],
        "tool": "tools/ad-budget-calculator.html",
        "template": "templates/website-proposal-template.html",
        "blog": "blog/google-ads-vs-meta-ads.html",
    },
    {
        "slug": "logo-design",
        "name": "Logo Design",
        "title": "Logo Design Service for Small Businesses | Assistly WS",
        "meta": "Get a clean logo direction for your small business with practical files, brand usage guidance, and founder-led communication.",
        "h1": "Logo Design for Small Businesses",
        "quick": "Logo design gives a business a recognizable visual mark that can be used on websites, invoices, social profiles, packaging, and marketing material.",
        "price": "&#8377;1,999 onwards",
        "timeline": "3-6 days depending on revisions",
        "best": "New businesses, local brands, freelancers, service providers, and early-stage product sellers",
        "docs": ["Business name", "Industry and audience", "Style references", "Preferred colors if any"],
        "gets": ["Logo concept direction", "Color and typography guidance", "Usable export files", "Basic usage note"],
        "mistakes": ["Choosing a design only because it looks trendy", "No usage planning", "Too many colors", "Copying competitor logos"],
        "faqs": [
            ("How many concepts are included?", "Concept count depends on package scope. I keep it clear before starting."),
            ("Will I get source files?", "Source or editable files can be included based on package."),
            ("Can you redesign an old logo?", "Yes, redesign can be reviewed with current logo and goals."),
            ("Do you check trademark availability?", "No legal trademark search is included by default. You should verify before final use."),
            ("Can you design full branding?", "Yes, branding support is available as a broader service."),
        ],
        "tool": "tools/logo-brief-generator.html",
        "template": "templates/branding-brief-template.html",
        "blog": "blog/local-business-marketing-guide.html",
    },
    {
        "slug": "branding",
        "name": "Branding",
        "title": "Branding Service for Small Businesses in India | Assistly WS",
        "meta": "Build a simple, practical brand identity with positioning, visual direction, colors, typography, and usage guidance.",
        "h1": "Branding Support for New and Small Businesses",
        "quick": "Branding support helps a business define how it should look, sound, and present itself consistently across website, social media, invoices, and customer communication.",
        "price": "&#8377;4,999 onwards",
        "timeline": "5-10 days depending on scope",
        "best": "New businesses, rebrands, local service providers, and founders who want consistent customer-facing material",
        "docs": ["Business goal", "Audience", "Competitor references", "Current logo or materials if available"],
        "gets": ["Brand direction", "Color palette", "Typography guidance", "Basic usage system"],
        "mistakes": ["Skipping audience clarity", "Using too many styles", "No consistency across materials", "Treating branding as only a logo"],
        "faqs": [
            ("Is branding only logo design?", "No. Branding includes positioning, style, colors, voice, and consistent presentation."),
            ("Can you help name my business?", "Yes, I can help explore names and check practical fit."),
            ("Do you create brand guidelines?", "A simple brand guide can be included based on scope."),
            ("Is branding needed for a small business?", "Even small businesses benefit from consistency and clarity."),
            ("Can branding be done before website?", "Yes. It often helps the website look clearer and more professional."),
        ],
        "tool": "tools/logo-brief-generator.html",
        "template": "templates/branding-brief-template.html",
        "blog": "blog/local-business-marketing-guide.html",
    },
    {
        "slug": "gst-registration",
        "name": "GST Registration",
        "title": "GST Registration Support in India | Assistly WS",
        "meta": "Get GST registration support with document guidance, process clarity, and founder-led communication for small businesses in India.",
        "h1": "GST Registration Support",
        "quick": "GST registration helps eligible businesses get a GSTIN, issue GST invoices, collect tax, claim input tax credit where allowed, and file GST returns.",
        "price": "Custom pricing after document review",
        "timeline": "Usually 3-7 working days after documents are ready",
        "best": "Eligible traders, service providers, ecommerce sellers, startups, and businesses needing GST invoices",
        "docs": ["PAN", "Aadhaar", "Photo", "Business address proof", "Bank details", "Business registration proof if applicable"],
        "gets": ["Document checklist", "Application support", "Status guidance", "Post-registration next steps"],
        "mistakes": ["Wrong business address proof", "Mismatch in name details", "Ignoring return filing after registration", "Not keeping login credentials safe"],
        "faqs": [
            ("Who needs GST registration?", "GST registration depends on turnover, business type, interstate supply, ecommerce activity, and applicable GST rules."),
            ("What documents are required?", "Common documents include PAN, Aadhaar, photo, address proof, bank details, and business proof if applicable."),
            ("How long does GST registration take?", "It often takes a few working days after documents are correct, but timelines can vary."),
            ("Do you file GST returns too?", "Yes, GST return filing support is available separately."),
            ("Can new businesses apply?", "Yes, new businesses can apply if registration is needed or beneficial for their situation."),
        ],
        "tool": "tools/gst-late-fee-calculator.html",
        "template": "templates/gst-invoice-format.html",
        "blog": "blog/gst-registration-guide.html",
    },
    {
        "slug": "msme-registration",
        "name": "MSME/Udyam Registration",
        "title": "MSME Udyam Registration Support in India | Assistly WS",
        "meta": "Get MSME/Udyam registration support for small businesses with document guidance and simple process explanation.",
        "h1": "MSME/Udyam Registration Support",
        "quick": "MSME/Udyam registration gives eligible businesses a recognition number that can support credibility, schemes, tenders, and finance-related requirements.",
        "price": "Custom pricing after details review",
        "timeline": "Usually 1-3 days when details are ready",
        "best": "Micro and small businesses, service providers, manufacturers, traders, and early-stage founders",
        "docs": ["Aadhaar", "PAN", "Business name", "Business activity", "Bank details", "Investment and turnover information"],
        "gets": ["Eligibility guidance", "Form support", "Certificate download guidance", "Correction guidance if needed"],
        "mistakes": ["Entering wrong activity", "Using inconsistent business details", "Not saving certificate details", "Assuming it replaces GST or company registration"],
        "faqs": [
            ("Is MSME registration mandatory?", "It may not be mandatory for every business, but it can be useful for recognition and some benefits."),
            ("Is Udyam the same as MSME registration?", "Udyam is the current registration system for MSME recognition."),
            ("Can service businesses register?", "Eligible service businesses can register based on applicable criteria."),
            ("Does MSME registration replace GST?", "No. GST registration and MSME/Udyam registration serve different purposes."),
            ("Can you help with updates?", "Yes, update or correction guidance can be reviewed."),
        ],
        "tool": "tools/profit-margin-calculator.html",
        "template": "templates/business-plan-template.html",
        "blog": "blog/msme-registration-benefits.html",
    },
    {
        "slug": "company-registration",
        "name": "Company Registration",
        "title": "Company Registration Guidance in India | Assistly WS",
        "meta": "Get practical company registration guidance for new founders, including structure selection, documents, and next compliance steps.",
        "h1": "Company Registration Guidance",
        "quick": "Company registration support helps founders understand entity options, required details, document preparation, and next steps after incorporation.",
        "price": "Custom pricing after structure review",
        "timeline": "Timeline depends on entity type, documents, approvals, and government processing",
        "best": "Founders planning private limited company, LLP, partnership, proprietorship, or formal business setup",
        "docs": ["PAN and Aadhaar", "Address proof", "Business name options", "Registered office proof", "Director or partner details"],
        "gets": ["Structure guidance", "Document checklist", "Name planning support", "Next compliance checklist"],
        "mistakes": ["Choosing structure without tax and compliance clarity", "Weak name options", "Missing address proof", "Ignoring post-registration compliance"],
        "faqs": [
            ("Which business structure should I choose?", "It depends on ownership, liability, funding plans, tax, compliance, and future goals."),
            ("Can you register a company directly?", "I can guide and coordinate support based on scope and requirements."),
            ("Is GST needed after company registration?", "GST depends on business activity, turnover, and applicable rules."),
            ("What happens after registration?", "You may need bank account setup, GST, accounting, invoices, and compliance calendar."),
            ("Can a solo founder register?", "Yes, options can be reviewed based on your business goal."),
        ],
        "tool": "tools/profit-margin-calculator.html",
        "template": "templates/service-agreement-format.html",
        "blog": "blog/gst-registration-guide.html",
    },
    {
        "slug": "gst-return-filing",
        "name": "GST Return Filing",
        "title": "GST Return Filing Support in India | Assistly WS",
        "meta": "Get GST return filing support for small businesses with document checklist, late fee review, invoice organization, and practical guidance.",
        "h1": "GST Return Filing Support",
        "quick": "GST return filing reports outward supplies, inward supplies, tax liability, eligible input tax credit, and payment details as required under GST.",
        "price": "Custom pricing based on return type and volume",
        "timeline": "Depends on data readiness and return type",
        "best": "GST-registered businesses that need monthly, quarterly, or pending return support",
        "docs": ["Sales invoices", "Purchase invoices", "GST portal access", "Bank/payment details", "Previous return status"],
        "gets": ["Data checklist", "Return preparation support", "Late fee estimate review", "Filing status guidance"],
        "mistakes": ["Missing invoices", "Wrong tax rate", "Late filing", "Not reconciling ITC"],
        "faqs": [
            ("Can you file pending GST returns?", "Pending return support can be reviewed after checking portal status and data availability."),
            ("What details are needed?", "Sales, purchases, tax payments, portal access, and previous filing status are commonly needed."),
            ("Can late fee be checked?", "Yes, late fee and interest estimates can be reviewed before filing."),
            ("Do you make GST invoices?", "I provide invoice format guidance and accounting support can help organize invoice data."),
            ("Is GST filing monthly or quarterly?", "Frequency depends on scheme, turnover, and applicable GST rules."),
        ],
        "tool": "tools/gst-late-fee-calculator.html",
        "template": "templates/gst-invoice-format.html",
        "blog": "blog/gst-invoice-format-guide.html",
    },
    {
        "slug": "accounting-support",
        "name": "Accounting Support",
        "title": "Accounting Support for Small Businesses in India | Assistly WS",
        "meta": "Get practical accounting support for invoices, expense tracking, basic reports, GST-ready records, and small business organization.",
        "h1": "Accounting Support for Small Businesses",
        "quick": "Accounting support helps small businesses organize invoices, expenses, receipts, payments, salary details, and basic reports so decisions and filings become easier.",
        "price": "Custom monthly pricing based on volume",
        "timeline": "Initial cleanup depends on record volume; ongoing support is monthly",
        "best": "Small businesses, service providers, freelancers, shops, and founders who need organized records",
        "docs": ["Sales and purchase records", "Bank statements", "Expense bills", "GST details if applicable", "Salary details if applicable"],
        "gets": ["Record organization", "Basic reporting", "Invoice support", "GST/accounting coordination"],
        "mistakes": ["Mixing personal and business expenses", "Keeping records only in WhatsApp chats", "No monthly review", "Ignoring cash expenses"],
        "faqs": [
            ("Do you provide monthly accounting?", "Monthly support can be planned based on transaction volume and required reports."),
            ("Can you organize old records?", "Yes, cleanup can be reviewed after seeing data volume."),
            ("Do you support GST records?", "Yes, accounting support can help prepare GST-ready records."),
            ("Can you make invoices?", "Invoice formats and simple invoice support can be included."),
            ("Is this suitable for freelancers?", "Yes, freelancers can use accounting support for income, expenses, invoices, and tax-ready records."),
        ],
        "tool": "tools/profit-margin-calculator.html",
        "template": "templates/salary-slip-format.html",
        "blog": "blog/local-business-marketing-guide.html",
    },
    {
        "slug": "tds-tcs-return",
        "name": "TDS/TCS Return",
        "title": "TDS/TCS Return Support in India | Assistly WS",
        "meta": "Get TDS/TCS return support with deduction calculation guidance, challan details, return preparation support, and compliance clarity.",
        "h1": "TDS/TCS Return Support",
        "quick": "TDS/TCS return support helps businesses organize deduction or collection details, challans, deductee data, and filing requirements.",
        "price": "Custom pricing based on entries and return type",
        "timeline": "Depends on data readiness and return period",
        "best": "Businesses deducting TDS, collecting TCS, paying vendors, or managing salary and professional payment compliance",
        "docs": ["TAN", "Deductee details", "PAN details", "Challan details", "Payment and deduction data"],
        "gets": ["Data review", "Calculation support", "Return preparation guidance", "Correction support if needed"],
        "mistakes": ["Wrong PAN details", "Wrong section or rate", "Late challan payment", "Mismatch in challan data"],
        "faqs": [
            ("What is needed for TDS return?", "TAN, deductee details, PAN, payment data, deduction data, and challan information are commonly needed."),
            ("Can you calculate TDS?", "Basic calculation support is available, but the correct section and threshold should be checked."),
            ("What if a return is late?", "Late filing and correction implications can be reviewed based on status."),
            ("Do freelancers need TDS?", "TDS may apply based on payer, payment type, threshold, and tax rules."),
            ("Can you help with corrections?", "Correction support can be reviewed after checking the issue."),
        ],
        "tool": "tools/tds-calculator.html",
        "template": "templates/service-agreement-format.html",
        "blog": "blog/gst-registration-guide.html",
    },
    {
        "slug": "esic-pf-support",
        "name": "ESIC/PF Support",
        "title": "ESIC PF Support for Small Businesses in India | Assistly WS",
        "meta": "Get ESIC and PF support guidance for small businesses with employee details, registration support, filing coordination, and document clarity.",
        "h1": "ESIC/PF Support for Small Businesses",
        "quick": "ESIC/PF support helps employers understand employee-related compliance requirements, registration needs, records, and monthly support requirements.",
        "price": "Custom pricing after employee and compliance review",
        "timeline": "Depends on registration status, employee count, and records",
        "best": "Employers with staff, growing teams, and businesses reviewing statutory employee compliance",
        "docs": ["Employer details", "Employee details", "Salary structure", "Business registration documents", "Existing PF/ESIC details if any"],
        "gets": ["Requirement review", "Document checklist", "Registration or filing coordination", "Monthly support guidance"],
        "mistakes": ["Ignoring employee thresholds", "Incomplete employee data", "Wrong salary breakup", "No monthly compliance calendar"],
        "faqs": [
            ("When does PF or ESIC apply?", "Applicability depends on employee count, salary, business type, and current rules."),
            ("Can you help with registration?", "Registration support can be reviewed based on documents and applicability."),
            ("Do you manage monthly filing?", "Monthly support can be discussed after checking employee count and records."),
            ("What employee details are needed?", "Name, identity details, salary, joining date, and other required employment information may be needed."),
            ("Can this be combined with accounting?", "Yes, payroll and accounting support can be coordinated."),
        ],
        "tool": "tools/tds-calculator.html",
        "template": "templates/salary-slip-format.html",
        "blog": "blog/local-business-marketing-guide.html",
    },
]


LEGAL = [
    ("privacy-policy", "Privacy Policy | Assistly WS", "Privacy Policy", "This privacy policy explains what information Assistly WS may collect through static forms, WhatsApp links, email, and analytics tools if added later."),
    ("terms", "Terms and Conditions | Assistly WS", "Terms and Conditions", "These terms explain how visitors and customers should use Assistly WS resources, consultations, templates, tools, and services."),
    ("disclaimer", "Disclaimer | Assistly WS", "Disclaimer", "This disclaimer explains that Assistly WS provides practical guidance and support, but website, marketing, tax, and compliance decisions should be verified for your situation."),
    ("refund-policy", "Refund Policy | Assistly WS", "Refund Policy", "This refund policy explains how service payments, digital work, consultation, and custom support may be handled with transparent communication."),
]


def nav_columns(current: str) -> str:
    columns = [
        (
            "Digital Growth",
            [
                ("Website Design", "services/website-design.html"),
                ("Landing Page", "services/landing-page-design.html"),
                ("SEO", "services/seo-services.html"),
                ("Meta Ads", "services/meta-ads.html"),
                ("Google Ads", "services/google-ads.html"),
                ("Branding", "services/branding.html"),
            ],
        ),
        (
            "Business Support",
            [
                ("GST Registration", "services/gst-registration.html"),
                ("MSME", "services/msme-registration.html"),
                ("Company Registration", "services/company-registration.html"),
                ("Accounting", "services/accounting-support.html"),
                ("TDS/TCS", "services/tds-tcs-return.html"),
                ("ESIC/PF", "services/esic-pf-support.html"),
            ],
        ),
        (
            "Free Resources",
            [
                ("Website Cost Calculator", "tools/website-cost-calculator.html"),
                ("GST Late Fee Calculator", "tools/gst-late-fee-calculator.html"),
                ("Ad Budget Calculator", "tools/ad-budget-calculator.html"),
                ("SEO Checklist", "tools/seo-checklist-tool.html"),
            ],
        ),
    ]
    html_columns = []
    for title, links in columns:
        items = "".join(f'<a href="{rel_link(current, url)}">{esc(label)} <span aria-hidden="true">-&gt;</span></a>' for label, url in links)
        html_columns.append(f'<div class="mega-column"><h3>{esc(title)}</h3><div class="mega-list">{items}</div></div>')
    return "".join(html_columns)


def header(current: str) -> str:
    cta = wa("Hi Assistly WS, I want a free consultation. Please guide me.")
    nav = [
        ("Services", "services.html"),
        ("Free Tools", "free-tools.html"),
        ("Templates", "templates.html"),
        ("Blog", "blog.html"),
        ("Projects", "demo-work.html"),
        ("About", "about.html"),
    ]
    nav_links = "".join(
        f'<a class="nav-link" href="{rel_link(current, path)}">{label}</a>'
        for label, path in nav[1:]
    )
    mobile_links = "".join(
        f'<a class="nav-link" href="{rel_link(current, path)}">{label}</a>'
        for label, path in nav
    )
    return f"""
    <a class="skip-link" href="#main">Skip to content</a>
    <div class="scroll-progress" aria-hidden="true"></div>
    <div class="announcement"><div class="announcement-inner"><span class="announcement-dot" aria-hidden="true"></span><span class="announcement-text">New founder-led agency - I work personally on every project with honesty and focus.</span></div></div>
    <header class="site-header">
      <nav class="nav-inner" aria-label="Main navigation">
        <a class="brand" href="{rel_link(current, 'index.html')}" aria-label="Assistly WS home">
          <span class="brand-mark" aria-hidden="true">AW</span>
          <span>Assistly WS<small>{TAGLINE}</small></span>
        </a>
        <div class="nav-links" data-mega-root>
          <div class="nav-item">
            <button class="mega-trigger" data-mega-trigger aria-expanded="false" aria-controls="servicesMega">Services</button>
            <div class="mega-menu" id="servicesMega">
              <div class="mega-grid">{nav_columns(current)}</div>
            </div>
          </div>
          {nav_links}
        </div>
        <div class="nav-actions">
          <a class="btn small desktop-cta" href="{cta}" target="_blank" rel="noopener">Get Free Consultation</a>
          <button class="mobile-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobilePanel"><span></span></button>
        </div>
      </nav>
      <div class="mobile-panel" id="mobilePanel">
        <div class="mobile-panel-inner" data-mega-root>
          <button class="nav-link mega-trigger" data-mega-trigger aria-expanded="false" aria-controls="mobileMega">Services <span aria-hidden="true">+</span></button>
          <div class="mobile-mega" id="mobileMega">{nav_columns(current)}</div>
          {mobile_links}
          <a class="btn" href="{cta}" target="_blank" rel="noopener">Get Free Consultation</a>
        </div>
      </div>
    </header>
    """


def footer(current: str) -> str:
    columns = [
        ("Company", [("About", "about.html"), ("Contact", "contact.html"), ("Projects", "demo-work.html"), ("Blog", "blog.html")]),
        ("Services", [("Website Design", "services/website-design.html"), ("SEO", "services/seo-services.html"), ("Branding", "services/branding.html"), ("GST Registration", "services/gst-registration.html"), ("MSME Registration", "services/msme-registration.html")]),
        ("Free Resources", [("Free Tools", "free-tools.html"), ("Templates", "templates.html"), ("Website Cost Calculator", "tools/website-cost-calculator.html"), ("GST Invoice Format", "templates/gst-invoice-format.html")]),
        ("Legal", [("Privacy Policy", "legal/privacy-policy.html"), ("Terms", "legal/terms.html"), ("Disclaimer", "legal/disclaimer.html"), ("Refund Policy", "legal/refund-policy.html")]),
    ]
    column_html = ['<div><a class="brand" href="' + rel_link(current, "index.html") + '"><span class="brand-mark" aria-hidden="true">AW</span><span>Assistly WS<small>Your Growth, Our Mission</small></span></a><p class="muted" style="color:#cbd5e1;margin-top:14px">Founder-led website, marketing, compliance, accounting support, free tools, and templates for Indian small businesses.</p></div>']
    for title, links in columns:
        items = "".join(f'<li><a href="{rel_link(current, url)}">{esc(label)}</a></li>' for label, url in links)
        column_html.append(f"<div><h3>{esc(title)}</h3><ul>{items}</ul></div>")
    contact = f"""
      <div>
        <h3>Contact</h3>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="tel:+918059134416">{PHONE}</a></li>
          <li>{LOCATION}</li>
          <li>Service Area: {SERVICE_AREA}</li>
        </ul>
      </div>
    """
    column_html.append(contact)
    return f"""
    <footer class="footer">
      <div class="footer-grid">{''.join(column_html)}</div>
      <div class="footer-bottom">
        <span>&copy; 2026 Assistly WS. New founder-led agency with honest positioning.</span>
        <span>No fake testimonials, no fake awards, no ranking promises.</span>
      </div>
    </footer>
    <button class="back-to-top" type="button" aria-label="Back to top">^</button>
    """


def breadcrumb_html(current: str, items: list[tuple[str, str]]) -> str:
    parts = []
    for index, (label, path) in enumerate(items):
        if index:
            parts.append('<span aria-hidden="true">/</span>')
        if index == len(items) - 1:
            parts.append(f"<span>{esc(label)}</span>")
        else:
            parts.append(f'<a href="{rel_link(current, path)}">{esc(label)}</a>')
    return '<nav class="breadcrumb" aria-label="Breadcrumb">' + "".join(parts) + "</nav>"


def faq_html(faqs: list[tuple[str, str]], prefix: str) -> str:
    items = []
    for idx, (question, answer) in enumerate(faqs, start=1):
        qid = f"{prefix}-faq-{idx}"
        items.append(
            f"""
            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false" aria-controls="{qid}">
                <span>{question}</span><span class="faq-icon" aria-hidden="true"></span>
              </button>
              <div class="faq-answer" id="{qid}">{answer}</div>
            </div>
            """
        )
    return '<div class="faq-list">' + "".join(items) + "</div>"


def render_page(
    path: str,
    title: str,
    meta: str,
    body: str,
    schemas: list[dict],
    og_type: str = "website",
) -> None:
    current_url = page_url(path)
    html_doc = f"""<!doctype html>
<html lang="en-IN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(meta)}">
  <link rel="canonical" href="{current_url}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(meta)}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:url" content="{current_url}">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta property="og:image" content="{DOMAIN}/assets/logo/assistly-ws-logo.svg">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(meta)}">
  <meta name="theme-color" content="#0F172A">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{asset(path, 'css/style.css')}">
  {''.join(json_ld(schema) for schema in schemas)}
</head>
<body>
  {header(path)}
  <main id="main">{body}</main>
  {footer(path)}
  <script src="{asset(path, 'js/main.js')}" defer></script>
</body>
</html>
"""
    output = ROOT / path
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html_doc, encoding="utf-8")


def page_hero(current: str, items: list[tuple[str, str]], eyebrow: str, h1: str, lead: str) -> str:
    return f"""
    <section class="page-hero">
      <div class="page-hero-inner">
        {breadcrumb_html(current, items)}
        <span class="section-eyebrow">{esc(eyebrow)}</span>
        <h1>{esc(h1)}</h1>
        <p class="lead">{esc(lead)}</p>
        <div class="article-meta">
          <span class="badge green">New founder-led agency</span>
          <span class="badge">India-focused support</span>
          <span class="badge orange">Last updated {UPDATED_LABEL}</span>
        </div>
      </div>
    </section>
    """


def card_grid(items: list[dict], current: str, kind: str = "web", grid_class: str = "grid-4", card_class: str = "") -> str:
    cards = []
    for item in items:
        icon_class = "orange" if item.get("accent") or item.get("badge") else ""
        classes = " ".join(part for part in ["card", card_class, "reveal"] if part)
        cards.append(
            f"""
            <article class="{classes}">
              <div class="card-top">
                <span class="icon-bubble {icon_class}">{icon(item.get('icon', kind))}</span>
                {f'<span class="badge {item.get("badge_class", "")}">{esc(item["badge"])}</span>' if item.get("badge") else ''}
              </div>
              <h3>{esc(item['title'])}</h3>
              <p class="muted">{esc(item['text'])}</p>
              <a class="card-link" href="{rel_link(current, item['url'])}">{esc(item.get('cta', 'Open'))} <span aria-hidden="true">-&gt;</span></a>
            </article>
            """
        )
    return f'<div class="grid {grid_class}">' + "".join(cards) + "</div>"


def homepage() -> None:
    current = "index.html"
    tool_cards = [
        {"title": t["name"], "text": t["short"], "url": f"tools/{t['slug']}.html", "badge": "Free", "badge_class": "green", "cta": "Use Tool", "icon": t.get("icon", "calc")}
        for t in TOOLS
    ]
    template_cards = [
        {"title": name, "text": desc, "url": f"templates/{slug}.html", "badge": file_type, "cta": "Download placeholder", "icon": "doc"}
        for slug, name, file_type, desc, *_ in TEMPLATES[:8]
    ]
    home_service_cards = [
        {"title": "Website Design", "text": "Clean, mobile-friendly business websites with clear pages, WhatsApp CTAs, and SEO-ready structure.", "url": "services/website-design.html", "cta": "View Service", "icon": "web", "accent": True},
        {"title": "Landing Pages", "text": "Focused campaign pages for leads, offers, launches, and service enquiries.", "url": "services/landing-page-design.html", "cta": "View Service", "icon": "web-calc"},
        {"title": "SEO Services", "text": "On-page SEO, local search basics, content structure, and practical improvement plans.", "url": "services/seo-services.html", "cta": "View Service", "icon": "seo"},
        {"title": "Logo & Branding", "text": "Logo direction, color systems, typography guidance, and brand consistency for small businesses.", "url": "services/branding.html", "cta": "View Service", "icon": "brand", "accent": True},
        {"title": "Meta Ads", "text": "Planning and setup support for Facebook and Instagram campaigns with clear budgets.", "url": "services/meta-ads.html", "cta": "View Service", "icon": "ads"},
        {"title": "Google Ads", "text": "Search campaign support for demand capture, landing page readiness, and tracking basics.", "url": "services/google-ads.html", "cta": "View Service", "icon": "growth"},
        {"title": "GST Registration", "text": "Document checklist, registration guidance, and practical post-registration next steps.", "url": "services/gst-registration.html", "cta": "View Service", "icon": "gst", "accent": True},
        {"title": "MSME Registration", "text": "Udyam registration guidance for eligible small businesses, traders, and service providers.", "url": "services/msme-registration.html", "cta": "View Service", "icon": "registration"},
        {"title": "Company Registration", "text": "Entity selection guidance, document planning, and startup compliance direction.", "url": "services/company-registration.html", "cta": "View Service", "icon": "compliance"},
        {"title": "Accounting Support", "text": "Invoice, expense, record, and basic report support for cleaner business decisions.", "url": "services/accounting-support.html", "cta": "View Service", "icon": "accounting", "accent": True},
        {"title": "GST Return Filing", "text": "Return filing support with invoice organization, late fee review, and GST-ready records.", "url": "services/gst-return-filing.html", "cta": "View Service", "icon": "gst"},
        {"title": "TDS/TCS Support", "text": "Deduction, challan, return, and correction support for TDS/TCS compliance workflows.", "url": "services/tds-tcs-return.html", "cta": "View Service", "icon": "tds"},
    ]
    demos = [
        ("Business Services Website Concept", "A clean service website structure for local consultants and professional service providers."),
        ("Accounting Software UI Concept", "Dashboard-style UI concept for invoices, reports, records, and small business tasks."),
        ("Local Business Website Concept", "Fast, mobile-first website concept for a local service provider with WhatsApp-first enquiries."),
        ("Shopify Store Concept", "Product catalog and store layout concept for small Indian ecommerce brands."),
        ("SEO Landing Page Concept", "Search-focused landing page concept with answer blocks, FAQs, and service CTAs."),
        ("Brand Identity Concept", "Simple visual identity concept with logo direction, colors, and usage notes."),
    ]
    demo_cards = "".join(
        f"""
        <article class="card reveal">
          <div class="demo-frame"><span class="badge orange">Concept Project</span></div>
          <h3>{esc(title)}</h3>
          <p class="muted">{esc(text)}</p>
          <a class="card-link" href="{rel_link(current, 'demo-work.html')}">View projects <span aria-hidden="true">-&gt;</span></a>
        </article>
        """
        for title, text in demos
    )
    pricing_cards = "".join(
        f"""
        <article class="card reveal">
          <span class="badge {badge}">{label}</span>
          <h3>{name}</h3>
          <div class="price">{price}</div>
          <ul class="list-check">{''.join(f'<li>{esc(item)}</li>' for item in items)}</ul>
          <a class="btn small" href="{wa('Hi Assistly WS, I want a quote for ' + name + '. Please guide me with scope and timeline.')}" target="_blank" rel="noopener">Request Quote on WhatsApp</a>
        </article>
        """
        for label, badge, name, price, items in [
            ("Starter", "green", "Starter Website", "&#8377;4,999 onwards", ["3-5 pages", "Mobile responsive design", "Contact form/WhatsApp button", "Basic SEO setup", "Delivery: 5-7 days"]),
            ("Growth", "", "Growth Website", "&#8377;9,999 onwards", ["6-10 pages", "SEO-friendly structure", "Blog setup", "Lead form", "Speed optimization", "Delivery: 10-15 days"]),
            ("Flexible", "orange", "Custom Business Support", "Custom pricing", ["GST", "Accounting", "Branding", "Ads", "Ongoing support"]),
        ]
    )
    blog_cards = [
        {"title": b["h1"].replace(": A Practical Guide for Small Businesses", ""), "text": b["short"], "url": f"blog/{b['slug']}.html", "cta": "Read guide", "icon": "doc"}
        for b in BLOGS[:6]
    ]
    faqs = [
        ("Is Assistly WS a new agency?", "Yes. Assistly WS is a new founder-led agency. The website uses honest positioning instead of fake client counts or awards."),
        ("Do you have client projects?", "Right now, concept projects are shown to explain the thinking, style, and practical approach."),
        ("Can I start with a small budget?", "Yes. The goal is to help small businesses start with a focused scope and upgrade as the business grows."),
        ("Do you provide GST and accounting support?", "Yes. GST registration, GST return filing, accounting support, TDS/TCS, and ESIC/PF support can be discussed based on requirements."),
        ("Do you build SEO-friendly websites?", "Yes. Website work includes clean structure, mobile-friendly design, basic SEO tags, and content guidance."),
        ("How can I contact you?", f"You can email {EMAIL}, call or WhatsApp {PHONE}, or use the consultation buttons on the website."),
    ]
    body = f"""
    <section class="hero">
      <div class="hero-grid">
        <div class="hero-copy reveal">
          <span class="section-eyebrow">Founder-led business support</span>
          <h1>Build your business online - without confusing tech, pricing, or paperwork.</h1>
          <p class="lead">Assistly WS helps Indian small businesses with websites, branding, marketing, GST, accounting support, and free business tools - all with clear guidance and transparent pricing.</p>
          <div class="hero-actions">
            <a class="btn" href="{wa('Hi Assistly WS, I want a free consultation for my business. Please guide me.')}" target="_blank" rel="noopener">Get Free Consultation</a>
            <a class="btn secondary" href="{rel_link(current, 'free-tools.html')}">Explore Free Tools</a>
          </div>
          <div class="trust-line"><span>New founder-led agency</span><span aria-hidden="true">&middot;</span><span>Concept projects available</span><span aria-hidden="true">&middot;</span><span>India-focused support</span></div>
        </div>
        <div class="hero-visual reveal" aria-label="Business services workspace illustration">
          <div class="support-dashboard">
            <div class="workspace-panel">
              <div class="panel-topbar"><div class="panel-dots"><span></span><span></span><span></span></div><div class="panel-title">Services Workspace</div></div>
              <div class="workspace-focus">
                <span class="workspace-mark" aria-hidden="true">AW</span>
                <div>
                  <strong>One support system</strong>
                  <small>Everything your business needs to start, organize, and grow.</small>
                </div>
              </div>
              <div class="workspace-modules">
                <div class="workspace-card"><span class="icon-bubble orange">{icon('web')}</span><strong>Website Design</strong><small>Pages, CTAs, SEO basics</small></div>
                <div class="workspace-card"><span class="icon-bubble">{icon('seo')}</span><strong>SEO Setup</strong><small>Search-ready structure</small></div>
                <div class="workspace-card"><span class="icon-bubble">{icon('gst')}</span><strong>GST Registration</strong><small>Documents and guidance</small></div>
                <div class="workspace-card"><span class="icon-bubble orange">{icon('accounting')}</span><strong>Accounting Support</strong><small>Records and reports</small></div>
              </div>
              <div class="workspace-strip"><span>Clear scope</span><span>Transparent pricing</span><span>Founder-led guidance</span></div>
            </div>
            <div class="floating-card fc-1"><span class="icon-bubble orange">{icon('brand')}</span><span>Branding<small>Logo and identity</small></span></div>
            <div class="floating-card fc-2"><span class="icon-bubble">{icon('ads')}</span><span>Google / Meta Ads<small>Budget-led growth</small></span></div>
            <div class="floating-card fc-3"><span class="icon-bubble">{icon('registration')}</span><span>MSME Registration<small>Udyam basics</small></span></div>
            <div class="floating-card fc-4"><span class="icon-bubble orange">{icon('tds')}</span><span>TDS/TCS Support<small>Deductions and returns</small></span></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head center reveal">
          <span class="section-eyebrow">Clear next steps</span>
          <h2>Most small businesses don't need confusing services. They need clear next steps.</h2>
        </div>
        <div class="grid grid-3">
          <article class="card reveal"><span class="icon-bubble orange">{icon('support')}</span><h3>The Problem</h3><p class="muted">Founders are often shown too many packages, vague promises, and technical words before anyone understands the actual business goal.</p></article>
          <article class="card reveal"><span class="icon-bubble">{icon('growth')}</span><h3>The Impact</h3><p class="muted">Budgets get wasted, launches get delayed, and small businesses avoid useful digital and compliance work because the process feels unclear.</p></article>
          <article class="card reveal"><span class="icon-bubble">{icon('spark')}</span><h3>The Solution</h3><p class="muted">Assistly WS keeps scope, pricing, documents, timelines, and next actions simple so you can start with confidence.</p></article>
        </div>
      </div>
    </section>

    <section class="section white">
      <div class="container service-universe">
        <div class="section-head reveal">
          <span class="section-eyebrow">Service universe</span>
          <h2>One practical support layer for your business basics.</h2>
          <p class="lead">Start with what matters now: a website, brand identity, marketing system, or compliance support. Build from there without pressure.</p>
          <a class="btn universe-cta" href="{rel_link(current, 'services.html')}">Explore Services <span aria-hidden="true">-&gt;</span></a>
        </div>
        <div class="ecosystem-visual reveal" aria-label="Four pillar business support ecosystem">
          <div class="ecosystem-center">
            <span class="workspace-mark" aria-hidden="true">AW</span>
            <strong>Your Business</strong>
            <small>One clear place to organize digital, growth, and compliance support.</small>
          </div>
          <article class="ecosystem-card pillar-web"><span class="icon-bubble orange">{icon('web')}</span><h3>Website</h3><p>Business websites, landing pages, SEO-ready pages, and WhatsApp-first contact paths.</p></article>
          <article class="ecosystem-card pillar-brand"><span class="icon-bubble">{icon('brand')}</span><h3>Branding</h3><p>Logo direction, visual identity, brand briefs, and clear customer-facing presentation.</p></article>
          <article class="ecosystem-card pillar-growth"><span class="icon-bubble">{icon('ads')}</span><h3>Marketing</h3><p>SEO basics, Meta Ads, Google Ads, campaign pages, and budget planning.</p></article>
          <article class="ecosystem-card pillar-compliance"><span class="icon-bubble orange">{icon('compliance')}</span><h3>Compliance</h3><p>GST, MSME, registration, accounting, return filing, and TDS/TCS support.</p></article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head reveal"><span class="section-eyebrow">Core services</span><h2>Services designed for small business growth</h2><p class="lead">We help Indian small businesses with practical digital and business support - from websites and branding to GST, compliance, and growth services.</p></div>
        {card_grid(home_service_cards, current, 'web', 'grid-4 core-services-grid', 'service-card')}
      </div>
    </section>

    <section class="section white">
      <div class="container">
        <div class="section-head reveal"><span class="section-eyebrow">Free tools marketplace</span><h2>Useful tools before you spend money.</h2><p class="lead">Estimate costs, prepare simple documents, and clarify decisions before starting a paid service.</p></div>
        {card_grid(tool_cards, current, 'calc', 'grid-4 tools-grid', 'tool-card')}
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head reveal"><span class="section-eyebrow">Templates library</span><h2>Small business templates you can adapt.</h2><p class="lead">Preview practical formats for invoices, proposals, salary slips, branding briefs, and content planning.</p></div>
        {card_grid(template_cards, current, 'doc')}
      </div>
    </section>

    <section class="section white">
      <div class="container">
        <div class="section-head reveal"><span class="section-eyebrow">Projects</span><h2>Concept projects built to show our thinking</h2><p class="lead">We are a new agency, so instead of fake client claims, we show concept projects, design concepts, and practical service examples.</p></div>
        <div class="grid grid-3">{demo_cards}</div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="founder-note reveal">
          <div class="avatar" aria-hidden="true">RT</div>
          <div>
            <span class="section-eyebrow">Founder-led advantage</span>
            <h2>You don't deal with a sales team. You talk directly with the person building your work.</h2>
            <p class="lead">Hi, I'm Rajat. I started Assistly WS to help small businesses get practical digital and business support with clear pricing, honest communication, and useful guidance. We are new, but our focus is simple: clean work, transparent process, and real value.</p>
          </div>
        </div>
        <div class="grid grid-4" style="margin-top:22px">
          {''.join(f'<article class="card reveal"><h3>{title}</h3><p class="muted">{text}</p></article>' for title, text in [
            ('Direct communication', 'Speak directly with the person planning and building the work.'),
            ('Affordable for small businesses', 'Start with a focused scope and upgrade as needs become clearer.'),
            ('No fake promises', 'No ranking promises, fake awards, or inflated claims.'),
            ('Practical guidance', 'Get simple recommendations for the next useful business step.'),
          ])}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head reveal"><span class="section-eyebrow">Process</span><h2>From idea to launch - simple 4-step process</h2></div>
        <div class="timeline">
          <div class="timeline-fill" aria-hidden="true"></div>
          {''.join(f'<div class="timeline-step reveal"><div class="timeline-number">{i}</div><div class="card no-hover"><h3>{title}</h3><p class="muted">{text}</p></div></div>' for i, (title, text) in enumerate([
            ('Understand', 'We discuss your business type, goal, budget, timeline, and current blockers.'),
            ('Plan', 'You get a practical scope, documents needed, page list, and next steps.'),
            ('Build', 'The agreed work is created with clear communication and review points.'),
            ('Support', 'You get handover guidance and optional support for updates or next services.'),
          ], start=1))}
        </div>
      </div>
    </section>

    <section class="section white">
      <div class="container">
        <div class="section-head reveal"><span class="section-eyebrow">Pricing preview</span><h2>Start small. Upgrade when your business grows.</h2></div>
        <div class="grid grid-3">{pricing_cards}</div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head reveal"><span class="section-eyebrow">Blog</span><h2>Learn before you spend</h2></div>
        {card_grid(blog_cards, current, 'doc')}
      </div>
    </section>

    <section class="section white">
      <div class="container narrow">
        <div class="section-head reveal"><span class="section-eyebrow">FAQ</span><h2>Questions small business owners ask first.</h2></div>
        {faq_html(faqs, 'home')}
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="cta-band reveal">
          <h2>Not sure what your business needs first?</h2>
          <p class="lead">Send your business type and goal. We'll suggest the best website, marketing, or business support plan.</p>
          <div class="cta-actions">
            <a class="btn" href="{wa('Hi Assistly WS, I am not sure what my business needs first. Please guide me.')}" target="_blank" rel="noopener">Chat on WhatsApp</a>
            <a class="btn secondary" href="{rel_link(current, 'services.html')}">Explore Services</a>
          </div>
        </div>
      </div>
    </section>
    """
    schemas = [organization_schema(), website_schema(), breadcrumb_schema([("Home", "index.html")]), faq_schema(faqs)]
    render_page(
        current,
        "Assistly WS | Founder-Led Website, Marketing and Business Support in India",
        "Assistly WS is a new founder-led service agency for Indian small businesses, offering websites, branding, marketing, GST, accounting support, free tools, and templates.",
        body,
        schemas,
    )


def service_cards(current: str) -> list[dict]:
    icon_map = {
        "website-design": "web",
        "landing-page-design": "web-calc",
        "wordpress-website": "web",
        "shopify-store": "web",
        "seo-services": "seo",
        "social-media-marketing": "ads",
        "meta-ads": "ads",
        "google-ads": "growth",
        "logo-design": "brand",
        "branding": "brand",
        "gst-registration": "gst",
        "msme-registration": "registration",
        "company-registration": "compliance",
        "gst-return-filing": "gst",
        "accounting-support": "accounting",
        "tds-tcs-return": "tds",
        "esic-pf-support": "compliance",
    }
    return [
        {
            "title": service["name"],
            "text": service["quick"],
            "url": f"services/{service['slug']}.html",
            "cta": "View service",
            "icon": icon_map.get(service["slug"], "support"),
            "accent": service["slug"] in {"website-design", "branding", "gst-registration", "accounting-support"},
        }
        for service in SERVICES
    ]


def listing_pages() -> None:
    # Services listing
    current = "services.html"
    crumbs = [("Home", "index.html"), ("Services", current)]
    body = page_hero(current, crumbs, "Services", "Services for websites, marketing, branding, and business support", "Choose a clear starting point for your small business. Each service page includes quick answers, pricing guidance, required details, process, mistakes, FAQs, and related resources.")
    body += f"""
    <section class="section"><div class="container">{card_grid(service_cards(current), current, 'web')}</div></section>
    <section class="section white"><div class="container"><div class="cta-band reveal"><h2>Need help choosing a service?</h2><p class="lead">Send your business type, current goal, and rough budget. I will suggest a practical first step.</p><a class="btn" href="{wa('Hi Assistly WS, I need help choosing the right service for my business.')}" target="_blank" rel="noopener">Ask on WhatsApp</a></div></div></section>
    """
    render_page(current, "Services | Assistly WS", "Explore Assistly WS services for website design, landing pages, WordPress, Shopify, SEO, ads, branding, GST, accounting, TDS/TCS, and ESIC/PF support.", body, [organization_schema(), breadcrumb_schema(crumbs)])

    # Free tools listing
    current = "free-tools.html"
    crumbs = [("Home", "index.html"), ("Free Tools", current)]
    cards = [{"title": t["name"], "text": t["short"], "url": f"tools/{t['slug']}.html", "badge": "Free", "badge_class": "green", "cta": "Use Tool", "icon": t.get("icon", "calc")} for t in TOOLS]
    body = page_hero(current, crumbs, "Free tools", "Free business tools for clearer decisions", "Use calculators, generators, and checklists before you buy a service or make a business decision.")
    body += f'<section class="section"><div class="container">{card_grid(cards, current, "calc", "grid-4 tools-grid", "tool-card")}</div></section>'
    render_page(current, "Free Tools for Indian Small Businesses | Assistly WS", "Use free calculators and practical tools for website cost, GST late fee, TDS, ad budget, SEO, profit margin, and logo briefs.", body, [organization_schema(), breadcrumb_schema(crumbs)])

    # Templates listing
    current = "templates.html"
    crumbs = [("Home", "index.html"), ("Templates", current)]
    cards = [{"title": name, "text": desc, "url": f"templates/{slug}.html", "badge": file_type, "cta": "Download placeholder", "icon": "doc"} for slug, name, file_type, desc, *_ in TEMPLATES]
    body = page_hero(current, crumbs, "Templates", "Templates library for small business work", "Preview practical templates for invoices, quotations, salary slips, business planning, proposals, social media, SEO, branding, onboarding, and service agreements.")
    body += f'<section class="section"><div class="container">{card_grid(cards, current, "doc")}</div></section>'
    render_page(current, "Templates Library | Assistly WS", "Browse practical business templates for GST invoices, quotations, salary slips, business plans, website proposals, social calendars, SEO checklists, and agreements.", body, [organization_schema(), breadcrumb_schema(crumbs)])

    # Blog listing
    current = "blog.html"
    crumbs = [("Home", "index.html"), ("Blog", current)]
    cards = [{"title": b["h1"], "text": b["short"], "url": f"blog/{b['slug']}.html", "cta": "Read guide", "icon": "doc"} for b in BLOGS]
    body = page_hero(current, crumbs, "Blog", "Helpful guides before you spend", "Simple explainers for websites, GST, MSME, ads, SEO, hosting, invoices, and local marketing for Indian small businesses.")
    body += f'<section class="section"><div class="container">{card_grid(cards, current, "doc")}</div></section>'
    render_page(current, "Blog | Assistly WS", "Read practical guides for Indian small businesses on website cost, GST registration, MSME benefits, ads, SEO, hosting, website checklists, invoices, and local marketing.", body, [organization_schema(), breadcrumb_schema(crumbs)])


def about_contact_pricing_demo() -> None:
    # About
    current = "about.html"
    crumbs = [("Home", "index.html"), ("About", current)]
    body = page_hero(current, crumbs, "About", "A new founder-led agency built on honest support", "Assistly WS is starting small and intentionally transparent: no fake numbers, no fake client logos, no inflated promises.")
    body += f"""
    <section class="section">
      <div class="container content-layout">
        <div class="content-main">
          <div class="answer-block reveal"><strong>Short answer:</strong> Assistly WS is a new solo founder-led service agency based around Sonipat / Delhi NCR, serving Indian small businesses with websites, marketing, branding, compliance support, accounting support, free tools, and templates.</div>
          <section class="content-block reveal"><h2>Why Assistly WS exists</h2><p>Many small businesses want to move online or organize compliance work, but the buying process is often confusing. Assistly WS is designed to make the first step clearer. You can use free tools, read guides, view concept work, and then request a practical quote.</p><p>The positioning is simple: new founder-led agency, direct communication, transparent pricing, and useful guidance. I do not claim fake clients, fake awards, or guaranteed outcomes.</p></section>
          <section class="content-block reveal"><h2>Founder note</h2><p>Hi, I am {FOUNDER}. I started Assistly WS to help small businesses with clean websites, useful marketing foundations, branding basics, GST/accounting support coordination, and resources that make decisions easier. The agency is new, so the focus is on practical value, concept projects, and honest conversations.</p></section>
          <section class="content-block reveal"><h2>What you can expect</h2><ul class="list-check"><li>Clear scope before work starts</li><li>Direct founder communication</li><li>India-focused support and documents</li><li>Simple pricing guidance</li><li>No fake promises or ranking promises</li></ul></section>
        </div>
        <aside class="card aside-card reveal"><h3>Contact details</h3><p><strong>Email:</strong><br><a href="mailto:{EMAIL}">{EMAIL}</a></p><p><strong>Phone/WhatsApp:</strong><br><a href="tel:+918059134416">{PHONE}</a></p><p><strong>Location:</strong><br>{LOCATION}</p><a class="btn" href="{wa('Hi Assistly WS, I want to know more about your services.')}" target="_blank" rel="noopener">Talk to Rajat</a></aside>
      </div>
    </section>
    """
    render_page(current, "About Assistly WS | Founder-Led Agency in Sonipat / Delhi NCR", "Learn about Assistly WS, a new founder-led service agency serving Indian small businesses with honest website, marketing, branding, GST, and accounting support.", body, [organization_schema(), breadcrumb_schema(crumbs)])

    # Contact
    current = "contact.html"
    crumbs = [("Home", "index.html"), ("Contact", current)]
    body = page_hero(current, crumbs, "Contact", "Tell me what your business needs", "Use the static form below to open a WhatsApp message with your details, or contact Assistly WS directly by email or phone.")
    body += f"""
    <section class="section">
      <div class="container tool-shell">
        <form class="card contact-form reveal" data-contact-form>
          <h2>Free consultation form</h2>
          <div class="form-grid">
            <div class="field"><label for="name">Name</label><input id="name" name="name" required autocomplete="name"></div>
            <div class="field"><label for="mobile">Mobile number</label><input id="mobile" name="mobile" required autocomplete="tel"></div>
            <div class="field"><label for="business">Business type</label><input id="business" name="business" required placeholder="Example: salon, CA firm, coaching, shop"></div>
            <div class="field"><label for="service">Required service</label><select id="service" name="service" required><option value="">Select a service</option>{''.join(f'<option>{esc(s["name"])}</option>' for s in SERVICES)}</select></div>
            <div class="field"><label for="budget">Budget</label><select id="budget" name="budget"><option>Not sure</option><option>Under Rs 5,000</option><option>Rs 5,000 - Rs 10,000</option><option>Rs 10,000 - Rs 25,000</option><option>Custom/ongoing</option></select></div>
          </div>
          <div class="field"><label for="message">Message</label><textarea id="message" name="message" placeholder="Tell me your goal, timeline, and any current challenge."></textarea></div>
          <button class="btn" type="submit">Open WhatsApp with details</button>
          <p class="muted">No backend is connected. This form creates a WhatsApp message. Google Forms, Formspree, or a custom backend can be connected later.</p>
        </form>
        <aside class="card reveal">
          <h2>Direct contact</h2>
          <p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>
          <p><strong>Phone/WhatsApp:</strong> <a href="tel:+918059134416">{PHONE}</a></p>
          <p><strong>Location:</strong> {LOCATION}</p>
          <p><strong>Service area:</strong> {SERVICE_AREA}</p>
          <a class="btn secondary" href="{wa('Hi Assistly WS, I want to discuss a project.')}" target="_blank" rel="noopener">Chat on WhatsApp</a>
        </aside>
      </div>
    </section>
    """
    render_page(current, "Contact Assistly WS | Free Consultation", "Contact Assistly WS for website design, branding, SEO, ads, GST, accounting, and business support. Static form opens WhatsApp with your details.", body, [organization_schema(), breadcrumb_schema(crumbs)])

    # Pricing
    current = "pricing.html"
    crumbs = [("Home", "index.html"), ("Pricing", current)]
    pricing = [
        ("Starter Website", "&#8377;4,999 onwards", ["3-5 pages", "Mobile responsive layout", "WhatsApp/contact CTA", "Basic SEO setup", "5-7 day delivery target"], "Hi Assistly WS, I want the Starter Website package. Please guide me."),
        ("Growth Website", "&#8377;9,999 onwards", ["6-10 pages", "SEO-friendly structure", "Blog setup", "Lead form guidance", "Speed optimization basics"], "Hi Assistly WS, I want the Growth Website package. Please guide me."),
        ("Landing Page", "&#8377;2,999 onwards", ["Single offer page", "Campaign-focused copy structure", "WhatsApp CTA", "FAQ section", "Mobile-first design"], "Hi Assistly WS, I want a landing page. Please guide me."),
        ("Logo Design", "&#8377;1,999 onwards", ["Logo direction", "Color guidance", "Basic file exports", "Usage note", "Revision scope discussed first"], "Hi Assistly WS, I need logo design. Please guide me."),
        ("SEO Support", "&#8377;4,999 onwards/month", ["Keyword mapping", "On-page review", "Internal linking", "Local SEO basics", "Monthly improvement plan"], "Hi Assistly WS, I need SEO support. Please guide me."),
        ("Business Support", "Custom pricing", ["GST", "Accounting", "TDS/TCS", "ESIC/PF", "Ongoing support"], "Hi Assistly WS, I need business support. Please guide me with cost and documents."),
    ]
    cards = "".join(f'<article class="card reveal"><h3>{name}</h3><div class="price">{price}</div><ul class="list-check">{"".join(f"<li>{esc(i)}</li>" for i in items)}</ul><a class="btn small" href="{wa(msg)}" target="_blank" rel="noopener">Request quote</a></article>' for name, price, items, msg in pricing)
    body = page_hero(current, crumbs, "Pricing", "Transparent starting prices for practical scopes", "These are starting prices for planning. Final pricing depends on pages, content, documents, integrations, timeline, and support needs.")
    body += f'<section class="section"><div class="container"><div class="grid grid-3">{cards}</div></div></section><section class="section white"><div class="container narrow"><div class="answer-block reveal"><strong>Pricing note:</strong> Assistly WS is a new founder-led agency. Pricing is kept transparent, but no package promises fixed ranking positions, fixed lead volume, or fake outcomes.</div></div></section>'
    render_page(current, "Pricing | Assistly WS", "View transparent starting prices for websites, landing pages, logo design, SEO support, and custom business support from Assistly WS.", body, [organization_schema(), breadcrumb_schema(crumbs)])

    # Projects
    current = "demo-work.html"
    crumbs = [("Home", "index.html"), ("Projects", current)]
    demo_items = [
        ("Business Services Website Concept", "A premium service website layout with service pages, FAQs, WhatsApp CTAs, pricing preview, and answer blocks."),
        ("Accounting Software UI Concept", "A dashboard-style concept showing invoice cards, monthly overview, compliance reminders, and business reports."),
        ("Local Business Website Concept", "A simple but polished website structure for a local business that needs calls, WhatsApp leads, and location clarity."),
        ("Shopify Store Concept", "A clean storefront concept for product categories, product cards, policy blocks, and checkout readiness."),
        ("SEO Landing Page Concept", "An answer-engine-friendly service page concept with quick answer, summary table, process, mistakes, and FAQs."),
        ("Brand Identity Concept", "A starter identity concept with logo direction, palette, typography, and practical usage examples."),
    ]
    cards = "".join(f'<article class="card reveal"><div class="demo-frame"><span class="badge orange">Concept Project</span></div><h3>{esc(name)}</h3><p class="muted">{esc(desc)}</p></article>' for name, desc in demo_items)
    body = page_hero(current, crumbs, "Projects", "Concept projects built to show the thinking", "Assistly WS is new. Instead of fake client claims, this page shows concept projects, service examples, and design thinking that reflect the practical approach.")
    body += f'<section class="section"><div class="container"><div class="grid grid-3">{cards}</div></div></section><section class="section white"><div class="container"><div class="cta-band reveal"><h2>Want a similar concept for your business?</h2><p class="lead">Share your business type and goal. I will suggest a simple direction before you commit to a full project.</p><a class="btn" href="{wa("Hi Assistly WS, I saw your concept projects and want a similar direction for my business.")}" target="_blank" rel="noopener">Discuss a concept</a></div></div></section>'
    render_page(current, "Projects and Concept Work | Assistly WS", "View honest concept projects from Assistly WS. No fake client claims, only practical examples and design thinking.", body, [organization_schema(), breadcrumb_schema(crumbs)])


def service_page(service: dict) -> None:
    current = f"services/{service['slug']}.html"
    crumbs = [("Home", "index.html"), ("Services", "services.html"), (service["name"], current)]
    faqs = service["faqs"]
    summary_rows = [
        ("Starting price", service["price"]),
        ("Timeline", service["timeline"]),
        ("Best for", service["best"]),
        ("Service area", "India, with support from Sonipat / Delhi NCR, Haryana"),
    ]
    body = page_hero(current, crumbs, "Service", service["h1"], service["quick"])
    body += f"""
    <section class="section">
      <div class="container content-layout">
        <div class="content-main">
          <div class="answer-block reveal"><strong>Short answer:</strong> {service['quick']}</div>
          <table class="summary-table reveal"><tbody>{''.join(f'<tr><th>{k}</th><td>{v}</td></tr>' for k, v in summary_rows)}</tbody></table>
          <section class="content-block reveal" id="who"><h2>Who this service is for</h2><p>{esc(service['best'])}. This is especially useful when you want practical support, clear communication, and a scope that fits a small business budget.</p></section>
          <section class="content-block reveal" id="what-you-get"><h2>What you get</h2><ul class="list-check">{''.join(f'<li>{esc(item)}</li>' for item in service['gets'])}</ul></section>
          <section class="content-block reveal" id="documents"><h2>Required details or documents</h2><ul class="list-check">{''.join(f'<li>{esc(item)}</li>' for item in service['docs'])}</ul></section>
          <section class="content-block reveal" id="process"><h2>Step-by-step process</h2><div class="grid grid-4">{''.join(f'<article class="card no-hover"><span class="badge">{i}</span><h3>{title}</h3><p class="muted">{text}</p></article>' for i, (title, text) in enumerate([('Understand', 'We discuss your goal, current status, budget, and timeline.'), ('Collect', 'You share required content, access, details, or documents.'), ('Prepare', 'I create the agreed work or coordinate the required support.'), ('Review', 'You review, ask questions, and receive next-step guidance.')], start=1))}</div></section>
          <section class="content-block reveal" id="mistakes"><h2>Common mistakes to avoid</h2><ul class="list-check">{''.join(f'<li>{esc(item)}</li>' for item in service['mistakes'])}</ul></section>
          <section class="content-block reveal" id="related"><h2>Related resources</h2><div class="grid grid-3">
            <article class="card"><span class="icon-bubble">{icon('calc')}</span><h3>Related tool</h3><a class="card-link" href="{rel_link(current, service['tool'])}">Open tool <span aria-hidden="true">-&gt;</span></a></article>
            <article class="card"><span class="icon-bubble">{icon('doc')}</span><h3>Related template</h3><a class="card-link" href="{rel_link(current, service['template'])}">View template <span aria-hidden="true">-&gt;</span></a></article>
            <article class="card"><span class="icon-bubble">{icon('doc')}</span><h3>Related guide</h3><a class="card-link" href="{rel_link(current, service['blog'])}">Read blog <span aria-hidden="true">-&gt;</span></a></article>
          </div></section>
          <section class="content-block reveal" id="faq"><h2>FAQs</h2>{faq_html(faqs, service['slug'])}</section>
        </div>
        <aside class="card aside-card reveal">
          <h3>{service['name']} at a glance</h3>
          <p><strong>Starting price:</strong><br>{service['price']}</p>
          <p><strong>Timeline:</strong><br>{esc(service['timeline'])}</p>
          <p><strong>Last updated:</strong><br>{UPDATED_LABEL}</p>
          <a class="btn" href="{wa('Hi Assistly WS, I need help with ' + service['name'] + '. Please share cost, process, and required details.')}" target="_blank" rel="noopener">Ask on WhatsApp</a>
        </aside>
      </div>
    </section>
    """
    schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": service["name"],
        "description": service["quick"],
        "provider": {"@type": "Organization", "name": SITE_NAME, "url": DOMAIN},
        "areaServed": {"@type": "Country", "name": "India"},
        "offers": {"@type": "Offer", "priceCurrency": "INR", "description": service["price"]},
    }
    render_page(current, service["title"], service["meta"], body, [schema, faq_schema(faqs), breadcrumb_schema(crumbs)])


def tool_form(tool: dict) -> str:
    kind = tool["kind"]
    if kind == "website-cost":
        return """
        <form class="tool-form" data-tool-form="website-cost">
          <div class="form-grid">
            <div class="field"><label>Website type</label><select name="websiteType"><option value="basic">Basic business website</option><option value="business">Growth business website</option><option value="ecommerce">Ecommerce website</option><option value="custom">Custom website</option></select></div>
            <div class="field"><label>Number of pages</label><input name="pages" type="number" value="5" min="1"></div>
            <div class="field"><label>Design level</label><select name="designLevel"><option value="simple">Simple clean design</option><option value="premium">Premium layout</option><option value="custom">Custom visual direction</option></select></div>
            <div class="field"><label>Delivery urgency</label><select name="urgency"><option value="normal">Normal</option><option value="fast">Fast delivery</option></select></div>
          </div>
          <label class="checkbox-row"><input type="checkbox" name="contactForm" value="yes" checked> Contact form / WhatsApp CTA</label>
          <label class="checkbox-row"><input type="checkbox" name="blog" value="yes"> Blog setup</label>
          <label class="checkbox-row"><input type="checkbox" name="seo" value="yes" checked> Basic SEO setup</label>
          <label class="checkbox-row"><input type="checkbox" name="content" value="yes"> Content writing support</label>
          <button class="btn" type="submit">Calculate estimate</button>
        </form>
        """
    if kind == "gst-late-fee":
        return """
        <form class="tool-form" data-tool-form="gst-late-fee">
          <div class="form-grid">
            <div class="field"><label>Days delayed</label><input name="days" type="number" value="10" min="0"></div>
            <div class="field"><label>Tax amount payable</label><input name="taxAmount" type="number" value="10000" min="0"></div>
          </div>
          <label class="checkbox-row"><input type="checkbox" name="nilReturn" value="yes"> Nil return</label>
          <button class="btn" type="submit">Estimate late fee</button>
        </form>
        """
    if kind == "tds-calculator":
        return """
        <form class="tool-form" data-tool-form="tds-calculator">
          <div class="form-grid">
            <div class="field"><label>Payment amount</label><input name="amount" type="number" value="50000" min="0"></div>
            <div class="field"><label>TDS rate (%)</label><input name="rate" type="number" value="10" min="0" step="0.1"></div>
          </div>
          <button class="btn" type="submit">Calculate TDS</button>
        </form>
        """
    if kind == "ad-budget":
        return """
        <form class="tool-form" data-tool-form="ad-budget">
          <div class="form-grid">
            <div class="field"><label>Monthly ad budget</label><input name="budget" type="number" value="15000" min="0"></div>
            <div class="field"><label>Meta Ads share (%)</label><input name="metaShare" type="number" value="50" min="0" max="100"></div>
            <div class="field"><label>Expected average CPC</label><input name="cpc" type="number" value="20" min="1"></div>
            <div class="field"><label>Expected conversion rate (%)</label><input name="conversionRate" type="number" value="3" min="0.1" step="0.1"></div>
          </div>
          <button class="btn" type="submit">Plan budget</button>
        </form>
        """
    if kind == "seo-checklist":
        checks = ["Unique title and meta description", "One clear H1", "Helpful service or answer block", "Mobile layout checked", "Page speed reviewed", "Internal links added", "FAQ section included", "Images have alt text", "Google Business Profile linked where relevant", "Tracking plan ready"]
        return f"""
        <form class="tool-form" data-tool-form="seo-checklist">
          <div class="progress-track" aria-hidden="true"><span></span></div>
          <div class="checklist-tool">{''.join(f'<label class="checkbox-row"><input type="checkbox"> {esc(item)}</label>' for item in checks)}</div>
        </form>
        """
    if kind == "profit-margin":
        return """
        <form class="tool-form" data-tool-form="profit-margin">
          <div class="form-grid">
            <div class="field"><label>Selling price / revenue</label><input name="revenue" type="number" value="10000" min="0"></div>
            <div class="field"><label>Direct cost</label><input name="cost" type="number" value="6000" min="0"></div>
            <div class="field"><label>Extra expenses</label><input name="extra" type="number" value="500" min="0"></div>
          </div>
          <button class="btn" type="submit">Calculate margin</button>
        </form>
        """
    if kind == "logo-brief":
        return """
        <form class="tool-form" data-tool-form="logo-brief">
          <div class="form-grid">
            <div class="field"><label>Brand name</label><input name="brand" value="Your Brand"></div>
            <div class="field"><label>Target audience</label><input name="audience" value="Small business owners"></div>
            <div class="field"><label>Preferred style</label><input name="style" value="Clean, premium, trustworthy"></div>
            <div class="field"><label>Color direction</label><input name="colors" value="Navy, orange, white"></div>
          </div>
          <div class="field"><label>Extra notes</label><textarea name="notes">Need a logo for website, social media, and invoices.</textarea></div>
          <button class="btn" type="submit">Generate logo brief</button>
        </form>
        """
    return ""


def tool_page(tool: dict) -> None:
    current = f"tools/{tool['slug']}.html"
    crumbs = [("Home", "index.html"), ("Free Tools", "free-tools.html"), (tool["name"], current)]
    faqs = [
        (f"Is the {tool['name']} free?", f"Yes. The {tool['name']} is free to use on this static website."),
        ("Is the result a final professional quote or compliance answer?", "No. The result is a planning estimate or draft. Final pricing, tax, accounting, or compliance decisions should be checked for your exact situation."),
        ("Can Assistly WS help after I use the tool?", "Yes. You can share the result on WhatsApp and ask for practical next-step guidance."),
        ("Does this tool save my data?", "No backend or database is connected in this static website. The tool runs in your browser."),
    ]
    body = page_hero(current, crumbs, "Free tool", tool["h1"], tool["summary"])
    body += f"""
    <section class="section">
      <div class="container tool-shell">
        <div class="card reveal">
          <h2>Use the tool</h2>
          <p class="muted">{esc(tool['short'])}</p>
          {tool_form(tool)}
        </div>
        <aside class="result-card reveal" aria-live="polite"><h3>Your result will appear here</h3><p class="muted">Enter details and use the tool to see an estimate, preview, or generated draft.</p></aside>
      </div>
    </section>
    <section class="section white">
      <div class="container content-layout">
        <div class="content-main article-body">
          <div class="answer-block reveal"><strong>Short answer:</strong> {esc(tool['summary'])}</div>
          <table class="summary-table reveal"><tbody>
            <tr><th>Best used for</th><td>Early planning, budget clarity, document preparation, and deciding what to ask before paying for support.</td></tr>
            <tr><th>Who can use it</th><td>Indian small business owners, freelancers, founders, local shops, service providers, and early-stage teams.</td></tr>
            <tr><th>Data storage</th><td>No backend or database is connected. The tool runs in your browser.</td></tr>
            <tr><th>Last updated</th><td>{UPDATED_LABEL}</td></tr>
          </tbody></table>
          <section class="content-block reveal" id="what-is-it"><h2>What is this tool?</h2><p>The {esc(tool['name'])} is a simple browser-based utility made for practical business planning. It is not designed to replace a professional consultation, but it helps you avoid a completely blank starting point. You can enter basic information, review a result, and then decide whether you need website, marketing, accounting, GST, or branding support.</p><p>Assistly WS is a new founder-led agency, so these tools are also part of the honest support approach. Instead of pushing you directly into a package, the goal is to help you understand the factors that affect cost, documents, timelines, and decisions.</p></section>
          <section class="content-block reveal" id="how-to-use"><h2>How to use it step by step</h2><ul class="list-check"><li>Enter realistic details instead of ideal guesses.</li><li>Review the result as a planning estimate or working draft.</li><li>Note the assumptions that affect the number or output.</li><li>Open the related service or template if you need a next step.</li><li>Send the result on WhatsApp if you want a human review.</li></ul></section>
          <section class="content-block reveal" id="factors"><h2>Cost, factors, or usage table</h2><table class="summary-table"><tbody><tr><th>Input quality</th><td>Better inputs create more useful planning results.</td></tr><tr><th>Business type</th><td>A local service business, ecommerce brand, freelancer, and registered company may need different follow-up steps.</td></tr><tr><th>Urgency</th><td>Urgent work can increase cost or reduce review time.</td></tr><tr><th>Compliance impact</th><td>Tax and compliance tools should be treated as estimates until verified.</td></tr></tbody></table></section>
          <section class="content-block reveal" id="mistakes"><h2>Common mistakes</h2><ul class="list-check"><li>Treating an estimate as a final quote without reviewing scope.</li><li>Ignoring documents, access, content, or approvals needed for execution.</li><li>Using old tax or compliance assumptions without checking current applicability.</li><li>Comparing only price and not timeline, support, clarity, and quality.</li><li>Not keeping a copy of the final details you want to share with a service provider.</li></ul></section>
          <section class="content-block reveal" id="founder-note"><h2>Founder note</h2><p>I built this page to make the first conversation easier. If you are unsure, share your result and business context. I will tell you what looks clear, what needs checking, and whether you should start small or wait until more details are ready.</p></section>
          <section class="content-block reveal" id="related"><h2>Related resources</h2><div class="grid grid-3"><article class="card"><h3>Related service</h3><a class="card-link" href="{rel_link(current, tool['service'])}">Open service <span aria-hidden="true">-&gt;</span></a></article><article class="card"><h3>Related template</h3><a class="card-link" href="{rel_link(current, tool['template'])}">View template <span aria-hidden="true">-&gt;</span></a></article><article class="card"><h3>Related guide</h3><a class="card-link" href="{rel_link(current, tool['blog'])}">Read guide <span aria-hidden="true">-&gt;</span></a></article></div></section>
          <section class="content-block reveal" id="faq"><h2>FAQs</h2>{faq_html(faqs, tool['slug'])}</section>
        </div>
        <aside class="card aside-card reveal"><h3>Need a human review?</h3><p class="muted">Send your result and business type. I will suggest the next practical step.</p><a class="btn" href="{wa('Hi Assistly WS, I used the ' + tool['name'] + '. Please review my result and guide me.')}" target="_blank" rel="noopener">Review on WhatsApp</a></aside>
      </div>
    </section>
    """
    schema = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": tool["name"],
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "Web browser",
        "url": page_url(current),
        "description": tool["summary"],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
    }
    render_page(current, tool["title"], tool["meta"], body, [schema, faq_schema(faqs), breadcrumb_schema(crumbs)])


def template_page(item: tuple) -> None:
    slug, name, file_type, desc, service, tool, blog = item
    current = f"templates/{slug}.html"
    crumbs = [("Home", "index.html"), ("Templates", "templates.html"), (name, current)]
    faqs = [
        (f"What is the {name}?", f"The {name} is a practical business document preview you can adapt for your own workflow."),
        ("Is the download button connected?", "This static version includes a placeholder download button. You can connect an actual PDF, DOCX, or XLSX file later."),
        ("Can Assistly WS customize this template?", "Yes. I can help adapt the template for your business, service, invoice, proposal, or internal process."),
        ("Should I get legal or tax review?", "For legal, tax, or compliance-sensitive documents, get professional review before final use."),
    ]
    fields = ["Business name", "Contact details", "Date and reference number", "Customer or client details", "Scope, items, or financial values", "Terms, notes, or approval fields"]
    body = page_hero(current, crumbs, "Template", name, desc)
    body += f"""
    <section class="section">
      <div class="container tool-shell">
        <div class="doc-preview reveal">
          <div class="doc-preview-header"><strong>{esc(name)}</strong><span>{esc(file_type)}</span></div>
          <div class="doc-lines" aria-label="{esc(name)} preview">
            <div class="doc-line"></div><div class="doc-line short"></div><div class="doc-line"></div><div class="doc-line"></div><div class="doc-line short"></div>
          </div>
        </div>
        <aside class="download-placeholder reveal">
          <span class="badge orange">{esc(file_type)}</span>
          <h2>Download placeholder</h2>
          <p class="muted">The static page is ready. Connect the actual downloadable file later in the assets or templates folder.</p>
          <button class="btn secondary" type="button" disabled aria-disabled="true">Download placeholder</button>
          <a class="btn" href="{wa('Hi Assistly WS, I want the ' + name + ' template. Please guide me.')}" target="_blank" rel="noopener">Request template on WhatsApp</a>
        </aside>
      </div>
    </section>
    <section class="section white">
      <div class="container content-layout">
        <div class="content-main article-body">
          <div class="answer-block reveal"><strong>Short answer:</strong> {esc(desc)} It is useful when you want a clean structure before creating a final business document.</div>
          <table class="summary-table reveal"><tbody><tr><th>File type</th><td>{esc(file_type)}</td></tr><tr><th>Best for</th><td>Small businesses, freelancers, service providers, and founders who need a practical format.</td></tr><tr><th>Last updated</th><td>{UPDATED_LABEL}</td></tr></tbody></table>
          <section class="content-block reveal"><h2>What is this template?</h2><p>The {esc(name)} gives you a clear starting structure so you do not have to create the document from zero. It is designed for small business use, simple editing, and practical communication with customers, vendors, employees, or service providers.</p></section>
          <section class="content-block reveal"><h2>When to use it</h2><p>Use this template when you need a cleaner way to document business information, pricing, scope, records, or next steps. It can help reduce confusion, but final legal, tax, or compliance details should be reviewed for your exact situation.</p></section>
          <section class="content-block reveal"><h2>Required fields</h2><ul class="list-check">{''.join(f'<li>{esc(field)}</li>' for field in fields)}</ul></section>
          <section class="content-block reveal"><h2>How to use it step by step</h2><ul class="list-check"><li>Duplicate the template for your business.</li><li>Replace placeholder details with accurate information.</li><li>Check calculations, dates, and terms before sharing.</li><li>Save a final PDF copy for records when needed.</li><li>Ask for review if the document affects payment, tax, or legal terms.</li></ul></section>
          <section class="content-block reveal"><h2>Common mistakes</h2><ul class="list-check"><li>Leaving old placeholder text in the document.</li><li>Using unclear payment or delivery terms.</li><li>Forgetting invoice numbers, dates, GST details, or client information where needed.</li><li>Sharing editable files when a locked PDF would be safer.</li></ul></section>
          <section class="content-block reveal"><h2>Related resources</h2><div class="grid grid-3"><article class="card"><h3>Related service</h3><a class="card-link" href="{rel_link(current, service)}">Open service <span aria-hidden="true">-&gt;</span></a></article><article class="card"><h3>Related tool</h3><a class="card-link" href="{rel_link(current, tool)}">Use tool <span aria-hidden="true">-&gt;</span></a></article><article class="card"><h3>Related guide</h3><a class="card-link" href="{rel_link(current, blog)}">Read guide <span aria-hidden="true">-&gt;</span></a></article></div></section>
          <section class="content-block reveal"><h2>FAQs</h2>{faq_html(faqs, slug)}</section>
        </div>
        <aside class="card aside-card reveal"><h3>Need customization?</h3><p class="muted">Share your business type and I can help adapt this format for your workflow.</p><a class="btn" href="{wa('Hi Assistly WS, I want help customizing the ' + name + ' template.')}" target="_blank" rel="noopener">Customize on WhatsApp</a></aside>
      </div>
    </section>
    """
    schema = {
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "name": name,
        "description": desc,
        "url": page_url(current),
        "creator": {"@type": "Organization", "name": SITE_NAME},
        "dateModified": UPDATED,
    }
    render_page(current, f"{name} Template | Assistly WS", f"{desc} Preview a practical {name.lower()} template for Indian small businesses and request customization from Assistly WS.", body, [schema, faq_schema(faqs), breadcrumb_schema(crumbs)])


def blog_page(blog: dict) -> None:
    current = f"blog/{blog['slug']}.html"
    crumbs = [("Home", "index.html"), ("Blog", "blog.html"), (blog["h1"], current)]
    faqs = [
        (f"What is the simple answer about {blog['topic']}?", blog["short"]),
        ("Is this guide enough for final decisions?", "It is a helpful starting point. For legal, tax, compliance, or large budget decisions, review your exact case before acting."),
        ("Can Assistly WS help with implementation?", "Yes. You can open the related service or contact on WhatsApp for founder-led support."),
        ("Why does the guide avoid big claims?", "Assistly WS is a new founder-led agency and uses honest positioning instead of fake client counts, fake awards, or guaranteed results."),
    ]
    toc = [("short-answer", "Short answer"), ("steps", "Step-by-step explanation"), ("examples", "Examples"), ("mistakes", "Common mistakes"), ("related", "Related pages"), ("faq", "FAQs")]
    body = page_hero(current, crumbs, "Guide", blog["h1"], blog["short"])
    body += f"""
    <section class="section">
      <div class="container content-layout">
        <article class="content-main article-body">
          <div class="article-meta"><span class="badge">Published {UPDATED_LABEL}</span><span class="badge orange">Updated {UPDATED_LABEL}</span><span class="badge green">Author: {FOUNDER}, Founder of Assistly WS</span></div>
          <section class="answer-block reveal" id="short-answer"><strong>Short answer:</strong> {esc(blog['short'])}</section>
          <section class="content-block reveal" id="steps"><h2>Step-by-step explanation</h2><p>Start by defining your business goal. For {esc(blog['topic'])}, the right decision depends on your current stage, budget, customer type, documents, and how quickly you need results. Small businesses should avoid copying a large company setup because the cost, team, and process are different.</p><p>Next, list what you already have: business name, contact details, website or social pages, invoices, documents, offers, customer questions, and current challenges. This makes the conversation with any service provider faster and more accurate.</p><p>Finally, choose the smallest useful next step. That could be a website page, GST checklist, SEO audit, ad budget plan, invoice format, or template. Starting small keeps the process clear and reduces waste.</p></section>
          <section class="content-block reveal" id="examples"><h2>Examples</h2><table class="summary-table"><tbody><tr><th>Local service business</th><td>Focus on a clear website, WhatsApp CTA, Google Business Profile, local SEO, and simple follow-up.</td></tr><tr><th>New product seller</th><td>Focus on product photos, pricing, margin, catalog structure, policies, and store readiness.</td></tr><tr><th>Professional service provider</th><td>Focus on trust-building service pages, FAQs, pricing clarity, lead forms, and compliance-ready documents.</td></tr></tbody></table></section>
          <section class="content-block reveal" id="mistakes"><h2>Common mistakes</h2><ul class="list-check"><li>Buying a service before the goal is clear.</li><li>Comparing providers only by lowest price.</li><li>Ignoring mobile users and WhatsApp enquiries.</li><li>Using generic content that does not explain your actual service.</li><li>Assuming marketing, SEO, or ads can guarantee results.</li><li>Not keeping documents, logins, and records organized.</li></ul></section>
          <section class="content-block reveal"><h2>Helpful table</h2><table class="summary-table"><tbody><tr><th>Best first action</th><td>Clarify the offer, audience, budget, and deadline.</td></tr><tr><th>Useful resource</th><td>Use the related tool or template before requesting a quote.</td></tr><tr><th>Support option</th><td>Ask Assistly WS for a founder-led review if you need practical guidance.</td></tr><tr><th>Last updated</th><td>{UPDATED_LABEL}</td></tr></tbody></table></section>
          <section class="content-block reveal" id="related"><h2>Related pages</h2><div class="grid grid-3"><article class="card"><h3>Related service</h3><a class="card-link" href="{rel_link(current, blog['service'])}">Open service <span aria-hidden="true">-&gt;</span></a></article><article class="card"><h3>Related tool</h3><a class="card-link" href="{rel_link(current, blog['tool'])}">Use tool <span aria-hidden="true">-&gt;</span></a></article><article class="card"><h3>Related template</h3><a class="card-link" href="{rel_link(current, blog['template'])}">View template <span aria-hidden="true">-&gt;</span></a></article></div></section>
          <section class="content-block reveal" id="faq"><h2>FAQs</h2>{faq_html(faqs, blog['slug'])}</section>
          <section class="cta-band reveal"><h2>Need help applying this guide?</h2><p class="lead">Send your business type and goal. I will suggest the cleanest next step.</p><a class="btn" href="{wa('Hi Assistly WS, I read your guide on ' + blog['topic'] + '. Please guide me for my business.')}" target="_blank" rel="noopener">Ask on WhatsApp</a></section>
        </article>
        <aside class="card aside-card reveal">
          <h3>Table of contents</h3>
          <ol class="toc">{''.join(f'<li><a href="#{anchor}">{label}</a></li>' for anchor, label in toc)}</ol>
        </aside>
      </div>
    </section>
    """
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": blog["h1"],
        "description": blog["meta"],
        "author": {"@type": "Person", "name": FOUNDER},
        "publisher": {"@type": "Organization", "name": SITE_NAME},
        "datePublished": UPDATED,
        "dateModified": UPDATED,
        "mainEntityOfPage": page_url(current),
    }
    render_page(current, blog["title"], blog["meta"], body, [schema, faq_schema(faqs), breadcrumb_schema(crumbs)], og_type="article")


def legal_page(item: tuple[str, str, str, str]) -> None:
    slug, title, h1, intro = item
    current = f"legal/{slug}.html"
    crumbs = [("Home", "index.html"), ("Legal", "legal/privacy-policy.html"), (h1, current)]
    body = page_hero(current, crumbs, "Legal", h1, intro)
    body += f"""
    <section class="section">
      <div class="container narrow article-body">
        <div class="answer-block reveal"><strong>Short answer:</strong> {esc(intro)} This page is written for a static website with WhatsApp, email, and optional future form or analytics integrations.</div>
        <section class="content-block reveal"><h2>Scope</h2><p>Assistly WS is a new founder-led agency. The website provides service information, free tools, templates, blog guides, and contact options. It does not use a backend or database in this static version.</p></section>
        <section class="content-block reveal"><h2>Important points</h2><ul class="list-check"><li>WhatsApp and email links open third-party communication tools.</li><li>Free tools provide estimates, previews, or drafts for planning only.</li><li>Final tax, legal, accounting, and compliance decisions should be verified for your situation.</li><li>Service scope, pricing, timeline, revisions, and deliverables should be agreed before work begins.</li><li>No fake testimonials, fake awards, fake client counts, or guaranteed results are claimed.</li></ul></section>
        <section class="content-block reveal"><h2>Contact</h2><p>For questions about this page, contact <a href="mailto:{EMAIL}">{EMAIL}</a> or WhatsApp <a href="tel:+918059134416">{PHONE}</a>.</p></section>
      </div>
    </section>
    """
    render_page(current, title, intro, body, [organization_schema(), breadcrumb_schema(crumbs)])


def write_static_files(paths: list[str]) -> None:
    logo = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" role="img" aria-labelledby="title desc">
  <title id="title">Assistly WS logo card</title>
  <desc id="desc">Assistly WS brand card with navy background and orange accent.</desc>
  <rect width="1200" height="630" fill="#0F172A"/>
  <rect x="90" y="90" width="1020" height="450" rx="24" fill="#FFFFFF"/>
  <rect x="130" y="140" width="120" height="120" rx="16" fill="#F97316"/>
  <text x="190" y="216" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="42" font-weight="800" fill="#FFFFFF">AW</text>
  <text x="290" y="205" font-family="Inter, Arial, sans-serif" font-size="70" font-weight="850" fill="#0F172A">Assistly WS</text>
  <text x="294" y="270" font-family="Inter, Arial, sans-serif" font-size="34" font-weight="600" fill="#64748B">Your Growth, Our Mission</text>
  <text x="294" y="350" font-family="Inter, Arial, sans-serif" font-size="28" font-weight="600" fill="#1E293B">Founder-led website, marketing, GST and business support for India.</text>
</svg>
"""
    (ROOT / "assets/logo/assistly-ws-logo.svg").write_text(logo, encoding="utf-8")

    sitemap_urls = []
    for path in paths:
        loc = page_url(path)
        sitemap_urls.append(f"  <url><loc>{loc}</loc><lastmod>{UPDATED}</lastmod><changefreq>weekly</changefreq><priority>{'1.0' if path == 'index.html' else '0.8'}</priority></url>")
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(sitemap_urls) + "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    robots = "User-agent: *\nAllow: /\n\nSitemap: https://assistlyws.in/sitemap.xml\n"
    (ROOT / "robots.txt").write_text(robots, encoding="utf-8")
    readme = """# Assistly WS Static Website

Assistly WS is a complete static, multipage website for a new founder-led service agency serving Indian small businesses. It uses clean HTML, CSS, and vanilla JavaScript only. No backend or database is required.

## Folder structure

- `index.html` and core pages live at the project root.
- `services/` contains individual service pages.
- `tools/` contains free calculators and generators.
- `templates/` contains template landing pages.
- `blog/` contains SEO/AIO-friendly guide pages.
- `legal/` contains policy pages.
- `css/style.css` contains the shared design system.
- `js/main.js` contains navigation, animation, FAQ, form, and tool logic.
- `assets/logo/` contains the SVG brand card.
- `sitemap.xml` and `robots.txt` are ready for deployment.

## Run locally

From this folder:

```bash
python -m http.server 8080
```

Then open `http://localhost:8080`.

## Deploy

### GitHub Pages

1. Push this folder to a GitHub repository.
2. In repository settings, enable Pages from the main branch.
3. Add your custom domain when ready.

### Netlify or Cloudflare Pages

Upload the folder or connect the repository. No build command is required because the site is already static.

## Edit contact details

Update the constants in `build_site.py`, then run:

```bash
python build_site.py
```

For direct edits without regenerating, search for:

- `teamassistly@gmail.com`
- `+91 8059134416`
- `https://wa.me/918059134416`
- `Sonipat / Delhi NCR, Haryana`

## Add a new service page

Add a new object to the `SERVICES` list in `build_site.py`, including title, meta description, quick answer, pricing, timeline, FAQs, and related links. Then run `python build_site.py`.

## Add a new blog page

Add a new object to the `BLOGS` list in `build_site.py` with title, meta, H1, short answer, topic, and related page links. Then run `python build_site.py`.

## SEO checklist

- One H1 per page.
- Unique title and meta description on every page.
- Canonical tags included.
- Open Graph and Twitter card tags included.
- Breadcrumb HTML and JSON-LD included.
- FAQ schema added only where visible FAQs exist.
- Sitemap and robots file included.
- Internal links connect services, tools, templates, and blog pages.

## Future Laravel migration notes

The repeated header, footer, cards, FAQ blocks, breadcrumbs, schema, and CTA sections can be moved into Blade components. The page data lists in `build_site.py` can become config arrays, database seeders, or simple CMS records later.
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")


def main() -> None:
    paths: list[str] = []
    homepage()
    paths.append("index.html")
    listing_pages()
    paths.extend(["services.html", "free-tools.html", "templates.html", "blog.html"])
    about_contact_pricing_demo()
    paths.extend(["about.html", "contact.html", "pricing.html", "demo-work.html"])
    for service in SERVICES:
        service_page(service)
        paths.append(f"services/{service['slug']}.html")
    for tool in TOOLS:
        tool_page(tool)
        paths.append(f"tools/{tool['slug']}.html")
    for template in TEMPLATES:
        template_page(template)
        paths.append(f"templates/{template[0]}.html")
    for blog in BLOGS:
        blog_page(blog)
        paths.append(f"blog/{blog['slug']}.html")
    for item in LEGAL:
        legal_page(item)
        paths.append(f"legal/{item[0]}.html")
    write_static_files(paths)
    print(f"Generated {len(paths)} HTML pages.")


if __name__ == "__main__":
    main()
