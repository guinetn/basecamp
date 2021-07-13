# Erlang

https://www.erlang.org/

Designed specifically for running distributed systems. It’s fault tolerant, and built for ‘hot swapping’ (what youdo if your trading server fails and need the backup working in seconds)

Elixir
A new language
Runs on top of Erlang
Designed to handle the large volumes of data that modern finance generates.

a functional language designed for concurrency and high availability. 
Erlang is popular in applications where high performance and scalability is critical. 
Popular use cases include image and signal processing or analysis of large amounts of data.

https://www.erlang.org/

2> (42 + 77) * 66 / 3.
tut.erl
	-module(tut).
	-export([double/1]).

	double(X) ->
	    2 * X.

3> c(tut).     		  compil	     
4> tut:double(10).    run the program:
20



