(() => {
  const routes = { intro: 'index.html', work: 'experience.html', project: 'projects.html', education: 'education.html', resume: 'Docs/Prakhar_Dixit_CV.pdf', contact: 'contact.html', publications: 'publications.html' };
  window.location.replace(routes[window.location.hash.slice(1)] || 'index.html');
})();
