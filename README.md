# Dr. Arafath Dental Clinic — Website Demo

> Official website demo for **Dr. Arafath Dental Clinic**, Mohammadpur, Dhaka.
> Built mobile-first according to `PROJECT_PLAN.md`.

- **Demo Subdomain:** [dr-arafat.d4f.me](https://dr-arafat.d4f.me/)
- **Clinic Address:** 75/C, 4th Floor, Asad Avenue, Main Road, beside Meena Bazar, Dutch-Bangla Bank Building, Mohammadpur, Dhaka 1207
- **WhatsApp Coordinator:** [+880 1684-885861](https://wa.me/8801684885861)
- **Deployment Platform:** Cloudflare Pages / Cloudflare Workers Static Assets

---

## Features

- **Mobile-First Luxury Design:** Clean, elite corporate dental aesthetic using deep navy, warm ivory, and restrained muted gold accents.
- **Custom Brand Monogram:** Temporary vector A + tooth emblem for small/large viewports and favicon.
- **Video-Ready Hero:** Configured for short looping clinic background video with static poster fallback.
- **6 Confirmed Provisional Services:**
  1. Oral Check-up & Consultation
  2. Scaling (Deep Cleaning)
  3. Tooth Polishing
  4. Root Canal Treatment (RCT)
  5. Aesthetic Dental Fillings
  6. Crown & Cap Restorations
- **WhatsApp Appointment Request Flow:**
  - Client-side validation adhering to modern web guidance (`:user-invalid` / `:user-valid` and ARIA sync).
  - Encodes formatted WhatsApp inquiry directly to `+880 1684-885861`.
  - Accessible success modal confirming dispatch.
  - Transparently marked as an appointment request requiring clinic confirmation.
- **Interactive Facilities & Video Gallery:** Modal lightboxes for operatory tour, autoclave sterilization bay, and consultation lounge.
- **Interactive Pre-Launch Checklist:** Accessible modal dialog tracking the 10 verification items from `PROJECT_PLAN.md` with localStorage persistence.
- **Sticky Mobile Booking Bar:** Dispatches quick WhatsApp chat or scrolls to appointment form without covering UI elements.
- **Cloudflare Optimizations:** Pre-configured `_headers`, `robots.txt`, `sitemap.xml`, and `wrangler.toml`.

---

## Quickstart

### Development
```bash
npm install
npm run dev
```

### Production Build
```bash
npm run build
npm run preview
```

### Deployment to Cloudflare Pages
See [DEPLOYMENT.md](DEPLOYMENT.md) for step-by-step instructions for connecting GitHub and pointing the custom domain `dr-arafat.d4f.me`.
