(function () {
  document.querySelectorAll('.has-submenu > a').forEach(function (el) {
    el.addEventListener('click', function (e) {
      e.preventDefault();
      var li = el.parentElement;
      var wasOpen = li.classList.contains('open');
      document.querySelectorAll('.has-submenu.open').forEach(function (x) {
        x.classList.remove('open');
      });
      if (!wasOpen) li.classList.add('open');
    });
  });
})();
