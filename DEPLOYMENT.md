# Deployment Guide — Dr. Arafath Dental Clinic Demo

This website is built with a lightweight, ultra-fast static architecture using **Vite**. The production output is located in the `dist/` directory and is optimized for zero-overhead hosting on **Cloudflare Pages** or **Cloudflare Workers Static Assets**.

- **Target Demo Subdomain:** `dr-arafat.d4f.me`
- **Root Apex Domain:** `d4f.me` (Managed in Cloudflare)
- **Repository:** `rajonu/dr-arafat-dental` (Branch: `main`)

---

## Method 1: Cloudflare Pages Git Integration (Recommended)

Connecting Cloudflare Pages directly to GitHub enables automatic builds on every `git push`.

### Step 1: Connect GitHub Repository
1. Log in to the [Cloudflare Dashboard](https://dash.cloudflare.com/).
2. In the left sidebar, navigate to **Compute (Workers) > Workers & Pages**.
3. Click **Create** > select the **Pages** tab > click **Connect to Git**.
4. Select your GitHub account (`rajonu`) and choose the repository `dr-arafat-dental`.
5. Click **Begin setup**.

### Step 2: Configure Build Settings
Fill in the build configuration:
- **Project name:** `dr-arafat-dental`
- **Production branch:** `main`
- **Framework preset:** `Vite` (or `None`)
- **Build command:** `npm run build`
- **Build output directory:** `dist`
- **Root directory:** *(Leave blank)*

Click **Save and Deploy**. Cloudflare Pages will fetch the code, run `npm run build`, and deploy the initial preview to `https://dr-arafat-dental.pages.dev` in less than a minute.

---

## Method 2: Connecting the Custom Domain (`dr-arafat.d4f.me`)

Once your Cloudflare Pages project is deployed:

1. In the Cloudflare Pages dashboard for `dr-arafat-dental`, click the **Custom domains** tab.
2. Click **Set up a custom domain**.
3. Enter the exact domain:
   ```text
   dr-arafat.d4f.me
   ```
4. Click **Continue**.
5. **DNS & SSL Verification:**
   - Since `d4f.me` is already hosted on your Cloudflare account, Cloudflare will automatically provision the DNS CNAME record pointing `dr-arafat` to `dr-arafat-dental.pages.dev` with Cloudflare Proxy (Orange Cloud) enabled.
   - An edge SSL/TLS certificate will be generated automatically.
6. Click **Activate domain**.
7. Within 1–3 minutes, your site will be live securely at:
   👉 **`https://dr-arafat.d4f.me/`**

---

## Method 3: Direct CLI Deployment via Wrangler

If you prefer deploying directly from your terminal using Cloudflare's Wrangler CLI:

### 1. Build Production Assets
```bash
npm run build
```

### 2. Login to Cloudflare via Wrangler (one-time)
```bash
npx wrangler login
```

### 3. Deploy `dist/` to Cloudflare Pages
```bash
npx wrangler pages deploy dist --project-name dr-arafat-dental
```

### 4. Link Custom Domain via CLI
```bash
npx wrangler pages domain create dr-arafat-dental dr-arafat.d4f.me
```

---

## Included Cloudflare Static Optimization Files

- **`public/_headers` (Copied to `dist/_headers`):**
  - Configures security headers: `X-Frame-Options`, `X-Content-Type-Options: nosniff`, `Referrer-Policy`, and modern permission policies.
  - Sets 1-year immutable caching for static assets in `/assets/*`.
- **`public/robots.txt` & `public/sitemap.xml`:**
  - Configured with the canonical domain `https://dr-arafat.d4f.me/`.
- **`wrangler.toml`:**
  - Configured with `[assets] directory = "./dist"` for Workers/Pages compatibility.

---

## Pre-Launch Verification Checklist

Before publishing this site as the official clinic website (transitioning from Demo to Launch), verify these items with Dr. Arafath:

- [ ] **Dentist Name & Degree:** Verify spelling (`Dr. Arafath Badrul Munna`), BM&DC registration number, and bio.
- [ ] **Confirmed Services:** Confirm the 6 provisional services and whether any specialized procedures should be added or removed.
- [ ] **Clinic Hours:** Confirm operational hours (currently provisional: Sat–Thu 4:00 PM – 9:00 PM).
- [ ] **Google Maps Pin:** Send the verified Google Maps pin link for 75/C Asad Avenue.
- [ ] **Facebook Links & Videos:** Supply public video post URLs or video files to embed in the video gallery.
- [ ] **Clinic Photography:** Replace placeholder SVGs in `/public/assets/images/` with real high-resolution photographs of Dr. Arafath and the operatory.
- [ ] **Promotional Offers:** Confirm whether the 35% poster discount is currently active.
- [ ] **Language Toggle:** Confirm whether an English/Bangla dual-language switcher is desired.
