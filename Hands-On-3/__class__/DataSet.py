class DataSet:
    def __init__( self, dataset = [] ):
        self.dataset = dataset
        self.n = len( self.dataset )

    def get_XY( self ):
        x = [ item[0] for item in self.dataset ]
        y = [ item[1] for item in self.dataset ]

        return x, y
    
    def get_n( self ):
        return self.n
