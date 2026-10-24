# Dr. Arafat Dental — Website Project Plan

> Working brief for the demo website. Build mobile-first and use only confirmed clinic facts. Provisional items must be verified before launch.

## 1. Project goals
- Create an elegant, elite corporate dental website that looks excellent on phones first and scales cleanly to desktop.
- Establish trust through the dentist's real photography, verified credentials, clinic imagery, and clear contact details.
- Let visitors submit an appointment request through WhatsApp.
- Prepare a hero area for a short, supplied clinic video as a muted looping background.
- Keep the demo fast, accessible, and easy to update when remaining assets arrive.

## 2. Brand direction
- Working brand: Dr. Arafath Dental
- Dentist name from supplied poster: Dr. Arafath Badrul Munna (verify spelling and details before launch).
- Draft tagline: “Confident Smiles. Thoughtful Care.”
- Palette: deep navy, warm ivory/off-white, restrained muted gold, and soft neutral grey.
- Logo concept: simple A integrated with a minimal tooth outline; gold-on-navy and navy-on-light variants, legible at small sizes.
- Use refined display typography for headings and readable sans-serif body text.
- Keep layouts spacious and clean. Gold is an accent, not a large shiny surface.

## 3. Confirmed details and supplied references
- Address: 75/C, 4th Floor, Asad Avenue, Main Road, beside Meena Bazar, Dutch-Bangla Bank Building, Dhaka 1207.
- WhatsApp: +880 1684-885861. WhatsApp URL digits: 8801684885861.
- Facebook share link: https://www.facebook.com/share/1DQSRCkBa4/?mibextid=wwXIfr
- Supplied images: dentist portrait in dark attire, dentist portrait in white coat, clinical treatment photo, and dental promotional poster.
- Poster is a visual reference for navy/gold styling. It lists Oral Checkup, Scaling, Root Canal, Crown/Cap, Polishing, and Fillings.
- Poster also shows a 35% offer. Do not publish it unless the clinic confirms it is currently valid.
- Facebook share link could not be opened here. Treat it as a reference; request direct public video-post URLs or supplied video files.

## 4. Mobile-first experience
- Design for narrow phone screens first, then expand for tablet and desktop.
- Compact header with logo, accessible menu, and clear booking CTA.
- Dentist, core message, and booking action visible immediately.
- Optional sticky bottom Book Appointment button that never covers content or controls.
- Large touch-friendly buttons and form fields.
- Stack service cards on phones; use columns only when there is room.
- Prevent clipped text, crowded controls, and horizontal scrolling.
- Build a polished desktop navigation and balanced wide-screen layout.

## 5. Page structure
### Header
Logo, Home, About, Services, Gallery, Contact, and Book Appointment. Mobile menu must be keyboard-accessible.

### Hero
Use the supplied doctor/clinic video when available. Add a navy translucent overlay, concise copy, Book Appointment and Explore Services actions. Use a static poster fallback. Tune mobile and desktop crops separately.

### Credentials strip
Show only credentials verified by the dentist. Until then use editable placeholders; do not invent experience, qualifications, awards, or certification.

### About the dentist
Use the white-coat portrait or approved professional photo, a concise biography, and verified education/training. Add a booking CTA.

### Services
Provisional cards based on the supplied poster: Oral check-up, Scaling, Polishing, Root canal treatment, Fillings, Crown/cap. Confirm list and descriptions with the dentist. Do not promise outcomes or make unsupported clinical claims.

### Clinic and photo gallery
Use approved clinic, equipment, and treatment photos. Compress and crop carefully. Obtain permission before publishing identifiable patients.

### Video gallery
Use selected public Facebook posts or supplied video files. Prefer thumbnails and explicit play. Lazy-load embeds and provide Watch on Facebook fallback if embedding fails. Never autoplay sound.

### Appointment request
Fields: patient name, phone/WhatsApp, requested service, preferred date, preferred time, optional message. Validate required fields and open a prepared WhatsApp message to 8801684885861. This is a request, not a confirmed booking. Sample time choices must not imply real availability.

### Contact and location
Show supplied address and WhatsApp. Add phone link only if a phone number is provided. Add opening hours when confirmed. Add Open in Google Maps once a verified map pin/link is supplied; do not guess coordinates.

### Footer
Logo, clinic name, address, WhatsApp, Facebook link, and section shortcuts.

