## git log

Learn to dig

git log 						Viewing the commit history: author and message,
git log -3
git log -p -2 					Shows the difference introduced in each commit at level 2...
git log -p index.js   			File history  
git log --oneline
git log --since=yesterday
git log --since=2.weeks
git log --stat
git blame author name, last modified date, commit hash 
git log to look at the commit history of the overall repo.
git log | grep someFunction -C 3  (3 lines of context)
git log --pretty=format:"%h %an %ar - %s"
git log --pretty=format:"%h %s" --graph
git log --pretty=oneline
			
git log
	Viewing the entire project commit history using the default format (author and message)	
	Displays committed snapshots. It lets you list the project history, filter it, and search for specific changes. 

	git log --oneline

	git log --oneline --decorate   
		git log shows where the branch pointers (master, Head) are pointing
			a33d80 (HEAD -` master) Revert "Fix username"
			82d742a Fix username
			b3756bf Name updated
			fc2470c Name added
	
	git log --since=yesterday
	git log --since=2weeks

	git log | grep someFunction -C 3 			(-C 3 will show your matches with three lines of context).

	git log --author="John Smith" -p hello.py
	This will display a full diff of all the changes John Smith has made to the file hello.py

	git log --oneline master..some-feature
	.. for comparing branches: displays a brief overview of all the commits that are in some-feature that are not in master.

	git log --graph --oneline --decorate

	git log --pretty=format:"%h %an %ar - %s"

	git log
		Display the entire commit history using the default formatting. If the output takes up more than one screen, you can use Space to scroll and q to exit.

	git log -n `limit`
		Limit the number of commits by `limit`. For example, git log -n 3 will display only 3 commits.

	git log --oneline
		Condense each commit to a single line. This is useful for getting a high-level overview of the project history.

	git log --stat
		Along with the ordinary git log information, include which files were altered and the relative number of lines that were added or deleted from each of them.

	git log -p
		Display the patch representing each commit. This shows the full diff of each commit, which is the most detailed view you can have of your project history.

	git log --author="`pattern`"
		Search for commits by a particular author. The `pattern` argument can be a plain string or a regular expression.

	git log --grep="#1234"
		to find all the commits containing #1234

	git log --grep="`pattern`"
		Search for commits with a commit message that matches `pattern`, which can be a plain string or a regular expression.

	git log `since`..`until`
		Show only commits that occur between `since` and `until`. Both arguments can be either a commit ID, a branch name, HEAD, or any other kind of revision reference.

	git log `file`
		Only display commits that include the specified file. This is an easy way to see the history of a particular file.

		git log -p index.js 				 history of a single file

		git log --since=yesterday
		git log --since=2weeks

	git log --graph --decorate --oneline
		A few useful options to consider.
		--graph 			draw a text based graph of the commits on the left hand side of the commit messages. 
		--C--decorate 		adds the names of branches or tags of the commits that are shown
		--oneline 			shows the commit information on a single line making it easier to browse through commits at-a-glance.


	SAMPLES

		git log 					Displays committed snapshots by date DESC
		git log `file` 				Only display commits that include the specified file
		git log -n `limit` 			Limit the number of commits
		git log -p -2 				Shows commits difference, limit to only the last two entries
		git log --stat 			 	Files altered & how many lines in those files were added and removed
		git log --oneline 			Condense each commit to a single line for getting a high-level overview of the project history
		git log --pretty=oneline 	changes the log output to +/- details
							short
							full
							fuller
		git log --pretty=format:"%h - %an, %ar : %s"
		git log --pretty=format:"%h %s" --graph 		Display an ASCII graph of the branch and merge history beside the log output.
			git log --since=2.weeks
			git log --since="2008-01-15"
			git log --since="2 years 1 day 3 minutes ago"
			git log --author="John Doe"
			git log --grep ="keywords in commit msg"
			git log -Sfunction_name 					 	Takes a string and only shows the commits that introduced a change
															to the code that added or removed that string.

		git log --decorate								Shows where the branch pointers (master, Head) are pointing
														Adds the names of branches or tags
		git log --graph --decorate --oneline 			Text based graph of the commits on the left hand side of the commit messages.

			~ character is useful for making relative references to the parent of a commit.
			For example
				3157e~1 refers to the commit before 3157e
				HEAD~3 is the great-grandparent of the current commit.


		git log -limit   				Limit number of commits by limit. E.g. git log -5 will limit to 5 commits.
		git log --oneline 				Condense each commit to a single line.
		git log -p 						Display the full diff of each commit.
		git log --stat 					Include which files were altered and the relative number of lines that were added or deleted from each of them.
		git log --author=”pattern” 		Search for commits by a particular author.
		git log --grep=”pattern” 		Search for commits with a commit message that matches pattern.
		git log since..until 			Show commits that occur between since and until. Args can be a commit ID, branch name, HEAD, or any other kind of revision reference.
		git log -- file 				Only display commits that have the specified file.
		git log --graph --decorate      --graph flag draws a text based graph of commits on left side of commit msgs. --decorate adds names of branches or tags of commits shown.






## git reflog

Git keeps track of updates to the tip of branches using a mechanism called reflog. This allows you to go back to changesets even though they are not referenced by any branch or tag. After rewriting history, the reflog contains information about the old state of branches and allows you to go back to that state if necessary.

$ git reflog
189aa32 HEAD@{0}: commit: all deleted: 0 files
e6f1ac7 HEAD@{1}: commit: 5th commit:  5 files
2792e62 HEAD@{2}: commit: 4th commit:  4 files
60699ba HEAD@{3}: commit: 3rd commit:  3 files
4ece4c7 HEAD@{4}: commit: 2nd commit:  2 files
cc6b274 HEAD@{5}: commit: 1st commit:  1 file

759a70d HEAD@{25}: checkout: moving from fix to master
1a7de13 HEAD@{26}: commit: fix virus 2
6b65e3d HEAD@{27}: commit: fix virus 1
759a70d HEAD@{28}: checkout: moving from master to fix
759a70d HEAD@{29}: checkout: moving from nf to master
8fb5e8e HEAD@{30}: commit: can mul
1055dd0 HEAD@{31}: commit: can add
759a70d HEAD@{32}: checkout: moving from master to nf
759a70d HEAD@{33}: commit: 1st change
debbc2e HEAD@{34}: commit (initial): 1st commit				
