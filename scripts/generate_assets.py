"""
Asset generator for Dr. Arafath Dental Clinic Demo.
Creates crisp, luxury SVGs for logo, favicon, service icons, and placeholder imagery.
"""
import os

os.makedirs("public/assets/images", exist_ok=True)
os.makedirs("public/assets/icons", exist_ok=True)
os.makedirs("public/assets/video", exist_ok=True)

# 1. Favicon (Tooth + A Monogram)
favicon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#dfb76c" />
      <stop offset="50%" stop-color="#c5a059" />
      <stop offset="100%" stop-color="#9a7530" />
    </linearGradient>
    <linearGradient id="navyBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e223d" />
      <stop offset="100%" stop-color="#081321" />
    </linearGradient>
  </defs>
  <rect width="64" height="64" rx="16" fill="url(#navyBg)" />
  <rect x="2" y="2" width="60" height="60" rx="14" fill="none" stroke="url(#goldGrad)" stroke-width="1.5" stroke-opacity="0.4" />
  
  <!-- A + Tooth Monogram -->
  <g transform="translate(14, 10)">
    <!-- Outer 'A' Arch / Tooth Crown -->
    <path d="M 18,2 C 22,2 27,4 30,8 C 34,13 35,21 33,28 C 31,34 29,39 28,44 C 27,46 25,46 24,44 C 23,40 21,34 20,30 C 19,27 17,27 16,30 C 15,34 13,40 12,44 C 11,46 9,46 8,44 C 7,39 5,34 3,28 C 1,21 2,13 6,8 C 9,4 14,2 18,2 Z" 
          fill="none" stroke="url(#goldGrad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
    <!-- Apex 'A' bridge & inner tooth crevice -->
    <path d="M 18,12 L 18,20" stroke="url(#goldGrad)" stroke-width="2.5" stroke-linecap="round" />
    <path d="M 11,24 L 25,24" stroke="url(#goldGrad)" stroke-width="2.5" stroke-linecap="round" />
    <!-- Center sparkle -->
    <circle cx="18" cy="12" r="1.5" fill="#ffffff" />
  </g>
</svg>'''

with open("public/favicon.svg", "w") as f:
    f.write(favicon_svg)

# 2. Main Logo (Horizontal for Dark Navy Header)
logo_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 64" width="320" height="64">
  <defs>
    <linearGradient id="logoGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ebd08e" />
      <stop offset="50%" stop-color="#c5a059" />
      <stop offset="100%" stop-color="#a07c33" />
    </linearGradient>
    <linearGradient id="logoShield" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#142c4c" />
      <stop offset="100%" stop-color="#0b1a2e" />
    </linearGradient>
  </defs>

  <!-- Emblem Badge -->
  <g transform="translate(4, 4)">
    <rect width="56" height="56" rx="14" fill="url(#logoShield)" stroke="url(#logoGold)" stroke-width="1.2" stroke-opacity="0.6"/>
    <g transform="translate(10, 6) scale(0.98)">
      <!-- Tooth + A Contour -->
      <path d="M 18,3 C 23,3 28,5 31,9 C 35,14 36,22 34,29 C 32,35 30,40 29,45 C 28,47 26,47 25,45 C 24,41 22,35 21,31 C 20,28 17,28 16,31 C 15,35 13,41 12,45 C 11,47 9,47 8,45 C 7,40 5,35 3,29 C 1,22 2,14 6,9 C 9,5 14,3 18,3 Z" 
            fill="none" stroke="url(#logoGold)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" />
      <!-- A Crossbar -->
      <path d="M 10,24 L 26,24" stroke="url(#logoGold)" stroke-width="2.4" stroke-linecap="round" />
      <!-- Inner apex detail -->
      <path d="M 18,10 L 18,17" stroke="url(#logoGold)" stroke-width="2" stroke-linecap="round" />
      <circle cx="18" cy="10" r="1.2" fill="#fff" />
    </g>
  </g>

  <!-- Brand Typography -->
  <g transform="translate(72, 16)">
    <!-- Primary Title -->
    <text x="0" y="18" font-family="'Cinzel', 'Playfair Display', 'Times New Roman', Georgia, serif" font-size="20" font-weight="700" letter-spacing="1.5" fill="#fcfaf6">
      DR. ARAFATH
    </text>
    <!-- Subtitle -->
    <text x="0" y="34" font-family="'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif" font-size="9.5" font-weight="600" letter-spacing="3.2" fill="url(#logoGold)">
      DENTAL CLINIC &bull; DHAKA
    </text>
  </g>
</svg>'''

