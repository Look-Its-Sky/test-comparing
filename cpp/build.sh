g++ -c -pipe -O3 -fomit-frame-pointer  --std=c++17 -I ./Include/gpp/vcl mandelbrot.gpp-0.c++ -o mandelbrot.gpp-0.c++.o &&  \
g++ mandelbrot.gpp-0.c++.o -o mandelbrot.gpp-0.gpp_run -pthread
