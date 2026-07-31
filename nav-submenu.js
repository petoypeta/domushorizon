(function () {
  function init() {
    var submenuLinks = document.querySelectorAll('.has-submenu > a');
    submenuLinks.forEach(function (el) {
      el.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        var li = el.parentElement;
        var wasOpen = li.classList.contains('open');
        document.querySelectorAll('.has-submenu.open').forEach(function (x) {
          x.classList.remove('open');
        });
        if (!wasOpen) li.classList.add('open');
      });
    });
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.has-submenu')) {
        document.querySelectorAll('.has-submenu.open').forEach(function (x) {
          x.classList.remove('open');
        });
      }
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
