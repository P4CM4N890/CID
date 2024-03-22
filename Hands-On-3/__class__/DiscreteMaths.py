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
    
    def sum_XnY( self, n = int, x = [], y = [], exponent = int ):
        # Sumatory of two arrays x * y
        total = 0
        for i in range( n ):
            total += (x[i] ** exponent ) * y[i]

        return total

    def sum_X_n( self, array = [], exponent = int ):
        total = 0
        for i in array:
            total += i ** exponent
        
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
    
    def array( self, *values ):
        return list( values )
    
    def calc_t_quadratic( self, v1 = [], v2 = [], v3 = []):
        t_plus = (
                    ( v1[0] * v2[1] * v3[2] ) + 
                    ( v2[0] * v3[1] * v1[2] ) + 
                    ( v3[0] * v1[1] * v2[2] )
                )
        t_minus = (
                    ( v1[2] * v2[1] * v3[0] ) + 
                    ( v2[2] * v3[1] * v1[0] ) + 
                    ( v3[2] * v1[1] * v2[0] )
                )

        return t_plus - t_minus
    
    def cramer_quadratic( self, values = [], n = int ):
        a = [ values[2], values[3], values[4] ]
        b = [ values[0], values[2], values[3] ]
        c = [ n, values[0], values[2] ]
        r = [ values[1], values[5], values[6] ]

        ts = self.calc_t_quadratic( a, b, c )
        ta = self.calc_t_quadratic( r, b, c )
        tb = self.calc_t_quadratic( a, r, c )
        tc = self.calc_t_quadratic( a, b, r )

        x = ta / ts
        y = tb / ts
        z = tc / ts

        return x, y, z
    
    def determinant( self, matrix = [] ):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        elif n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            det = 0
            for j in range(n):
                det += (-1) ** j * matrix[0][j] * self.determinant( self.minor( matrix, 0, j ))
            return det
        
    def minor( self, matrix, i = int, j = int ):
        return [ row[ :j ] + row[ j + 1:] for row in ( matrix[ :i ] + matrix[ i + 1: ])]
    
    def gauss_cubic( self, values=[], n=int ):
        a = [ values[3], values[4], values[5], values[6] ]
        b = [ values[2], values[3], values[4], values[5] ]
        c = [ values[0], values[2], values[3], values[4] ]
        d = [ n, values[0], values[2], values[3] ]
        r = [ values[1], values[7], values[8], values[9] ]

        matrix = [
            [ a[0], b[0], c[0], d[0] ],
            [ a[1], b[1], c[1], d[1] ],
            [ a[2], b[2], c[2], d[2] ],
            [ a[3], b[3], c[3], d[3] ]
        ]

        m = len( matrix )
        det_A = self.determinant( matrix )
        if det_A == 0:
            return "El determinante de la matriz de coeficientes es cero. El sistema no tiene solución única."

        solutions = []
        for i in range( m ):
            temp_matrix = [row[:] for row in matrix]

            for j in range( m ):
                temp_matrix[j][i] = r[j]

            solutions.append( self.determinant( temp_matrix ) / det_A)

        return solutions
