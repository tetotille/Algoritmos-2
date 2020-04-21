function [resultado] = flowers(k,n)
  limite = floor(n/k)+1;
  valor = zeros(limite,1);
  valor(1) = 1;
  x = [0:limite];
  valor(2:limite) = 1 + n - (x(2:limite)*k);
  display(valor)
  resultado = sum(valor);
end  