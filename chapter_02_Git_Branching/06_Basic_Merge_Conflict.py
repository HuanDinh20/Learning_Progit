"""
Occasionally, this process doesn’t go smoothly. If you changed the same part of the same file
differently in the two branches you’re merging, Git won’t be able to merge them cleanly. If your fix
for issue #53 modified the same part of a file as the hotfix branch, you’ll get a merge conflict.
take example like:

apple
red
green
blue
yellow
white
- now create 2 branches name: dev1, dev2
dev 1: change line 11, 12 to yellow and white
dev 2: change line 11, 12 to john and james


"""