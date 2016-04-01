set terminal png
set output 'ethnicity.png'
set xrange [2012:2019]
set yrange [0:95]
set grid
set xtics 2012,1,2019
plot 'ethnicity.tsv' using 1:2 title "Caucasian" w lines, 'ethnicity.tsv' using 1:3 title "Oriental" w lines, 'ethnicity.tsv' using 1:4 title "Hispanic" w lines, 'ethnicity.tsv' using 1:5 title "African American" w lines, 'ethnicity.tsv' using 1:6 title "Native American" w lines, 'ethnicity.tsv' using 1:7 title "Mulitple Selection" w lines, 'ethnicity.tsv' using 1:8 title "Undeclared" w lines
