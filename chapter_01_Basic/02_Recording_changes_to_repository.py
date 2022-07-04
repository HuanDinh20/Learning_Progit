"""
Remember that each file in your working directory can be in one of two states: tracked or
untracked. Tracked files are files that were in the last snapshot, as well as any newly staged files;
they can be unmodified, modified, or staged. In short, tracked files are files that Git knows about.
Untracked files are everything else — any files in your working directory that were not in your last
snapshot and are not in your staging area. When you first clone a repository, all of your files will be
tracked and unmodified because Git just checked them out and you haven’t edited anything


********************* Checking the Status of Your File *****************************
git status

************** Tracking New Files
git add <directory to the files>

"""
# change some thing like this
print('hello world')
"""
and status like: 
1. You canChanges to be committed:
2. Changes not staged for commit: — which
means that a file that is tracked has been modified in the working directory but not yet staged.
To stage it, you run the git add command. 

********** Short Status
git status -s

********** Ignoring Files
Often, you’ll have a class of files that you don’t want Git to automatically add or even show you as
being untracked.
In such cases, you can create a file listing patterns to match them
named .gitignore.

***** Viewing the Staged and Unstaged changes
If the git status command is too vague for you — you want to know exactly what you changed, not
just which files were changed — you can use the git diff command.
    git diff
    git diff --staged
It’s important to note that git diff by itself doesn’t show all changes made since your last
commit — only changes that are still unstaged.

************** Committing Your Changes
git commit

************* Skipping the Staging Area
Although it can be amazingly useful for crafting commits exactly how you want them, the staging
area is sometimes a bit more complex than you need in your workflow.
git commit -a -m "messages"
skip the git add part

************** Removing files
git rm <directory where want to delete>
git rm --cached :  o keep the file in your working tree but remove it from
your staging area

****** Moving files
Unlike many other VCSs, Git doesn’t explicitly track file movement. If you rename a file in Git, no
metadata is stored in Git that tells it you renamed the file. However, Git is pretty smart about
figuring that out after the fact — we’ll deal with detecting file movement a bit later

git mv file_from file_to
"""