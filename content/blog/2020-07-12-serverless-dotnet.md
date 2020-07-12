Title: Step by step starting serverless asp.net
Date: 2020-07-12 21:30:00 +1200
Category: Serverless
Tags: aws, serverless, dotnetcore 
Slug: dotnet-lambda-serverless

The CSOD "Spring" Hackathon was held last week. My team spent a whole day to help me finish an ambitious idea. Though we didn't win the competition in the end, we had a lot of fun and did learn many things.

The AWS lambda serverless with dotnetcore, one of "new" technologies that we used during the event, surprised me with its simplicity and dev-friendliness. It's something could be used for a very quick prototyping in the future. 

Here's how we built up a **production ready** REST backend in a few easy steps.

Before start, we decided our backend stack as *asp.net core* + *MySql*. The asp.net core will be transformed to *api gateway + lambda*, while the MySql will be replaced by the *Aurora Serverless*. A pure serverless architecture.


First of all, we need to get a local MySQL up and running. It can be easily accomplished by a `docker-compose`, nice and clean:

```yaml
version: '3.3'

services:

  db:
    image: mysql
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    ports:
      - '3306:3306'
    environment:
      MYSQL_DATABASE: 'db'
      MYSQL_USER: 'user'
      MYSQL_PASSWORD: 'password'
      MYSQL_ROOT_PASSWORD: 'password'
    volumes:
      - my-db:/var/lib/mysql

  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
volumes:
  my-db:
```

Second step, scaffolding the asp.net serverless project. Amazon engineering team provided [a set of tools integrated with dotnet-cli](https://github.com/aws/aws-extensions-for-dotnet-cli#aws-lambda-amazonlambdatools), which contains a few of serverless templates. 

### 1) Install global tools set

```sh
dotnet tool install -g Amazon.Lambda.Tools
```

### 2) Install project templates

```sh
dotnet new -i "Amazon.Lambda.Templates::*"
```

To view the installed lambda templates, run

```sh
dotnet new lambda --list
```

### 3) Create new project with serverless template

```sh
dotnet new serverless.AspNetCoreWebAPI -n serverless
```

It will create a folder of `example` with the structure

```sh
example
├── src
│   └── serverless
│       ├── Controllers
│       │   ├── S3ProxyController.cs
│       │   └── ValuesController.cs
│       ├── LambdaEntryPoint.cs
│       ├── LocalEntryPoint.cs
│       ├── Readme.md
│       ├── Startup.cs
│       ├── appsettings.Development.json
│       ├── appsettings.json
│       ├── aws-lambda-tools-defaults.json
│       ├── serverless.csproj
│       └── serverless.template
└── test/*        # test projects folder
```

The files are almost minimal to develop and deploy the application. Let's quickly walk though the key files

* `aws-lambda-tools-defaults.json`: Used for `dotnet lambda` cli command. It defines the necessary deployment parameters.
* `serverless.template`: CloudFormation template that defines the resources to be created in the deployment. By default, it already includes a lambda definition with `proxy+` API Gateway trigger.
* `LambdaEntryPoint.cs`: The class wrapped with built-in `APIGatewayProxyFunction` to enable lambda hosting the web app.
* `LocalEntryPoint.cs`: Local asp.net hosting entrance that uses Kestrel.
* `Startup.cs`: Where all the configurations and warmup happen for both local and lambda.
* `S3ProxyController.cs`: A sample controller with AWS s3 client, where we can start to build our app straightforward.

### 4) Integrate with EF core

As part of dotnetcore family, Entity Framework Core could be easily integrated within an asp.net project.

There is also a dotnet-cli tools set for EF core. 

```sh
dotnet tool install --global dotnet-ef
```

The cli sets provides a few useful commands to manage DbContext and DbMigrations. For more information, refer to [here](https://docs.microsoft.com/en-us/ef/core/miscellaneous/cli/dotnet).

To add MySql, you need to install another package via `dotnet package add` command. The full provider plugins could be found [here](https://docs.microsoft.com/en-us/ef/core/providers/?tabs=dotnet-core-cli). We used the [Pomelo.EntityFrameworkCore.MySql](https://github.com/PomeloFoundation/Pomelo.EntityFrameworkCore.MySql) for our project.

Once it's connected, put the `ConnectionString` into an config file or environment variable. Then goto AWS RDS console, create an Aurora Serverless database and get the connection link. Put the link into your production configuration.

### 5) Development and deployment

To start coding, we just need to code as our normal asp.net project. Open the project with your favorite IDE.

To deploy your project, just get your AWS api key setup locally and run command:

```sh
dotnet lambda deploy-serverless
```

It will automatically load settings in `aws-lambda-tools-defaults.json` (if not, then prompt to ask for input).

At the end of deployment, you'll get an API url:

```sh
Output Name                    Value
------------------------------ --------------------------------------------------
ApiURL                         https://xxxxxxxx.execute-api.us-west-2.amazonaws.com/Prod/
```

Till now, our backend project is ready for client consuming. 
