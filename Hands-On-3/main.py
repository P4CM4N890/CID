from __class__.SLR import SLR
from __class__.DataSet import DataSet 
from __class__.DiscreteMaths import DiscreteMaths
from __class__.PrintInfo import PrintInfo as pinf
from __data__.data import dataSet, sample

def main():
#| Data initialize
    data    = DataSet( dataSet )
    dm      = DiscreteMaths()

    x, y    = data.get_XY()
    n       = data.get_n()

#| Summations
    sum_X = dm.sum( x )
    sum_Y = dm.sum( y )

    sum_X2 = dm.sum_X_n( x, 2 )
    sum_X3 = dm.sum_X_n( x, 3 )
    sum_X4 = dm.sum_X_n( x, 4 )
    sum_X5 = dm.sum_X_n( x, 5 )
    sum_X6 = dm.sum_X_n( x, 6 )

    sum_XY  = dm.sum_XY( n, x, y )
    sum_X2Y = dm.sum_XnY( n, x, y, 2 )
    sum_X3Y = dm.sum_XnY( n, x, y, 3 ) 

#| Simple Linear Regression
    slr = SLR( n, sum_XY, sum_X2, sum_X, sum_Y )

#| Quadratic Regression
    values_quadratic    = dm.array( sum_X, sum_Y, sum_X2, sum_X3, sum_X4, sum_XY, sum_X2Y  )
    rx, ry, rz          = dm.cramer_quadratic( values_quadratic, n )

    quadratic_regression = slr.regression_quadratic( x, rx, ry, rz )

#| Cubic Regression
    values_cubic    = dm.array( sum_X, sum_Y, sum_X2, sum_X3, sum_X4, sum_X5, sum_X6, sum_XY, sum_X2Y, sum_X3Y )
    a, b, c, d      = dm.gauss_cubic( values_cubic, n )

    cubic_regression = slr.regression_cubic( x, a, b, c, d )

#| Averages and Deviations
    average_Y   = dm.average( y )
    deviation_Y = dm.deviation( y, average_Y )

    sum_deviation_Y_Square = dm.sum_X_n( deviation_Y, 2 )

#| Coefficient of Determination
    #* Linear Regression
    estimate    = slr.regression( x )
    sce         = dm.sce( y, estimate, n )

    r_squared = slr.r_squared( sce, sum_deviation_Y_Square )

    #* Quadratic Regression
    num_quadratic       = dm.sum_X_n( dm.deviation( quadratic_regression, average_Y ), 2 )    
    r_squared_quadratic = num_quadratic / sum_deviation_Y_Square

    #* Cubic Regression
    num_cubic       = dm.sum_X_n( dm.deviation( cubic_regression, average_Y ), 2 )
    r_squared_cubic = num_cubic / sum_deviation_Y_Square

#| Coefficient of Correlation
    #* Linear Regression
    r = slr.r( r_squared )

    r_quadratic = slr.r( r_squared_quadratic )
    r_cubic     = slr.r( r_squared_cubic )

#? Predicts
    predict     = slr.regression( sample )
    predict2    = slr.regression_quadratic( sample, rx, ry, rz )
    predict3    = slr.regression_cubic( sample, a, b, c, d )

#| Prints
    print()
    pinf.barra()
    slr.print_regression()
    slr.print_r( r )
    slr.print_r_squared( r_squared )

    pinf.barra()

    slr.print_quadratic_regression( rx, ry, rz )
    slr.print_r( r_quadratic )
    slr.print_r_squared( r_squared_quadratic )

    pinf.barra()

    slr.print_cubic_regression( a, b, c, d )
    slr.print_r( r_cubic )
    slr.print_r_squared( r_squared_cubic )

    pinf.barra()

#? Print predicts
    
    pinf.print_data( sample )
    pinf.barra()
    pinf.print_predict( predict )
    pinf.barra()
    pinf.print_predict( predict2 )
    pinf.barra()
    pinf.print_predict( predict3 )

    #! TEST
    # print( cubic_regression )

if __name__ == '__main__':
    main()