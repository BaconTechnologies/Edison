all:

commit_master: all
	git checkout master
	git add --all
	git commit -m "testing grove button"
	git push origin master

commit_dev: all
	git checkout dev
	git add --all
	git commit -m "testing grove button"
	git push origin dev