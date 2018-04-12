all: \
    	slides.pdf

%.pdf: %.md
	pandoc --data-dir=/home/alli/common --filter=pandoc-citeproc --from=markdown --to=beamer -o $@ $<
