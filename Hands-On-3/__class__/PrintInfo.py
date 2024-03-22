
class PrintInfo:

    def barra():
        print( '-' * 40 )

    def print_predict( data = [] ):
        for i in data:
            print( 'ŷ = {}'.format( i ) )

    def print_data( data ):
        print( 'x = {}\n'.format( data ) )
