function updateSlide(content) {
  console.log("update slide")
  var previewWindow = document.getElementById('previewIframe').contentWindow,
    //editorText = editorTextarea.value,
    //TODO handle invalid content
    editorText = content,
    //editorText = editor.getText(),
    editingContent = '',
    page = 0;
  //editingContent = editorText.substring(0, editorTextarea.selectionStart);
  //page = markdownHelper.pageNumber(editingContent);
  console.log(previewWindow)
  console.log(editorText)
  previewWindow.postMessage(
    {
      content: editorText,
      //TODO make page work
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
//TODO refactor this function to meet codemirror and textarea input
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

//TODO: user addEventListener
/*
window.onload = function(){
  inputEventTrigger(document.getElementById('editorTextarea'), updateSlide)
}
*/


//TODO: wrap this into init
function init(editor){
  var oReq = new XMLHttpRequest();
  oReq.onload = function(e){
    console.log("Received content")
    console.log(oReq)
    console.log(oReq.response)
    editor.setValue(oReq.response)
    //document.getElementById('editorTextarea').value = oReq.response
    updateSlide(editor.getValue())
    //document.getElementById('previewIframe').addEventListener('load', function(){
    //  updateSlide(editor.getText())
    //})
    //window.setTimeout(updateSlide, 1000)
    //updateSlide()
  }
  //oReq.addEventListener("load", reqListener);
  //TODO Dynamic file name
  oReq.open("GET", "slide.md");
  oReq.send();
}
