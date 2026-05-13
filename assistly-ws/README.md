# Assistly WS Static Website

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
- `_unused-python/` contains an archived generator backup only. It is not part of the active website.

## Run locally

Open `index.html` directly in a browser, or serve the folder with any static file server. No build command, Python runtime, Node backend, PHP, or database is required.

## Deploy

### GitHub Pages

1. Push this folder to a GitHub repository.
2. In repository settings, enable Pages from the main branch.
3. Add your custom domain when ready.

### Netlify or Cloudflare Pages

Upload the folder or connect the repository. No build command is required because the site is already static.

## Edit contact details

Search the static files for:

- `teamassistly@gmail.com`
- `+91 8059134416`
- `https://wa.me/918059134416`
- `Sonipat / Delhi NCR, Haryana`

## Add a new service page

Duplicate an existing file in `services/`, update the content, metadata, breadcrumbs, related links, and add the new URL to the relevant navigation/footer links and `sitemap.xml`.

## Add a new blog page

Duplicate an existing file in `blog/`, update the content, metadata, breadcrumbs, related links, and add the new URL to `blog.html` and `sitemap.xml`.

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

The repeated header, footer, cards, FAQ blocks, breadcrumbs, schema, and CTA sections can be moved into Blade components later. For now, the GitHub Pages version is fully static and browser-run.
