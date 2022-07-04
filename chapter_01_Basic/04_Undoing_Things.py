"""
************ Undoing Thing ************
At any stage, you may want to undo something. Here, we’ll review a few basic tools for undoing
changes that you’ve made. Be careful, because you can’t always undo some of these undos. This is
one of the few areas in Git where you may lose some work if you do it wrong

git commit --amend

**** Note
1. Only amend commits that are still local and have not been pushed somewhere.
2. It’s important to understand that when you’re amending your last commit, you’re
not so much fixing it as replacing it entirely with a new, improved commit that
pushes the old commit out of the way and puts the new commit in its place.

************ Unstaging a Staged File *********************
to unstage a staged file:
git reset HEAD <path to staged file>

*********** Unmodifying a Modified File **************
Dangerous:

git checkout -- <path to reververt file>

It’s important to understand that git checkout -- <file> is a dangerous command.
Any local changes you made to that file are gone — Git just replaced that file with
the last staged or committed version. Don’t ever use this command unless you
absolutely know that you don’t want those unsaved local changes

********* Undoing things with git restore ******************
From Git version 2.23.0 onwards, Git will use git restore instead of git
reset for many undo operations

**** Unstaging a Staged File with git restore
git restore --staged <file path to unstaged>
unadded what is add

******* Unmodifying a Modified File with git restore ******

git restore <file path>

It’s important to understand that git restore <file> is a dangerous command. Any
local changes you made to that file are gone — Git just replaced that file with the
last staged or committed version. Don’t ever use this command unless you
absolutely know that you don’t want those unsaved local changes




"""