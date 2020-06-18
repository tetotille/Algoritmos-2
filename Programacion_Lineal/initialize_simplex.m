## Copyright (C) 2020 Jorge Tilleria
## 
## This program is free software; you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

## Author: Jorge Tilleria <jtilleria@fiuna.edu.py>
## Created: 2020-06-17

function [N,B,A,b,c,v] = initialize_simplex (A,b,c)
#Definicion de variables
[n,m] = size(A)
N = [1:n];
B = [n+1:m+n];
v=0;

#Algoritmo
[minimo,k] = min(b); #Sea k el indice minimo de b
if b(k) >= 0
  return ([1:n],[n+1:n+m],A,b,c,0);
endif

[N,B,A,b,c,v] = LtoLaux(N,B,A,b,c,v);

#Parte del algorimo Simplex
Delta = zeros(n,1);
x = zeros(n,1);
while max(c)>0
  e = encontrarE(c,N+1);
  for i=B(1):B(end)
    if A(i,e) > 0 
      Delta(i) = b(i)/a(i,e);
    else
      Delta(i) = inf;
    endif
  endfor
  [minimo,l]=min(Delta);
  if Delta(l) == inf
    return "Unbounded";
  else
    [N,B,A,b,c,v] = Pivot(N,B,A,b,c,v,l,e);
  endif
endwhile
#### Hasta aca el codigo de Simplex ####

if x(1) == 0
  if sum(B==0)==1
    [aux,indice] = max(c)
    Pivot(N,B,A,b,c,v,indice,1)
  endif
  
    
  
  
endfunction
