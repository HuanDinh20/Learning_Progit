"""
To switch to an existing branch, you run the git checkout command. Let’s switch to the new testing
branch:
git checkout -branch_name

This moves HEAD to point to the testing branch

What is the significance of that? Well, let’s do another commit

This is interesting, because now your testing branch has moved forward, but your master branch
still points to the commit you were on when you ran git checkout to switch branches. Let’s switch
back to the master branch
git checkout master

That command did two things. It moved the HEAD pointer back to point to the master branch, and it
reverted the files in your working directory back to the snapshot that master points to. This also
means the changes you make from this point forward will diverge from an older version of the
project. It essentially rewinds the work you’ve done in your testing branch so you can go in a
different direction.
"""