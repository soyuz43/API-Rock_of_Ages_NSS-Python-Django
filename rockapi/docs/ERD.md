# ERD for Rock of Ages API Project
The Entity-Relationship Diagram (ERD) for the Rock of Ages API project will include the Rock, Type, and User tables, as well as additional details related to user authentication. The auth.py script for user registration and login adds relationships and dependencies to the ERD, which need to be reflected accurately.
## DBDiagram.io compatible code:

```sql
Table type {
  id int [pk, increment] // auto-increment primary key
  label varchar(155)
}

Table rock {
  id int [pk, increment] // auto-increment primary key
  user_id int
  type_id int
  name varchar(155)
  weight decimal(5,2)
}

Table auth_user {
  id int [pk, increment] // auto-increment primary key
  username varchar(150)
  password varchar(128)
  email varchar(254)
  first_name varchar(150)
  last_name varchar(150)
  // Additional fields as needed
}

Table authtoken_token {
  key char(40) [pk]
  user_id int
  created datetime
}

Ref: rock.user_id > auth_user.id
Ref: rock.type_id > type.id
Ref: authtoken_token.user_id > auth_user.id
```
**Note** - DBDiagram.io expects a slightly different syntax for defining references.
### Explanation of Changes:
- **Foreign Keys in `rock` Table:** The `user_id` and `type_id` columns are defined without direct foreign key syntax but references are specified separately.
- **Foreign Key in `authtoken_token` Table:** The `user_id` column is defined similarly without direct foreign key syntax, and references are specified separately.
- **Separate `Ref` Statements:** Each reference is defined in a `Ref` statement to clearly specify relationships between tables.

### Steps to Use This Code in DBDiagram.io:
1. **Copy the code provided above.**
2. **Open DBDiagram.io and start a new diagram.**
3. **Paste the copied code into the editor.**
4. **DBDiagram.io will render the ERD with the correct relationships.**

