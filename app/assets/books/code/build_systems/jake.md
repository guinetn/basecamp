## JAKE

JavaScript build tool for NodeJS  
Similar tools in the Node and JavaScript ecosystem are Grunt and Gulp.

https://jakejs.com/

> jake -t      list of tasks available in a Jakefile

task(name, [prerequisites], [action]);

Jakefile detected: Jakefile, Jakefile.js, jakefile, jakefile.js. will look its parent directory and so on... 
```js
let { task, desc } = require('jake');

desc('This is the default task.');        ← add a string description of the task
task('default', function () {
  console.log('This is the default task.');
  console.log('Jake will run this task if you run `jake` with no task specified.');
});

desc('This is some other task. It depends on the default task');
task('otherTask', ['default'], function () {
  console.log('Some other task');
});
```

```js
let { task, desc } = require('jake');

desc('This is the foo task.');
task('foo', function () {
  console.log('This is the foo task.');
});

desc('This is the bar task.');
task('foo', function () {
  console.log('This is the bar task.');
});

desc('This async task has prerequisites.');
task('hasPrereqs', ['foo', 'bar'], async function () {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log('Ran some prereqs first.');
      resolve();
    }, 2000);
  });
});
```