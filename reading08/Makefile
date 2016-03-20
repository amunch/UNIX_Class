all: reading08.pdf

reading08.pdf: results.png
	pdflatex reading08.tex
	pdflatex reading08.tex

results.png:
	./experiment.sh > results.dat
	gnuplot histogram.plt

clean:
	rm -f reading08.pdf results.png
