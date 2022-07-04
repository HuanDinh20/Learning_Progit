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


"""