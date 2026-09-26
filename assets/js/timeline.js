// Experience timeline: the centre line draws downward, then each card slides in
// from its side as it scrolls into view. Without JS (or with reduced motion)
// everything is simply shown.
(() => {
  const tl = document.querySelector('.timeline');
  if (!tl || !('IntersectionObserver' in window)) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  tl.classList.add('tl-animate');
  setTimeout(() => tl.classList.add('tl-started'), 200);

  const items = tl.querySelectorAll('.timeline-item');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('tl-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  items.forEach((el, i) => {
    el.style.transitionDelay = `${i * 80}ms`;
    el.querySelector('.tl-card').style.transitionDelay = `${i * 80}ms`;
    observer.observe(el);
  });
})();
