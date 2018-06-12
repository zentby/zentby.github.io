Title: Entity Object Tracking
Date: 2018-04-04 21:09:00 +1200
Category: tech
Tags: ef
Slug: entity-object-tracking

**Object State**

Last time we introduced how to query database from conceptual models. It includes LINQ to Entities and Entity SQL. With `IQueryable` object, the sql script will be built and executed automatically within the method `.ToList()`. After the data is loaded in our program, we'll operate against them and save changes back to the database. Today we'll talk about how Entity Framework manage the changes in our program.

When the query executes through `ObjectContext` and is materialized into objects, Entity Framework takes a snapshot of an entity’s values. The context stores two set of values of the entity. One of them is the original values of the object and it remains static. The other one will be a realtime values that being modified in the program. The object that saved the two set of values is named `ObjectStateEntry`. Every object returned from database will have an instance of `ObjectStateEntry` as a shadow.

Each `ObjectStateEntry` has a property `State` to reflect the state of the entity(`Unchanged`, `Modified`, `Added` or `Deleted`). As the user modifies the objects, the `ObjectContext` updates  the  current  values  of  the  related  `ObjectStateEntry`  as  well  as  its `State`

The entity object  itself  also has an `EntityState` property, which it inherits from `EntityObject`. As long as the object is being managed by the context, its `EntityState` will always match the `State` of the `ObjectStateEntry`. If the object is not being managed by the context, there is no `ObjectStateEntry` and the entity’s `State` is `Detached`.

**Save Changes**

After finish modifying conceptual objects that loaded from context, we could easily get these changes applied to database by call the method of `SaveChanges` against the context. And by doing that all the SQL scripts will be automatically generated and executed.

When the context was notified of a property change, not only did it modify the current value in the `ObjectStateEntry`, but it also set another tracking value that indicates that the property was changed. During `SaveChanges`, the context then looks for those tracking values to determine which fields were changed.

```csharp
var customer = context.Customers.FirstOrDefault.Where(c => c.Name == "Jason");
customer.IsObsolete = true;
context.SaveChanges();
```

WIth SQL Profiler, we'll get the executing sql:

```
exec sp_executesql N'update [dbo].[Customers]
set [IsObsolete] = @0
where ([Name] = @1)'
,N'@0 bit,@1 nvarchar(50)'
,@0=1, @1='Jason'
```

**No Tracking**

No tracking query, as the name suggest, means the objects that returned by the query would not be managed by the context. Though it relates to what is called `MergeOption` for querying, which controls how to deal with result with existing cached objects in context (queried in the same transaction).

When querying with `NoTracking` option, it does not only means the `SaveChanges` will not save any changes on those objects, but also means all the `ObjectStateEntry` objects creation will be skipped by Entity Framework. Based on these two features, `NoTracking` is often used for readonly data querying and it improves the performance significantly for large volume of data.
