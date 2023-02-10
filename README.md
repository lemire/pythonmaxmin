# pythonmaxmin
Fast minimum-maximal filter in Python



This code implements the algorithms described in the following paper:

Daniel Lemire, [Streaming Maximum-Minimum Filter Using No More than 
Three Comparisons per Element](http://arxiv.org/abs/cs.DS/0610046). Nordic Journal of Computing, 13 (4), pages 328-339, 2006. 




The main algorithm presented in this package is used in [Apache Hive](https://github.com/apache/hive).

Suitability 
------------

The new algorithm introduced in the manuscript is most suitable for piecewise monotonic
data or when low-latency is required. Otherwise, Gil-Kimmel and van Herk
are good choices.

See also
---------
For an application in C++:
https://github.com/lemire/runningmaxmin

For an application of this idea to rolling statistics in JavaScript, see

https://github.com/shimondoodkin/efficient-rolling-stats

For an application in Go, please see 

https://github.com/notnot/movingminmax

