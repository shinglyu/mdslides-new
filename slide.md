class: center
###Test slides for
#MDSlides New 
Hello world
efhieh
Eifjei
oefjied
efjei
### 2015/11/9, Somebody


???
top, middle, bottom
left, center, right

---
name: toc
###Table of content
1. Category 
1. Category 
1. Category 
1. Category 
1. Category 
1. Category 
1. Category 

???
This is a template
---
###Bullets and numbers
* Bullet 1
* __Bullet 2__
* _Bullet 3_

1. Number 1
2. Number 2
3. Number 3

---
###Custom class
*  __bold__
* _italic_
* .red[This is a red text]
* .footnote[very small text]
* [link](www.mozilla.org)

---

###Images
.halfwidth[![remote cat](http://7-themes.com/data_images/out/66/6997052-funny-cat.jpg)]
.halfwidth[![local cat](test/cat.png)]

---

class:center
### Images
![tall](https://placehold.it/100x400)
![wide](https://placehold.it/350x100)

---

###Embed Video
<iframe width="100%" height="500px" src="https://www.youtube.com/embed/9VChusdIqU4" frameborder="0" allowfullscreen></iframe>
---
background-image: url('http://people.mozilla.org/~smartell/blog/dino-wallpaper.png')
class: bottom, right

# Mozilla Rocks

???
Scale to fit
---
background-image: url('http://7-themes.com/data_images/out/66/6997052-funny-cat.jpg')
class: bleed

???
Bleed will leave no margin and center align it

---
###Code

```javascript
window.addEventListener('message', function(event) {
  //console.log(event)
  var data = event.data;
  // TODO: Render the slide in specified page number, not all.
  slideRender.render(data.content, data.page);
  // // Go to the page edited by user currently.
  //slideRender.showSlide(data.page);
  //
});

```
---
template: toc
???
reuse the template

---
### Gradual revealing sections
* Step 1

--

* Step 2
  * Sub-step 2-1
  * Sub-step 2-2
  
--

* Step 3
