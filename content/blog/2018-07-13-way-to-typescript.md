Title: Way to typescript
Date: 2018-07-13 20:30:00 +1200
Category: Web
Tags: web
Slug: way-to-typescript

![grunt-typescript]({attach}/images/grunt-ts.jpg)

Recently team **BOLT** just upgraded the NPM packages in **Unleashed.UI** project and enabled the support of Typescript in the AngularJS app.

**TL;DR**
The key to support TS in Unleashed.UI is to install the required packages and integrate with existing Grunt tasks. This article will give a quick catchup of what Grunt is and how we integrate typescript with it in Unleashed solution.

## What's Grunt

Unleashed.UI project uses Grunt as it's packing tools. In front-end world, a packing tool is used to process your code from writting language/format to a small/compatitable/performant version for real-world browsers. 

Strictly speaking, Grunt is not a packing tool. It is designed as a "**Task Runner**" that techinically can run every program on the machine. It has thousands of plugins for different scenarios to use. Packing a web application is one of the most common one. 

## Understand the Grunt tasks

Let's dive into the Grunt in Unleashed repo.

The Grunt auto loads the definitions of tasks from a `Gruntfile`. It looks for the default name `Gruntfile.js` or `Gruntfile.coffee` under the same folder. (Only the config supports CoffeeScript natively) 
_The file can also be specified with option `--Gruntfile <filename>`._

A task can be declared in two ways. One of them is to load tasks from plugin - NPM packages.

```js
grunt.loadNpmTasks('grunt-contrib-clean');
```

The other way is to call `registerTask`:

```js
grunt.registerTask('default', ['clean', 'build']);
grunt.registerTask('buildScript', function(target) {
    grunt.task.run(['ngtemplates']);
    if (target === 'dist') {
      grunt.task.run(['browserify:dist', 'uglify:dist']);
    } else {
      grunt.task.run(['browserify:debug', 'concat:js']);
    }
    return grunt.task.run(['copy:scripts']);
  });
```

The tasks loaded into grunt will be saved in key-value pairs. Each key represents the task name and the value is either the task option or the task implementation (function). You can run a specific task either by direct call with command `grunt <task name>` or within another task. 

In the above example, the task 'default' is defined to run task 'clean' and 'build'. The task 'buildScript' is a function that has our own implementation.

## Task Types

* Task from a grunt plugin

You can install a Grunt plugin from NPM. For example, the task 'clean' was from a plugin `grunt-contrib-clean`. It can be installed as dev-dependencies:

```bash
npm install --save-dev grunt-contrib-clean
```

Afterward we can load the tasks from the plugin with `grunt.loadNpmTasks(...)`. The usage/option usually can be found at its website, e.g. https://www.npmjs.com/package/grunt-contrib-clean. 

* Task to Run Multiple Tasks

The value of the task definition is an array of string, e.g. `'default': ['clean', 'build']`. It helps to run multiple tasks with one command. It will run the tasks in sequence.

* Custom Task

Grunt supports to register a task as a function. When run the task it will just run the function. The function also supports parameters by using colon: `buildScript:dist` equals to `buildScript(dist)`. In each function you can run other tasks with method `grunt.task.run` function.

## Configurations

The options for each task is usually passed in with the object when initialize. 
e.g. 

```js
grunt.initConfig({
        clean: {
            options: {force: true}
            dist: {files: [{ dot: true, src: [ '<%= config.tmp %>', '<%= config.dist %>']}]}
        }
    })
```

## Task "browserify"

The project [browserify][1] resolves the usage of 'require' for browsers. It bundles all the javascript codes that browsers need into a single `.js` file.

Browserify supports plugins, The '[coffeeify][2]' is one of which that allows the 'browserify' to load coffee scripts and transform them into javascript. The '[tsify][3]' is the one for typescript.

Therefore, to support typescript in Unleashed.UI, we need to install '**tsify**' along with native typescript package. 

```bash
npm install --save-dev typescrip tsify
```

One difference between 'tsify' and 'coffeeify' is that the 'tsify' doesn't support parameter 'transform'. So we need to [do some hack][4] to make it work with 'coffeeify':

```js
browserify: {
    options: {
        configure: function(b) {
            return b.plugin('tsify');
        }
    },
    server: {
        options: {
            transform: ['coffeeify']
        },
        files: ...
    }
}
```

## AngularJS Component in Typescript

It's time to add a component in typescripts now!


First of all, install "type" for angular 1:

```bash
npm install --save-dev @types/angular
```

Then, we add "scripts" in `components/typescripts/hello.compoment.ts`:

```js
class HelloController implements ng.IComponentController {
  public message: String;

  constructor() {
      this.message = `Hello Typescript`
  }
}

export class HelloOption implements ng.IComponentOptions {
  public controller: ng.Injectable<ng.IControllerConstructor>;
  public controllerAs: string;
  public templateUrl: string;

  constructor(){
    this.controller = HelloController;
    this.controllerAs = 'vm';
    this.templateUrl = 'components/typescripts/hello.tpl.html';
  }
}

declare var angular: ng.IAngularStatic
angular.module('typescript', []).component("unlHello", new HelloOption())
```

In real world usage, you may want to declare all components for the same module together. So let's extract the last two lines into a seperate file. 

```typescript
import { HelloOption } from "./hello.component";
declare var angular: ng.IAngularStatic
angular.module('typescript', [])
    .component("unlHello", new HelloOption())
```

Then, run the grunt task to transpile & package:

```bash
grunt build
```

Now you have a new component `unl-hello` available in Unleashed web page!

You may have found that we use **component** instead of **directive** here. Moving forward it would be better to use the "component" instead of the "directives". The Angular Component was introduced in Angular 1.5 and is [recommended for upgrade to Angular 2+][5].

At last, don't forget import your module in the Angular bootstraping file `app.coffee`.

```coffeescript
require './components/typescripts/typescript'
```

## Summary

In modern web application development, packaging is becoming more and more important. It empowers the developers to generate more productivity with less efforts. With GruntJS's help, we can code with typescript in Unleashed.UI project now.



[1]:	http://browserify.org/
[2]:	https://www.npmjs.com/package/coffeeify
[3]:	https://www.npmjs.com/package/tsify
[4]:	https://stackoverflow.com/questions/40182786/how-to-set-up-grunt-browserify-tsify-babelify
[5]:	https://angular.io/guide/upgrade#using-component-directives