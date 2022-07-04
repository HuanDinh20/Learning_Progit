"""
After you have created several commits, or if you have cloned a repository with an existing commit
history, you’ll probably want to look back to see what has happened. The most basic and powerful
tool to do this is the git log command.

clone this git:  git clone https://github.com/schacon/simplegit-progit
and check git log
By default, with no arguments, git log lists the commits made in that repository in reverse
chronological order; that is, the most recent commits show up first. As you can see, this command
lists each commit with its SHA-1 checksum, the author’s name and email, the date written, and the
commit message.
One of the more helpful options is -p or --patch, which shows the difference (the patch output)
introduced in each commit.
git log -p

git log --stat
One of the more helpful options is -p or --patch, which shows the difference (the patch output)
introduced in each commit.

git log --pretty
This option changes the log output to formats other than
the default. short, full, fuller

************* limiting log outputs


"""