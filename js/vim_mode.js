var editor = undefined;
window.addEventListener('load', function() {
  editor = CodeMirror.fromTextArea(document.getElementById('editorTextarea'), {
    keyMap: 'vim',
    lineNumbers: true,
    theme: 'colorforth'
  });
  console.log(editor)
  init(editor);

  editor.on('change', function(evt){
    updateSlide(editor.getValue())
  })
});


