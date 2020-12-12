# BKA markdown samples

**"BKA"** allow to display markdown slides.

* Simple
* Beautiful
* Easy
* Emojis :+1: :dog: Details: https://github.com/showdownjs/showdown/wiki/emojis

# Arrays
Key      | Value                  | Default
---------|------------------------|--------
slide    | directory name         | sample
progress | show progress bar      | false
limit    | progress limit minutes | 5
time     | progress start minutes | 0

# Images
![](assets/img/cloud.png)

# Code snippets

```js
// Javascript snippet
var a = 1;
const pi = 3.14;
```

```css
#css {
  background-image: url(background-image.jpg);
  background-size: cover;
  color: darkred;
}
```

# You tube extension
[The Map of Physics](https://www.youtube.com/watch?v=ZihywtixUYo)
[Natural Language Processing With RNNs  H - TensorFlow 2.0 Course](https://www.youtube.com/watch?v=hEUiK7j9UI8&t=6s)

# Iframe
<iframe src="//www.youtube.com/embed/I0eVwo1VCuU?rel=0" frameborder="0" allowfullscreen></iframe>

# Download files...

## Render file as raw text or call api
My ip from https://httpbin.org/ip: download.raw(https://httpbin.org/ip)

## Render others markdown files
download.md(assets/slides/toolbox_subpage_1.md)

## Render file as code snippet (file extension is checked)
download.code(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.cpp)

