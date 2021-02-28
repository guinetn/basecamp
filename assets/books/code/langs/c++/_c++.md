# C++

download.page(code/langs/c/c_libs/dll.md)
::::
download.slideshow(assets/books/code/langs/c++/c++_compilers.md)
::::
download.slideshow(assets/books/code/langs/c++/c++01.md)
::::
download.page(code/langs/c++/c++_98.md)
download.page(code/langs/c++/c++_11.md)
download.page(code/langs/c++/c++_14.md)
download.page(code/langs/c++/c++_17.md)
download.page(code/langs/c++/c++_20.md)
::::


### Boost

Portable C++ source libraries:
JSON, LEAF, PFR. Updated Libraries: Asio, Atomic, Beast, Container, Endian, Filesystem, GIL, Histogram, Interprocess, Intrusive, Log, Move, Mp11, Optional, Outcome, Polygon, Preprocessor, Rational, Signal2, System, uBLAS, VMD, Wave...

https://www.boost.org/
```c++
#include <boost/lambda/lambda.hpp>
#include <iostream>
#include <iterator>
#include <algorithm>

int main()
{
    using namespace boost::lambda;
    typedef std::istream_iterator<int> in;

    std::for_each(
        in(std::cin), in(), std::cout << (_1 * 3) << " " );
}
```
## More

- https://docs.microsoft.com/fr-fr/c++/build/walkthrough-creating-and-using-a-static-library-cpp?view=msvc-160
- https://www.codeproject.com/Articles/5278932/Synchronization-with-Visual-Cplusplus-and-the-Wind