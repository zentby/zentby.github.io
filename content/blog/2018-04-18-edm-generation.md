Title: Entity Data Model Generation
Date: 2018-04-18 23:10:00 +1200
Category: tech
Tags: ef
Slug: edm-generation


**Database/Model First**

Let's get one step back and have a quick look at how the conceptual models had been built at the beginning.

Before we build the database and the program, there's an equal chance for either having database design first or having domain model design first. Initially Visual Studio supports both ways to create the Entity Data Model, one of which called **Database First** and the other called **Model First**.
 
The **Database First** utilizes reverse engining to generate the EMD from an existing database. **Model First** is the other way around that the database is created/updated after EDM is finished in the designer.

With **Database First**, the update direction will always be from database to models. Every changes on databases can be updated to models by redo the operation. On the other hand, in **Model First** any changes to the database may be before you applied them to models. However, Model First allows developers to design the app without concerning too much on database structure, which can help build the prototype quickly.

These days, the border between these two ways has been becoming more blurrier. They all eventually build up with the EDMX file and can be maintained from the “designer”— either use command `Update Model from Database` to update the EDM, or `Generate Database from Model` to create sql scripts re-generating the whole database.

![Operation in Visual Studio EDMX Designer]({attach}/images/EDM-designer.png)
*Operation in Visual Studio EDMX Designer

**Code First**

The **Code First** was a “new” concept since EF 4.1 but it didn’t get much promotion until EF 6. A lot of  improvements were made in EF 6 including Fluent API (*to configure EDM mappings by codes*) and migration tools(*to manage database changes*). Hardcore programmers finally got rid of the designer when deal with databases. At the version of EF 6.1, it introduced the ability to generate**Code First** model from database — it helps existing app get transfered to **Code First** if the team wants. 

In EF Core (or EF7), the **Code First** will be the only way to create EDM.( We can tell how much MS is willing to retire the visual designer. The key feature to support “code first” is **migration**, it allows developers update both the classes and database at the same time without losing any data. The migration also makes it possible to upgrade the db at any point to the latest version. The developers will not need to maintain the DB upgrade manually anymore.

I am in favor of the **Code First** as I really love the idea that maintaining the database via codes. It means by tracking the code changes you’ll be able to have the view of the actually history of the realistic entity.

![Choose how to create EDM]({attach}/images/modeling-work-flow-options.png)
*Choose how to create EDM
