-module(rpn).
-export([calculate/1]).

calculate(Expression) when is_list(Expression) -> 
  [Res] = lists:foldl(fun calculate/2, [], string:tokens(Expression, " ")),
  Res.

calculate("+", [N1,N2|S]) -> [N2+N1|S];
calculate("-", [N1,N2|S]) -> [N2-N1|S];
calculate("*", [N1,N2|S]) -> [N2*N1|S];
calculate("/", [N1,N2|S]) -> [N2/N1|S];
calculate("^", [N1,N2|S]) -> [math:pow(N1,N2)|S];
calculate(X, Stack)       -> [read(X)|Stack].

read(N) ->
  case string:to_float(N) of 
    {error, no_float} -> list_to_integer(N);
    {F, _} -> F
  end.
