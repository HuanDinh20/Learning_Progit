"""
Like most VCSs, Git has the ability to tag specific points in a repository’s history as being important.
Typically, people use this functionality to mark release points

*********** Listing Your Tags ********
Listing the existing tags in Git is straightforward. Just type git tag (with optional -l or --list)
git tag -l
git tag -l "version-0.5*"
If you want just the entire list of tags, running the command git tag implicitly
assumes you want a listing and provides one; the use of -l or --list in this case is
optional.
If, however, you’re supplying a wildcard pattern to match tag names, the use of -l
or --list is mandatory

***********************************************************************************************************
**************************** Creating Tags *****************************************

Git supports two types of tags: lightweight and annotated
1.  A lightweight tag is very much like a branch that doesn’t change — it’s just a pointer to a specific
commit.
2. Annotated tags, however, are stored as full objects in the Git database. e. They’re checksummed;
contain the tagger name, email, and date; have a tagging message; and can be signed and verified
with GNU Privacy Guard (GPG).

note: It’s generally recommended that you create annotated tags so you
can have all this information; but if you want a temporary tag or for some reason don’t want to
keep the other information, lightweight tags are available too.

***** Annotated Tags
very easy, for example,  you want create a tag v1.4, and tagging messages "my version 1.4":

git tag -a v1.4 -m "my version 1.4"
show the tag:
git show v1.4

***** lightweight tags
Another way to tag commits is with a lightweight tag. This is basically the commit checksum stored
in a file — no other information is kept.


******* Tagging Later

You can also tag commits after you’ve moved past them
for exmaple:
git log pretty=oneline
3838925d9845d3ad380ed58f44eeb80059a35d5d (HEAD -> master, tag: v1.1-lw, tag: v1.0) chapter 01, part 04, undoing things
59dcae6ed1a0db186b030d3734b0d9b6b7bd48de chapter 01, part 05, working with remotes
52af24c8152d157749da3aae61c39eb6b29fd4ca commit and then restore
ce65ea78af1b8b21c227cc5391da3ee9ab9f6b3d commit and then restore
02c694d13711948a61788047e4f0b76ce008a55e commit and then unmofying
d92ae16dc4d0e006e91b4fab2ac0657926c3aa2e add this and then undo
a2fcf15bf75547bb5a0ce8a5aa16e9e7b56b40bc chapter 01, part 03, Viewing commit  History
4970ede1987be1940c2cfa349f600d693b400e7d chapter 01, part 03, Viewing commit  History
cd8a69b4d247fd19f477d7958b773203be867ef7 chapter 01,  part 2 ----- done
b90a9ce2bc433b8c105766a6511942171e473acc this file if for moving purpose
214c0425e367f2354a42c4d7cbb214d6a2515009 ignore this shit
4a716761d492286d23fac61cdc758ee76e0bb03b ignore this shit
bb028f6a6f8f1f6552022388b2aa1e01badc8610 hello word
ae9ed67d7613cf3309719e762fd0827be5c08a77 getting_git_repository.py

Now, suppose you forgot to tag the project at v1.2, which was at the "hello word" commit. You
can add it after the fact. To tag that commit, you specify the commit checksum (or part of it) at the
end of the command:

git tag -a v0.1 bb028f6a6f8f

************* Sharing Tags
By default, the git push command doesn’t transfer tags to remote servers. You will have to explicitly
push tags to a shared server after you have created them.
git push origin <tagname>
If you have a lot of tags that you want to push up at once, you can also use the --tags option to the
git push command. This will transfer all of your tags to the remote server that are not already
there.
git push origin --tags

************ Deleting tags
To delete a tag on your local repository, you can use git tag -d <tagname>
git tag -d v0.1

************ Checking out Tags
If you want to view the versions of files a tag is pointing to, you can do a git checkout of that tag,
although this puts your repository in “detached HEAD” state, which has some ill side effects:
git checkout v1.0:
In “detached HEAD” state, if you make changes and then create a commit, the tag will stay the same,
but your new commit won’t belong to any branch and will be unreachable, except by the exact
commit hash.
 Thus, if you need to make changes — say you’re fixing a bug on an older version, for
instance — you will generally want to create a branch
git checkout -b version2 v2.0.0

Switched to a new branch 'version2'
If you do this and make a commit, your version2 branch will be slightly different than your v2.0.0
tag since it will move forward with your new changes, so do be careful.

"""