## 6. Hero video requirements
- Use a short compressed MP4 or WebM background clip.
- Muted, autoplay, loop, plays-inline; never autoplay with sound.
- Provide poster image and graceful fallback.
- Do not load multiple videos on initial page load; lazy-load gallery videos.
- Keep text contrast clear on every frame and test separate mobile/desktop crops.
- Avoid flashing, fast cuts, or distracting movement behind text.
- Respect reduced-motion preferences and data-saving behavior where practical.

## 7. Motion and interaction
Use restrained hero text entrance, subtle section reveals, small card/button transitions, and modest image reveals. Respect prefers-reduced-motion. Avoid scroll hijacking, heavy parallax, perpetual motion, and animation that delays content.

## 8. Booking flow
Demo flow: visitor enters details and preferred service/date/time; form validates; site creates a URL-encoded WhatsApp message; WhatsApp opens to the clinic number; clinic confirms availability separately. Live availability, booking storage, reminders, and staff management require a later calendar/backend integration.

## 9. Performance, accessibility, and search basics
- Optimize supplied photos and use modern image formats where supported.
- Compress hero video and provide poster fallback.
- Lazy-load below-fold images, videos, and embeds.
- Use semantic HTML, clear heading order, descriptive alt text, visible keyboard focus, accessible form labels, and sufficient contrast.
- Ensure keyboard and touch operation.
- Add page title, meta description, favicon, and social preview image.
- Keep content and booking usable if media fails.
- Test phone widths, tablet, and desktop; check layout, links, form errors, and loading behavior.

## 10. Cloudflare hosting and demo URL
- Deploy the demo as a lightweight static site through Cloudflare Pages or Cloudflare Workers static assets, choosing the simplest option supported by the repository/build output.
- Use the custom subdomain arafat.dforet.me as the shareable demo address.
- Connect the subdomain to the Cloudflare deployment and configure DNS/SSL through the user's existing Cloudflare account.
- Keep deployment configuration and build instructions in the repository; do not put secrets or account tokens in Git.
- Verify the deployed site loads over HTTPS on mobile and desktop before sharing.
- Keep the site as a demo until the dentist approves the content and supplied assets.

## 11. Demo versus launch
### Demo
Temporary A/tooth logo, supplied photos, provisional editable services, video-ready hero with poster fallback, WhatsApp request flow, supplied address, and placeholders for missing details.

### Before launch
Verify brand name/logo, dentist name and credentials, services and descriptions, clinic hours, actual booking rules, Maps pin, Facebook page and direct video links or approved files, permissions for identifiable patient media, any current offer, and preferred languages.

## 12. Remaining inputs checklist
- [ ] Confirm dentist name spelling, credentials, and biography
- [ ] Confirm final services and descriptions
- [ ] Send clinic hours
- [ ] Send Google Maps pin/link
- [ ] Send Facebook page and direct video post links
- [ ] Send hero video(s), if available
- [ ] Confirm photo/video permissions
- [ ] Confirm whether Bangla/English toggle is needed
- [ ] Confirm whether the 35% poster offer is active
- [ ] Confirm Cloudflare account access/DNS setup when ready to deploy

## 13. Gemini build prompt
Build a complete responsive website demo from this project plan. Start with the mobile layout and make the first screen feel premium, trustworthy, and visually striking without looking crowded. Use deep navy, warm ivory, and restrained muted gold. Create a simple temporary A/tooth logo. Use supplied images when available; otherwise use clearly replaceable placeholders.

Implement the page sections, provisional service cards, video-ready hero with muted looping video support and poster fallback, gallery, contact/location block, and validated WhatsApp appointment-request form as described above. Use the supplied WhatsApp number and address exactly. Treat unverified credentials, hours, availability, service details, and offers as editable placeholders. Do not invent facts or publish the 35% offer. The booking flow must say request, open a prepared WhatsApp message, and never claim confirmation.

Make animations subtle and respect reduced motion. Optimize images/video, lazy-load below-fold media, use accessible semantic markup, and check mobile, tablet, and desktop layouts. Prepare the project for Cloudflare Pages or Workers static hosting, whichever best fits the generated app. Document build/deploy steps and configure the demo for the custom subdomain arafat.dforet.me; do not commit secrets or claim deployment until it is actually verified. Return a working demo and a concise list of inputs still needed before launch.