# Cal definir:
# - narr : nombre d'arrels
# - farr : fitxer amb la llista d'arrels i colors (entre cometes)
# - fout : fitxer de sortida (entre cometes)
# - xmn : extrem esquerre de la finestra inicial
# - xmx : extrem dret de la finestra inicial
# - nx : nombre de píxels horitzontals menys un 
# - ymn : extrem inferior de la finestra inicial
# - ymx : extrem superior de la finestra inicial
# - ny : nombre de píxels verticals menys un
# - tolcnv : tolerància per la convergència de Newton
# - maxit : nombre màxim d'iterats de Newton

epsx=(xmx-xmn)/20.
epsy=(ymx-ymn)/20.
set xrange [xmn-epsx:xmx+epsx]
set yrange [ymn-epsy:ymx+epsy]
set size ratio -1
unset key

cmd='./dibfr '\
   .sprintf("%d",narr).\
   '=narr '\
   .sprintf("%.16g",xmn).\
   '=xmn '\
   .sprintf("%.16g",xmx).\
   '=xmx '\
   .sprintf("%d",nx).\
   '=nx '\
   .sprintf("%.16g",ymn).\
   '=ymn '\
   .sprintf("%.16g",ymx).\
   '=ymx '\
   .sprintf("%d",ny).\
   '=ny '\
   .sprintf("%.16g",tolcnv).\
   '=tolcnv '\
   .sprintf("%d",maxit).\
   '=maxit < '\
   .farr.\
   ' > '\
   .fout

system(cmd)

plot fout w rgbimage
bind z "load 'recalczoom.gnu'"