with open("public/logo.svg", "w") as f:
    f.write(logo_svg)

# 3. Light Logo (For Ivory/Light backgrounds)
logo_light_svg = logo_svg.replace('fill="#fcfaf6"', 'fill="#0b192c"').replace('url(#logoShield)', '#f4f5f7').replace('fill="#fff"', '#c5a059')
with open("public/logo-light.svg", "w") as f:
    f.write(logo_light_svg)

# 4. Service Icons
service_icons = {
    "oral-checkup.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="21" cy="21" r="13" stroke="#c5a059" stroke-width="2.5" />
      <path d="M 30.5 30.5 L 43 43" stroke="#c5a059" stroke-width="3" />
      <!-- Inner tooth silhouette -->
      <path d="M 17 15 C 19 13 23 13 25 15 C 27 17 27 21 26 24 C 25 26 23 27 22 28 C 21 28 20 28 19 26 C 18 24 17 23 16 21 C 15 18 15 16 17 15 Z" fill="#c5a059" fill-opacity="0.25" stroke="#c5a059" stroke-width="1.5" />
      <circle cx="20" cy="18" r="1" fill="#fff" />
    </svg>''',

    "scaling.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <!-- Tooth crown -->
      <path d="M 14 18 C 14 12 18 8 24 8 C 30 8 34 12 34 18 C 34 26 31 34 29 40 C 28 42 26 42 25 40 C 24 37 23 32 21 32 C 19 32 18 37 17 40 C 16 42 14 42 13 40 C 11 34 8 26 8 18" stroke="#c5a059" stroke-width="2" />
      <!-- Ultrasonic scaler tool -->
      <path d="M 38 6 L 27 17" stroke="#38bdf8" stroke-width="2.5" />
      <path d="M 27 17 L 23 20" stroke="#38bdf8" stroke-width="2" />
      <!-- Water spray / sonic waves -->
      <path d="M 29 13 C 31 15 33 14 34 12" stroke="#bae6fd" stroke-width="1.5" />
      <path d="M 23 16 L 20 14" stroke="#bae6fd" stroke-width="1.5" />
      <circle cx="24" cy="20" r="1.5" fill="#38bdf8" />
    </svg>''',

    "polishing.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <!-- Tooth base -->
      <path d="M 12 20 C 12 14 16 10 24 10 C 32 10 36 14 36 20 C 36 28 32 36 30 41 C 29 43 27 43 26 41 C 25 38 23 33 21 33 C 19 33 17 38 16 41 C 15 43 13 43 12 41 C 10 36 6 28 6 20" stroke="#c5a059" stroke-width="2" />
      <!-- Prophy polishing head -->
      <path d="M 32 6 L 42 16" stroke="#c5a059" stroke-width="2" />
      <ellipse cx="28" cy="18" rx="4" ry="2" transform="rotate(-45 28 18)" fill="#c5a059" fill-opacity="0.3" stroke="#c5a059" stroke-width="2" />
      <!-- Starburst shines -->
      <path d="M 18 16 L 18 20 M 16 18 L 20 18" stroke="#ffffff" stroke-width="2" />
      <path d="M 26 26 L 26 30 M 24 28 L 28 28" stroke="#dfb76c" stroke-width="1.5" />
    </svg>''',

    "root-canal.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <!-- Tooth outline with split roots -->
      <path d="M 12 18 C 12 11 16 7 24 7 C 32 7 36 11 36 18 C 36 26 33 34 31 41 C 30 43 28 43 27 41 C 26 36 24 30 22 30 C 20 30 18 36 17 41 C 16 43 14 43 13 41 C 11 34 8 26 8 18" stroke="#c5a059" stroke-width="2" />
      <!-- Canal pathways & precision gutta-percha filling line -->
      <path d="M 24 14 L 24 24" stroke="#f43f5e" stroke-width="2" />
      <path d="M 24 24 C 23 27 20 33 19 38" stroke="#f43f5e" stroke-width="2" stroke-linecap="round" />
      <path d="M 24 24 C 25 27 28 33 29 38" stroke="#f43f5e" stroke-width="2" stroke-linecap="round" />
      <circle cx="24" cy="14" r="2.5" fill="#f43f5e" fill-opacity="0.3" stroke="#f43f5e" stroke-width="1.5" />
    </svg>''',

    "fillings.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <!-- Tooth -->
      <path d="M 12 18 C 12 11 16 8 24 8 C 32 8 36 11 36 18 C 36 26 33 34 31 41 C 30 43 28 43 27 41 C 26 37 24 32 22 32 C 20 32 18 37 17 41 C 16 43 14 43 13 41 C 11 34 8 26 8 18" stroke="#c5a059" stroke-width="2" />
      <!-- Occlusal composite restoration inlay -->
      <path d="M 18 14 C 20 12 28 12 30 14 C 31 16 30 20 28 22 C 25 23 23 23 20 22 C 17 20 17 16 18 14 Z" fill="#38bdf8" fill-opacity="0.35" stroke="#38bdf8" stroke-width="2" />
      <path d="M 20 18 L 28 18" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2 2" />
    </svg>''',

    "crown-cap.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <!-- Tooth lower roots -->
      <path d="M 13 26 C 13 32 14 36 15 41 C 16 43 18 43 19 41 C 20 37 22 32 24 32 C 26 32 28 37 29 41 C 30 43 32 43 33 41 C 34 36 35 32 35 26" stroke="#c5a059" stroke-width="2" />
      <!-- Golden Dental Crown sitting gracefully on tooth -->
      <path d="M 10 24 L 14 11 L 20 17 L 24 9 L 28 17 L 34 11 L 38 24 Z" fill="#c5a059" fill-opacity="0.35" stroke="#c5a059" stroke-width="2.5" stroke-linejoin="round" />
      <!-- Crown jewels / shine gems -->
      <circle cx="14" cy="11" r="1.5" fill="#dfb76c" />
      <circle cx="24" cy="9" r="1.5" fill="#ffffff" />
      <circle cx="34" cy="11" r="1.5" fill="#dfb76c" />
    </svg>'''
}

