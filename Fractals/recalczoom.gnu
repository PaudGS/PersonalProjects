# Cal definir:
# - narr : nombre d'arrels
# - farr : fitxer amb la llista d'arrels i colors
# - fout : fitxer de sortida
# - nx : nombre de píxels horitzontals menys un 
# - ny : nombre de píxels verticals menys un
# - tolcnv : tolerància per la convergència de Newton
# - maxit : nombre màxim d'iterats de Newton

cmd='./dibfr '\
   .sprintf("%d",narr).\
   '=narr '\
   .sprintf("%.16g",GPVAL_X_MIN).\
   '=xmn '\
   .sprintf("%.16g",GPVAL_X_MAX).\
   '=xmx '\
   .sprintf("%d",nx).\
   '=nx '\
   .sprintf("%.16g",GPVAL_Y_MIN).\
   '=ymn '\
   .sprintf("%.16g",GPVAL_Y_MAX).\
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
