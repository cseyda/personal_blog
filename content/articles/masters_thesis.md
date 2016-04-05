Title: My master's thesis
Date: 2010-12-03 10:20
Category: Python
Tags: pelican, publishing
Slug: master-thesis
Summary: Short version for index and feeds

# Comparison of graph-based and vector-space geographical topic detection

## Abstract
The popularity of social networks like Facebook and Twitter, together with media sharing plattforms like Flickr and the ubiquity of modern smart phones and cameras with GPS sensors have lead to a vast amount of data with documents containing locations, text, and even more information. this data can be leveraged to optimise search results, perform targeted advertisement and even help people and authorities in case of nature catastrophes, for example as early warning systems. Geographic topic detection aims at providing meaningful topics for specific regions. One way to perform this task is to use a clustering algorithm with an appropriate distance function.

This thesis compares two such distance functions by performing DBSCAN and comparing the fount topics. A naive vector-based approach based on linear composition of a jaccard distance on a text vector, and a euclidean distance based on the location vector. The second approach uses a graph build with a Delaunay triangulation based on the location data, and additional nodes and edges based on the text data. A random walk method is then performed to determine the distances between points.

Another important part is the quantitative evaluation of the found geographic topics with four standard cluster quality measures, and how well the scores from these measures resemble die actual quality of the topics. Used and evaluated datasets contain up to one million points, which is very much compared to other works.

Results show that both distance function are able to perform basic geographic topic discovery, but the graph-based approach usually outperforms the vector-based approach. Cluster quality measures, especially Silhouette width, give a general indication of the goodness of the performed topic discovery, but are unfortunately not suitable for direct comparison with the used base distances.
