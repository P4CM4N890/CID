class DiscreteMaths:

    def sum( self, array = [] ):
        # Sumatory of an array
        total = sum( array )

        return total

    def sum_XY( self, n = int, x = [], y = []):
        # Sumatory of two arrays x * y
        total = 0
        for i in range( n ):
            total += x[i] * y[i]

        return total

    def sum_X_Square( self, array = [] ):
        total = 0
        for i in array:
            total += i ** 2
        
        return total
    
    def average( self, array = [] ):
        sumArray = self.sum( array )
        n = len( array )

        result = sumArray / n
        return result
    
    def deviation( self, x = [], average = float ):
        array = []
        for i in x:
            array.append( i - average )

        return array
    
    def sce( self, y = [], y_ = [], n = int ):
        #| Sum of the squared error
        array = []
        for i in range( n ):
            array.append( ( y[i] - y_[i] ) ** 2 )


        sum = self.sum( array )
        return sum