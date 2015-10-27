function updateSlide() {
  console.log("update slide")
  var previewWindow = document.getElementById('previewIframe').contentWindow,
    editorText = editorTextarea.value,
    editingContent = '',
    page = 0;
  editingContent = editorText.substring(0, editorTextarea.selectionStart);
  //page = markdownHelper.pageNumber(editingContent);
  console.log(previewWindow)
  console.log(editorText)
  previewWindow.postMessage(
    {
      content: editorText,
      //page: page

    },
    location.origin

  );
  var pReq = new XMLHttpRequest();
  pReq.onload = function(e){
    console.log("saved")
  }
  //oReq.addEventListener("load", reqListener);
  pReq.open("POST", "http://127.0.0.1:9876/save");
  pReq.send(editorText);
}
function inputEventTrigger(inputElement, options, callback) {
  const DEFAULT_INTERVAL = 400;
  var prevUpdateSlideTime = new Date().getTime(),
    lastKeyupTime,
  updateSlideTimer,
  postMessageInterval;
  if (typeof(options) === 'function') {
    callback = options;
    postMessageInterval = DEFAULT_INTERVAL;

  } else {
    postMessageInterval =
      options.postMessageInterval || DEFAULT_INTERVAL;

  }
  inputElement.addEventListener('input', function(event) {
    var now = new Date().getTime();
    if (now - prevUpdateSlideTime > postMessageInterval) {
      callback();
      prevUpdateSlideTime = now;
    }
  });
  inputElement.addEventListener('keydown', function(event) {
    console.log("KEYDOWN!")
    if (!updateSlideTimer) {
      updateSlideTimer = setInterval(function() {
        var now = new Date().getTime();
        if ((now - lastKeyupTime) > postMessageInterval) {
          callback();
          clearInterval(updateSlideTimer);
          updateSlideTimer = undefined;

        }

      }, postMessageInterval);
    }
  });
  inputElement.addEventListener('keyup', function(event) {
    lastKeyupTime = new Date().getTime();
  });
}

window.onload = function(){
  inputEventTrigger(document.getElementById('editorTextarea'), updateSlide)
}

var oReq = new XMLHttpRequest();
oReq.onload = function(e){
  console.log(oReq.response)
  document.getElementById('editorTextarea').value = oReq.response
  document.getElementById('previewIframe').onload = function(){
    updateSlide()
  }
  //window.setTimeout(updateSlide, 1000)
  //updateSlide()
}
//oReq.addEventListener("load", reqListener);
oReq.open("GET", "slide.md");
oReq.send();
