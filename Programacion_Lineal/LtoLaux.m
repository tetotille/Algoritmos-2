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

function [N,B,A,b,c,v] = LtoLaux (N,B,A,b,c,v)
c=[-1;c];
A = [-1*ones(length(A),1),A];
N = [0;N]

return
endfunction
