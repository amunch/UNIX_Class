all: report.pdf

report.pdf: report.tex ethnicity.png gender.png
	pdflatex report.tex
	pdflatex report.tex

ethnicity.png: ethnicity.plt ethnicity.tsv 
	gnuplot ethnicity.plt

gender.png: gender.plt gender.tsv
	gnuplot gender.plt

ethnicity.tsv: 
	ethnicity_analyze.sh > ethnicity.tsv

gender.tsv:
	gender_analyze.sh > gender.tsv

clean:
	rm *.tsv *.png *.aux *.log *.out *.pdf
