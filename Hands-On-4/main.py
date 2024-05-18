from __class__.DiscreteMaths import DiscreteMaths
from __data__.data import dataset

dm = DiscreteMaths()

sample = [ 161, 61, '' ]
dataset.append( sample )

x, y, z = dm.get_XYZ( dataset )

x_standardized = dm.standardization( x )
y_standardized = dm.standardization( y )


distances = dm.euclidean_distance( x_standardized, y_standardized )
knn = dm.knn( distances, 3 )

neighbors = dm.search_neighbors( dataset, knn )

print( '\n{}\n'.format( dataset ) )

print( distances )
print( '\n{}\n'.format( knn ) )

print( neighbors )