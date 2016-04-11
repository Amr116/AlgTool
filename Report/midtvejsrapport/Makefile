TEX=pdflatex

afl.pdf: Midtvejsrapport.tex
	while ($(TEX) -shell-escape $^ ; \
	grep -q "Rerun to get cross" afl.log ) do true ; \
	done

clean:
	rm -f *.log *.aux *.out *.pf *.eps *.dvi *.gnuplot *.log *.table *.*~ *.aux *.toc

