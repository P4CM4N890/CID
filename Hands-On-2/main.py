from __class__.SLR import SLR
from __class__.DataSet import DataSet 
from __class__.DiscreteMaths import DiscreteMaths
from __class__.PrintInfo import PrintInfo as pinf
from __data__.data import dataSet, sample

def main():
#| Data initialize
    data = DataSet( dataSet )
    dm = DiscreteMaths()

    x, y = data.get_XY()
    n = data.get_n()

#| Summations
    sum_X = dm.sum( x )
    sum_Y = dm.sum( y )
    sum_XY = dm.sum_XY( n, x, y )
    sum_X_Square = dm.sum_X_Square( x )

#| Simple Linear Regression
    slr = SLR( n, sum_XY, sum_X_Square, sum_X, sum_Y )

    predict = slr.regression( sample )

#| Averages and Deviations
    average_X = dm.average( x )
    average_Y = dm.average( y )

    deviation_X = dm.deviation( x, average_X )
    deviation_Y = dm.deviation( y, average_Y )

    sum_deviation_XY = dm.sum_XY( n, deviation_X, deviation_Y )
    sum_deviation_X_Square = dm.sum_X_Square( deviation_X )
    sum_deviation_Y_Square = dm.sum_X_Square( deviation_Y )

#| Coefficient of Correlation
    slr.r( sum_deviation_XY, sum_deviation_X_Square, sum_deviation_Y_Square )

    estimate = slr.regression( x )
    sce = dm.sce( y, estimate, n )

#| Coefficient of Determination
    slr.r_squared( sce, sum_deviation_Y_Square )

#| Prints
    print()
    pinf.barra()
    slr.print_regression()
    pinf.barra()
    pinf.print_data( sample )
    pinf.print_predict( predict )
    pinf.barra()
    slr.print_r()
    pinf.barra()
    slr.print_r_squared()
    pinf.barra()
    print()

if __name__ == '__main__':
    main()