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
        self.r_ = 0
        self.r_squared_ = 0

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
    
    def regression( self, value ):
        self.beta_1()
        self.beta_0()
        result = [ self.beta0 + ( self.beta1 * v ) for v in value ]
        
        return result
    
    def print_regression( self ):
        print( 'Ecuación de regresión lineal\n' )
        print( 'ŷ = {} + {} * Xi'.format( self.beta0, self.beta1 ) )

    def r( self, sum_desv_XY = float, sum_desv_X_Squared = float, sum_desv_Y_Squared = float ):
        #| that measures the strength and direction on the linear relationship
        #| between two variables. The range is from -1 to +1
        num = sum_desv_XY
        den = math.sqrt( sum_desv_X_Squared ) * math.sqrt( sum_desv_Y_Squared )

        self.r_ = num / den
        return self.r_

    def r_squared( self, sce = float, stc = float ):
        #| that measures the proportion of the variation in the dependent variable
        #| that is explained by the indenpendent variables
        #| The range is from 0 to 1 ( 0% - 100% )
        scr = stc - sce
        
        self.r_squared_ = scr / stc
        return self.r_squared_
    
    def print_r( self ):
        print( 'Coeficiente de Correlación\n' )
        print( 'r = {}'.format( self.r_ ) )
    
    def print_r_squared( self ):
        print( 'Coeficiente de Determinación\n' )
        print( 'r2 = {}'.format( self.r_squared_ ) )