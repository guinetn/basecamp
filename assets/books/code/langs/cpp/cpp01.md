# Basic C++ program

```html
#include <iostream>
void main()
{
    std::cout << "Hello World";    
}

g++ cpp01.cpp && ./a.out   
g++ cpp01.cpp -o cpp01.exe && ./cpp01.exe  
```

::::

# Define a container element 

```cpp
#include <iostream>
std::string name;
int main() {
std::cout << i << std::endl;
return 0;
}

#include <iostream>
using namespace std;
int main() {
cout <<  "Hello World" << endl;
return 0;
}

```

::::

# noname

```js

```

::::

C++11 INHERITANCE

 ```c++
class GameObject
{
    public:
        virtual ~GameObject() {}
        virtual void update() {}
        virtual void draw() {}
        virtual void collide(Object objects[]) {}
};

class Visible : public GameObject
{
    public:
        virtual void draw() override { /* draw model at position of this object */ };
    private:
        Model* model;
};

class Solid : public GameObject
{
    public:
        virtual void collide(GameObject objects[]) override { /* check and react to collisions with objects */ };
};

class Movable : public GameObject
{
    public:
        virtual void update() override { /* update position */ };
};
 ```

// "dynamic memory" 
int main(){
    int * myptr = new int;
    * myptr = 1;
    printf("myptr[0] is %i\n",*myptr);
    return 0;
}
 
 
// C89 compatible file
int main()
{
    int x[] = {0, 2};
    return sizeof(x);
}

// C99 compatible file
int main()
{
    int x[] = {[1]=2};
    return sizeof(x);
}

// C++1998,2003 compatible file
class X{};
int main()
{
    X x;
    return sizeof(x);
}

// C++11
#include <vector>
enum class Color : int{red,green,blue}; // scoped enum
int main()
{
    std::vector<int> a {1,2,3}; // bracket initialization
    return 0;
}