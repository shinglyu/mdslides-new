MDSlides
==================
# Installation

Run `install.sh` or

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Add `bin/` to your `PATH`

# Usage
Create a `slides.md` file, and put your pictures or static file in `pic/` dir

* Start dev server

```
mdslides
```

* Export as a single HTML file

```
mdslides publish
```

# Raw Usage

```
source venv/bin/activate
python application.py <path/to/slides.md>
```

Then open http://localhost:5000


# Credit: 
async_flask by Shane Lynn 15/07/2014
