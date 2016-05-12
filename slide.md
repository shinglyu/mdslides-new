class: center, middle
###Test slides for
#MDSlides New 
### 2015/11/9
### Somebody


???
top, middle, bottom
left, center, right

---
name: toc
###Agenda
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
###Table of content
* Category 
* Category 
* Category a very very very long line that will overflow the width of the page
* Category a very very very long line that will overflow the width of the page
* Category a long line that has many words
* Category a very very very long line that will overflow the width of the page
* Category 
* Category 
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
* This is an `inline code`
* [link](https://www.mozilla.org)

---

###Images
.halfwidth[![remote cat](http://7-themes.com/data_images/out/66/6997052-funny-cat.jpg)]
.halfwidth[![local cat](static/pic/doge.jpeg)]
.footnote[photocredit:unknown]

---

###Side by side
<div class="column-2">
  <h4>Pros</h4>
  <ul>
    <li>Fast</li>
    <li>Fast</li>
    <li>Fast</li>
    <li>Efficient</li>
    <li>Easy to maintain</li>
  </ul>
</div>

<div class="column-2">
<h4>Cons</h4>
  <ul>
    <li>Fast</li>
    <li>Fast</li>
    <li>Fast</li>
    <li>Efficient</li>
    <li>Easy to maintain</li>
  </ul>
</div>

---

###Float right img
.float-right-half[![local cat](static/pic/doge.jpeg)]
#### Doge
* Fun
* Cute
* Kind
* Too many thing to be put in a single line

---
### Tables



| Title | From   | To        |
|-------|--------|-----------|
| Bus   | Taipei | Taoyuan   |
| ANA   | Taipei | Tokyo     |
| CX    | Taipei | Hong Kong |


---

class:center
### Images
![tall](https://placehold.it/100x400)
![wide](https://placehold.it/350x100)

---

###Embed Video
<iframe width="100%" height="500px" src="https://www.youtube.com/embed/9VChusdIqU4" frameborder="0" allowfullscreen></iframe>
---
background-image: url('static/pic/dino-wallpaper.png')
class: bottom, right

# Mozilla Rocks
.footnote[photo credit: unknown]

???
Scale to fit
---
background-image: url('static/pic/dino-wallpaper-vert.png')
class: bottom, right

#Mozilla Rocks
.footnote[photo credit: unknown]

???
Scale to fit
---
background-image: url('static/pic/dino-wallpaper.png')
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
