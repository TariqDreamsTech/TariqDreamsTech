document.addEventListener('DOMContentLoaded', () => {

    // ─── Year ─────────────────────────────────────────
    document.getElementById('year').textContent = new Date().getFullYear();

    // ─── Scroll Progress Bar ──────────────────────────
    const progressBar = document.getElementById('scroll-progress');
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        const total = document.documentElement.scrollHeight - window.innerHeight;
        progressBar.style.width = (scrolled / total * 100) + '%';
    }, { passive: true });

    // ─── Header shrink on scroll ──────────────────────
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        header.classList.toggle('scrolled', window.scrollY > 60);
    }, { passive: true });

    // ─── Custom Cursor ────────────────────────────────
    const cursorDot = document.querySelector('.cursor-dot');
    const cursorOutline = document.querySelector('.cursor-outline');
    let mouseX = 0, mouseY = 0;
    let outlineX = 0, outlineY = 0;

    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX; mouseY = e.clientY;
        cursorDot.style.left = mouseX + 'px';
        cursorDot.style.top = mouseY + 'px';
    });

    // Smooth outline with lerp
    function animateCursor() {
        outlineX += (mouseX - outlineX) * 0.12;
        outlineY += (mouseY - outlineY) * 0.12;
        cursorOutline.style.left = outlineX + 'px';
        cursorOutline.style.top = outlineY + 'px';
        requestAnimationFrame(animateCursor);
    }
    animateCursor();

    document.querySelectorAll('a, button, .btn, .exp-card-cell, .exp-nav-btn, .exp-page-pill, .skill-tags span, .project-card, .field-card, .field-competencies span, .about-highlight-card, .lightbox-trigger').forEach(el => {
        el.addEventListener('mouseenter', () => cursorOutline.classList.add('hovered'));
        el.addEventListener('mouseleave', () => cursorOutline.classList.remove('hovered'));
    });

    // ─── Mobile Nav ───────────────────────────────────
    const menuBtn = document.querySelector('.menu-btn');
    const mobileNav = document.querySelector('.mobile-nav');
    const navOverlay = document.querySelector('.nav-overlay');

    function toggleNav(open) {
        menuBtn.classList.toggle('open', open);
        mobileNav.classList.toggle('open', open);
        navOverlay.classList.toggle('open', open);
        document.body.style.overflow = open ? 'hidden' : '';
    }

    menuBtn.addEventListener('click', () => toggleNav(!mobileNav.classList.contains('open')));
    navOverlay.addEventListener('click', () => toggleNav(false));
    mobileNav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => toggleNav(false)));

    // ─── Active Nav on Scroll ─────────────────────────
    const navAnchors = document.querySelectorAll('.nav-links a[href^="#"], .mobile-nav a[href^="#"]');
    const sectionEls = document.querySelectorAll('section[id]');

    const navObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                navAnchors.forEach(a => {
                    a.classList.toggle('active', a.getAttribute('href') === '#' + entry.target.id);
                });
            }
        });
    }, { threshold: 0.35 });

    sectionEls.forEach(s => navObserver.observe(s));

    // ─── Typing Animation ─────────────────────────────
    const roles = [
        'AI Product Builder',
        'Founder @ Ranbval',
        'Senior Python Engineer',
        'N8N Automation Architect',
        'Encrypted Infra Engineer',
    ];
    const roleEl = document.querySelector('.hero-role');
    if (roleEl) {
        roleEl.innerHTML = '<span class="typed-text"></span><span class="typed-cursor">|</span>';
        const typedText = roleEl.querySelector('.typed-text');
        let roleIdx = 0, charIdx = 0, deleting = false;

        function type() {
            const current = roles[roleIdx];
            typedText.textContent = deleting
                ? current.slice(0, charIdx--)
                : current.slice(0, charIdx++);

            let delay = deleting ? 45 : 90;
            if (!deleting && charIdx === current.length + 1) {
                delay = 1800; deleting = true;
            } else if (deleting && charIdx === 0) {
                deleting = false;
                roleIdx = (roleIdx + 1) % roles.length;
                delay = 400;
            }
            setTimeout(type, delay);
        }
        setTimeout(type, 800);
    }

    // ─── Experience Grid Pagination (9 per page) ──────
    const expCells = document.querySelectorAll('.experience-grid .exp-card-cell');
    const expPrevBtn = document.getElementById('exp-prev-btn');
    const expNextBtn = document.getElementById('exp-next-btn');
    const expPagePills = document.querySelectorAll('.exp-page-pill');
    const expPageRange = document.getElementById('exp-page-range');
    const expTotalCount = document.getElementById('exp-total-count');

    if (expCells.length && expPrevBtn && expNextBtn) {
        const itemsPerPage = 9;
        const totalItems = expCells.length;
        const totalPages = Math.ceil(totalItems / itemsPerPage);
        let currentPage = 1;

        if (expTotalCount) expTotalCount.textContent = totalItems;

        function renderExpPage(page, shouldScroll) {
            currentPage = page;
            const start = (page - 1) * itemsPerPage;
            const end = Math.min(start + itemsPerPage, totalItems);

            expCells.forEach((cell, index) => {
                if (index >= start && index < end) {
                    cell.style.display = 'block';
                    setTimeout(() => {
                        cell.classList.add('visible');
                        cell.style.opacity = '1';
                        cell.style.transform = 'translateY(0)';
                    }, (index - start) * 35);
                } else {
                    cell.style.display = 'none';
                    cell.classList.remove('visible');
                    cell.style.opacity = '0';
                    cell.style.transform = 'translateY(16px)';
                    cell.classList.remove('is-expanded');
                }
            });

            if (expPageRange) {
                expPageRange.textContent = `${start + 1}–${end}`;
            }

            if (expPrevBtn) expPrevBtn.disabled = (currentPage === 1);
            if (expNextBtn) expNextBtn.disabled = (currentPage === totalPages);

            expPagePills.forEach(pill => {
                const pageNum = parseInt(pill.getAttribute('data-page'), 10);
                if (pageNum === currentPage) {
                    pill.classList.add('active');
                } else {
                    pill.classList.remove('active');
                }
            });

            if (shouldScroll) {
                const expSec = document.getElementById('experience');
                if (expSec) {
                    expSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        }

        expPrevBtn.addEventListener('click', () => {
            if (currentPage > 1) renderExpPage(currentPage - 1, true);
        });

        expNextBtn.addEventListener('click', () => {
            if (currentPage < totalPages) renderExpPage(currentPage + 1, true);
        });

        expPagePills.forEach(pill => {
            pill.addEventListener('click', () => {
                const page = parseInt(pill.getAttribute('data-page'), 10);
                if (page && page !== currentPage) {
                    renderExpPage(page, true);
                }
            });
        });

        // Tap/click to toggle expanded state on touch/mobile
        expCells.forEach(cell => {
            cell.addEventListener('click', (e) => {
                // If user clicks a link inside, let it navigate
                if (e.target.tagName === 'A' || e.target.closest('a')) return;
                const wasExpanded = cell.classList.contains('is-expanded');
                expCells.forEach(c => {
                    if (c !== cell) c.classList.remove('is-expanded');
                });
                if (!wasExpanded) {
                    cell.classList.add('is-expanded');
                } else {
                    cell.classList.remove('is-expanded');
                }
            });
        });

        // Initialize Page 1
        renderExpPage(1, false);
    }

    // ─── Scroll Reveal ────────────────────────────────
    const revealEls = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, i) => {
            if (entry.isIntersecting) {
                setTimeout(() => entry.target.classList.add('visible'), i * 60);
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    revealEls.forEach(el => revealObserver.observe(el));

    // ─── Achievement Counter Animation ────────────────
    document.querySelectorAll('.achievement-content .highlight').forEach(el => {
        const text = el.textContent;
        const num = parseInt(text);
        if (isNaN(num)) return;
        const suffix = text.replace(String(num), '');
        el.textContent = '0' + suffix;

        const counterObserver = new IntersectionObserver(([entry]) => {
            if (!entry.isIntersecting) return;
            counterObserver.disconnect();
            let start = 0;
            const step = Math.ceil(num / 40);
            const interval = setInterval(() => {
                start = Math.min(start + step, num);
                el.textContent = start + suffix;
                if (start >= num) clearInterval(interval);
            }, 40);
        }, { threshold: 0.5 });
        counterObserver.observe(el);
    });

    // ─── Image Lightbox ───────────────────────────────
    const lightboxOverlay = document.getElementById('lightbox-overlay');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxCaption = document.getElementById('lightbox-caption');
    const lightboxClose = lightboxOverlay.querySelector('.lightbox-close');

    document.querySelectorAll('.lightbox-trigger').forEach(el => {
        el.style.cursor = 'zoom-in';
        el.addEventListener('click', (e) => {
            const imgEl = el.tagName === 'IMG' ? el : el.querySelector('img');
            if (!imgEl) return;
            lightboxImg.src = imgEl.src;
            lightboxImg.alt = imgEl.alt;
            const caption = imgEl.getAttribute('data-caption') || imgEl.alt || '';
            if (lightboxCaption) {
                lightboxCaption.textContent = caption;
                lightboxCaption.style.display = caption ? 'block' : 'none';
            }
            lightboxOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    });

    function closeLightbox() {
        lightboxOverlay.classList.remove('active');
        document.body.style.overflow = '';
        lightboxImg.src = '';
        if (lightboxCaption) lightboxCaption.textContent = '';
    }

    if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
    lightboxOverlay.addEventListener('click', (e) => {
        if (e.target === lightboxOverlay || e.target === lightboxImg) closeLightbox();
    });
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && lightboxOverlay.classList.contains('active')) closeLightbox();
    });

    // ─── Back to Top ──────────────────────────────────
    const backToTop = document.getElementById('back-to-top');
    window.addEventListener('scroll', () => {
        backToTop.classList.toggle('visible', window.scrollY > 500);
    }, { passive: true });
    backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

    // ─── Smooth Scroll ────────────────────────────────
    document.querySelectorAll('a[href^="#"]').forEach(a => {
        a.addEventListener('click', (e) => {
            const target = document.querySelector(a.getAttribute('href'));
            if (!target) return;
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth' });
        });
    });

    // ─── Canvas Background ────────────────────────────
    const canvas = document.getElementById('bg-animation');
    const ctx = canvas.getContext('2d');
    let W, H, particles = [];
    const COUNT = 80;
    const MAX_DIST = 140;

    class Particle {
        constructor() { this.reset(true); }
        reset(init = false) {
            this.x = Math.random() * W;
            this.y = init ? Math.random() * H : (Math.random() > 0.5 ? -5 : H + 5);
            this.vx = (Math.random() - 0.5) * 0.4;
            this.vy = (Math.random() - 0.5) * 0.4;
            this.r = Math.random() * 1.5 + 0.5;
            this.alpha = Math.random() * 0.4 + 0.15;
        }
        update() {
            this.x += this.vx; this.y += this.vy;
            if (this.x < -20 || this.x > W + 20 || this.y < -20 || this.y > H + 20) this.reset();
        }
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(255,186,73,${this.alpha})`;
            ctx.fill();
        }
    }

    function resize() {
        W = canvas.width = window.innerWidth;
        H = canvas.height = window.innerHeight;
    }

    function initParticles() {
        particles = [];
        for (let i = 0; i < COUNT; i++) particles.push(new Particle());
    }

    function drawFrame() {
        ctx.clearRect(0, 0, W, H);
        for (let i = 0; i < particles.length; i++) {
            particles[i].update();
            particles[i].draw();
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const d = Math.sqrt(dx * dx + dy * dy);
                if (d < MAX_DIST) {
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.strokeStyle = `rgba(255,186,73,${0.08 * (1 - d / MAX_DIST)})`;
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
            }
        }
        requestAnimationFrame(drawFrame);
    }

    window.addEventListener('resize', () => { resize(); initParticles(); });
    resize(); initParticles(); drawFrame();

});
