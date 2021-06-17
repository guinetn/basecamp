## git revert (safe)

	  _____  
	 /     \ 
	/       ↓  
o---x---o---N---→ reverting
		↓
		this will be 'undoes' by the creation of a new commt (N)

git checkout hotfix
git revert commit       Create new commit that undoes all of the changes made in `commit`, then apply it to the current branch.
git revert HEAD~2

Reverting undoes a commit by creating a new commit. 
This is a safe way to undo changes, as it has no chance of re-writing the commit history.

Undoes a committed snapshot (do not delete it) safely
Generate a new commit that undoes all of the changes introduced in `commit`, then apply it to the current branch.
It doesn’t change the project history

To remove a bug introduced by a single commit instead of manually fixing it and committing a new snapshot
Able to target an individual commit at an arbitrary point in the history, whereas git reset can only work backwards from the current commit

git revert `commit` 	Undo an old commit on the current branch (without deleting it, ie not modifying history)
						GENERATE A NEW COMMIT that undoes all of the changes introduced in `commit`
						Then apply it to the current branch
						it does not “revert” back to the previous state of a project by removing all subsequent commits

	git commit -m "Make some changes that will be undone"
	git revert HEAD    # Revert the commit we just created

	git revert HEAD
		revert the last commit (create new one)	

	# Edit some tracked files
	# Commit a snapshot
	git commit -m "Make some changes that will be undone"
	# Revert the commit we just created
	git revert HEAD


git revert `commit`    	Create new commit that undoes all of the changes made in `commit`, then apply it to the current branch.

