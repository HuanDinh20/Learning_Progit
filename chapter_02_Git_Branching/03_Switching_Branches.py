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

Because a branch in Git is actually a simple file that contains the 40 character SHA-1 checksum of
the commit it points to, branches are cheap to create and destroy. Creating a new branch is as quick
and simple as writing 41 bytes to a file (40 characters and a newline).

It’s typical to create a new branch and want to switch to that new branch at the
same time — this can be done in one operation with
git checkout -b <newbranchname>.
From Git version 2.23 onwards you can use git switch instead of git checkout to
 Switch to an existing branch: git switch testing-branch.
 Create a new branch and switch to it: git switch -c new-branch. The -c flag
stands for create, you can also use the full flag: --create
Return to your previously checked out branch: git switch -
"""