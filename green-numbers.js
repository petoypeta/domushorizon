(function() {
  function wrapNumbers(el) {
    var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null, false);
    var nodes = [];
    var node;
    while (node = walker.nextNode()) {
      if (node.parentElement && (
        node.parentElement.tagName === 'SCRIPT' ||
        node.parentElement.tagName === 'STYLE' ||
        node.parentElement.classList.contains('math-inline') ||
        node.parentElement.classList.contains('math-display') ||
        node.parentElement.classList.contains('code-block') ||
        node.parentElement.tagName === 'CODE'
      )) continue;
      if (/\d/.test(node.nodeValue)) nodes.push(node);
    }
    nodes.forEach(function(n) {
      var span = document.createElement('span');
      span.innerHTML = n.nodeValue.replace(/(\d[\d.,]*)/g, '<span class="num-green">$1</span>');
      n.parentNode.replaceChild(span, n);
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() { wrapNumbers(document.querySelector('.page') || document.body); });
  } else {
    wrapNumbers(document.querySelector('.page') || document.body);
  }
})();
