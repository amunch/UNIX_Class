reset
set term png truecolor
set output 'results.png'
set xrange [0:7]
set yrange [0:200]
set grid
set boxwidth 0.95 relative
set style fill solid 0.8 noborder
plot 'results.dat' u 1:2 w boxes lc rgb"blue" notitle
