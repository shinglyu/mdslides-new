//var content ="#FOOBAR\n---\n#Yeeha"
/*
var slideArea = document.querySelector('.remark-slides-area'),
    markdownSource = document.querySelector('#source');
// Remove the slide div before we recreate it
// with calling remark.create().
if (!!slideArea && !!slideArea.parentNode) {
  slideArea.parentNode.removeChild(slideArea);
}
if (!!markdownSource && !!content) {
  markdownSource.innerHTML = content;
}
remark.create();
*/

//TODO: do we really need this wrapping?
var slideRender = {
  // TODO: Render the slide in specified page number, not all.
  /**
   * Render the slide.
   *
   * @param {String} [content] the markdown content.
   * @param {Number} [page] the page number.
   */
  render: function(content, page) {
    var slideArea = document.querySelector('.remark-slides-area'),
      markdownSource = document.querySelector('#source');
    // Remove the slide div before we recreate it
    // with calling remark.create().
    if (!!slideArea && !!slideArea.parentNode) {
      slideArea.parentNode.removeChild(slideArea);
    }
    if (!!markdownSource && !!content) {
      markdownSource.innerHTML = content;
    }
    remark.create();
    this.showSlide(page);
  },
          /**
           * Show the slide in the specificed page.
           *
           * @param {Number} page page number between 1 to n.
           */
  showSlide: function(page) {
    var slides = document.querySelectorAll(
      '.remark-slides-area .remark-slide-container'
    ),
    slideLength = slides.length;
    for (var i = 0; i < slideLength; i++) {
      // Array index is between 0 to n,
      // but the page number is between 1 to n.
      if ((i + 1) === page) {
        slides[i].classList.add('remark-visible');
      } else if (slides[i].classList.contains('remark-visible')) {
        slides[i].classList.remove('remark-visible');
      }
    }
  }
};

window.addEventListener('message', function(event) {
  //console.log(event)
  var data = event.data;
  // TODO: Render the slide in specified page number, not all.
  slideRender.render(data.content, data.page);
  // // Go to the page edited by user currently.
  //slideRender.showSlide(data.page);
  //
});