for filename, content in service_icons.items():
    with open(f"public/assets/icons/{filename}", "w") as f:
        f.write(content)

# 5. Doctor White Coat Portrait (Placeholder SVG)
doc_white_coat = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 1000" width="800" height="1000">
  <defs>
    <linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a192f" />
      <stop offset="50%" stop-color="#112240" />
      <stop offset="100%" stop-color="#071321" />
    </linearGradient>
    <linearGradient id="goldG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ebd08e" />
      <stop offset="50%" stop-color="#c5a059" />
      <stop offset="100%" stop-color="#8c6823" />
    </linearGradient>
    <linearGradient id="coatG" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="100%" stop-color="#e2e8f0" />
    </linearGradient>
    <radialGradient id="halo" cx="50%" cy="35%" r="45%">
      <stop offset="0%" stop-color="#c5a059" stop-opacity="0.25" />
      <stop offset="100%" stop-color="#0a192f" stop-opacity="0" />
    </radialGradient>
  </defs>

  <rect width="800" height="1000" fill="url(#bgG)" />
  <circle cx="400" cy="360" r="320" fill="url(#halo)" />

  <!-- Subtle luxury border -->
  <rect x="24" y="24" width="752" height="952" rx="20" fill="none" stroke="url(#goldG)" stroke-width="2" stroke-opacity="0.4" />
  <rect x="36" y="36" width="728" height="928" rx="14" fill="none" stroke="url(#goldG)" stroke-width="1" stroke-opacity="0.2" />

  <!-- Dentist Silhouette Illustration -->
  <g transform="translate(0, 40)">
    <!-- Shoulders & Clinical White Coat -->
    <path d="M 180,820 C 180,680 240,610 320,580 L 400,680 L 480,580 C 560,610 620,680 620,820 L 620,960 L 180,960 Z" fill="url(#coatG)" />
    <!-- Coat Lapels -->
    <path d="M 320,580 L 400,750 L 370,960 L 320,960 Z" fill="#cbd5e1" opacity="0.6"/>
    <path d="M 480,580 L 400,750 L 430,960 L 480,960 Z" fill="#94a3b8" opacity="0.4"/>
    
    <!-- Dark Inner Shirt & Gold Tie / Collar -->
    <polygon points="360,540 440,540 400,630" fill="#0b192c" />
    <polygon points="392,570 408,570 404,650 396,650" fill="url(#goldG)" />
    
    <!-- Neck -->
    <rect x="365" y="470" width="70" height="80" rx="10" fill="#d4af88" />
    <!-- Head / Face Silhouette -->
    <ellipse cx="400" cy="380" rx="90" ry="110" fill="#e2be9b" />
    <!-- Professional Hair Style -->
    <path d="M 305,370 C 300,280 340,240 400,240 C 460,240 500,280 495,370 C 480,310 440,290 400,290 C 350,290 320,320 305,370 Z" fill="#1e293b" />
    
    <!-- Doctor Glasses / Loupes (Restrained elegance) -->
    <rect x="335" y="360" width="50" height="28" rx="8" fill="none" stroke="url(#goldG)" stroke-width="2.5" />
    <rect x="415" y="360" width="50" height="28" rx="8" fill="none" stroke="url(#goldG)" stroke-width="2.5" />
    <line x1="385" y1="374" x2="415" y2="374" stroke="url(#goldG)" stroke-width="2.5" />

    <!-- Stethoscope -->
    <path d="M 310,630 C 290,700 320,830 380,830 C 400,830 405,800 405,790" fill="none" stroke="#64748b" stroke-width="5" stroke-linecap="round"/>
    <circle cx="405" cy="790" r="14" fill="#94a3b8" stroke="url(#goldG)" stroke-width="2.5" />
    <circle cx="405" cy="790" r="7" fill="#0b192c" />
  </g>

  <!-- Elegant Metadata Card Over Portrait -->
  <g transform="translate(60, 780)">
    <rect width="680" height="150" rx="16" fill="#081423" fill-opacity="0.94" stroke="url(#goldG)" stroke-width="1.5" />
    
    <text x="340" y="45" font-family="'Cinzel', 'Playfair Display', Georgia, serif" font-size="24" font-weight="700" letter-spacing="1.5" fill="#fcfaf6" text-anchor="middle">
      DR. ARAFATH BADRUL MUNNA
    </text>
    
    <text x="340" y="75" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="600" letter-spacing="2.5" fill="url(#goldG)" text-anchor="middle">
      DENTAL SURGEON &bull; SPECIALIZED CARE
    </text>

    <line x1="160" y1="92" x2="520" y2="92" stroke="url(#goldG)" stroke-width="1" stroke-opacity="0.4" />

    <text x="340" y="118" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">
      [Supplied White-Coat Portrait Slot &bull; Ready for final clinic photograph]
    </text>
  </g>
