## Cherry Picking

ability to git cherry-pick a commit is one of the most useful skills a developer can employ when trying to isolate a software bug or fix a broken build.
The goal of a cherry-pick is to “apply the changes introduced by some existing commit.” Essentially, a cherry-pick will look at a previous commit in the repository’s history and apply the changes that were part of that earlier commit to the current working tree. The definition is seemingly straight forward, yet in practice there is a great deal of confusion over what exactly happens when someone tries to git cherry-pick a commit, or even cherry-pick from another branch. This git cherry-pick example will eliminate that confusion.

When a developer encounters a problem in the repository, the ability to git cherry-pick a commit can be extremely helpful in fixing bugs and resolving problems in GitHub, which is why understanding how the command works and the impact it will have on the current development branch is pivotal. Hopefully, with this git cherry-pick example under your belt, you will have the confidence needed to use the command to resolve problems in your own development environment.


	## cherry-pick tutorial
	$ git init 	Initialized empty Git repository in C:/ git cherry-picktutorial/.git/

		create five, alphabetically ordered .html files along with the git commands required to add each file independently to the git index and subsequently commit those files to the repository

	$ echo 'alpha' ` alpha.html
	$ git add . | git commit -m "1st commit: 1 file"

	$ echo 'beta' ` beta.html
	$ git add . | git commit -m "2nd commit: 2 files"

	$ echo 'charlie' ` charlie.html
	$ git add . | git commit -m "3rd commit: 3 files"

	$ echo 'whip it' ` devo.html
	$ git add . | git commit -m "4th commit: 4 files"

	$ echo 'Big Lebowski' ` eagles.html
	$ git add . | git commit "5th commit: 5 files"

	Delete and commit before the cherry-pick
	$ rm *.html
	$ git add . | git commit -m "all deleted: 0 files"
	To recap, five files were created, and each file created has a corresponding commit. And then all the files were deleted and a sixth commit was issued. A chronicling of this commit history can be concisely viewed in the reflog. Take special note of the hexadecimal  identifier on the third commit, which we will cherry-pick in a moment:

	/c/ git cherry-pick tutorial
	$ git reflog
	189aa32 HEAD@{0}: commit: all deleted: 0 files
	e6f1ac7 HEAD@{1}: commit: 5th commit:  5 files
	2792e62 HEAD@{2}: commit: 4th commit:  4 files
	60699ba HEAD@{3}: commit: 3rd commit:  3 files
	4ece4c7 HEAD@{4}: commit: 2nd commit:  2 files
	cc6b274 HEAD@{5}: commit: 1st commit:  1 file

	What happens when we git cherry-pick a commit?
	This is where the git cherry-pick example starts to get interesting. We need to git cherry-pick a commit, so let’s choose the third commit where the file named charlie.html was created. But before we do, ask yourself what you believe will happen after the command is issued. When we git cherry-pick a commit, will we get all of the files associated with that commit, which would mean alpha.html, beta.html and charlie.html will come back? Or will we get just one file back? Or will the attempt to git cherry-pick a commit fail since all of the files associated with the commit have been deleted from our workspace?

	$ git cherry-pick 60699ba
	[master eba7975] 3rd commit: 3 files
	1 file changed, 1 insertion(+)
	create mode 100644 charlie.html

		only one file was added to the working directory, namely charlie.html. The files that were added to the repository in prior commits were not added, which tends to be the expectation of many users.
		When you git cherry-pick a commit, only the change associated with that commit is re-applied to the working tree.
		it’s not just the working tree that is updated. When you git-cherry-pick a commit, a completely new commit is created on the branch, as the following reflog command indicates:

	/c/ git cherry-pick tutorial (master)
	$ git reflog
	eba7975 HEAD@{0}: cherry-pick: 3rd commit: 3 files
	189aa32 HEAD@{1}: commit: all deleted: 0 files
	e6f1ac7 HEAD@{2}: commit: 5th commit: 5 files
	2792e62 HEAD@{3}: commit: 4th commit: 4 files
	60699ba HEAD@{4}: commit: 3rd commit: 3 files
	4ece4c7 HEAD@{5}: commit: 2nd commit: 2 files
	cc6b274 HEAD@{6}: commit (initial): 1st commit: 1 file







Pick changes from another branch, then apply them to the current branch.
Usually happens, before branch merge.
$ git checkout $my_branch
$ git cherry-pick $git_revision
$ git cherry-pick `hash-id|ref` 

selectively choose (the most beneficial items) from what is available.
when many conflict, be able to pick out individual commits and simply merge those into the main branch.


One of the advantages of small commits is that you can be  (hard) about which ones you want to merge.
This problem particularly concerns long-lived branches, that have become out of date with the main branch resulting in too many conflicts to simply merge. This is a very common occurrence on very active open source projects.
When this occurs you want to be able to pick out individual commits and simply merge those into the main branch.
It's important to note that cherry picking only works if you keep your commits small and focused, otherwise you'll include unwanted changes. 

A number of commits in the _newbranch which has created two html files. 
In this scenario we only care about changes to one of the files but if we merged the branch then we'd merge all five commits and the unwanted changes.

git cherry-pick `hash-id|ref`
	merge individual commits
	This behaves in a similar way to merge, if no conflicts exist then the commit will be automatically merged.

In the same way the merging can result in conflicts so can cherry picking. You solve conflicts in the same way as with merging a branch either manually fixing the files or selecting theirs or ours via git checkout.
If you feel like you've made a mistake, you can stop and revert the pick using 
git cherry-pick --abort

Resolving Cherry Picking Conflict
git cherry-pick new_branch~1
This will result in a merge conflict. Resolve the conflict using git checkout and select the picked commit.
git status
git diff
git checkout --theirs list2.html

git cherry-pick --continue.
Once the conflicts have been resolved you can continue with the cherry pick
Similar to using merge, resolving a cherry-pick will result in a commit.

Complete the cherry pick by first adding the previously conflicted item and then using the --continue option.
git add list2.html
git cherry-pick --continue
At this point the default editor, in this case vim, will pop up allowing you to edit the cherry-picked commit message to include details of the conflict and how it was resolved. To save and quit vim type :wq
