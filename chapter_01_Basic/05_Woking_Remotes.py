"""
Remote repositories can be on your local machine.
It is entirely possible that you can be working with a “remote” repository that is, in
fact, on the same host you are. The word “remote” does not necessarily imply that
the repository is somewhere else on the network or Internet, only that it is
elsewhere. Working with such a remote repository would still involve all the
standard pushing, pulling and fetching operations as with any other remote.
***** Showing Your Remotes
git remote
To see which remote servers you have configured, you can run the git remote command.
If you’ve cloned your repository, you should at
least see origin — that is the default name Git gives to the server you cloned from
---- clone something
git remote -v
to see where fetch and where push

***************Adding Remote Repositories
To add a new remote Git
repository as a shortname you can reference easily, run git remote add <shortname> <url>
 use the string pb on the command line in lieu of the whole URL
git remove add pb <https.........>
. For example, if you
want to fetch all the information that Paul has but that you don’t yet have in your repository, you
can run git fetch pb
Paul’s master branch is now accessible locally as pb/master — you can merge it into one of your
branches, or you can check out a local branch at that point if you want to inspect it.

**************** Fetching and Pulling from Your Remotes
git fetch <remote>
The command goes out to that remote project and pulls down all the data from that remote project
that you don’t have yet. After you do this, you should have references to all the branches from that
remote, which you can merge in or inspect at any time

If you clone a repository, the command automatically adds that remote repository under the name
“origin”. So, git fetch origin fetches any new work that has been pushed to that server since you
cloned (or last fetched from) it. It’s important to note that the git fetch command only downloads
the data to your local repository —

, you can use the git pull command to automatically fetch and then merge that
remote branch into your current branch.

From git version 2.27 onward, git pull will give a warning if the pull.rebase
variable is not set. Git will keep warning you until you set the variable.
If you want the default behavior of git (fast-forward if possible, else create a merge
commit): git config --global pull.rebase "false"
If you want to rebase when pulling: git config --global pull.rebase "true"


***** Pushing to Your Remotes When you have your project at a point that you want to share, you have to push it
upstream. The command for this is simple: git push <remote> <branch>. >. If you want to push your master branch to
your origin server (again, cloning generally sets up both of those names for you automatically), then you can run
this to push any commits you’ve done back up to the server: git push master origin This command works only if you
cloned from a server to which you have write access and if nobody has pushed in the meantime. If you and someone else
clone at the same time and they push upstream and then you push upstream, your push will rightly be rejected. You’ll
have to fetch their work first and incorporate it into yours before you’ll be allowed to push.

***** Inspecting a Remote *****
If you want to see more information about a particular remote, you can use the
git remote show <remote> command.

***** Renaming and Removing Remotes
You can run git remote rename to change a remote’s shortname. For instance, if you want to rename
pb to paul, you can do so with git remote rename:
git remote rename old-name new-name
git remote remove name

"""