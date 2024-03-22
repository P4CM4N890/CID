import math

class SLR:

    def __init__( self, n = int, sum_XY = float, sum_X_Squared = float,  sum_X = float, sum_Y = float ):
        self.n = n
        self.sum_X = sum_X
        self.sum_Y = sum_Y
        self.sum_XY = sum_XY
        self.sum_X_Squared = sum_X_Squared
        self.beta1 = 0
        self.beta0 = 0

    def beta_1( self ):
        num = ( self.n * self.sum_XY ) - ( self.sum_X * self.sum_Y )
        den = ( self.n * self.sum_X_Squared ) - ( self.sum_X * self.sum_X )

        self.beta1 = num / den
        return self.beta1

    def beta_0( self ):
        num = self.sum_Y - ( self.beta1 * self.sum_X )
        den = self.n

        self.beta0 = num / den
        return self.beta0
    
    def regression( self, values ):
        self.beta_1()
        self.beta_0()
        result = [ self.beta0 + ( self.beta1 * v ) for v in values ]
        
        return result
    
    def regression_quadratic( self, x = [], a = float, b = float, c = float ):
        result = [(( a * ( i ** 2 )) + ( b * i ) + c ) for i in x ]
        return result
    
    def regression_cubic( self, x = [], a = float, b = float, c = float, d = float ):
        result = [(( a * ( i ** 3 )) + ( b * ( i ** 2 ) ) + ( c * i ) + d ) for i in x ]
        return result

    def r( self, r_squared = float ):
        #| that measures the strength and direction on the linear relationship
        #| between two variables. The range is from -1 to +1
        result = math.sqrt( r_squared )
        return result

    def r_squared( self, sce = float, stc = float ):
        #| that measures the proportion of the variation in the dependent variable
        #| that is explained by the indenpendent variables
        #| The range is from 0 to 1 ( 0% - 100% )
        scr = stc - sce
        
        return scr / stc
    
    def print_r( self, value = float ):
        print( 'Coeficiente de Correlación      = {}\n'.format( value ) )
    
    def print_r_squared( self, value = float ):
        print( 'Coeficiente de Determinación    = {}\n'.format( value ) )

    def print_regression( self ):
        print( 'Ecuación de regresión lineal\n' )
        print( 'ŷ = {} + {} * Xi\n'.format( self.beta0, self.beta1 ) )

    def print_quadratic_regression( self, *values ):
        print( 'Ecuación de regresión cuadrática\n' )
        print( 'ŷ = {} x2 + {} x + {}\n'.format( values[0], values[1], values[2] ) )

    def print_cubic_regression( self, *values ):
        print( 'Ecuación de regresión cúbica\n' )
        print( 'ŷ = {} x3 + {} x2 + {} x + {}\n'.format( values[0], values[1], values[2], values[3] ) )
        