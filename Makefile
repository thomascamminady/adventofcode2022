# use "run" as default
.DEFAULT_GOAL := run


run:
	poetry run python adventofcode/$(shell date +%d).py

git:
	git add .
	git commit -m "Day $(shell date +%d)"
	git commit -m "Day $(shell date +%d)"
	git push