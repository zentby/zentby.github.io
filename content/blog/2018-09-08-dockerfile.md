Title: Building Docker Image
Date: 2018-09-08 21:30:00 +1200
Category: Container
Tags: docker, container, 
Slug: dockerfile

## Dockerfile

Docker images are built from layered containers. The `Dockerfile` is a tool that lets you define reproducable docker image.

Generally, we are doing a few things inside a Dockerfile to define an image:

**1. Basic Running Environment**

Is your app running on Linux or Windows? Which version do you prefer? 

**2. Dependent Packages**

What else packages does your app need? e.g. npm/nuget packages

**3. Copy Application**

Copy the generated binary files into the image.

**4. Set up interfaces**

Expose the port you want to listen, mounting point you want to monitor, etc.


### Example

Here is a simple proxy server that I'd like to move it into the container.

The App is simple HTTP proxy that attach CORS header for each request to a specific server. (Useful when you can't/don't want to update the API server)

```js
var http = require('http')
var httpProxy = require('http-proxy');
var proxy = httpProxy.createServer({});
proxy.on('proxyRes', function (proxyRes, req, res) {
proxyRes.headers['Access-Control-Allow-Origin'] = '*'
});
var server = http.createServer(function (req, res) {
proxy.web(req, res, {
target: process.env.TARGET_URL
});
}
});
server.listen(80);
```

The code structure is like this:
```bash
app
├── index.js
├── node_modules
└── package.json
```

Now let's build an image for it.

Firstly, choose to use "Alpine Linux" as its the smallest Linux (5MB)

```Dockerfile
FROM alpine
```

Then install NodeJS and NPM.

```Dockerfile
RUN apk update && apk upgrade && apk add --update --no-cache nodejs npm
```

Now we can copy our source code into the image.

```Dockerfile
COPY proxy /proxy
```

To save the time after the container starts, we should use NPM-installed image.

```Dockerfile
RUN npm install
```

Lastly, make the Node command as our image entry point. Don't forget to expose port 80 so our app can listen to it.

```Dockerfile
EXPOSE 80
ENTRYPOINT ["/bin/sh", "-c", "node /proxy/index.js"]
```

Now let's get them together to see how a Dockerfile looks like:

```Dockerfile
FROM alpine
RUN apk update && apk upgrade && apk add --update --no-cache nodejs npm
COPY proxy /proxy
RUN npm install
EXPOSE 80
ENTRYPOINT ["/bin/sh", "-c", "node /proxy/index.js"]
```