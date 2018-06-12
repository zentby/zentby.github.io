Title:  Docker and dockerspace
Date:   2017-06-26 21:14:00 +1200
Category: blog
Tags: docker
Slug: docker-and-dockerspace

### Dev
There’s a common experience for every developer that new to a company. It’s painful, annoying and frustrating. Everyone knows it would be there but nobody can avoid it. And the pain itself, later on, would also become a sort of asset, privilege or proof that the people experienced this are more senior. 

The name of this experience is called ’setup’. You’ll have to setup many softwares on your computer before you really start writing  piece of code. And normally it won’t success at the first time. You’ll have to pray and try again for quite a few times.

### QA
Similar pain happens to new QA as well. However, instead of downloading and clicking the setup files one by one, the things they need to know before testing is to familiar with all QA environments. Which one is for functional testing, which one is for alpha/beta testing, etc.

Different than developers, what’s more, their pain doesn’t stop there. There are a lot of conversations between developers and QA are like, “it’s start not working on A machine. ” “Let me see..(after a while)..I have no idea. Have you tried on other environments?” ”Let me try… It’s working in B!” ”Sh\*t, Could you switch to B for testing for now?” Moreover, the most famous rumor from developers: **works on my machine** is happening day by day.

### Ops
Infrastructures are becoming more and more complicated but unfortunately, it can be hardly tested by our QA before it is released. So we’ll always need a post release test to make sure what have deployed is as same as what have been tested. So every release will be a gambling. It makes our system unstable and by nature we don’t like it .

As we’re growing quickly, the system will be also introducing more technologies along with more infrastructures. Think about what have we started using in our production during the past few years. Redis, Riak, Rackspaces, Azure WorkerRole/WebRole/ServiceBus, CouchDB, ElasticSearch and there will be more, I believe, are coming.

### Docker
As you can see, things are getting complicated. People don’t like complicity, that’s why they use Unleashed. We don’t like complicity either, so we should use Docker.

Literally docker is the person that working on a dock. They help manage containers and ship them to anywhere.

![docker-logo]({attach}/images/docker-logo.png)
I’d say that's a very accurate analogy for Docker actually. Container technology has been in Linux system for years and Docker is actually a tool that written in Go managing those containers on Linux. It only helps us manage these containers so that we can use a few of simple commands to start or stop our apps in a single computing resource, which mostly is our server or vm whatever, in few seconds.

![container]({attach}/images/container.png)

If you used to know what virtual machine is and you may feel  container is very similar to it. Yes they are similar but not that very. 

Both VM and container are designed to provide an isolated environment in which to run an application. Additionally, in both cases that environment is represented as a binary artifact which can be moved between different hosts. 
![container-vm]({attach}/images/container-vm.png)

They are very like house and apartment. For a house you'll need to build your own heat system, plumbing, electricity and network but for an apartment they are all shared. Furthermore, in majority of cases houses are all going to have at least a bedroom, a living area and a kitchen. It’s incredibly difficult to find a ‘studio house’ So back to vm, you liked it or not, you will have to install your guest operating system and set up and configure softwares for every one of them. On the other hand, Docker just did these for you and you, the user, just focus on your idea.

### Image, Container and Repository
There are three important concept in Dockers: image, container and repository. Image is your application and it’s dependencies, from operating system to the end program. Image is like Lego brick, while you’re building something from scratch, you’ll need at least to have a base, an OS images, it’s where your app will be on, most famous OS have started support Docker such as Ubuntu, CentOS, Mint, Alpine and … Windows! 

Next, with your base, you start to create your astonishing architecture upon it with a Dockerfile. In a Dockerfile you define how it will be built and in the end you’ll get a list of steps that to build your image. With these steps in the Dockerfile, Docker build the image for you. Once the building is finished, it will be transferred to your own repository.

![dockers]({attach}/images/dockers.png)

And at this point, your app is actually ready to run at anywhere of the world. Whenever you decide wherever of the world you are likely to launch your app, Docker will take out your image from repository, fill them into a container and it will run at where you’ve asked for.

## How it helps
The Docker company has published the largest image platform ‘DockerHub’. Everyone can share their images or Dockerfile there. Almost all of the famous softwares have pushed their own official images there. Developer can explore or start to use any technology they are interested without caring too much about the details.

Have you noticed that we have gradually illustrated how Docker would help QA? The places that your want the app to run, in the reality, are those different testing environments! One image, run any environments! Because apart from the configurations, they are all the same! We’ll never need those many machines standby for QA and we’ll never heard developers complaining about ‘working on my machine’.

As part of Docker toolset, ‘docker-compose’ allows us using one file to define what and how many containers would you like to run, how would you like to build network between them. Based on this concept, you’ll have the ability to define your infrastructure in a structured way, also a stable way. Because we know the container already has all our app needs and it will always be running consistently.


## Dockerspace
[Dockerspace](https://zentby.github.io/dockerspace/) is an side project that focus on helping developers in Unleashed can easily get their development environments setup without much effort.

[Go get your copy now and get dockerized today.](https://github.com/zentby/dockerspace)