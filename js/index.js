var lastUpdate=-1;
function getCurrentPage(content){
  var MARKDOWN_PAGE_LINE = '---';
  console.log(content)
  return content
    //.join('\n')
    .replace(/^\s+|\s+$/g, '')
    .split(MARKDOWN_PAGE_LINE).length;
}
function updateSlide(content) {
  //console.log("update slide");
  var previewWindow = document.getElementById('previewIframe').contentWindow,
    //editorText = editorTextarea.value,
    //TODO handle invalid content
    editorText = content,
    //editorText = editor.getText(),
    editingContent = '',
    page = 1;
  //editingContent = editorText.substring(0, editorTextarea.selectionStart);
  console.log(window.editor.getCursor())
  editingContent = window.editor.getValue().split('\n', window.editor.getCursor().line).join('\n')
  //console.log(editingContent)
  //page = markdownHelper.pageNumber(editingContent);
  page = getCurrentPage(editingContent);
  console.log(page)
  //console.log(previewWindow);
  //console.log(editorText);
  previewWindow.postMessage(
    {
      content: editorText,
      //TODO make page work
      //page: page
      page: page

    },
    location.origin

  );
}
function save(editorText){
  var pReq = new XMLHttpRequest();
  /*
  pReq.onload = function(e){
    console.log("saved");
  };
  */
  /*
  pReq.addEventListener("load", function(e){
    console.log(pReq.status)
    //if (e.status)
    lastUpdate = Date.now();

  });
  */
  pReq.open("POST", "http://127.0.0.1:9876/save");
  //pReq.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  pReq.onreadystatechange = function(){
    console.log(pReq)
    if (pReq.readyState == 4 && pReq.status == 200){
      console.log('saved successfully')
      lastUpdate = Date.now();
    }
    else if (pReq.readyState == 4 && pReq.status == 409){
      alert("You are already editing this document in another window, to prevent data loss, please close this one and use the existing window.")
    }
  }
  pReq.send(JSON.stringify({
    'text': editorText, 'lastUpdate': lastUpdate
  }));
}
//TODO refactor this function to meet codemirror and textarea input
function inputEventTrigger(inputElement, options, callback) {
  //const DEFAULT_INTERVAL = 400;
  const DEFAULT_INTERVAL = 600;
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
  //inputElement.addEventListener('input', function(event) {
  inputElement.on('change', function(event) {
    //console.log('changed')
    if (!updateSlideTimer) {
      updateSlideTimer = setInterval(function() {
        var now = new Date().getTime();
        if ((now - prevUpdateSlideTime) > postMessageInterval) {
          callback();
          prevUpdateSlideTime = now;
          clearInterval(updateSlideTimer);
          updateSlideTimer = undefined;
        }

      }, postMessageInterval);
    }
    /*
    var now = new Date().getTime();
    if (now - prevUpdateSlideTime > postMessageInterval) {
      callback();
      prevUpdateSlideTime = now;
    }
    */
  });
  //inputElement.addEventListener('keydown', function(event) {
  /*
  inputElement.on('keydown', function(event) {
    console.log('keydown');
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
  //inputElement.addEventListener('keyup', function(event) {
  inputElement.on('keyup', function(event) {
    console.log('keyup');
    lastKeyupTime = new Date().getTime();
  });
  */
}

//TODO: user addEventListener
/*
window.onload = function(){
  inputEventTrigger(document.getElementById('editorTextarea'), updateSlide)
}
*/

function toggleMode(){
  var editor = document.getElementById('editor')
  var preview = document.getElementById('preview')
  var toggle = document.getElementById('modeToggle')
  if (editor.style.display !== "none"){
    editor.style.display = "none";
    preview.style.width = "100%";
    toggle.textContent = ">";

  }
  else {
    editor.style.display = "block";
    preview.style.width = "50%";
    toggle.textContent = "<";
  }
}

function init(editor){
  editor.setValue('Loading...')
  var oReq = new XMLHttpRequest();
  oReq.onreadystatechange= function(e){
    if (oReq.readyState == 4 && oReq.status == 200){
      console.log("Received content");
      console.log(oReq);
      console.log(oReq.response);
      editor.setValue(oReq.response);
      //document.getElementById('editorTextarea').value = oReq.response
      updateSlide(editor.getValue());
      //document.getElementById('previewIframe').addEventListener('load', function(){
      //  updateSlide(editor.getText())
      //})
      //window.setTimeout(updateSlide, 1000)
      //updateSlide()
      // Init handlers after first load
      inputEventTrigger(editor, function(){
        updateSlide(editor.getValue());
        save(editor.getValue());
      });
    }
  };
  //oReq.addEventListener("load", reqListener);
  //TODO Dynamic file name
  oReq.open("GET", "slide.md?rand=" + Date.now());
  oReq.send();

  document.getElementById('modeToggle').addEventListener('click', function(e){
    toggleMode();
  })
}
