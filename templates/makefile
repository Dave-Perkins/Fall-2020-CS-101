%.mk: %.clean %.pdf %.tex
	@echo -n

%.pdf: %.tex
	TEXINPUTS=$$TEXINPUTS:../config latexmk -xelatex -pvc -f $<

%.clean:
	/bin/rm -f $*.pdf $*.aux $*.fdb_latexmk $*.fls $*.log $*.xdv

clean:
	/bin/rm -f *.aux *.fdb_latexmk *.fls *.log *.xdv *~
