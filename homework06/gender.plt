set terminal png
set output 'gender.png'
set xrange [2012:2019]
set yrange [0:100]
set grid
set style data histogram
set style histogram cluster
set style fill solid border
set boxwidth 0.40
set xtics 2012,1,2019
plot 'gender.tsv' using ($1-0.21):2 title "Males" with boxes, 'gender.tsv' using ($1+0.21):3 title "Females" with boxes 
