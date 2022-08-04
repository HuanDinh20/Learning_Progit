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

"""