/**
 * Dr. Arafath Dental Clinic Demo — Master Client Logic
 * Mobile-First, Accessible, Zero-Dependency
 * Form Validation, WhatsApp Message Generator, Modal Handlers
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Accessibility & Form Validation Bridge (Modern Web Guidance)
  const appointmentForm = document.getElementById('appointmentForm');
  const dateInput = document.getElementById('prefDate');
  const serviceSelect = document.getElementById('prefService');
  const successModal = document.getElementById('successModal');
  const checklistModal = document.getElementById('checklistModal');
  const lightboxModal = document.getElementById('lightboxModal');
  const videoModal = document.getElementById('videoModal');

  // Set minimum date to today
  if (dateInput) {
    const today = new Date().toISOString().split('T')[0];
    dateInput.min = today;
  }

  // Modern Web Guidance: Sync aria-invalid with CSS :user-invalid state
  const syncAriaInvalid = (input) => {
    if (!input || !input.checkValidity) return;
    const isInvalid = input.matches?.(':user-invalid') || (!input.checkValidity() && input.classList.contains('user-invalid-fallback'));
    if (isInvalid) {
      input.setAttribute('aria-invalid', 'true');
    } else {
      input.removeAttribute('aria-invalid');
    }
  };

  if (appointmentForm) {
    // Listen in capture phase for blur
    appointmentForm.addEventListener('blur', (e) => {
      if (e.target.matches('input, select, textarea')) {
        syncAriaInvalid(e.target);
      }
    }, true);

    // Clear error on input if user fixes it
    appointmentForm.addEventListener('input', (e) => {
      if (e.target.matches('input, select, textarea') && e.target.hasAttribute('aria-invalid')) {
        if (e.target.checkValidity()) {
          syncAriaInvalid(e.target);
        }
      }
    });

    // Fallback for browsers lacking CSS selector(:user-invalid)
    if (!CSS.supports('selector(:user-invalid)')) {
      const dirtyInputs = new WeakSet();
      appointmentForm.addEventListener('blur', (e) => {
        const input = e.target;
        if (input.matches?.('input, select, textarea')) {
          dirtyInputs.add(input);
          if (!input.checkValidity()) {
            input.classList.add('user-invalid-fallback');
          } else {
            input.classList.remove('user-invalid-fallback');
          }
          syncAriaInvalid(input);
        }
      }, true);

      appointmentForm.addEventListener('input', (e) => {
        const input = e.target;
        if (dirtyInputs.has(input)) {
          if (!input.checkValidity()) {
            input.classList.add('user-invalid-fallback');
          } else {
            input.classList.remove('user-invalid-fallback');
          }
          syncAriaInvalid(input);
        }
      });
    }

    // Appointment Request WhatsApp Handler
    appointmentForm.addEventListener('submit', (e) => {
      e.preventDefault();

      // Check HTML5 validity
      if (!appointmentForm.checkValidity()) {
        appointmentForm.reportValidity();
        return;
      }

      const patientName = document.getElementById('patientName').value.trim();
      const patientPhone = document.getElementById('patientPhone').value.trim();
      const service = serviceSelect.options[serviceSelect.selectedIndex].text;
      const date = dateInput.value;
      const sessionRadio = document.querySelector('input[name="sessionSlot"]:checked');
      const session = sessionRadio ? sessionRadio.value : 'Any available session';
      const notes = document.getElementById('notes').value.trim();

      // Build structured WhatsApp inquiry message (Explicitly marked as request, not confirmed booking)
      const message = [
        `*Dr. Arafath Dental — Appointment Request*`,
        `------------------------------------------`,
        `👤 *Patient Name:* ${patientName}`,
        `📱 *Contact / WhatsApp:* ${patientPhone}`,
        `🦷 *Requested Service:* ${service}`,
        `📅 *Preferred Date:* ${date}`,
        `⏰ *Preferred Slot:* ${session}`,
        notes ? `📝 *Dental Notes:* ${notes}` : `📝 *Notes:* None specified`,
        `------------------------------------------`,
        `_Note: This is an appointment request via dr-arafat.d4f.me. Please verify slot availability._`
      ].join('\n');

      const whatsappNumber = '8801684885861';
      const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`;

      // Show confirmation dialog to user
      if (successModal) {
        document.getElementById('modalPatientName').textContent = patientName;
        document.getElementById('modalService').textContent = service;
        document.getElementById('modalDate').textContent = `${date} (${session})`;
        successModal.showModal();
      }

      // Open WhatsApp in new tab / app
      window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
    });
  }

  // 2. Service Card CTA Pre-Selection
  const serviceButtons = document.querySelectorAll('.btn-service-select');
  serviceButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const targetServiceValue = btn.getAttribute('data-service');
      if (serviceSelect && targetServiceValue) {
        serviceSelect.value = targetServiceValue;
        // Scroll smoothly to appointment section
        const appointmentSection = document.getElementById('appointment');
        if (appointmentSection) {
          appointmentSection.scrollIntoView({ behavior: 'smooth' });
          serviceSelect.focus();
          serviceSelect.classList.add('highlight-glow');
          setTimeout(() => serviceSelect.classList.remove('highlight-glow'), 1800);
        }
      }
    });
  });

  // 3. Mobile Navigation Drawer
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const mobileDrawer = document.getElementById('mobileDrawer');
  const mobileNavLinks = document.querySelectorAll('.mobile-drawer a');

  if (mobileMenuBtn && mobileDrawer) {
    const toggleMenu = (open) => {
      const isOpen = open !== undefined ? open : mobileMenuBtn.getAttribute('aria-expanded') !== 'true';
      mobileMenuBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      mobileDrawer.classList.toggle('open', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    };

    mobileMenuBtn.addEventListener('click', () => toggleMenu());

    mobileNavLinks.forEach(link => {
      link.addEventListener('click', () => toggleMenu(false));
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileDrawer.classList.contains('open')) {
        toggleMenu(false);
      }
    });
  }

  // 4. Sticky Mobile Bottom Bar Visibility (IntersectionObserver)
  const heroSection = document.getElementById('hero');
  const stickyMobileBar = document.getElementById('stickyMobileBar');

  if (heroSection && stickyMobileBar && 'IntersectionObserver' in window) {
    const heroObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        // When hero is NOT intersecting (user scrolled past hero), show bar
        if (!entry.isIntersecting) {
          stickyMobileBar.classList.add('visible');
        } else {
          stickyMobileBar.classList.remove('visible');
        }
      });
    }, { threshold: 0.15 });

    heroObserver.observe(heroSection);
  }

  // 5. Modern Web Guidance <dialog closedby="any"> Light-Dismiss Fallback
  const allDialogs = document.querySelectorAll('dialog');
  allDialogs.forEach(dialog => {
    if (!('closedBy' in HTMLDialogElement.prototype)) {
      dialog.addEventListener('click', (event) => {
        if (event.target !== dialog) return;
        const rect = dialog.getBoundingClientRect();
        const isDialogContent = (
          rect.top <= event.clientY &&
          event.clientY <= rect.top + rect.height &&
          rect.left <= event.clientX &&
          event.clientX <= rect.left + rect.width
        );
        if (!isDialogContent) {
          dialog.close();
        }
      });
    }

    // Modal close buttons
    const closeBtn = dialog.querySelector('.modal-close-btn');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => dialog.close());
    }
  });

  // 6. Pre-Launch Checklist Modal & LocalStorage persistence
  const checklistBtn = document.getElementById('openChecklistBtn');
  const checklistBtnMobile = document.getElementById('openChecklistBtnMobile');
  const checklistCheckboxes = document.querySelectorAll('.checklist-item input[type="checkbox"]');

  const openChecklist = () => {
    if (checklistModal) {
      checklistModal.showModal();
    }
  };

  if (checklistBtn) checklistBtn.addEventListener('click', openChecklist);
  if (checklistBtnMobile) checklistBtnMobile.addEventListener('click', openChecklist);

  // Restore checklist states
  checklistCheckboxes.forEach((cb, idx) => {
    const saved = localStorage.getItem(`dr_arafat_checklist_${idx}`);
    if (saved === 'true') cb.checked = true;
    cb.addEventListener('change', () => {
      localStorage.setItem(`dr_arafat_checklist_${idx}`, cb.checked ? 'true' : 'false');
    });
  });

  // 6.5 Interactive Clinic Practice Slider (Modern Web Guidance: scroll-snap-state-sync)
  const sliderTrack = document.getElementById('clinicSliderTrack');
  const prevBtn = document.querySelector('.slider-nav-btn.prev-btn');
  const nextBtn = document.querySelector('.slider-nav-btn.next-btn');
  const sliderDots = document.querySelectorAll('.slider-dot');
  const activeIndexEl = document.querySelector('.slider-counter .active-index');
  const progressBar = document.getElementById('sliderProgressBar');
  const slides = document.querySelectorAll('.clinic-slide');

  if (sliderTrack && slides.length > 0) {
    let currentIndex = 0;
    let autoplayTimer = null;
    let progressTimer = null;
    let progressPercent = 0;
    const AUTOPLAY_DURATION = 5000;
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const updateSliderState = (index) => {
      currentIndex = index;
      if (activeIndexEl) {
        activeIndexEl.textContent = String(index + 1).padStart(2, '0');
      }
      sliderDots.forEach((dot, idx) => {
        const isActive = idx === index;
        dot.classList.toggle('is-active', isActive);
        dot.setAttribute('aria-selected', isActive ? 'true' : 'false');
      });
      slides.forEach((slide, idx) => {
        slide.classList.toggle('is-active', idx === index);
      });
      resetProgress();
    };

    const scrollToIndex = (index) => {
      if (index < 0) index = slides.length - 1;
      if (index >= slides.length) index = 0;
      const targetSlide = slides[index];
      if (targetSlide) {
        sliderTrack.scrollTo({
          left: targetSlide.offsetLeft,
          behavior: prefersReducedMotion ? 'auto' : 'smooth'
        });
      }
      updateSliderState(index);
    };

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        scrollToIndex(currentIndex - 1);
        restartAutoplay();
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        scrollToIndex(currentIndex + 1);
        restartAutoplay();
      });
    }

    sliderDots.forEach((dot, idx) => {
      dot.addEventListener('click', () => {
        scrollToIndex(idx);
        restartAutoplay();
      });
    });

    // Keyboard navigation when track is focused
    sliderTrack.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        scrollToIndex(currentIndex - 1);
        restartAutoplay();
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        scrollToIndex(currentIndex + 1);
        restartAutoplay();
      }
    });

    // Modern Web Guidance: scroll-snap-state-sync using IntersectionObserver
    const slideObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && entry.intersectionRatio >= 0.55) {
          const index = Array.from(slides).indexOf(entry.target);
          if (index !== -1 && index !== currentIndex) {
            updateSliderState(index);
          }
        }
      });
    }, {
      root: sliderTrack,
      threshold: 0.6
    });

    slides.forEach(slide => slideObserver.observe(slide));

    // Also support native scrollsnapchange if available
    if ('onscrollsnapchange' in window) {
      sliderTrack.addEventListener('scrollsnapchange', (e) => {
        const snappedEl = e.snapTargetInline || e.snapTargetBlock;
        if (snappedEl) {
          const index = Array.from(slides).indexOf(snappedEl);
          if (index !== -1) updateSliderState(index);
        }
      });
    }

    // Autoplay & Progress Bar
    const resetProgress = () => {
      progressPercent = 0;
      if (progressBar) progressBar.style.width = '0%';
    };

    const startAutoplay = () => {
      if (prefersReducedMotion) return;
      stopAutoplay();
      const interval = 50;
      const step = 100 / (AUTOPLAY_DURATION / interval);
      
      progressTimer = setInterval(() => {
        progressPercent += step;
        if (progressBar) progressBar.style.width = `${Math.min(progressPercent, 100)}%`;
      }, interval);

      autoplayTimer = setTimeout(() => {
        scrollToIndex(currentIndex + 1);
        startAutoplay();
      }, AUTOPLAY_DURATION);
    };

    const stopAutoplay = () => {
      if (autoplayTimer) clearTimeout(autoplayTimer);
      if (progressTimer) clearInterval(progressTimer);
      resetProgress();
    };

    const restartAutoplay = () => {
      stopAutoplay();
      startAutoplay();
    };

    sliderTrack.parentElement.addEventListener('mouseenter', stopAutoplay);
    sliderTrack.parentElement.addEventListener('mouseleave', startAutoplay);
    sliderTrack.parentElement.addEventListener('focusin', stopAutoplay);
    sliderTrack.parentElement.addEventListener('focusout', startAutoplay);
    sliderTrack.addEventListener('touchstart', stopAutoplay, { passive: true });

    startAutoplay();

    // Slide Media Lightbox trigger
    slides.forEach(slide => {
      const mediaWrap = slide.querySelector('.slide-media-wrap');
      if (mediaWrap) {
        mediaWrap.addEventListener('click', () => {
          const img = mediaWrap.querySelector('img');
          const title = slide.querySelector('.slide-title')?.textContent || 'Clinical Photograph';
          const badge = slide.querySelector('.slide-badge')?.textContent || '';
          const desc = slide.querySelector('.slide-text')?.textContent || '';
          if (lightboxModal && lightboxImg && img) {
            lightboxImg.src = img.currentSrc || img.src;
            lightboxImg.alt = title;
            if (lightboxCaption) {
              lightboxCaption.textContent = `${badge} — ${title}: ${desc}`;
            }
            lightboxModal.showModal();
          }
        });
      }
    });
  }

  // 7. Photo Gallery Lightbox
  const galleryCards = document.querySelectorAll('.gallery-card');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxCaption = document.getElementById('lightboxCaption');

  galleryCards.forEach(card => {
    card.addEventListener('click', () => {
      const img = card.querySelector('img');
      const title = card.querySelector('h4')?.textContent || 'Clinic Photo';
      const desc = card.querySelector('p')?.textContent || '';
      if (lightboxModal && lightboxImg && img) {
        lightboxImg.src = img.src;
        lightboxImg.alt = title;
        if (lightboxCaption) {
          lightboxCaption.textContent = `${title} — ${desc}`;
        }
        lightboxModal.showModal();
      }
    });
  });

  // 8. Video Gallery Lightbox / Player
  const videoCards = document.querySelectorAll('.video-thumb-wrap');
  const videoPlayerTitle = document.getElementById('videoPlayerTitle');
  const videoPlayerDesc = document.getElementById('videoPlayerDesc');

  videoCards.forEach(card => {
    card.addEventListener('click', () => {
      const parent = card.closest('.video-card');
      const title = parent?.querySelector('h4')?.textContent || 'Clinic Video';
      const desc = parent?.querySelector('p')?.textContent || '';
      if (videoModal && videoPlayerTitle) {
        videoPlayerTitle.textContent = title;
        if (videoPlayerDesc) videoPlayerDesc.textContent = desc;
        videoModal.showModal();
      }
    });
  });
});
