var gulp = require('gulp')

gulp.task('default', function(){
  var inline = require('gulp-inline')
    , uglify = require('gulp-uglify')
    //, minifyCss = require('gulp-minify-css');

  gulp.src(['index.html', 'slide.html'])
  .pipe(inline({
    base: '.',
    js: uglify,
    //css: minifyCss,
    //disabledTypes: ['svg', 'img', 'js'], // Only inline css files 
    //ignore: ['./css/do-not-inline-me.css']

  }))
  .pipe(gulp.dest('dist/'));
})
