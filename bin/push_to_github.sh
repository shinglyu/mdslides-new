script_dir=${0%/*}/..
ghpages_dir=$script_dir/my_presentations
# github link domain
ghpages_domain="https://shinglyu.github.io/my_presentations/" # Read this from .git?

if [ $# -eq 0 ]
  then 
    echo "Usage: push_to_github.sh <filename>"
    exit 1
fi
# Clone or update git repo
pushd $ghpages_dir
git pull

# git checout master
git checkout master
# copy the single html to my_presentations folder
popd 
cp $1 $ghpages_dir
# check if link exist in index.html
pushd $ghpages_dir
if $(grep -q "$ghpages_domain$1" index.html)
then
  echo "Slide already exist, don't update the index link"
else
  echo "<a href=\"$ghpages_domain$1\">$1</a><br>" >> index.html
fi
# append the link to index.html
# git add
git add $1
git add index.html
# git commit
git commit -m "Added $1"

# git checkout gh-pages
git checkout gh-pages
# git merge master
git merge master
# git push master
git push 
# git push gh-pages
# echo the link
echo "You presentation is pushed to $ghpages_domain$1"
