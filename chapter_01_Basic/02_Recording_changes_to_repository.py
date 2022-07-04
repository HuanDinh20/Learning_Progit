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
To stage it, you run the git add command. g
"""