</svg>'''

with open("public/assets/images/doctor-white-coat.svg", "w") as f:
    f.write(doc_white_coat)

# 6. Hero Poster Graphic
hero_poster = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
  <defs>
    <linearGradient id="bgH" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06121f" />
      <stop offset="60%" stop-color="#0c2038" />
      <stop offset="100%" stop-color="#081422" />
    </linearGradient>
    <linearGradient id="goldH" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ebd08e" />
      <stop offset="50%" stop-color="#c5a059" />
      <stop offset="100%" stop-color="#8c6823" />
    </linearGradient>
    <radialGradient id="lightBeam" cx="70%" cy="40%" r="55%">
      <stop offset="0%" stop-color="#c5a059" stop-opacity="0.18" />
      <stop offset="50%" stop-color="#142c4c" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#06121f" stop-opacity="0" />
    </radialGradient>
  </defs>

  <rect width="1920" height="1080" fill="url(#bgH)" />
  <rect width="1920" height="1080" fill="url(#lightBeam)" />

  <!-- Modern Architectural Dental Clinic Silhouette Lines -->
  <g opacity="0.18" stroke="url(#goldH)" stroke-width="1.5">
    <line x1="200" y1="0" x2="200" y2="1080" />
    <line x1="600" y1="0" x2="600" y2="1080" />
    <line x1="1400" y1="0" x2="1400" y2="1080" />
    <line x1="0" y1="880" x2="1920" y2="880" />
  </g>

  <!-- Operatory Chair Silhouette on the right -->
  <g transform="translate(1100, 320)" opacity="0.35">
    <!-- Dental Chair -->
    <path d="M 120,480 C 180,480 260,450 320,400 L 460,280 C 490,250 510,210 500,170 C 490,130 450,110 410,120 L 290,160 C 230,180 180,240 160,300 Z" fill="#1e3a5f" stroke="url(#goldH)" stroke-width="2" />
    <rect x="220" y="470" width="160" height="40" rx="10" fill="#0f243c" stroke="url(#goldH)" stroke-width="1.5" />
    <rect x="280" y="510" width="40" height="160" fill="#0f243c" />
    <rect x="200" y="670" width="200" height="24" rx="12" fill="#0b1a2e" stroke="url(#goldH)" stroke-width="1" />
    
    <!-- Overhead Surgical LED Lamp -->
    <path d="M 60,650 L 60,180 C 60,100 120,60 200,60 L 320,60" fill="none" stroke="url(#goldH)" stroke-width="6" stroke-linecap="round" />
    <ellipse cx="340" cy="60" rx="45" ry="20" fill="#c5a059" fill-opacity="0.8" />
    <!-- Light cone -->
    <polygon points="340,75 220,380 460,380" fill="url(#goldH)" opacity="0.15" />
  </g>

  <!-- Big Decorative A-Tooth Monogram Watermark -->
  <g transform="translate(1380, 180) scale(4)" opacity="0.08">
    <path d="M 18,3 C 23,3 28,5 31,9 C 35,14 36,22 34,29 C 32,35 30,40 29,45 C 28,47 26,47 25,45 C 24,41 22,35 21,31 C 20,28 17,28 16,31 C 15,35 13,41 12,45 C 11,47 9,47 8,45 C 7,40 5,35 3,29 C 1,22 2,14 6,9 C 9,5 14,3 18,3 Z" 
          fill="none" stroke="url(#goldH)" stroke-width="2" />
  </g>
</svg>'''

