"""
Let’s go through a simple example of branching and merging with a workflow that you might use in
the real world. You’ll follow these steps:
1. Do some work on a website.
2. Create a branch for a new user story you’re working on.
3. Do some work in that branch.

At this stage, you’ll receive a call that another issue is critical and you need a hotfix. You’ll do the
following:
1. Switch to your production branch.
2. Create a branch to add the hotfix.
3. After it’s tested, merge the hotfix branch, and push to production
4. Switch back to your original user story and continue working.

************* Basic Branching ***************
First, let’s say you’re working on your project and have a couple of commits already on the master
branch.

You’ve decided that you’re going to work on issue #53 in whatever issue-tracking system your
company uses. To create a new branch and switch to it at the same time, you can run the git
checkout command with the -b switch:

    git checkout -b iss53

You work on your website and do some commits. Doing so moves the iss53 branch forward,
because you have it checked out (that is, your HEAD is pointing to it)

 The iss53 branch has moved forward with your work


    Now you get the call that there is an issue with the website, and you need to fix it immediately. With
Git, you don’t have to deploy your fix along with the iss53 changes you’ve made, and you don’t
have to put a lot of effort into reverting those changes before you can work on applying your fix to
what is in production. All you have to do is switch back to your master branch.

    However, before you do that, note that if your working directory or staging area has uncommitted
changes that conflict with the branch you’re checking out, Git won’t let you switch branches. It’s
best to have a clean working state when you switch branches.
    git checkout master
    for example: error: Your local changes to the following files would be overwritten by checkout:
        chapter_02_Git_Branching/04_Basic_Branching_Merging.py
Please commit your changes or stash them before you switch branches.
Aborting

At this point, your project working directory is exactly the way it was before you started working
on issue #53, and you can concentrate on your hotfix. This is an important point to remember:
when you switch branches, Git resets your working directory to look like it did the last time you
committed on that branch. It adds, removes, and modifies files automatically to make sure your
working copy is what the branch looked like on your last commit to it


Next, you have a hotfix to make. Let’s create a hotfix branch on which to work until it’s completed

You can run your tests, make sure the hotfix is what you want, and finally merge the hotfix branch
back into your master branch to deploy to production. You do this with the git merge command:

using:
git branch -d <name>
to delete branch

Now you can switch back to your work-in-progress branch on issue #53 and continue working on it.
"""