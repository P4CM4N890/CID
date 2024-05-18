from typing import List

class DiscreteMaths:

    def get_XYZ( self, data: List[ any ] ):
        x = [ item[0] for item in data ]
        y = [ item[1] for item in data ]
        z = [ item[2] for item in data ]

        return x, y, z

    def square_root( self, number: float ):
        return number ** 0.5
    
    def mean( self, data: List[ float ] ):
        return sum( data ) / len( data )
    
    def exponentiation( self, number: float, exponent: int ):
        return number ** exponent
    
    def variance( self, data: List[ float ] ):
        mean        = self.mean( data )
        variance    = sum( self.exponentiation(( x - mean ), 2 ) for x in data ) / len( data )

        return variance
    
    def standard_deviation( self, data: List[ float ] ):
        variance    = self.variance( data )
        deviation   = self.square_root( variance )

        return deviation

    def standardization( self, data: List[ float ] ):
        standardization = []
        mean            = self.mean( data )
        deviation       = self.standard_deviation( data )

        for x in data:
            standardization.append( ( x - mean ) / deviation )

        return standardization
    
    def euclidean_distance( self, x: List[ float ], y: List[ float ] ):
        n           = len( x ) - 1      # Subtract -1 to not count the sample dataset
        distances   = []

        for i in range( n ):
            x_distance = self.exponentiation( x[-1] - x[i], 2 )
            y_distance = self.exponentiation( y[-1] - y[i], 2 )
            distance = self.square_root( x_distance + y_distance )

            distances.append( distance )

        return distances
      
    def index_data( self, data: List[ any ] ):
        indexes = [ ( dist, i ) for i, dist in enumerate( data ) ]
        return indexes
    
    def knn( self, distances: List[ float ], k: int ):
        distances_with_id = self.index_data( distances )
        ordered_distances = sorted( distances_with_id )
        neighbors = []
        
        for i in range( k ):
            neighbors.append( ordered_distances[i][1] )

        return neighbors
    
    def search_neighbors( self, data: List[ any ], knn: List[ int ] ):
        neighbors = []
        n = len( data )

        for index in knn:
            for i in range( n ):
                if( i == index ): neighbors.append( data[i] )

        return neighbors