#### Microtask 6:
Using the SortingHat GraphQL Console, create a query that fetches the data (identities, enrollments) of an individual profile.


Query:
```
{
  individuals(filters: {term: "Alastor Moody"}) {
    entities {
      profile {
        email
        name
        id
        gender
        individual{
         identities{
          name
          email
          username
        } 
          enrollments{
            organization{
              name
            }
            start
            end
          }
        }
      }
    }
  }
}

```

![Screenshot](https://github.com/Rashmi-K-A/chaoss-sortinghat/blob/master/assets/mt6.png)
