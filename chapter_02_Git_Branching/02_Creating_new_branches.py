"""
What happens when you create a new branch? Well, doing so creates a new pointer for you to
move around. Let’s say you want to create a new branch called testing. You do this with the git
branch command:
 git branch testing

This creates a new pointer to the same commit you’re currently on.
How does Git know what branch you’re currently on? It keeps a special pointer called HEAD


 In Git, this is a pointer to the local branch you’re currently on. In this case,
you’re still on master. The git branch command only created a new branch — it didn’t switch to that
You can easily see this by running a simple git log command that shows you where the branch
pointers are pointing. This option is called --decorate

"""