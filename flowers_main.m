function [resultado] = flowers_main(a,b,k)
  resultado = 0;
  for i = a:b
    resultado = resultado + flowers(k,i);
  endfor
end