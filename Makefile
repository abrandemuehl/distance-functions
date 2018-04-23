all: \
    	slides.pdf

%.pdf: %.md
	pandoc --filter=pandoc-citeproc --from=markdown --to=beamer -o $@ $<
