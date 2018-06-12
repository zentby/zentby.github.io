Title: Introduction to Entity Data Model
Date: 2018-03-08 23:14:00 +1300
Category: tech
Tags: ef
Slug: introduction-to-entity-data-model


>There is always something exists for a mysterious reason. 'Mysterious' doesn't mean it is unknown, but we are too lazy to know. The Entity Framework technology is one of those things for me. It was set up at the very beginning for a solution and it only needs a very little bit maintenance. Detailed instructions have been written and all we need to do is to follow them and make sure nothing is broken. Recently we met a few of issues related to entity framework and it drives me to take some effort on it.

>While learning on the big topic, I’m going to post some notes as well. I'm going to talk about Entity Framework by sessions in the following few weeks. I will cover as much as I can for the topic and hopefully I can stick to it. Today I'll start with entity data model(EDM), a very core and basic concept in Entity Framework.

## Entity Data Model

In terms of model, we have two kinds of types here - one for database and one for the application that we build.

On application side, a model particularly means an object of a class that developers code against with. It is from the concept of 'object-oriented' programming and an object is an abstraction of the real world.

In database, on the other hand, a model is more likely a schema of how data being stored. As we're talking about relational database, a schema is a database structure that is designed based on [Entity Relationship Model]. 

To fill the gap between application and database, developers used to manually writing SQLs to handle the communications and conversions.  It takes long time to code and longer time to maintain them. To resolve the complicity and time-wasting, the technology of ORM ([object relational mapping]) came into being. The ORM is trying to build a bridge between database and programming language, helping you do the dirty jobs. 

Entity Framework is one of ORM technology and Entity Data Model is a middle layer that abstracts entities from database into programming objects. It abstracts the database tables into objects, which you can directly code against with. Also the EDM designer helps you to virtualize you database structures so you could have a greater view of what your data would looks like. What's more, it split the responsibilities of program design and database design. With EDM, you can have your database administrator to design a well normalized database when your developer can comfortably program with business objects. EDM covers the underlying operations.

## Example

To make it more sensible, I'm giving(copying) a simple example here:

![DB schema]({attach}/images/db-schema.png)

The figure shows the schema of a typical set of tables in a database. `PersonalDetails` provides additional information about a `Person` that the database administrator has chosen to put into a separate table for the sake of scalability. `SalesPerson` is a table that is used to provide additional information for those who are salespeople. 

Working with this data from an application requires queries that are full of inner joins and outer joins to access the additional data about Person records. Or you will access a variety of predefined stored procedures and views, which might each require a different set of parameters and return data that is shaped in a variety of ways. 

![Entities]({attach}/images/entities-models.png)

By using EDM, the application could have its own view of what you wish the database looked like. Figure above reshapes the schema. 

All of the fields from `PersonalDetails` are now part of `Person`. And `SalesPerson` is doing something that is not even possible in a database: it is deriving from `Person`, just as you would in an object model. 

In summary, the Entity Data Model enables you to code against strongly typed entity classes, not database schema and objects. Also it enables you to customize the mappings between entity classes and database tables to move beyond one-to-one mapping or class-to-table mapping.