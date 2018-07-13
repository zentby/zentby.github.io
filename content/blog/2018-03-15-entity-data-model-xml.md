Title: Entity Data Model XML
Date: 2018-03-15 22:00:00 +1300
Category: EntityFramework
Tags: ef
Slug: entity-data-model-xml

Last time, we described how Entity Data Model(EDM) was designated to help DBA and developer to work with their own contexts. Today let’s dig deeper into EDM to see what it consists of and what it looks like in reality.

## Core Concepts

The EDM uses three key concepts to describe the structure of data: **entity type**, **association type**, and **property**. These are the most important concepts in describing the structure of data in any implementation of the EDM.

![entity data model](https://i-msdn.sec.s-msft.com/dynimg/IC315129.gif)

1. Entity Type

In a conceptual model, entity types are constructed from properties and describe the structure of top-level concepts, such as a customers and orders in a business application. It is not necessarily A table in database, it is meant to face the application.
_Inheritance is supported with entity types._

2. Property

Like an object in a programming language, entity types contain properties that define the structure and characteristics. For example, a Customer entity type may have properties such as CustomerId, Name, and Address.
_Normal properties can only contains primitive data(string/int/bit)_

3. Association Type

An association represents a relationship between two entity types (such as Customer and Order). Every association has two ends that specify the entity types involved. An association end owns a multiplicity that can have a value of one (1), zero or one (0..1), or many (*). 
_Entities at one end of an association can be accessed through navigation properties. We’ll talk navigation properties in later posts_

## Entity Data Model XML (EDMX)

Entity Data Model is a concept. The Entity Framework has a particular implementation that is realized as the EDMX file at design time. The EDMX file is a XML document under the cover and it is made of three layers. These three layers have nothing to do with EDM but an implementation within Entity Framework.

The first one layer of the three represents the conceptual model, which is the actual EDM. The second one represents the database schema, and the third represents the mappings between the first two. Each of the layers will become a XML file at run time, ended with CSDL, SSDL and MDL respectively.

If we open an EDMX file in XML editor, you’ll see these three parts in the file content.

![EDMX]({attach}/images/EDMX.png)

The file composed of two main sections: the runtime information and the designer information. The three parts that we are going to talk about are all in the runtime section.

### CSDL

The conceptual content includes everything needed in a EDM model, including entity type/property/association. Check out the file yourself:

![CSDL]({attach}/images/CSDL.png)

The entity container have EntitySets and AssociationSets. Each child represents a Entity Type or Association Type. After the container it lists all the entity type with defined properties and property’s properties.

### SSDL

The StorageModels section of an EDMX file is a schematic representation of its associated data store. The elements of this file are similar to those of the CSDL file. 

![EDMX]({attach}/images/SSDL.png)

For consistency, the tables and columns are called EntityType and Property. You will see these referred to in documentation as tables and columns, and even as such in the visual tools.  The difference is: the entity type names are the actual names of the tables in the database and the property types are the data store data types. 

### MDL

The Mapping section is quite straight forward that it contains the field mappings between conceptual model and store model. As we talked in [last post]({filename}./2018-03-08-entity-data-model.md), one entity type in CSDL may relate to multiple tables from SSDL. In that case you would see multiple _MappingFragment_ nodes under each entity set mapping.

## Summary

So far we have had a general view of what entity data model consists of in real life and the inner structures in EDMX file. One practical benefit I had seen from these knowledge is that this give us a way to update the EDMX file without manually “Update Model from Database” from UI — which cost one hour to finish! 
_(PS: A good news is in Entity Framework 6, the reload performance has been improved from 60 minutes to 30 seconds!)_