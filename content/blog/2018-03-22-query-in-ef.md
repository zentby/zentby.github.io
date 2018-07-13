Title: Query in Entity Framework
Date: 2018-03-22 21:09:00 +1300
Category: EntityFramework
Tags: ef
Slug: query-in-ef

With Entity Data Model, we built the connection between conceptual models and database schema. The next question would be how we’re going to code with the EDM objects.

Today we’ll have a quick view to LINQ to Entities, which is the main way developing with conceptual models, as well as Entity SQL —a storage independent query language. Either way the queries would eventually be transformed to corresponding sql query to database.

### LINQ to Entities

LINQ is an acronym stands for [Language-INtegrated Query](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/). It is a set of query technologies that allow you to create an unified query against different data sources. So on language level, it represents a bunch of methods to operate object sets. 

When LINQ applied with Entity Framework, we got three different technologies: [LINQ to DateSet, LINQ to SQL and LINQ to Entities](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/linq-and-ado-net). This time we'll talk about LINQ to Entities only.

LINQ to Entities supports both query syntax and method syntax of LINQ. Query syntax is similar to SQL query, writing with c#, you can compose you LINQ inline by using _from/where/select_ keywords:

```csharp
var customers = from c in DbContext.Set<Customers>()
                            where c.Deleted = false
                            select c.Id
```

> The reason why LINQ query starts with `from` instead of `select`, it must be for enabling IntelliSense while editing. It's happening all the time in Sql Server Management Tool that column names only get populated after you typed table name -- which always be the second line of your script.

WIth method syntax, on the other hand, the code can be more straight forward:

```csharp
var customers = DbContext.Set<Customers>()
                .Where(c => c.Deleted == false)
                .Select(c => c.Id);
```

Both methods result to a same data set in `customers` variable and both the types of the variables would  be `IQueryable`. Everyone new to LINQ to Entities must be careful with the differences between `IQueryable` and `IEnumerable`. The `IQueryable` contains metadata about the query, such as the query expression and the provider being used, and it only has result returned within the object after the query inside is executed. The easiest way to execute the query and convert a `IQueryable` to a `IEnumerable` is call `.ToList()`.

```csharp
customers.ToList()
```

> Under the cover, `IQueryable` is building an expression tree when you fill your chaining methods. The execution of the `IQueryable` varies based on different data provider. It converts the expression tree into format the provider recongnized and send it to the corresponding server. Potentially it could support all data sources, as long as there is an implementation of `IQueryable` from those providers.

The expression above  would be executed on our DB server  and return the result into a `List<T>` object. This query can be easily monitored with [SQL Server Profiler](https://docs.microsoft.com/en-us/sql/tools/sql-server-profiler/sql-server-profiler) if you're using MS SQL Server. It would look like:

```sql
SELECT
[Extent1].[Id] AS [Id]
FROM [dbo].[Customers] AS [Extent1]
WHERE [Extent1].[Deleted] = 0
```
It's fairly a simple SQL query that generated from our code but sometimes the queries may look more complex. We might come back and talk to its impact on performance later.

### Entity SQL

What is Entity SQL? 

Well, Entity SQL is another query language Microsoft invented .... to consume your enthusiasms on SQL-like languages. 

Here's the way using Entity SQL to implement our query to get customers id:

```csharp
EntityCommand cmd = conn.CreateCommand();
cmd.CommandText = @"SELECT VALUE c.Id FROM Customers AS c WHERE c.Deleted = 0"
EntityDataReader reader = cmd.ExecuteReader(CommandBehavior.SequentialAccess)
// Extract data from reader
```

## Summary

In this post we talked about approaches to query database with Entity Framework. There is no doubt that my favorite one is to use LINQ chaining methods. It helps you validate in compile time so you can always focus on the business logics.