with open("public/assets/images/hero-poster.svg", "w") as f:
    f.write(hero_poster)

# 7. Clinic Gallery Placeholders
gallery_images = {
    "operatory-suite.svg": ('OPERATORY SUITE', 'Ergonomic treatment unit, sterile setup, and daylight spectrum surgical illumination.', '#0d1f36'),
    "sterilization-bay.svg": ('CLASS B STERILIZATION', 'Multi-stage ultrasonic cleaning, vacuum autoclave, and sealed hygiene packs.', '#0a1a2e'),
    "consultation-desk.svg": ('PRIVATE CONSULTATION', 'One-on-one treatment planning, digital imaging review, and clear care guidance.', '#0e2440'),
    "advanced-diagnostic.svg": ('DIGITAL RADIOGRAPHY', 'Low-dose precision diagnostics and instant high-definition tooth imaging.', '#09182b')
}

for filename, (title, desc, bg_color) in gallery_images.items():
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 450" width="600" height="450">
  <defs>
    <linearGradient id="gGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#dfb76c" />
      <stop offset="100%" stop-color="#9a7530" />
    </linearGradient>
  </defs>
  <rect width="600" height="450" fill="{bg_color}" />
  <rect x="16" y="16" width="568" height="418" rx="12" fill="none" stroke="url(#gGrad)" stroke-width="1.2" stroke-opacity="0.3" />
  
  <!-- Subtle background grid -->
  <g stroke="#ffffff" stroke-opacity="0.04" stroke-width="1">
    <line x1="0" y1="150" x2="600" y2="150" />
    <line x1="0" y1="300" x2="600" y2="300" />
    <line x1="200" y1="0" x2="200" y2="450" />
    <line x1="400" y1="0" x2="400" y2="450" />
  </g>

  <!-- Center Badge -->
  <g transform="translate(300, 180)">
    <circle cx="0" cy="0" r="44" fill="#081320" stroke="url(#gGrad)" stroke-width="2" />
    <!-- Tooth silhouette -->
    <path d="M -12,-16 C -6,-16 0,-12 0,-8 C 0,-12 6,-16 12,-16 C 18,-16 20,-8 18,-2 C 16,6 12,18 8,24 C 6,26 4,26 3,24 C 2,20 0,16 -1,16 C -2,16 -4,20 -5,24 C -6,26 -8,26 -9,24 C -13,18 -17,6 -19,-2 C -21,-8 -18,-16 -12,-16 Z" fill="none" stroke="url(#gGrad)" stroke-width="2" />
  </g>

  <text x="300" y="275" font-family="'Cinzel', 'Playfair Display', serif" font-size="20" font-weight="700" letter-spacing="2" fill="#ffffff" text-anchor="middle">
    {title}
  </text>
  <text x="300" y="308" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">
    {desc}
  </text>
  <text x="300" y="340" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" fill="url(#gGrad)" text-anchor="middle">
    [Supplied Clinic Photo Slot &bull; Asad Avenue, Dhaka]
  </text>
</svg>'''
    with open(f"public/assets/images/{filename}", "w") as f:
        f.write(svg_content)

print("Generated all SVG assets successfully.")
