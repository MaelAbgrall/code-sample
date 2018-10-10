# C++

Depending on the os there is multiple compilers (MinGW, GCC, CLang, etc)

On linux, you can use a file called makefile. make, a program that will help compiling big projects will read this file to produce an executable.

for cross platform, CMake is "recommanded" ? because it can produce different build scripts depending on your target os. Same as make, it use a file called CMakeLists.txt

common practice is to have a build folder where all your build script and binnaries will go.


```shell
mkdir build

cd build

#creating build scripts
cmake .. 

#and now calling those build scripts
make

#run program
./my_program

```

once this step has been done, you don't need to call again cmake, because the created makefile will call cmake command if there is any modification on CMakeLists.txt

[A good tutorial on cmake](https://www.johnlamp.net/cmake-tutorial-4-libraries-and-subdirectories.html)

[and another one](https://cmake.org/cmake-tutorial/)