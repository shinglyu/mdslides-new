window.addEventListener('load', function() {
  var editor = CodeMirror.fromTextArea(document.getElementById('editorTextarea'), {
    keyMap: 'vim',
    lineNumbers: true,
    theme: 'colorforth'
  });

  editor.on('change', function(evt){
    updateSlide(editor.getValue())
  })
});


