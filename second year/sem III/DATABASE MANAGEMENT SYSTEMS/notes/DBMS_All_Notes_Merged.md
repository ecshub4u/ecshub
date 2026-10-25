# DBMS Notes — Merged Markdown File
> Combined from the four original `.md` files. Original content and page-image references are preserved.


---

# Source file: 01_DDL_commands.md

# DDL commands

- Original PDF: `notes\DDL commands.pdf`
- Pages: 45
- Preservation: every original page is rendered below; extracted text follows each page image.

## Page 1

![Original page 1](assets/01_DDL_commands/page-001.jpg)

### Extracted text

`````text
                                                         U n i t - 0 1  DDL Commands

     Classification of SQL           commands
        commands      can  be  used   not only   for searching   the  database    but  also
         to  perform various     other  functions like, for   example,    you  can  create
         tables, add   data to  tables,  or modify    data, drop   the  table, set
         permissions     for users.



















         DDL: Data Definition Language
       DDL commands are auto-committed. That                means it   saves all the
       changes permanently in the database.

             DDL statements are used to build and modify             the objects and
              structure of tables in    database.
             The  DDL part     of SQL   permits database tables       to be created     or
              deleted.
             It also defines   indexes (keys), specifies links       between
              tables, and   imposes constraints between tables.
       These SQL commands are used for creating, modifying,                and dropping
       the structure    of database    objects.  The commands        are  CREATE,
       ALTER,    DROP,    RENAME,     and TRUNCATE
          Command                                        Description
        Create            Creates a new table, a view of a table, or other object in




1
`````

## Page 2

![Original page 2](assets/01_DDL_commands/page-002.jpg)

### Extracted text

`````text
                                                         U n i t - 0 1  DDL Commands

                          database
        Alter             Alters the   structure   or Modifies   an  existing  database object, such
                          as
                          a  table.
        truncate          remove    all records   from   a table, including   all spaces allocated
                          for the records are     removed
        Drop              Deletes   an  entire  table, a view   of a  table or  other  object  in the
                          database.
        Rename            Rename     a table, a  view   of a table  or  other  object  in  the
                          database.

          DML: Data Manipulation Language
       DML statements       allow  changing data     within the database.      DML
       commands      are  not  auto- committed. It means changes are not
       permanent to database, they can          be rolled back. These SQL commands
       are used for    storing, retrieving, modifying, and deleting data.
       These   commands       are  SELECT,     INSERT,    UPDATE,     and   DELETE.

         Command                                         Description
         Insert          insert   data  (new   row)    into  a table
         Update          updates existing     data(row) within     a table
         Delete          deletes   all records  from   a  table, the  space  for  the records   remain
         TCL: Transaction          Control    Language
       TCL  statements  are  used  to  manage  the  changes  made  by  DML
       statements.  It  allows  statements  to  be  grouped  together  into  logical
       transactions.  These  commands  can  cancel  changes  made  by  other
       commands by rolling        back to original state. It can also make changes
       permanent.

         Command                                          Description
         Commit           to permanently     save
         rollback         restore database to original since the last          COMMIT( to undo
                          change)






2
`````

## Page 3

![Original page 3](assets/01_DDL_commands/page-003.jpg)

### Extracted text

`````text
                                                         U n i t - 0 1  DDL Commands

         Savepoint        identify a point in a    transaction   to which   you can    later roll back
                          (to
                          save   temporarily)
                          x

         DCL : Data Control          Language
          DCL statements control access to data and to the database. It is used
          to give the permission      to  user  to  use  the  database    or  object.  It can
          also take back the permission. It allows central administration of user
          privileges and access. Data control         language    provides    command       to
          grant  and   take  back  authority.
         Command                                       Description
         Grant                 gives   user's  access   privileges to
                                                            database
         Revoke            withdraw    access   privileges   given  with the GRANT command
                           (take  back
                           permission)
         DQL:    Data    Query     Language
          DQL allows getting data from the database. This              command is
          heart of SQL. When SELECT is          fired  against a table    or tables, the
          result is compiled into      a temporary table.
           Command                                 Description
         Select             retrieve  records   from one    or  more   table

          DDL: Data
       Definition
       Language
       CREATE
       Statement
       SQL CREATE TABLE          statement    is  used to create table in a database. It
       defines   each column of the table uniquely. Each column has a minimum
       of three attributes, a name, data      type   and  size  (i.e. column   width).
       Each table column definition is separated from the other by a comma. SQL



3
`````

## Page 4

![Original page 4](assets/01_DDL_commands/page-004.jpg)

### Extracted text

`````text
                                                    U n i t - 0 1  DDL Commands

      statement is terminated with     a semi  colon.  Whenever user     creates table,
      the  table name must     be a legal SQL   name   and  it must  not conflict with
      the name   of any  of your  existing  tables.
      Rules for Creating Tables
       1. A name    can  have  maximum     up  to 30  characters
       2. Alphabets   from   A-Z, a-z  and  numbers    from 0-9    are allowed
       3. A name   should   begin with an    alphabet
       4. The  use  of the special character like _   is allowed and   also
          recommended. (Special characters        like $, #  are allowed   only  in
          Oracle).

       5. SQL reserved    words   not allowed. For example: create, select,     and so
          on.
      Syntax:
          CREATE    TABLE     < TableName     >
          (< ColumnName1 >< DataType >< size               >,
         < ColumnName2 >< DataType >< size >…….,
         <  ColumnNameN        ><  DataType    ><  size  >);
      Example :       CREATE TABLE EMP
                         (ENO    NUMBER       (3),
                         ENAME      VARCHAR2 (15),
                         EMPADD VARCHAR2             (20));
      Creating A Table From
      Previously Created Table
      Syntax:
       CREATE TABLE < TableName1 > (< ColumnName1 >, <
       ColumnName2 > …..< ColumnNameN               >)  AS   SELECT
       <ColumnName1>,       <ColumnName2>…..<         ColumnNameN
       > FROM     < TableName2       >  WHERE      <condition>;
      If the TableName2     is having records   then  the target table – Table
      Name1 will    be occupied with the same records.
      Example
       1. CREATE TABLE EMP1 AS SELECT * FROM EMP;
       2. Change column name at       table creation  time.  For  example-CURBAL      to
          BALANCE.
       3. CREATE     TABLE     EMP2



4
`````

## Page 5

![Original page 5](assets/01_DDL_commands/page-005.jpg)

### Extracted text

`````text
                                                      U n i t - 0 1  DDL Commands

          (ENO,ENMAE,EADDRESS) AS               SELECT
          ENO,ENMAE,EMPADD             FROM     EMP;
      ➢   Create Table without Records
      To create a target table without records from the source table (i.e. create
      the structure only) then the AS      SELECT    statement    have  to use WHERE
      clause  with   condition  that cannot   be  satisfied.(i.e. SELECT statement     in
      the  CREATE     TABLE    will not  retrieve any rows from the source code. It
      will just retrieve the table structure. Thus, the target table will be created
      empty.)
      Syntax:    CREATE     TABLE    <new    table  name>    AS  SELECT * FROM
      <old   table name> WHERE         1=2;
      CREATE      TABLE     EMP3    (ENO,   ENMAE,      EADDRESS)       AS  SELECT
      ENO,    ENMAE, EMPADD          FROM     EMP    WHERE      ENO=1;
          Alter Table (Modifying The Structure Of Table)
            The  ALTER    TABLE    statement   is used to   add, modify   or
             delete  columns   in an existing   table. It is also used   to
             rename    a table.
            You  can  also  use  ALTER    TABLE    command     to add   and  drop
             various  constraints on an     existing  table.
            ALTER    TABLE     can
                o  add  or delete   columns
                o  add or   remove   constraints
                o  create or destroy indexes
                o  change   data  types  of columns
                o  Rename     columns.
      Restrictions on the ALTER table
          1) User cannot   change   the column    name
          2) User  cannot  decrease   the  size of column   if record  in the  column.
      ➢   Adding New Columns
          ▪  If you  want  to single  add  columns   in  table
             Syntax:   ALTER TABLE table_name ADD column_name column-
             definition;
             Example:      ALTER    TABLE     EMP    ADD    (CITY   VARCHAR2
             (20));


5
`````

## Page 6

![Original page 6](assets/01_DDL_commands/page-006.jpg)

### Extracted text

`````text
                                                  U n i t - 0 1  DDL Commands


         ▪  If you want  to add  multiple columns   in table
         Syntax: ALTER TABLE table_name       ADD (column1
                 column_definition, column2 column_definition,
                  ............................................... Column_n column-
                 definition);
         Example: ALTER TABLE EMP ADD (CITY VARCHAR2
         (20),GENDER CHAR(6));
    ➢   Dropping a Column: remove        column   from  the
                                                    table
         Syntax:   ALTER    TABLE    <TableName>      DROP   COLUMN
         <ColumnName>;
         Example:    ALTER    TABLE    EMP   DROP    COLUMN      CITY;
      ➢  Modifying    Existing   Columns
         ▪  If you want  to modify  an existing column   in table
      Syntax: ALTER TABLE table_name MODIFY (<ColumnName>
      <NewDatatype>     <Size>);
      Example: ALTER TABLE EMP MODIFY (NAME VARCHAR2 (40)
      );
         ▪  If you want  to modify multiple  columns in  table
      Syntax:   ALTER TABLE table_name MODIFY (<ColumnName1>
      <NewDatatype><Size>,
      <ColumnName2> <NewDatatype><Size> ... <ColumnName
      n><NewDatatype> <Size>); Example:           ALTER    TABLE    EMP1
      MODIFY    (ENAME     VARCHAR2(20),EADD         VARCHAR2(20));
      ➢  RENAME Existing Column:         Alter  table rename   column
      Syntax:  ALTER TABLE table_name RENAME COLUMN old_name                col to
      new_name    col;
      Example:    ALTER TABLE       EMP RENAME         COLUMN     EMPADD      TO
      EMPADDRESS;
      ➢  Making Column Unused
         Syntax:  ALTER    TABLE    <Table_Name>      SET   UNUSED    COLUMN
         <Col>;
         Example: ALTER      TABLE    STUDENT      SET  UNUSED     COLUMN
         MARKS;
      Even  though  the column   is unused  still it will occupy memory.
      ➢  DROPPING UNUSED COLUMNS
         Syntax:   ALTER    TABLE    <table_name>     DROP   UNUSED     COLUMNS;
         Example: ALTER      TABLE    STUDENT      DROP    UNUSED    COLUMNS;



6
`````

## Page 7

![Original page 7](assets/01_DDL_commands/page-007.jpg)

### Extracted text

`````text
                                                     U n i t - 0 1  DDL Commands

      You cannot drop individual unused columns         of  a table.
      ➢   Alter Table To Add / Remove Constraints
           To  add a  primary   key  constraint  after creation of a  table
            Syntax:    ALTER     TABLE    <TableName>       ADD   PRIMARY      KEY
            (column(s));
            Example:         ALTER    TABLE     EMP    ADD
                   PRIMARY      KEY   (ENO); ALTER       TABLE
                   EMP    ADD   PRIMARY      KEY    (ID,
                   NAME);
            It will add  a primary   key  constraint to a  specified columns   .If
            there  is more  than one   column   to specify then  all the columns   are
            separated   by  commas   and  will create  composite   primary  key.
                   ALTER    TABLE     EMP    MODIFY     SALARY     DECIMAL      (18,  2)
                   NOT   NULL;
           To  add a  foreign  key  constraint  after creation of a  table
            Example:      ALTER    TABLE     EMP   ADD    FOREIGN      KEY
            (DEPTNO)      REFERENCES DEPT           (DEPTNO);
           To remove primary key constraint
                   Syntax: ALTER      TABLE    <TableName>       DROP    PRIMARY
                   KEY;
                   Example: ALTER       TABLE     EMP   DROP     PRIMARY     KEY;
            It will remove primary key constraint      from  a table.
           To add user defined     constraint
            Example: ALTER        TABLE    EMP ADD      CONSTRAINT
            myUniqConstraint       UNIQUE (AGE,      SALARY);
            It will add  the constraint  on  the table.
           To remove user     defined  constraint
            Syntax: ALTER      TABLE    <TableName>       DROP    CONSTRAINTS
            <Const_Name>
            Example:     ALTER    TABLE    EMP    DROP   CONSTRAINT
            myUniqConstraint; It     will remove the constraint,
            which   was  defined on   the table.
         DROP TABLE (to drop the table from the database)
            DROP    TABLE    statement   is used  to remove    a table definition




7
`````

## Page 8

![Original page 8](assets/01_DDL_commands/page-008.jpg)

### Extracted text

`````text
                                                        U n i t - 0 1  DDL Commands

       and all data, indexes, triggers, constraints, and permission
       specifications for that table. If a table is dropped,       all records within
       table are lost and    cannot   be recovered.     DROP TABLE statement
       once  executed is permanent. So we have to use            very careful this
       command. Syntax:
                 DROP    TABLE    <  TableName      >; OR  DROP    DATABASE
       DatabaseName;
             Example:       DROP     TABLE    EMP;
       Note:
          1. DROP statement removes          the table.
          2. It deletes  all its data.
          3. It deletes  constraints   and  indexes associated with      it.
          4. Any views     and synonyms      are  remain but     are invalid.
          5. Any pending      Transaction    is committed.
          6. Only   the  creator  of the table    as user with the DROP        ANY
             TABLE privilege      can remove     a  table.
          TRUNCATE         Statement
       It is used to delete the entire table data permanently and           free the
       containing space. Records      cannot    be  ROLLBACK.
             Syntax:       TRUNCATE        TABLE     <Table_Name>;
             Example:      TRUNCATE TABLE EMP;
       ➢   Difference b/w DROP and               TRUNCATE statements
       When    you  drop   a  table:
          ▪ Table   structure  will be dropped
          ▪ Relationship will    be dropped
          ▪ Integrity  constraints  will be  dropped
          ▪ Access privileges will also be dropped
       When we TRUNCATE a           table, the  table  structure remains     the same.
          ▪ Truncate operations drop recreate         the  table which   much faster
            than deleting    rows one    by  one.
          ▪ Truncate    operations  are  not  transaction   safe.
          ▪ The   numbers    of  deleted  rows   are  not  returned.
          RENAME        Statement
       It is used  to  change   the  name   of  a table.
       Syntax:      RENAME < OldTableName >               TO  <  NewTableName>;



8
`````

## Page 9

![Original page 9](assets/01_DDL_commands/page-009.jpg)

### Extracted text

`````text
                                                        U n i t - 0 1  DDL Commands

                                         OR
                    ALTER TABLE table_name RENAME TO new_table_name;
       Example: RENAME          EMP    TO
                 EMPLOYEE;
       OR ALTER      TABLE     EMP    RENAME       TO    EMPLOYEE;
          DESC     (Viewing      Table    Structure)
       It used  to view   structure  of  a table.
       Syntax:        DESCRIBE       <Table_Name> OR            DESC <Table_Name          >
       Example:       DESC    EMP;
       ➢   Difference between           DROP, DELETE          and TRUNCATE

                  Drop                         Delete                           Truncate
       1. Whole structure and         1. Structure  will not        1. Structure will   not drop,   all
                                      drop,
       data will  drop.               data will drop.               data  will drop.
       2.can’t  Rollback              2.can  Rollback               2.can’t  Rollback
       3.can’t  use where    clause   3.can  use   WHERE            3.can’t   use  WHERE      clause
                                      clause
       4.All data  and   structure    4.Row   by   Row   data       4. truncate   operation   drop and
       drop simultaneously            Delete                        recreate  the  table.

          DML: Data
       Manipulation
       Language
       INSERT
       STATEMENT
           It is used  to insert  a single  or  a multiple   records  in  a table. When
           inserting  a single row   of data   into the  table, the  insert  operation:
           ▪  Creates   a  new   row   (empty)    in the  database    table
           ▪  Loads   the  values   passed   (by the   SQL   insert)  into  the  specified
              columns
       In INSERT     INTO    sentence,   table   columns    and   values   have   a  one   to
       one  relationship.
       i.e. First value  is inserted into first   column, second value       is inserted into





9
`````

## Page 10

![Original page 10](assets/01_DDL_commands/page-010.jpg)

### Extracted text

`````text
                                                     U n i t - 0 1  DDL Commands

      second   column   and  so  on.
         1.  There are exactly same     number of values as columns and
         2.  The values are in sequence     exactly in accordance with data type of
             table columns.
      Syntax:    INSERT    INTO   <Table_Name> < ColumnName1              >, <
               ColumnName2        >…..< ColumnNameN >          VALUES     (< Value1    >,
               < Value2    >……< Value        N  >);
      Example:      INSERT INTO EMP (ENO,           ENAME,     EADD) VALUES (1,
      ‘ABHI’,’  PUNE’);
      You   can specify  or  ignore  the  column   names    while  using  INSERT    INTO
      statement.
      We have two    methods to   insert.
             Ø  By  value   method:
                1. By  specifying column    names
                2. Without specifying column names
             Ø  By   address   method

      ➢   Using Value Method:
           Inserting  Data  Into Specified  Columns    Using Value Method
         Syntax:    INSERT    INTO   <table_name>      (col1,  col2…Col    n)  VALUES
                  (value1,   value2… Value     n);
         Example: INSERT INTO            STUDENT       (ENO, ENAME) VALUES (5,
         ’RAMESH’);
           Inserting  Data  Into Without   specifying  column   names   Using   Value
            Method
         Syntax: INSERT INTO TABLE_NAME VALUES (value1, value2, value 3,
                   Value N);
         Example:      INSERT     INTO    EMP   VALUES      (1,
                    ’SUDHA’,    ‘SANGOLA’); INSERT         INTO    EMP
                    VALUES      (2, ’SAKETH’,     ‘SOLAPUR’);
      To  insert a  new  record  again  you  have  to type  entire  insert command,    if
      there  is lot of records this will  be difficult. This will be avoided   by  using
      address   method.

      ➢   Using   Address     Method
         Syntax:      INSERT     INTO    <TABLE_NAME)         VALUES
         (&COL1,&COL2,&COL3….&COLN);



10
`````

## Page 11

![Original page 11](assets/01_DDL_commands/page-011.jpg)

### Extracted text

`````text
                                                   U n i t - 0 1  DDL Commands

      This will prompt   you for the  values but for every  insert you  have  to use
      forward  slash.
      Example: INSERT       INTO    EMP   VALUES     (&ENO,
                  '&ENAME',     &EADD); ENTER        VALUE
                  FOR   ENO:   3
                  ENTER    VALUE    FOR
                  ENAME:    JAGAN
                  ENTER    VALUE    FOR
                  EADD:   PUNE
                  OLD   1:  INSERT    INTO   EMP    VALUES    (&ENO,
                  '&ENAME',     &EADD) NEW       1:  INSERT    INTO
                  EMP    VALUES     (3, 'JAGAN',   ‘PUNE’) SQL>    /
                  ENTER     VALUE    FOR
                  ENO:   4 ENTER
                  VALUE    FOR   ENAME:
                  RAM ENTER      VALUE
                  FOR   EADD:   MUMBAI
                  OLD   1: INSERT     INTO   EMP   VALUES     (&ENO,
                  '&ENAME',     &EADD) NEW        1: INSERT    INTO
                  EMP    VALUES    (4, 'RAM',   ‘MUMBAI’)
      ➢  Inserting Data Into A Table From Another Table
         Syntax: INSERT    INTO   tablename   SELECT    col_name,  col_name
                  FROM    table_name [WHERE      <condition>];
         Example:     INSERT INTO EMP2 SELECT * FROM EMP1;
         SELECT     (Retrieving    Data   Using Query)
      SQL  SELECT   Statement   is used  to fetch the  data from a   database  table
      which  returns data in the form of result table. These result     tables are
      called result-sets. The  SELECT command is used to       retrieve rows
      selected from   one or  more tables.
      ➢  All Rows and All Columns




11
`````

## Page 12

![Original page 12](assets/01_DDL_commands/page-012.jpg)

### Extracted text

`````text
                                                       U n i t - 0 1  DDL Commands

         Syntax: SELECT * FROM            <
                    TableName      >;
                    SELECT * FROM
                    EMP;
      It will display all  the  data  from  all rows and    columns   from  the  table.
      ➢   Filtering Table Data
      While   viewing   data from   a table, it is rare that all  the data  from  the
      table  will be required   each  time.  So, SQL   provides   a method    of
      filtering table  data  that is not required.   Ways   for filtering data  are:
                1.  Selected  columns and     all rows
                2.  Selected   rows and all columns
                3.  Selected  columns    and selected rows
       1. Selected Columns and All Rows
      It will display all records    with specific fields that user has specified
      with SELECT command.
       Syntax:   SELECT  <Col_Name1>,<Col_Name2>,…..<Col_NameN>  FROM                        <
       TableName  >;
        Example:       SELECT * FROM EMP;
       2.   Selected Rows and All Columns
      Syntax:    SELECT     *  FROM     <  TableName      >  WHERE      <  Condition    >;
      Example:         SELECT * FROM EMP              WHERE ENO=10;
      The Oracle engine displays only those records that satisfy the specified
      condition after WHERE        will become    true.  WHERE      clause   applies  a
      filter on  the rows   retrieved.
      When a WHERE clause is added to the              SQL query, the Oracle engine
      compares  each  record  in  the  table  with  the  condition  specified  in
      WHERE clause. All operators such as logical,            arithmetic,   etc. can   be
      used   in the  condition of   WHERE      clause.
       3. Selected Columns and Selected Rows
      Syntax: SELECT       <Col_Name1>,       <Col_Name2>,….<Col_Name             N>  FROM
                 <TableName> WHERE            <  Condition    >  ;
      Example:       SELECT     ENO,    ENAME      FROM     EMP    WHERE      ENO=10;
      It  will  display  all  records   with   specific  fields  after  specified  condition
      WHERE will be true.
      ➢   ELIMINATING DUPLICATE ROWS




12
`````

## Page 13

![Original page 13](assets/01_DDL_commands/page-013.jpg)

### Extracted text

`````text
                                                        U n i t - 0 1  DDL Commands

       DISTINCT    command      is used to   retrieve only distinct     or unique    data.
       In a table, there may be     a chance    to exist a  duplicate   value  and we
       want to retrieve    only  unique values. SQL     SELECT     UNIQUE    and   SQL
       SELECT    DISTINCT    statements    are  same.
       Syntax:   SELECT     DISTINCT      <Col_Name1>,
       <Col_Name2>,…<Col_NameN>             FROM     < TableName>; OR
                          SELECT DISTINCT * FROM <TableName>;
       Example:       SELECT     DISTINCT      ENO,    ENAME      FROM     EMP;    OR
                  SELECT DISTINCT * FROM EMP;
       DISTINCT clause allows removing duplicates from the result set. This
       clause can be used only with SELECT statement. It scans all the values of
       the specified columns and display only unique values. It eliminates rows
       that have   exactly same    contents in each column.
       ➢   Arithmetic calculation
       Example:    Select employee      name,   salary   and  compute     salary *
       0.05  for each   row retrieved:    SELECT     ename,   sal, sal * 0.05
       “Salary”  from   emp;
       Here  the default output column sal*0.05         is renamed with      Salary.
         DELETE      (Deleting     Data)
          ▪  The   DELETE    statement    only  deletes  the rows   from   the table
             based   on  the condition   defined   by  WHERE     clause  or delete  all
             the  rows   from  the  table  when condition is    not  specified.  But  it
             does   not free  the  space  containing   by  the  table.

          ▪  But  The   TRUNCATE      statement:   it is used  to delete  all the  rows
             from   the  table and  free  the containing   space.
         Syntax: DELETE        FROM <     Table_Name       >  [WHERE      <  condition    >];
          ▪  If WHERE     clause   is not  specified  then   all rows   will be  deleted.
          ▪  If WHERE     clause  is specified  then  it will delete  all rows   that
             satisfy  the condition specified    after WHERE.
         Example:      DELETE      FROM  EMP;        // it will delete all the   records
         from   a CUST table.
                    DELETE      FROM     EMP    WHERE       CUSTNO      >  10;




13
`````

## Page 14

![Original page 14](assets/01_DDL_commands/page-014.jpg)

### Extracted text

`````text
                                                      U n i t - 0 1  DDL Commands

                   It will delete  all the records for which     CUSTNO is    greater than
                   10.
        UPDATE (Updating A            Contents Of A Table)
      The UPDATE statement changes data           in existing  rows   either by  adding
      new data    or modifying existing    data.
      User   can  update
      ➢   all rows  from   table
      ➢   selected  rows from table
      Syntax:   UPDATE      <Table_Name>       SET
      <ColumnName1>=<Expression1>,<ColumnName2>=
      <Expression2>……,        <ColumnNameN>=<ExpressionN>                [ WHERE
      <Condtion>      ] ;
                                OR
      UPDATE table_name SET column_name = expression WHERE conditions
      Example:     UPDATE      EMP    SET   CITY   =  ‘BARODA’;
      ➢    All rows from table: If   you are   not specifying any    condition,
          this will update entire table.    UPDATE     EMP    SET   SALARY     =
          500;
                   UPDATE      EMP    SET   ADDRESS      =  'Pune',   SALARY     =
                   1000.00;
      ➢   selected rows      from table
             UPDATE      EMP    SET   CITY   =  ‘BARODA’     WHERE      ENO
                                          =  10;
         TCL: Transaction        Control    Language
      TCL   commands     are  used   to manage    transactions   in  database.
      These   are  used  to manage the change which is made in the
      database by a DML statement will be called as           a transaction. We
      need to control    these transactions     made   by  DML statements.     It also










      allows statements to be grouped together into logical transactions.




14
`````

## Page 15

![Original page 15](assets/01_DDL_commands/page-015.jpg)

### Extracted text

`````text
                                                         U n i t - 0 1  DDL Commands

       Change will    not  reside permanently      in the  database, unless auto
       commit option enabled in the session. Those changes will               reside in
       temporary memory. So, we need to handle these                changes.   TCL
       statements will     be  used for   this  purpose.
       TCL statements are:
               COMMIT
               ROLLBACK
               SAVEPOINT
        ➢  COMMIT       (used    to permanently        save   any    transaction     into
           database):
               The   COMMIT      command is      used  to  save changes invoked by         a
          transaction    to the database.    The   COMMIT      command      saves   all
          transactions    to  the  database    since  the last  COMMIT      or ROLLBACK
          command.      TCL   are  only  used   with  the  DML    commands INSERT,
          UPDATE      and  DELETE     only.  They   cannot    be  used   while  creating
          tables  or dropping     them because     these operations are automatically
          committed in     the  database. Syntax: COMMIT;
          If Auto  commit    option   for session   is enabled,   then  this is not
          required   as  commit takes    place  automatically.    DDL   statements    will
          run  implicit  commit.
        ➢  Rollback     command        (restores    the database to        last  committed
           state)
               Rollback will be used to       reject the changes made        by  DML
          statements in     the database. If   auto   commit option enabled in the
          session, then there is no use with Rollback statements as transactions
          will be  committed automatically.
               If we  give  Rollback    then  any   pending   changes    in  the  database
          which   are  made by     DML   statements    will  be  rejected.  It is also  use
          with  savepoint    command     to  jump to   a savepoint   in  a transaction.
          Syntax:      Rollback;          OR          rollback  to savepoint-name;
        ➢  Savepoint      command
          Savepoint command is used          to temporarily     save a transaction     so
          that  you  can rollback to that point whenever necessary.
          Syntax:      savepoint    savepoint-name;




15
`````

## Page 16

![Original page 16](assets/01_DDL_commands/page-016.jpg)

### Extracted text

`````text
                                                         U n i t - 0 1  DDL Commands

          Example: Savepoint      and   Rollback on class table,

                       I       NAM
                       D       E
                       1       abhi
                       2       adam
                       4       alex
              SQL>   INSERT     into  class   values
              (5,'Rahul'); SQL>     Commit;
              SQL>   UPDATE     class  set
              name='abhijit'    where    id='5'; SQL>
              savepoint   A;
              SQL>   INSERT     into  class   values
              (6,'Chris'); SQL>    savepoint     B;
              SQL>   INSERT     into  class   values
              (7,'Bravo'); SQL>     savepoint     C;
              SQL>    SELECT * from         class;
                             I       NAM
                             D       E
                             1       abhi
                             2       adam
                             4       alex
                             5       abhijit
                             6       chris
                             7       bravo
          Now rollback     to
          savepoint B
          SQL>    Rollback    o  B;
          SQL>    SELECT * from       class;
          The  resultant  table  will look  like



                                            ID      NAM
                                                    E



16
`````

## Page 17

![Original page 17](assets/01_DDL_commands/page-017.jpg)

### Extracted text

`````text
                                                          U n i t - 0 1  DDL Commands

                                             1       abhi
                                             2       adam
                                             4       alex
                                             5       abhijit
                                             6       chris

          ow rollback to
          savepoint A
          SQL>    Rollback
          to  A;
          SQL>    SELECT *
          from   class; The
          result table will
          look like
                         I       NAM
                         D       E
                         1       abhi
                         2       adam
                         4       alex
                         5       abhijit
          DCL : Data Control Language
           DCL   commands      are  used to enforce      database    security   in a
        multiple user database environment.            These   statements will be used
        by  DBA   people    to control   the  access of users to the database. Only
        Database Administrator's or owners of the database object can
        provide /    remove privileges      on a   database    object.  DCL statements:
                  1. GRANT
                  2. REVOKE
     1) GRANT: GRANT          is a command      used   to  provide    access  or
         privileges   on  the  database objects     to  the  users.  We   can give    any
         type  of  permissions     to the  users on    the database     using   grant
         command.



17
`````

## Page 18

![Original page 18](assets/01_DDL_commands/page-018.jpg)

### Extracted text

`````text
                                                         U n i t - 0 1  DD   L Commands

          Syntax:   GRANT     privilege_name    ON   object_name     TO
                  {user_name|PUBLIC|role_name} [WITH             GRANT     OPTION];


  privilege_name            It is the  access  right or  privilege  granted   to the  user.
                            Some   of  the
                            access   rights  are  ALL,  EXECUTE,     and   SELECT.
  object_name               It is the  name   of a database    object  like  TABLE,   VIEW,
                            STORED
                            PROCEDURE        and   SEQUENCE.
  user_name                 It is the  name   of the user   to whom     an  access  right is
                            being   granted.
  PUBLIC                    It is used  to  grant  access rights to    all users.
  ROLES                     They   are  a set of  privileges  grouped   together.
  WITH GRANT                It allows a user to    grant access rights to other users.
  OPTION

         Example:      GRANT      SELECT     ON   EMP    TO   BCA;
         This command grants        a SELECT permission on        employee table      to
         user1.
           ➢  if we want    to give Select   permission on     all the database tables    to a
              user
               Syntax:      GRANT     SELECT     ANY    TABLE     TO   user_name;
               Example: GRANT        SELECT     ANY    TABLE     TO   BCA;

           ➢  if  we  want  to  give  select  permission  on
              specific table then Syntax:      GRANT SELECT
              ON   tab_name   TO   user_name;         Example:
              GRANT     SELECT     ON   EMP     TO  BCA;
           ➢  If we want to    give Create table
              permission then, Syntax:        GRANT
              CREATE     TABLE    TO  user_name;
              Example:  GRANT       CREATE     TABLE
              TO   BCA;
              Like  this we  can give any privilege to the users on the         database.
        2) REVOKE:



 18
`````

## Page 19

![Original page 19](assets/01_DDL_commands/page-019.jpg)

### Extracted text

`````text
                                                        U n i t - 0 1  DDL Commands

       Revoke will    be  used to   remove user     access  permissions which      are
      granted previously      to the  users  on  the  database.
       Syntax: REVOKE        privilege_name     ON   object_name     FROM
       {user_name|PUBLIC|role_name};
            Example: REVOKE          SELECT     ON    EMP    FROM     BCA;
          ➢  if we want to    give  Select permission on all the database tables to a
             user,
             Syntax:       REVOKE      SELECT     ANY    TABLE     TO   user_name;
             Example: REVOKE          SELECT     ANY    TABLE     TO   BCA;
          ➢  If we want to    give select permission on
            specific table   then Syntax:           REVOKE
            SELECT     ON  tab_name     TO  user_name;
            Example: REVOKE          SELECT     ON   EMP    TO
            BCA;
          ➢  If we  want  to give   Create table
            permission     then, Syntax:
             REVOKE     CREATE     TABLE    TO
            user_name; Example:              REVOKE
            CREATE      TABLE    TO   BCA;
            Like this we can     give  any  privilege to   the  users  on  the database.
         ROLES
          ▪  A  role is a  privilege  (license) or set of    privileges that   allows a
             user to perform certain functions in the database.
          ▪  When    there  are  many   users  in a  database   it becomes    difficult to
             grant  or  revoke   privileges  to  users.
          ▪  Therefore,   if you  define  roles, you  can  grant   or revoke   privileges
             to  users, thereby automatically     granting   or revoking   privileges.
             Syntax:    CREATE      ROLE     role_name;     Example: CREATE         ROLE
             ASSISTANT;
       ➢   After creating role    to assign  permission    to newly   create role
             Example:      GRANT      CREATE      TABLE,    CREATE      SESSION     TO
             ASSISTANT;
       ➢   After assigning    permission to role then you        can  that permission to
           user by using    role.
             Example:      GRANT      ASSISTANT      TO   BCA;
       ➢   If WITH ADMIN        OPTION    is used,  that user can    then   grant




19
`````

## Page 20

![Original page 20](assets/01_DDL_commands/page-020.jpg)

### Extracted text

`````text
                                                      U n i t - 0 1  DDL Commands

             roles to  other users. Syntax:     GRANT     <ROLE_NAME>         TO
             <USER_NAME>        WITH    ADMIN     OPTION; Example:
                         GRANT     ASSISTANT     TO   BCA   WITH    ADMIN
             OPTION;
       ➢   If role is removing   then  user cannot login because users        have
           permission    of the role.
             Example:         DROP    ROLE    ASSISTANT       CASCADE;

      Three type roles:
             Connect
             Resource
             DBA    (or database    administrator)
      Connect Role
      The  Connect role is the    entry-level role.  Connect role access can be
      granted permission with       a database.
      Example: GRANT        CONNECT       TO  BCA;    OR     REVOKE      CONNECT       TO
      BCA;
      Resource Role
      The Resource     role gives the user more access to Oracle databases.
      In addition   to the permissions that can      be granted   to  the Connect
      role, Resource roles     can  also be granted permission      to create
      procedures,    triggers, and  indexes.
       Example:REVOKEGRANT   RESOURCE RESOURCE TO TO BCA; BCA; OR

      DBA Role
      The DBA role includes all permission. Users with this role are able to do
      anything  they  want  to  the  database  system.  You  should  keep  the
      number of users with this role to a minimum to ensure system integrity.
      Example:      GRANT     DBA   TO   BCA;    OR      REVOKE     DBA    TO   BCA;
          Creating Users:     Create   a new   user   in the  database.
      Syntax:
      CREATE     USER    user_name     IDENTIFIED     {BY   password    |
      EXTERNALLY} [DEFAULT           TABLESPACE      tablespace_name]
      [TEMPORARY         TABLESPACE       tablespace_name]
      [QUOTA     {integer   [K|M]   | UNLIMITED}      ON   tablespace]    [PROFILE
      profile];
      Example:     CREATE     USER    BCA



20
`````

## Page 21

![Original page 21](assets/01_DDL_commands/page-021.jpg)

### Extracted text

`````text
                                                   U n i t - 0 1  DDL Commands

                  IDENTIFIED     BY   SANGOLA
                  DEFAULT      TABLESPACE
                  SYSTEM
                  TEMPORARY
                  TABLESPACE
                  TEMP QUOTA
                  UNLIMITED      ON
                  SYSTEM;
                               OR
                  CREATE     USER    BCA   IDENTIFIED     BY   SANGOLA;
      ➢  To assigning permission    to user  one or  more permission using
         without role command.
            Syntax:   GRANT     <Permission>     TO   USERNAME;
            Example: GRANT        CONNECT      TO   BCA;
                      GRANT     CONNECT,      CREATE    TABLE,    CREATE     SESSION
                      TO   BCA;
      ➢  To  change  the user’s  password:
            Example: ALTER        USER   BCA   IDENTIFIED      BY  SANGOLA;

      ➢  To change the   default table space:
            Example: ALTER        USER    BCA   DEFAULT     TABLESPACE        USERS;
      ➢  To remove a user entry from system        database.
            Syntax:    DROP    USER    USER_NAME       [CASCADE];
            Example: DROP        USER    BCA   CASCADE;
            OR
            DROP    USER    BCA;
      If the CASCADE option     is used, all objects owned by    username are
      dropped along    with the  user's  account.  If CASCADE    is not used  then
      user  still owns  objects, that user  is not dropped.   This feature is
      confusing, but  it is useful to drop  users.
      ➢   To connect other   user and   another  user  table data  and also  perform
          DML   operation.
            CREATE     USER   BCA   IDENTIFIED
            BY  SANGOLA; CREATE         USER
            BCS   IDENTIFIED     BY   SANGOLA;



21
`````

## Page 22

![Original page 22](assets/01_DDL_commands/page-022.jpg)

### Extracted text

`````text
                                                     U n i t - 0 1  DDL Commands

      After creating  two  users  then assign permission     to both  user.
            CREATE      ROLE    ASSISTANT;
            GRANT     CREATE     TABLE,    CREATE
            SESSION     TO  ASSISTANT;      GRANT
            ASSISTANT      TO   BCA;
            GRANT     ASSISTANT      TO   BCS;
      After granting permission then      user bca create a
            table  stud CREATE      TABLE    STUD    (ID   INT,
            NAME     VARCHAR2       (10));
      Insert one  record  in the table  stud
            INSERT     INTO    STUD    VALUES     (1,’SHYAM’);
      Connect to another user bcs      and use stud    table for DML operation but
      before performing operation      to  grant  DML   permission    to user  bcs.
            CONNECT       BCA/SANGOLA
      Syntax:   GRANT     <Permission>     ON   <  table name>
            TO   <username>; GRANT         SELECT,    INSERT,
            UPDATE,     DELETE     ON   STUD    TO  BCS;
            CONNECT      BCS/SANGOLA
            INSERT     INTO    BCA.STUD
            VALUES      (2,’RAM’); SELECT *
            FROM      BCA.STUD;
      When    revoke  permission then access is denied for
            specified user CONNECT       BCA/SANGOLA
            REVOKE      SELECT     ON   STUD    FROM     BCS;

         SQL operators and         clauses
      The symbols which      are used  to perform logical and mathematical
      operations in SQL are called     SQL operators.    SQL  reserved   words or
      characters are    known   as  operators.
      Generally  there  are three  types  of operators  in SQL:
         1. SQL   Arithmetic  Operators
         2. SQL   Comparison     Operators
         3. SQL   Logical  Operators



22
`````

## Page 23

![Original page 23](assets/01_DDL_commands/page-023.jpg)

### Extracted text

`````text
                                                         U n i t - 0 1  DDL Commands


      ➢   SQL Arithmetic Operators:
         Arithmetic    operators   in SQL are used     to perform    mathematical
         calculations like addition, subtraction, multiplication,        division   and
         modulus in SQL      statements.
                     Operators/OperationArithmetic          Example
                           +  (Addition)                        A+B
                        –   (Subtraction)                       A-B
                       *   (multiplication)                    A*B
                           /  (Division)                        A/B
                          %   (Modulus)                        A%B
      ➢   SQL Comparison Operators:
         Relational   operators    in SQL are used to     find the relation between       two
         columns. i.e. to compare       the  values   of two   columns    in SQL   statements.

              Operators                          Example/Description
                    >           x  >  y (x  is greater    than  y)
                    <           x  <  y  (x  is less  than   y)
                   >=           x >=   y  (x is  greater   than   or equal   to  y)
                   <=           x  <=   y (x  is less  than   or  equal   to y)
                    =           x  ==  y  (x  is equal   to  y)
              !=   or  <  >      x !=   y or  x  <>   y  (x  is not  equal   to  y)
                    !<           x !<   y (x   is not  less  than y)
                    !>           x !>   y (x is  not   greater   than  y)


      ➢   SQL Logical Operators:
         Logical operators      in SQL are used to perform         logical operations     on
         the given expressions in       SQL   statements. There are many operators
         in  SQL  which    are  used  in SQL   statements     in the  WHERE      clause.
         They   are
        Operator                                   Description
       AND             The AND operator       in  SQL  is used   to compare     data  with
                       more    than  one condition. If all   the  conditions returns
                       TRUE then      only it will display   records.





23
`````

## Page 24

![Original page 24](assets/01_DDL_commands/page-024.jpg)

### Extracted text

`````text
                                                          U n i t - 0 1  DDL Commands

       OR               The OR operator      in SQL is   used to compare data with
                        more than     one condition. If    either  of condition is TRUE
                        it will return   data.
       ALL              The ALL operator      in SQL   returns true when       value
                        matches    with all  values in single    column    set  of values.
                        It’s like AND operator it      will  compare     value against
                        with  all values in    column.
       ANY              The Any operator      in SQL returns     true when value
                        matches    with any    value in single   column     set of  values.
                        It’s like OR operator it     will  compare     value against    with
                        any  value   in column.
       LIKE             The LIKE operator in SQL is used to search for
                        character string with specified pattern using           wildcards
                        in column.
       IN               The IN operator in SQL is       used to search for specified
                        value  matches any
                        value in  set  of multiple   values.
       BETWEEN          The BETWEEN operator           in SQL   is  used   to get  values
                        within   range.
       EXISTS           The EXISTS operator        in SQL   is used   to show    result  if
       NOT              subquery    returns    data.
                        The NOT operator in       SQL   is a negate operator that
                        means it   will show    data for   opposite   of conditions    what
                        we  mentioned in SQL statement.
       SOME             The SOME operator        in  SQL  is  used  to  compare     value
                        with  a  single  column set of values returned by
                        subquery. SOME must         match at least one      value in
                        subquery    and that value     must be preceded by
                        comparison operators.
       ➢  USING =, >, <, >=, <=, !=, <>
       Example:       select * from     student
                      where no      =  2; select *
                      from   student    where no
                      < 4; select * from




24
`````

## Page 25

![Original page 25](assets/01_DDL_commands/page-025.jpg)

### Extracted text

`````text
                                                         U n i t - 0 1  DDL Commands

                      student   where    no   > 3;
                      select * from student
                      where no <= 7; select *
                      from   student where no
                      >= 3; select * from
                      student   where no != 2;
                      select * from student
                      where no <> 2;
       ➢  Using And: This     will  give  the  output   when   all the  conditions   become
          true.
       Syntax:    select  * from   <table_name>      where    <condition1>     and
       <condition2>     and….
                 <condition    n>;
       Example:      select * from     student   where    no  =  2  and   marks    >=  200;
       ➢  Using OR: This     will  give the  output   when    either  one  of  the  conditions
          becomes    true.
       Syntax:    select * from <table_name> where            <condition1>     and
       <condition2> or ..
                 <conditionn>;
       Example: select * from         student    where    no  =  2 or   marks    >=   200;
       ➢  NOT   will negate   the  condition.  It will select the records
         where condition is      not satisfied.
       ➢  Range Searching: Oracle         provides    3  predicates    for searching    data  in
          a range.
           1.  BETWEEN
           2.  IN
           3.  IS
       1) Using Between
           ▪  BETWEEN       operator    is use  to select  data that   is within   a range    of
              values.
           ▪  BETWEEN operators         select rows that     contain  values within
              specified   lower  and upper     limit.

           ▪  Lower value must be written          first. Two values in    the range
              must   be linked with keyword        AND.
           ▪  BETWEEN       operators can be used       with numeric and       character data


25
`````

## Page 26

![Original page 26](assets/01_DDL_commands/page-026.jpg)

### Extracted text

`````text
                                                     U n i t - 0 1  DDL Commands

             types.
      Syntax:     select * from   <table_name>     where   <col>  between    <lower
      bound>    and
                 <upper    bound>;
      Example:        select * from student where marks between
       200 and    400; SELECT      EMPNO,     ENAME,     DEPTNO      FROM
       EMP    WHERE      DEPTNO>=15       AND DEPTNO<=25;
       Using Not Between
       We   can  use  NOT   BETWEEN      to select data  which   is not within   the
       range.
      Syntax:   select * from    <table_name>     where   <col>  not  between    <lower
      bound>    and
          <upper    bound>;
      Example:      select * from   student where marks not between
                 200 and 400; SELECT *           FROM    EMP    WHERE
                 EMPNO      NOT BETWEEN           10  AND    20;
      2) Using In
         ▪ If a value  is required  to be  compared   with  list of values  then IN
           predicate  is used.
         ▪ IN predicate   reduces the   need to  use  multiple  OR  conditions.
         ▪ Arithmetic operator (=) compares        a single value  to another single
           value.
       Syntax:    select * from <table_name> where <col> in (value1, value2,
       value3…valuen);
       Example:      select * from student     where   no  in  (1, 2, 3);
              SELECT     EMPNO,     ENAME,     DEPTNO     FROM     EMP    WHERE
              DEPTNO      10  OR
              DEPTNO=20;
              SELECTEMPNO,        ENAME,     DEPTNO      FROM     EMPWHERE
              DEPTNO IN      (20,30);
       Using Not In: NOT IN      predicate   is will select all the  rows  where
         value  does not   match the   list of values  specified
      Syntax: select   *  from  <table_name>     where   <col>   not  in(value1,
      value2,value3…valuen);
      Example: select * from        student  where no    not in   (1, 2, 3);
         SELECT    EMPNO,      ENAME,     DEPTNO      FROM     EMP   WHERE
         DEPTNO      NOT IN    (20,30);
      ➢  Using IS NULL:      IS NULL condition     is used to  test for a  NULL



26
`````

## Page 27

![Original page 27](assets/01_DDL_commands/page-027.jpg)

### Extracted text

`````text
                                                           U n i t - 0 1  DDL Commands

          value   in the  specified column.
       Syntax:     select * from <table_name> where <col> is null;
       Example: select *       from   student    where marks       is null;
               1)  If expression is a NULL value, the condition evaluates to TRUE.
               2)  If expression is not a NULL value, the condition evaluates to
                   FALSE.
       ➢  Using   Is Not Null: IS NOT NULL can             be  used    to  test
          for  NOT    NULL    value in   the   specified   column.
       Syntax:    select   * from    <table_name>       where    <col>   is not   null;
       Example:      select * from student         where marks is not null;
       ➢  Using Like
       This  will  be  used   to search   through    the  rows   of  database   column
       based   on  the  pattern you    specify.
       The   LIKE keyword selects       rows   containing    fields  that  match   specified
       portions   of character strings.     LIKE   is used   with  char,  varchar,   text, date
       time   and  small   date  time   data.  A wildcard allows     the  user  to  match fields
       that  contain certain letters.
       Syntax:    select * from      <table_name>       where     <col>   like  <pattern>;

               %        Any string    of zero or    more characters
                _       Any   single  character
               [ ]      Any single character       within    the  specified   range   (e.g., [a-f])
                        or
                        set  (e.g., [abcdef])
              [^]       Any single character       not  within   the specified range (e.g., [^a
                        –
                        f]) or   set  (e.g.,  [^abcdef])

       Example:
       i)  This  will  give   the  rows   whose
                marks    are  100. Select * from
                student where marks         like 100;
              NO         NAME          MARKS
              1          Sudha         100
       ii) This will give    the rows     whose    name



27
`````

## Page 28

![Original page 28](assets/01_DDL_commands/page-028.jpg)

### Extracted text

`````text
                                                         U n i t - 0 1  DDL Commands

              start with ‘S’. Select * from
              student   where    name    like 'S%';
              NO        NAME         MARKS
              1         Sudha        100
              2         Saketh       200
       iii) This will give   the rows    whose name
              ends with ‘h’. Select * from
              student   where    name    like '%h';
              NO        NAME         MARKS
              2         Saketh       200
              3         Ramesh       100
       iv)  This  will give the rows whose       name’s    second
              letter start  with  ‘a’. Select * from    student
              where    name   like  '_a%';
              NO        NAME         MARKS
              2         Saketh       200
              3         Ramesh       100
              4         Jagan        300
              5         Naren        400
              6         Madhu        100
              7         Rattu        300
       V) This   will give  the rows whose name’s third letter
               start  with ‘d’. Select * from     student    where
               name    like '   d%';
              NO        NAME         MARKS
              1         Sudha        100
              6         Madhu        100
       Vi) This will   give  the  rows whose     name’s    second   letter start  with   ‘t’
              from  ending.   select * from     student    where   name    like  '%_t%';
              NO        NAME         MARKS
              2         Saketh       200
              7         Rattu        100
       Vii) This will give   the rows whose name’s         third  letter start with ‘e’   from




28
`````

## Page 29

![Original page 29](assets/01_DDL_commands/page-029.jpg)

### Extracted text

`````text
                                                        U n i t - 0 1  DDL Commands

       ending.
               Select * from    student   where name       like '%e  %';

             NO         NAME        MARKS
             2          Saketh      200
             3          Ramesh      100
       Viii) This  will give  the  rows   whose    name
             cotains   2 a’s. select * from    student
             where name       like '%a%    a %';
             NO         NAME        MARKS
             4          Jagan       300
       You  have to specify the patterns in like       using underscore      (_).
      ➢  ORDER BY Clause
       The  SQL   ORDER     BY  clause   is used  for  sorting  data   in ascending    and
       descending    order based     on one or    more   columns.    Some   databases
       sort query   results in   ascending    order by   default.
       Syntax:
       SELECT expressions FROM tables WHERE conditions ORDER BY
       expression [ASC | DESC]; Sort       the  result  in ascending    order   by
       NAME    and   SALARY.
             SELECT * FROM EMP            ORDER BY ENAME, SALARY;
       To sort the result in descending order
             by NAME. SELECT * FROM EMP
             ORDER BY NAME DESC;
      ➢  GROUP BY Clause
        ▪  GROUP BY       clause  is  another   section   of  the  select  statement.
        ▪  This optional   clause   tells Oracle  to group rows based on       distinct
           values that exist for
           specified    columns.
        ▪  GROUP    BY   clause  creates   a data   set, containing   several   sets  of
           records   grouped together        based   on  a condition.
        ▪  A query containing a group by clause          is processed    in the  following
           way:
              1. Select all rows that   satisfy the  condition   specified in  the  where
                 clause.



29
`````

## Page 30

![Original page 30](assets/01_DDL_commands/page-030.jpg)

### Extracted text

`````text
                                                     U n i t - 0 1  DDL Commands


             2. From   these rows   form  groups according     to the group   by clause.
             3. Discard  all groups  that do  not satisfy the  condition in  the having
                clause.
             4. Apply  aggregate functions    to each group.
             5. Retrieve  values  for the columns   and aggregations    listed in the
                select clause.
      Syntax:
      SELECT    <ColumnName1>,        <ColumnName2>,       <ColumnNameN>,
      AGGREGATE_FUNCTION (<Expression>)               FROM    TableName      WHERE
      <condition>    GROUP BY       <ColumnName1>,
      <ColumnName2>,        <ColumnNameN>;
      Example: SELECT         DNO,    SUM(SAL)      FROM    EMP    GROUP      BY   DNO;

     ➢  HAVING      Clause
         ▪  HAVING     clause  can  be used   in conjunction with the     GROUP    BY
            clause.
         ▪  HAVING imposes a condition on the GROUP BY clause, which
            further filters the groups    created  by  the  GROUP    BY  clause.

         ▪  Each column specification specified in the HAVING           clause must
            occur within a statistical function or must occur in the list of
            columns named in the GROUP BY clause
      Syntax:
      SELECT    <ColumnName1>,        <ColumnName2>,       <ColumnNameN>,
      AGGREGATE_FUNCTION (<Expression>)               FROM    TableName      WHERE
      <condition>    GROUP BY       <ColumnName1>,
      <ColumnName2>,        <ColumnNameN>         HAVING
      AGGREGATE_FUNCTION            (<Expression>)
      <operator>    <value>;
      Example:      SELECT DNO, COUNT (ENO) FROM EMP GROUP
      BY DNO HAVING COUNT              (ENO)     >  2;
      Rules for Group By and having Clause
           Columns listed    in the  select statement have to     be listed in the
            GROUP BY clause
           Columns    listed  in the GROUP BY      clause  need  not  be
                   listed in the  SELECT statement.



30
`````

## Page 31

![Original page 31](assets/01_DDL_commands/page-031.jpg)

### Extracted text

`````text
                                                          U n i t - 0 1  DDL Commands


             Only   group   functions    can  be  used   in the  HAVING      clause.
             The  group    functions listed in the having        clause need not     be
                     listed  in the SELECT statement.
                           Where                                              Having
           1.Without group      by  clause                     1.With   group   by clause
           2.  Where    clause   select  Row    before         2.Having    clause  select  after
                                                               grouping
           grouping.                                           3.Having clause     contain aggregate
           3. Where     clause can’t   contain   aggregate     Function.
           function.

          SQL    Functions
          Oracle functions can be used to          manipulate data and returning          the
          result. A function is performs a specific task. A function            can accept
          user-supplied     variables   or constants and perform operation            on
          them. Such variables / constants are           known as arguments.
          Function_Name          [ (argument-1,        argument-2,.)       ]
       Functions are
            1)  Scalar  Function    (Single   Row    Function)
            2)  Aggregate    (Group    Function)
            3)  Miscellaneous     Function
       ➢   Single Row Functions
              ▪  Functions that      work   on only one     value   at a time are called
                 SCALAR     Functions.
              ▪  A single row function returns         one  result for   every
                 row   of table / view mentioned         in query.
                 Example:    LENGTH      function   calculates length    of  one  string value.
              ▪  Single row functions can be grouped together depending on
                 the data   type of their arguments and return values.
                 Example: LENGTH function is related to string data type.
           Functions      can   be  classified    according to       different data       types
           are:
              1. Numeric Functions (For         Number data      type)
              2. Character /    String Functions (For       String   data type)
              3. Date  Function    (For Date    data   type)
              4. Conversion     Functions (For     Conversion of     one   data type to



31
`````

## Page 32

![Original page 32](assets/01_DDL_commands/page-032.jpg)

### Extracted text

`````text
                                                            U n i t - 0 1  DD     L Commands

                  another)
         ➢   Aggregate      functions
             ▪  Functions that     act  on a set of values are called Aggregate /
                Group Functions. Example: SUM function calculates                  total of a
                column.
             ▪  Group function returns a        single  result  row   for a group of rows.
             ▪  Aggregate    functions    can   appear    in SELECT     lists and   in ORDER
                BY  and   HAVING clauses.       They   are  commonly       used   with  the
                GROUP     BY  clause   in  a SELECT statement.
             ▪  Aggregate    functions perform a calculation         on a set   of values
                and return a single, or      summary,     value.
   Function                                           Description
      AVG         Returns   the  average  value  of  the  given  column  or  expression
                    Ex:  SELECT AVG (salary) AS          ‘Average    Salary’  FROM emp;
    COUNT         Number    of rows   where  the  value  of  the column   is not  NULL
                  Ex:   SELECT    COUNT    (dno)   AS   ‘Number    of  Deptwise    ’ FROM    emp;
                  Number    of rows  returned   including duplicates  and NULLs
  COUNT(*)         Ex:   SELECT    COUNT     (*) FROM      Employees     WHERE     eno  =  5;
                  Return Maximum       value of  the  given  column   or expression.    MAX  can  be
                  used with numeric,     character   and date   time  columns.   With character

      MAX         columns,    MAX   finds the  highest  value in   the collating   sequence.   MAX
                  ignores   any  null values.
                  Ex:    SELECT MAX (salary) FROM Emp;
      MIN         Return Minimum value of        the given   column or expression. MIN can be
                    used  with   numeric,   character    and  date   time  columns.    With

                    character columns,     MIN    finds  the value   that  is lowest   in the  sort
                    sequence.   MIN ignores     any   null values.
                     Ex:  SELECT       MIN (salary) FROM emp;
                    Returns the sum of all     the  values  given column     or  expression. SUM
      SUM           can be  used   with   numeric    columns    only.

                    Ex:   SELECT     SUM     (salary)   AS   ‘Total   Salary’   FROM      emp;
         ➢   Numeric Functions (For Number data type)
           ABS:     Absolute value is     the measure of the       magnitude of value.
            Absolute    value is always     a  positive   number.


 32
`````

## Page 33

![Original page 33](assets/01_DDL_commands/page-033.jpg)

### Extracted text

`````text
                                                           U n i t - 0 1  DDL Commands

       Syntax:   abs   (value)
       Ex:   select   abs(5),    abs(-5),    abs(0),    abs(null)      from    dual;
             ABS(5)               ABS(-5)       ABS(0)                ABS(NULL)

                       5                   -5               0
         SIGN:    Sign  gives   the
       sign  of  a value. Syntax:
       sign  (value)
       Ex:    select sign(5), sign(-5), sign(0), sign(null)
              from dual; SIGN(5)                         SIGN(-5)
                                    SIGN(0)              SIGN(NULL)

                     1              -1                      0
         SQRT:     This will give the square        root  of
       the given value. Syntax:       sqrt  (value) -- here
       value   must   be  positive.
       Ex:    select sqrt(4), sqrt(0), sqrt(null), sqrt(1) from dual;
       SQRT(4)              SQRT(0)               SQRT(NULL) SQRT(1)

                2                            0                                                1
         MOD:     This will give the     remainder. Syntax:       mod    (value,  divisor)
       Ex:  select   mod(7,4),      mod(1,5),     mod(null,null),       mod(0,0),     mod(-7,4)
       from    dual;
       MOD(7,4)        MOD(1,5)         MOD(NULL,NULL)MOD(0,0)                        MOD(-
       7,4)


              3        1                                    0                         -3
         NVL:    This  will substitute    the specified   value   in the
       place  of  null values. Syntax:    nvl  (null_col,
       replacement_value)
       Ex:    select * from student; -- here for 3rd row
              marks value is      null
              NO      NAME     MARKS
              1        a           100
              2        b           200




33
`````

## Page 34

![Original page 34](assets/01_DDL_commands/page-034.jpg)

### Extracted text

`````text
                                                             U n i t - 0 1  DDL Commands

               3       c
       select   no, name,    nvl(marks,300)
       from   student;

       NO       NAME
                NVL(MARKS,300)
       1        a            100
       2        b            200
       3        c            300
       select    nvl(1,2),    nvl(2,3),    nvl(4,3),    nvl(5,4)     from    dual;
       NVL(1,2)              NVL(2,3)              NVL(4,3)               NVL(5,4)
       1                     2                     4                      5
       select   nvl(0,0),    nvl(1,1),    nvl(null,null),    nvl(4,4)    from    dual;
       NVL(0,0)              NVL(1,1)              NVL(null,null)                       NVL(4,4)
                       0                    1                                    4
          POWER:       Power is    the   ability  to raise   a  value   to a
       given   exponent. Syntax:        power    (value,   exponent)
       Ex: select power(2,5), power(0,0),               power(null,null),
       power(2,-5) from dual;
       POWER(2,5)          POWER(0,0)              POWER(NULL,NULL)
       POWER(2,-5)
          32                                                                                                       1 .03125
           EXP:   This will raise e      value   to
       the  give   power. Syntax:      exp   (value)
       Ex:    select exp(1), exp(2), exp(0), exp(null),
       exp(-2) from        dual; EXP(1)            EXP(2)
       EXP(0)         EXP(NULL)                    EXP(-2)

       2.71828183       7.3890561                                      1  .135335283
          CEIL:   This will produce a whole number that is greater than or
           equal to the specified value.
       Syntax: ceil (value)
       Ex:    select ceil(5), ceil(5.1),        ceil(-5), ceil( -5.1), ceil(0),




34
`````

## Page 35

![Original page 35](assets/01_DDL_commands/page-035.jpg)

### Extracted text

`````text
                                                      U n i t - 0 1  DDL Commands

      ceil(null) from     dual; CEIL(5)                      CEIL(5.1)    CEIL(-5)
      CEIL(-5.1) CEIL(0)        CEIL(NULL)

      5              6            -5           -5            0
         FLOOR:    This will produce a whole number that is less than            or
          equal to  the specified value.
      Syntax: floor   (value)
      Ex:   select   floor(5),  floor(5.1),  floor(-5), floor( -5.1),     floor(0),
      floor(null)   from dual;
      FLOOR(5)FLOOR(5.1)                    FLOOR(-5)        FLOOR(-5.1)
      FLOOR(0)        FLOOR(NULL)

      5               5               -5               -6             0
         ROUND:     This will rounds numbers to        a given number of
      digits of  precision. Syntax:   round    (value, precision)
      Ex:   select   round(123.2345),       round(123.2345,2),
      round(123.2354,2)        from   dual; ROUND(123.2345)
      ROUND(123.2345,0)          ROUND(123.2345,2)           ROUND(123.2345,-
      2)

      123                   123                      123.23                    100
         TRUNC:    This will  truncates or chops off digits of
      precision from a number. Syntax:         trunc  (value,  precision)
      Ex:   select   trunc(123.2345),      trunc(123.2345,2),      trunc(123.2354,2)
      from   dual; TRUNC(123.2345)           TRUNC(123.2345,2)
      TRUNC(123.2345,-1)           TRUNC(123.2345,-2)

      123                   123.23                   120                        100

         GREATEST:      This  will give  the
      greatest   number. Syntax: greatest
      (value1, value2, value3    … valuen)
      Ex:  select  greatest (1,   2, 3),  greatest (-1, -2, -3)      from   dual;
      GREATEST       (1,2,3)             GREATEST(-1,-2,-3)



35
`````

## Page 36

![Original page 36](assets/01_DDL_commands/page-036.jpg)

### Extracted text

`````text
                                                              U n i t - 0 1  DDL Commands



               3                              -1
               Ø  If all the  values   are   zeros   then   it will  display   zero.
               Ø  If any   of one   or  all the  parameters      are  nulls  then   it will  display
               nothing.
          LEAST:     This   will  give   the  least
       number. Syntax: least (value1,
       value2, value3 … valuen)
       Ex:    select   least(1,    2, 3),   least(-1, -2, -3) from          dual;
       LEAST(1,2,3)                          LEAST(-1,-2,-3)
   1                                                     -3
               Ø  If all the  values   are   zeros   then   it will  display   zero.
               Ø  If any   of one   or  all the  parameters      are  nulls  then   it will  display
               nothing.

       ➢    String Functions
          INITCAP:      This  will capitalize    the  initial
       letter  of the   string. Syntax:    initcap    (string)
       Ex: select initcap('computer')
       from dual; INITCAP

       Computer
          UPPER:      This will convert the string
       into uppercase. Syntax:         upper    (string)
       Ex: select upper('computer')
       from dual; UPPER

       COMPUTER
          LOWER:       This  will convert the string
       into  lowercase. Syntax:        lower   (string)
       Ex:  select   lower('COMPUTER')
          from    dual; LOWER

       computer




36
`````

## Page 37

![Original page 37](assets/01_DDL_commands/page-037.jpg)

### Extracted text

`````text
                                                           U n i t - 0 1  DDL Commands


         LENGTH:       This  will  give
       length   of the string. Syntax:
       length   (string)
       Ex: select length('computer') from dual;
       LENGTH
               8
         RPAD:     This   will allows    you to pad the right side of        a
           column    with   any  set  of characters.
       Syntax: rpad     (string,  length [,  padding_char])
       Ex:  select  rpad('computer',15,'*'),
       rpad('computer',15,'*#')        from   dual;
       RPAD('COMPUTER'                     RPAD('COMPUTER'

   computer*******              computer*#*#*#*
       -- Default   padding character was blank space.
         LPAD:     This  will  allows  you   to pad   the  left side  of a  column
           with  any  set  of characters.
          Syntax:   lpad (string,   length   [, padding_char])
       Ex:    select  lpad('computer',15,'*'),
       lpad('computer',15,'*#')       from    dual;
       LPAD('COMPUTER'                     LPAD('COMPUTER'

    *******computer                        *#*#*#*computer
       -- Default   padding character was blank space.
         LTRIM: This will trim off unwanted characters from the
       left end of string. Syntax: ltrim       (string  [,unwanted_chars])
       Ex:    select ltrim('computer','co'),
       ltrim('computer','com')       from dual;
        LTRIM(         LTRIM
              mputer     puter

       select ltrim('computer','puter'),
       ltrim('computer','omputer') from dual;
       LTRIM('Csel LTRIM('C

           computer       computer



37
`````

## Page 38

![Original page 38](assets/01_DDL_commands/page-038.jpg)

### Extracted text

`````text
                                                              U n i t - 0 1  DDL Commands

       -- If you haven’t specify any         unwanted      characters it     will display    entire
       string.
          RTRIM:     This will trim off      unwanted      characters from the
          right end of string. Syntax:        rtrim    (string  [,
          unwanted_chars])
       Ex:    select   rtrim('computer','er'),
       rtrim('computer','ter')       from   dual;
       RTRIM(         RTRIM
           comput     compu
       select rtrim('computer','comput’),
       rtrim('computer','compute') from dual;
        RTRIM('C        RTRIM('C
          computer         computer
       -- If you haven’t specify any         unwanted      characters it     will display    entire
       string.
          TRIM:     This will trim off     unwanted characters from            the
       both sides of string. Syntax: trim (unwanted_chars from
       string)
       Ex:  select   trim(   'i' from 'indiani')    from dual;
       TRIM(
              ndian
       select trim( leading'i' from 'indiani') from dual;
       -- this will work as LTRIM TRIM(L
            Ndiani

       select   trim(   trailing'i'  from   'indiani') from     dual;
        -- this will work as RTRIM TRIM(T
              Indian
          TRANSLATE:         This will   replace    the  set of characters,
       character by character. Syntax: translate (string, old_chars,
       new_chars)
       Ex:    select translate('india','in','xy') from dual;
       TRANS



38
`````

## Page 39

![Original page 39](assets/01_DDL_commands/page-039.jpg)

### Extracted text

`````text
                                                             U n i t - 0 1  DDL Commands

           xydxa
          REPLACE:       This will replace      the set of characters,
       string by string. Syntax:        replace    (string,  old_chars    [,
       new_chars])
       Ex:    select   replace('india','in','xy'),
       replace(‘india’,’in’)    from    dual; REPLACE
              REPLACE

       Xydia            dia
          CONCAT:       This  will  be   used to
       combine      two   strings   only. Syntax:
       concat    (string1,   string2)
        Ex:   select concat('computer',' operator') from dual;
        CONCAT('COMPUTER'
            computer   operator
       If you want     to combine more than two strings you have to use
       concatenation operator (||).
       select 'how'      || ' are' || ' you'    from dual;
       'HOW'||'ARE
             how are  you
          ASCII:   This will return      the  decimal representation         in the database
           character set     of the first
       character    of
       the  string.
       Syntax:
       ascii
       (string)
       Ex:    select ascii('a'),
       ascii('apple') from dual;
       ASCII('A')       ASCII('APPLE')


       97                     97
          CHR:    This  will  return   the character having        the binary equivalent        to




39
`````

## Page 40

![Original page 40](assets/01_DDL_commands/page-040.jpg)

### Extracted text

`````text
                                                             U n i t - 0 1  DDL Commands

           the  string in either the database character            set  or the national
           character set.
       Syntax: chr (number)
       Ex:    select
       chr(97) from
       dual;
       CHR
           a

          SUBSTR:      This   will  be  used   to
       extract   substrings. Syntax: substr        (string,
       start_chr_count [, no_of_chars])
       Ex:select    substr('computer',2),        substr('computer',2,5),
       substr('computer',3,7)         from   dual;
        SUBSTR(              SUBSTR                  SUBSTR
         omputer             omput                   mputer

               Ø If no_of_chars    parameter is negative then          it will display nothing.
               Ø If both   parameters      except string    are  null  or zeros    then   it will
               display nothing.
               Ø If no_of_chars     parameter is greater       than   the  length of the string
               then it  ignores and     calculates based       on  the orginal string length.
               Ø  If start_chr_count   is  negative   then  it will  extract  the  substring    from
               right end.
               1       2     3       4      5        6     7      8
               C      O      M       P      U      T       E        R
               -8     -7     -6       -5    -4       -3     -2    -1
          INSTR:     This  will allows you for searching through a string for
       set  of characters. Syntax: instr        (string,  search_str    [,
       start_chr_count [, occurrence] ])
       Ex:    select   instr('information','o',4,1),
       instr('information','o',4,2)       from dual;
       INSTR('INFORMATION','O',4,1)
              INSTR('INFORMATION','O',4,2)





40
`````

## Page 41

![Original page 41](assets/01_DDL_commands/page-041.jpg)

### Extracted text

`````text
                                                          U n i t - 0 1  DDL Commands



                     4                                  10
          Ø  If you  are not specifying start_chr_count and occurrence then it
          will start search from     the  beginning    and  finds  first occurrence    only.
          Ø  If both  parameters    start_chr_count   and  occurrence   are  null, it will
          display  nothing.
       ➢   DATE FUNCTIONS
       Oracle   default date format is      DD-MON-YY.
       We   can  change   the  default  format   to our  desired   format   by  using the
       following command.
       alter  session   set nls_date_format      =  ‘DD-
       MONTH-YYYY’; But         this will  expire   once
       the  session   was   closed.
         SYSDATE:      This  will  give  the  current
       date and time. Ex:              select  sysdate
       from   dual;
       SYSDATE

       24-DEC-06
         CURRENT_DATE:          This   will returns    the  current   date in   the
       session’s timezone. Ex: select current_date           from dual;
       CURRENT_DATE

       24-DEC-06
         CURRENT_TIMESTAMP:               This  will return   the  current   timestamp
          with   the active  time zone    information.
       Ex:   select
       current_timestamp     from
       dual;
       CURRENT_TIMESTAMP

       24-DEC-06       03.42.41.383369         AM    +05:30
         SYSTIMESTAMP:          This will returns the system date, including
          fractional   seconds and time       zone   of the  database.




41
`````

## Page 42

![Original page 42](assets/01_DDL_commands/page-042.jpg)

### Extracted text

`````text
                                                       U n i t - 0 1  DDL Commands

      Ex:  select systimestamp
         from dual;
         SYSTIMESTAMP

      24-DEC-06       03.49.31.830099        AM    +05:30
          LOCALTIMESTAMP: This will returns local             timestamp in
          the active  time zone information, with       no  time  zone
          information shown.
      Ex: select
      localtimestamp     from
      dual;
      LOCALTIMESTAMP


      24-DEC-06       03.44.18.502874        AM
         DBTIMEZONE: This        will returns the current database time
          zone in  UTC format. (Coordinated        Universal   Time)
      Ex: select
      dbtimezone from
      dual; DBTIMEZONE

      -07:00
         SESSIONTIMEZONE: This          will  returns   the value   of the  current
      session’s   time  zone. Ex:           select sessiontimezone from        dual;
      SESSIONTIMEZONE

      +05:30
         TO_CHAR:     This will be used to     extract
      various date formats. Syntax:       to_char   (date,
      format)
      Ex:  select  to_char(sysdate,'dd month       yyyy hh:mi:ss am dy')       from dual;
      TO_CHAR(SYSDATE,'DD            MONTH      YYYYHH:MI

      24   december     2006   02:03:23    pm   sun



42
`````

## Page 43

![Original page 43](assets/01_DDL_commands/page-043.jpg)

### Extracted text

`````text
                                                       U n i t - 0 1  DDL Commands

      select  to_char(sysdate,'dd    month   year')  from   dual;
      TO_CHAR(SYSDATE,'DDMONTHYEAR')

      24 december two thousand six
      select  to_char(sysdate,'dd fmmonth year')        from
      dual; TO_CHAR(SYSDATE,'DD            FMMONTH
      YEAR')

      24 december two thousand six
      select to_char(sysdate,'ddth DDTH')
      from dual; TO_CHAR(S

      24th   24TH
      select  to_char(sysdate,'ddspth      DDSPTH')     from  dual;
      TO_CHAR(SYSDATE,'DDSPTHDDSPTH

      twenty-fourth    TWENTY-FOURTH
      select  to_char(sysdate,'ddsp     Ddsp   DDSP    ') from  dual;
      TO_CHAR(SYSDATE,'DDSPDDSPDDSP')

      twenty-four    Twenty-Four     TWENTY-FOUR
         TO_DATE: This will be used         to convert the string
      into data format.     Ex:  select to_char   ('24/dec/2006',
      'dd      *       month       *       day')      from        dual;
      TO_CHAR(TO_DATE('24/DEC/20

      24 * december * Sunday
      -- If you  are not  using to_char oracle will display output in default         date
      format.
         ADD_MONTHS:        This  will  add  the  specified  months
      to  the given   date. Syntax:  add_months      (date,
      no_of_months)
      Ex:   select  add_months       ('11-jan-
      1990'),   5)  from   dual; ADD_MONTHS


43
`````

## Page 44

![Original page 44](assets/01_DDL_commands/page-044.jpg)

### Extracted text

`````text
                                                        U n i t - 0 1  DDL Commands



       11-JUN-90
       select add_months ('11-jan-1990', -5)
       from dual; ADD_MONTH

       11-AUG-89
             Ø  If no_of_months    is zero  then  it will display
             the  same   date. Ø  If no_of_months    is null then   it
             will  display  nothing.
         MONTHS_BETWEEN:             This  will give  difference   of months
       between    two   dates. Syntax:   months_between        (date1,  date2)
       Ex:   select  months_between       ('11-aug-1990','11-jan-
            1990')   from   dual; MONTHS_BETWEEN               ('11-
            AUG-1990','11-JAN-1990')

              7
       select  months_between       ('11-jan-1990','11-aug-1990')
       from  dual; MONTHS_BETWEEN               ('11-JAN-1990','11-
       AUG-1990')

       -7
         NEXT_DAY:       This will produce next day of the given day from
       the specified date. Syntax:     next_day    (date,  day)
       Ex: select next_day ('24-dec-
       2006','sun') from dual; NEXT_DAY(

       31-DEC-06
       -- If the day parameter is null then it will display nothing.
         LAST_DAY:      This  will  produce last    day  of
       the given   date. Syntax:   last_day   (date)
       Ex: select last_day ('24-dec-
       2006','sun') from dual; LAST_DAY(




44
`````

## Page 45

![Original page 45](assets/01_DDL_commands/page-045.jpg)

### Extracted text

`````text
                                                         U n i t - 0 1  DDL Commands

       31-DEC-06
         EXTRACT:       This  is used   to extract   a portion    of the  date  value.
       Syntax:   extract  ((year   | month    | day  | hour   | minute    |
       second),   date) Ex:   select  extract  (year   from   sysdate)
       from   dual; EXTRACT(YEARFROMSYSDATE)

       2006
       -- You   can  extract   only  one   value  at  a time.






















































45
`````


---

# Source file: 06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2.md

# Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity (2)

- Original PDF: `notes\Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity (2).pdf`
- Pages: 50
- Preservation: every original page is rendered below; extracted text follows each page image.

## Page 1

![Original page 1](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-001.jpg)

### Extracted text

`````text
                                                                                                    B.Sc(ECS)-II Sem-III
                                                                                                        DBMS (2025-26)
What is SQL?
   ●   SQL (Structure Query Language) is a database language used for retrieve, manage and manipulate
       the data stored in relational databases (A relational database stores data in tables. Each table consists
       of rows (records or tuples) and columns (fields or attributes))
   ●   SQL is the primary way to interact with RDBMS like Oracle, MySQL, PostgreSQL, SQL Server, and
       SQLite etc. Further these RDBMS manages and manipulates the database with the help of SQL.
   ●   SQL was developed at IBM by Donald D. Chamberlin and Raymond F. Boyce in the early 1970s.
   ●   This SQL version is initially called SEQUEL (Structured English Query Language).

Characteristics or Properties or Features or Advantages of SQL:
1. Simple and easy to Learn:
    •   SQL uses High-level language (English language) to write the commands hence it is simple and easy
        to learn.
2. Case insensitive:
    •   SQL syntax is case insensitive means uppercase and lowercase letters are treated as the same.
    •    Eg. CREATE is same as create
3. Quick and Efficient:
    •   SQL retrieves large amount of data (i.e. records) from a database very quickly and efficiently.
4. Declarative Language:
    •   SQL specifies what to do (e.g., retrieve data), not how to do it.
    •   SQL Focuses on data and results, not procedures hence it is declarative.
5. Portable Across RDBMS platforms:
    •   SQL is Standardized i.e. it is ANSI SQL, so it works on multiple RDBMS platforms like MySQL,
        PostgreSQL, Oracle etc. with minor syntax differences.
6. Set-Based Processing:
    •   Operates on sets or bunch of data rather than row-by-row (though some row-level control exists).
7. Data Manipulation and Definition:
    •   SQL uses commands for data definition, retrieval and manipulation as follow-
    •   Data Definition Language (DDL) – CREATE, ALTER, DROP
    •   Data Manipulation Language (DML) – SELECT, INSERT, UPDATE, DELETE
    •   Data Control Language (DCL) – GRANT, REVOKE
    •   Data Query Language (DQL)- SELECT
    •   Transaction Control Language (TCL) – COMMIT, ROLLBACK, SAVEPOINT, SET TRANSACTION
8. Interactive and Embedded
             o   SQL Can be used Interactively via command-line or GUI tools.
             o   SQL can be Embedded in other languages such as Python, Java etc. through libraries like
                 JDBC, ODBC
9. Robust Query Capabilities:
             o   SQL Supports complex operations on database to make it as robust these operations are- Joins,
                 Subqueries, Grouping & aggregation, Sorting, Filtering
10. Integrity and Security:
             o   SQL enforces data integrity with Constraints (e.g., PRIMARY KEY, FOREIGN KEY)
             o   SQL provides Security by Permissions (access control)
11. Transaction Management:
             o   SQL    Supports    ACID     (Atomicity,     Consistency,     Isolation,   Durability)     properties    that
                 ensures safe and consistent data updates.

Components of SQL (Basic Structure of SQL) (Commands in SQL):
   ●   To interact with databases there is a need to learn different commands available in SQL.
   ●   SQL  is  made  up  of  different  types  of  commands  which  are  grouped  into  following  categories
       (Depending upon task of command):
`````

## Page 2

![Original page 2](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-002.jpg)

### Extracted text

`````text
       1)   Data Definition Language (DDL)
       2)   Data Manipulation Language (DML)
       3)   Data Control Language (DCL)
       4)   Data Query Language (DQL)
       5)   Transaction Control Language (TCL)
Let’s see these components in details-
1) Data Definition Language (DDL):
●   DDL (Data Definition Language) in SQL is used to define, create, modify, delete and manage database
    structures such as tables, schemas, indexes, and constraints etc.
●   DDL focuses on how data is stored, not the data itself.
●   These commands are used by DBA user (system user) such as database designer or application developer.
    Note that these commands are not used by general user.
●   These commands are immediate i.e. they are not having tendency to ROLLBACK. That is, once these
    commands are fired then it will not rollback to the previous state. There is no effect of ROLLBACK on
    these commands.
❖   Key Characteristics of DDL Commands:
1) Structure-Oriented: DDL commands deal with the structure of the database, not the data itself.
Examples include creating, altering, or deleting tables and other objects.
2) Auto-Commit: DDL statements automatically commit any changes made to the database.
You cannot roll back a DDL command once executed.
3) Implicit Transactions: Each DDL statement is treated as a complete transaction by itself.
There's no need (or option) to manually commit or rollback.
4) Affects Schema Objects:          DDL commands modify schema objects like tables, indexes, views, stored
procedures, etc.
5) Do Not Manipulate Data: DDL commands do not insert, update, or delete records or data; they only define
or change the structure of the database.
6) Access Control and Privileges: Executing DDL commands often requires higher access control and higher
privileges, such as DBA users.
7) Modifies Metadata: DDL commands directly affect the metadata stored in the data dictionary of the
DBMS.
Common DDL Commands in SQL are:
  DDL Commands                                                 Purpose
 CREATE                   Create database objects (tables, views, index etc.)
 ALTER                    Modify existing database structures.
 DROP                     Delete database objects (tables, views, index etc.)
 TRUNCATE                 Delete all rows from a table (faster than DELETE)
 RENAME                   Rename a database object. (tables, views, index etc.)

2) Data Manipulation Language (DML):
●   DML commands are used to           manipulate (storing, retrieving, modifying, & deleting) the data stored in
    database tables.
●   Unlike DDL, which deals with database structure, DML focuses on actual data stored in database tables.
●   DML commands are not auto-committed i.e. When DML commands are fired, changes are not permanent
    to the database; they can be rolled back.
❖   Key Characteristics of DML Commands:
1.  Data-Centric:
        ●    DML operates on the data within tables, not the schema or structure of the database.
        ●    It is used to insert, update, delete, or retrieve       records of the database table.
2.  Transactional Control:
        ●    DML statements are part of a transaction.
        ●    Changes are not permanent until a COMMIT is issued.
        ●    You can ROLLBACK changes if needed before committing.
3.  Requires Existing Structure:
        ●    DML commands operate on          existing tables created using DDL commands.
`````

## Page 3

![Original page 3](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-003.jpg)

### Extracted text

`````text
4.  Can Be Rolled Back:
        ●    DML operations can be undone using ROLLBACK, as they do not auto-commit by default.
5.  Affects Table Rows:
        ●    DML commands typically target rows—they add, change, or remove data from them.
6.  Permission-Based:
        ●    Users need appropriate privileges         (e.g., INSERT, UPDATE, DELETE, SELECT) to perform
             DML operations.
Common DML Commands in SQL are:
   DML Command                                            Purpose
 SELECT                      Retrieves data from one or more tables
 INSERT                      Adds a new row (Record) into a table.
 UPDATE                      Modifies existing table data in one or more rows
 DELETE                      Removes rows from a table.(slower than TRUNCATE)

3) Data Control Language (DCL):
●   DCL commands are used to control access of data in a database.
●   They manage permissions and security levels, ensuring that only authorized users can perform specific
    actions.
❖   Key Characteristics of DCL Commands:
1.  Permission Management:
        ●    DCL is used to grant or revoke user rights and permissions on database objects like tables,
             views, and procedures.
2.  Security-Focused:
        ●    DCL helps maintain data security and integrity by controlling access to data.
3.  Dependent on Privileges:
        ●    To use DCL commands, a user typically needs administrative privileges (like DBA or GRANT
             OPTION).
4.  Affects Access, Not Data or Structure:
        ●    DCL doesn’t alter data (like DML) or structure (like DDL). It only changes who can access and
             what in the database.
Common DCL Commands in SQL are:
  DCL Command                                          Purpose
 GRANT                    Gives specific privileges to user
 REVOKE                   Removes privileges from a user

4) Data Query Language (DQL):
●   DQL stands for Data Query Language, and it is primarily used to retrieve data from database objects.
●   SELECT command also belongs to DQL, when SELECT is fired against a table or tables, then the result
    is compiled into a temporary table which is displayed at the front-end.
●   DQL is    technically a subset of DML, it's often treated as a separate category               because of its specific
    purpose: querying data without modifying it.
Key Characteristics of DQL Commands:
1.  Data Retrieval Only:
        ●    DQL is used only to query data, not to insert, update, or delete it.
        ●    It does not change the data or database structure.
2.  Centered Around the SELECT Statement:
        ●    The core and only DQL command is SELECT.
        ●    It is used to only fetch data from one or more tables, views, or other database objects.
3.  Non-Transactional:
        ●    Since DQL does not modify data, it is      not part of a transaction      and does not require COMMIT
             or ROLLBACK.
4.  Highly Flexible and Powerful:
        ●    SELECT can retrieve specific columns, filter rows, join multiple tables, group results, and apply
             functions.
`````

## Page 4

![Original page 4](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-004.jpg)

### Extracted text

`````text
5.  Does Not Require High Privileges:
        ●   Most users with basic read access can use DQL, provided they have SELECT privileges on the
            target objects.
Common DCL Commands in SQL are:
   DQL Command                                   Purpose
 SELECT                     Retrieves data from the database objects.

5) Transaction Control Language (TCL):
●   TCL statements are used to manage the changes made by DML statements.
●   TCL commands are used to manage transactions in a database. A transaction is a sequence of operations
    performed as a single logical unit of work, and TCL ensures that these operations are executed reliably
    and consistently.
●   These commands can cancel changes made by DML commands using ROLLBACK and also it can make
    changes permanent using COMMIT.
●   TCL allows several statements to be grouped together as logical transactions and allows to set a marker
    (savepoint) within that transaction so we can roll back only these statements.

❖   Key Characteristics of TCL Commands:
    1.  Transaction Management:
            ●    TCL commands control when and how changes made by DML statements are saved or
                 undone in the database.
    2.  Ensures Data Integrity:
            ●    TCL helps to    maintain ACID properties (Atomicity, Consistency, Isolation, Durability) of
                 transactions.
    3.  Works with DML:
            ●    TCL applies only to DML operations (INSERT, UPDATE, DELETE) and has no effect on
                 DDL or DCL (which usually auto-commit).
    4.  Explicit Control of Changes:
            ●    Changes made using DML are not permanent (not auto commit) until COMMIT is issued.
            ●    You can undo changes using ROLLBACK before committing.
    5.  Savepoints for Partial Rollback:
            ●    SAVEPOINT allows setting a marker (savepoint) within a transaction so you can roll back
                 only some part of the transaction if needed.
Common TCL Commands in SQL are:
       TCL Commands                                                        Purpose
 COMMIT                              Saves all changes made during the transaction permanently
 ROLLBACK                            Undoes changes made during the transaction
 SAVEPOINT                           Sets a point in a transaction to roll back to selectively
 SET TRANSACTION                     Sets properties for the current transaction (like mode or isolation level)
Following diagram shows Classification of SQL commands:
`````

## Page 5

![Original page 5](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-005.jpg)

### Extracted text

`````text
Rules to use SQL: (Rules to use SQL commands):

There are following rules which are used while entering SQL commands-
1)  SQL starts with a verb (i.e. a SQL action word).
    Example: SELECT statements. This verb may have additional adjectives like FROM
2)  Each verb is followed by number of clauses.
    Example: FROM, WHERE, HAVING etc.
3)  Each verb and clause are separated from each other by space.
    Example: DROP   TABLE   EMP;
4)  A comma (,) separates parameters.
    Example: SELECT   rollno, name   FROM   student;
5)  SQL statement is terminated with a semicolon (;)
6)  Reserved words cannot be used as identifiers (Name given by programmer for table, table field, function,
    variable etc.)
7)  Identifiers are can be combination of alphabets, digits or underscore _
8)  Identifiers must start with alphabets or underscore. i.e. it does not start with digit.
9)  Length of identifier is up to 30 characters long.
10) Special characters like # , %, @ etc. also spaces are not allowed in identifier.
11) Character and date constants (literals) must be enclosed within single quotes like ‘01-may-2001’ or ‘10d’
SQL reserve words:
•   To learn SQL, we have to know different reserve words available in it.
•   The total number of SQL reserved words varies depending on the specific SQL standard (SQL
    version) or the particular database system. The most commonly used SQL reserve words are-
 SQL Keyword                                                        Description
 SELECT               Used to retrieve data from a database.
 FROM                 Specifies the table(s) from which to retrieve data in a SELECT statement.
 WHERE                Filters records based on a specified condition in SELECT, UPDATE, or DELETE
                      statements.
 INSERT               Used to add new rows of data into a table.
 INTO                 Used with INSERT to specify the target table.
 VALUES               Used with INSERT to specify the data values to be inserted.
 UPDATE               Used to modify existing data in a table.
 SET                  Used with UPDATE to specify the new values for columns.
 DELETE               Used to remove rows from a table.
 CREATE               Used to create new database objects like tables, views, indexes, or databases.
 TABLE                Used with CREATE to define a new table.
 ALTER                Used to modify the structure of an existing database object.
 DROP                 Used to remove database objects from the database.
 AND                  A logical operator used to combine multiple conditions in a WHERE clause.
`````

## Page 6

![Original page 6](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-006.jpg)

### Extracted text

`````text
 OR                   A logical operator used to combine multiple conditions in a WHERE clause.
 NOT                  A logical operator used to negate a condition.
 NULL                 Represents a missing or unknown value.
 ORDER BY             Sorts the result set of a query.
 GROUP BY             Groups rows that have the same values in specified columns into summary rows.
 HAVING               Filters groups based on a specified condition, used with GROUP BY.
 JOIN                 Combines rows from two or more tables based on a related column between them.
 AS                   Used to assign an alias to a column or table.
 DISTINCT             Used with SELECT to retrieve only unique values.
 PRIMARY              A constraint that uniquely identifies each record in a table.
 KEY
 FOREIGN              A constraint that links two tables together.
 KEY
 CHECK                A constraint that limits the value range that can be placed in a column.
 CONSTRAINT           Adds or deletes a constraint on a table.

SQL data types used in Oracle:
Oracle SQL provides a range of built-in data types to store various kinds of information.
The following table shows commonly SQL data types used in Oracle along with their descriptions and
typical uses:
          Data Type                                   Description                                       Typical Use
 VARCHAR2(size)                   Variable-length character string up to size              Storing text strings of variable
                                                                                           length
 CHAR(size)                       Fixed-length character string of length size             Storing text strings of fixed
                                                                                           length
                                  Numeric data with precision p and scale s
                                  E.g.
                                     Definition           Allowed            Notes
                                                           Values
                                    NUMBER(5,2)        Max 5 digits,       123.45
                                                       2 after             valid,
                                                       decimal             1234.56
                                                                           invalid (6
                                                                           digits)         Storing integers and decimals
 NUMBER(p,s)                        NUMBER(7,0)        Max 7 digits,       1234567         (financial data)
                                                       no decimal          valid,
                                                                           12345678
                                                                           invalid
                                    NUMBER             No                  Any
                                                       precision/scale     number
                                                       specified           within
                                                                           Oracle
                                                                           limits

 FLOAT                            Floating-point number                                    Storing approximate numeric
                                                                                           values
 DATE                             Date and time (year, month, day, hour,                   Storing dates and timestamps
                                  minute, second)
`````

## Page 7

![Original page 7](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-007.jpg)

### Extracted text

`````text
 TIMESTAMP                         Date and time with fractional seconds                      Storing precise timestamps
 CLOB                              Character Large Object                                     Storing large text data
 BLOB                              Binary Large Object                                        Storing large binary data (images,
                                                                                              audio files, and video files etc.)
 RAW(size)                         Raw binary data of length size                             Storing binary data of fixed
                                                                                              length
 LONG                              Variable-length character data                             Legacy support for large text
                                   Fixed-length Unicode character string                      Storing fixed-length Unicode
 NCHAR(size)                       (making suitable for multi-language                        data
                                   applications)
                                   Variable-length Unicode character string                   Storing variable-length Unicode
 NVARCHAR2(size)                   (making suitable for multi-language                        text
                                   applications)
 INTERVAL YEAR TO                  Interval of years and months                               Storing periods like '2 years 3
 MONTH                                                                                        months'
 INTERVAL DAY TO                   Interval of days, hours, minutes, seconds                  Storing periods like '10 days 5
 SECOND                                                                                       hours'


Explanation of all DDL (Data Definition Language) Commands-
1) CREATE command-
•   The CREATE command is used to create new database objects such as tables, views, indexes, or even
    entire databases.
•   Most commonly, it is used to create a new table in a database.
•   When creating a table, we have to define the table’s name and specify its columns (attributes or fields)
    along with their data types and any constraints (like primary key, not null, unique, check etc.)
Syntax to create table:

 CREATE   TABLE   table_name (
     column1      datatype     constraint,
     column2      datatype     constraint,
     column3      datatype     constraint,
     .  .  .  .  .  .
  );


Example:
SQL> CREATE   TABLE   employee (
    employee_id     NUMBER(5)    PRIMARY KEY,
    first_name        VARCHAR2(50),
    last_name         VARCHAR2(50)  NOT NULL,
    email                VARCHAR2(100)  UNIQUE,
    hire_date          DATE,
    salary               NUMBER(8, 2)  CHECK (salary > 0)
);
    Explanation of Each Part of above query:
1. CREATE TABLE emplo (...)
    •    This creates a new table named employee.
    •    The table will have six columns (fields).
    •    You define the structure of the table inside the parentheses.
2. employee_id    NUMBER(5) PRIMARY KEY
    •    employee_id is a column that stores numeric values, up to 5 digits.
    •    PRIMARY KEY means:
             o    This column must have unique values (no duplicates).
             o    It cannot be NULL (must always have a value).
`````

## Page 8

![Original page 8](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-008.jpg)

### Extracted text

`````text
              o   It uniquely identifies each row in the table.
3. first_name    VARCHAR2(50)
    •    first_name is a column for storing a string (text).
    •    VARCHAR2(50) means it can store up to 50 characters.
    •    It is optional (can be NULL).
4. last_name     VARCHAR2(50) NOT NULL
    •    Stores the employee's last name.
    •    Same as first_name, but:
              o   NOT NULL makes it mandatory. You must enter a last name when inserting a row.
5. email   VARCHAR2(100) UNIQUE
    •    Stores email addresses.
    •    VARCHAR2(100) allows up to 100 characters.
    •    UNIQUE means:
              o   All email values must be different.
              o   If you try to insert a duplicate email, Oracle will return an error.
6. hire_date    DATE
    •    Stores the date the employee was hired.
    •    DATE is a special Oracle data type that stores both        date and time (although time is optional if you don't
         specify it).
7. salary    NUMBER(8, 2)     CHECK (salary > 0)
    •    Stores the employee’s salary.
    •    NUMBER(8, 2) means:
              o   Up to 8 digits in total, with 2 digits after the decimal point.
              o   Example: 123456.78 is valid.
    •    CHECK (salary > 0) adds a constraint:
              o   It ensures that the salary must be greater than 0.
              o   If someone tries to insert a salary of 0 or a negative number, the query will fail.
Note:  After executing above table creation query, ‘employee’ table structure created in database.
Also, we can see the created table structure using ‘desc’ command as follow-
➢   DESC (or DESCRIBE) Command in Oracle:
•   The DESC (short for DESCRIBE) command in Oracle is used to display the structure of a table — i.e.,
    the list of its columns along with their data types, nullability, and other attributes.
•   When you run this command, Oracle returns information like:
 Name              Null?      Type
 Column            NULL       Data type(Size)
 name
Example-








Creating a Table from Previously Created Table:
We can also able to create a new table from previously created table.
Syntax:
         SQL> create   table    TargetTableName    as   select   *   from    SourceTableName;
•   This query creates a new table (TargetTableName) and copies the structure and data from an existing
    table (SourceTableName).
•   This is often called a CTAS operation (Create Table As Select).
Example:
         SQL> create   table    employeeDemo    as   select   *   from    employee;
➢   This command creates a new table named                  employeeDemo by          copying the structure
    (column  names  and  data  types)           and  all  data  (rows)  from  an  existing  table  called
`````

## Page 9

![Original page 9](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-009.jpg)

### Extracted text

`````text
    employee.
🔍 Detailed Explanation of above query:
🔸 What is copied:
    •   ✅ Column names
    •   ✅ Column data types
    •   ✅ All rows from the employee table
🔸 What is not copied:
    •   ❌ Constraints like PRIMARY KEY, NOT NULL, UNIQUE, CHECK
    •   ❌ Indexes
    •   ❌ Triggers
    •   ❌ Sequences or auto-increment settings
    •   ❌ Default values
So,  the new table     employeeDemo        will have the same data and structure          but without
constraints or special properties.

Creating a Table from Previously Created Table by taking appropriate fields of existing
table also change the column name at table creation:

SQL> create   table    TargetTableName(newColName1,newColName2, . . )    as   select
           oldColName1,oldColName2,…   from    SourceTableName;
Example:
SQL>create table empDemo1(empno,fname,lname) as select employee_id,first_name,last_name from
employee;
➢   Explanation of above query:
This query creates a new table called empDemo1 by selecting specific columns (employee_id, first_name,
last_name) from the existing employee table. It also renames the columns in the new table having names
empno,fname,lname respectively.

 SQL Constraints used in oracle: (Data integrity in oracle)
 •   We know that, at the time of table creation we specify the constraints for the column of table.
 •   SQL constraints are the rules that are applied to columns in a database table to enforce data integrity.
 •   SQL constraints ensure the accuracy of the data, and limit the type of data that can be inserted or updated.
     Because of constraints, correct data will be inserted into database table.
 •   Constraints can be divided into two types as follow:
 1) Column-level Constraint- The constraints can be specified immediately after the column definition is
 called “column-level constraint”.
 Example-         SQL> create   table   emp( eid   number   primary key,ename char(10));
 In above example, primary key constraint is specified to eid column immediately hence it is column-level
 constraint.
 2) Table-level Constraint- The constraints can be specified after all columns and at the end of table called
 “table-level constraint”.
 E.g.-  SQL>create      table      emp(eid      number,ename  char(10),           CONSTRAINT  pkey  PRIMARY
 KEY(eid));
 In above example, primary key constraint is         specified to eid column at the end of table creation hence it is
 table-level constraint.
 •   Below are the most commonly SQL constraints used in oracle:
      Constraint                                        Description
  NOT NULL                Column cannot have NULL values
  UNIQUE                  All values in the column must be unique.
`````

## Page 10

![Original page 10](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-010.jpg)

### Extracted text

`````text
 CHECK                   Value must satisfy a condition
 DEFAULT                 Sets a default value when none is provided during insertion
 PRIMARY KEY             Uniquely identifies each row (NOT NULL + UNIQUE)
 FOREIGN KEY             Enforces referential integrity between tables
•   We explain all these constraints with example as follow-
1. NOT NULL Constraint:
•   In Oracle Database, the NOT NULL constraint is used to ensure that a column cannot store NULL
    values. It is one of the most basic integrity constraints and is typically used when a column must
    always have a value for every row in a table.
•   NOT NULL ensures that the column must have a value i.e. it cannot be left blank (NULL) during an
    INSERT or UPDATE.
•   NOT NULL constraint defined only at the column level, not at the table level.
   Example:
SQL> CREATE  TABLE  Student (
           StudentID    NUMBER,
           Name          VARCHAR2(50) NOT NULL);
  Invalid Insert:
SQL>INSERT INTO Student (StudentID) VALUES (1);
-- ORA-01400: cannot insert NULL into ("STUDENT"."NAME")

2. UNIQUE Constraint:
•   In Oracle, the UNIQUE constraint ensures that all values in a column (or combination of columns)
    are distinct (i.e. unique.) — no two rows can have the same value(s) in the specified column(s).
•   The  UNIQUE constraint          prevents   duplicate values     in a column or group of columns but            allows
    NULLs (because NULL is not considered equal to any other NULL in SQL Oracle).
•   UNIQUE constraint can be defined at both Column-level and also Table-level.
•   A single table can have multiple UNIQUE constraints on different columns or combinations.
•   UNIQUE constraint can be applied to multiple columns together (composite unique constraint).
•   Basically, UNIQUE key constraint used for maintaining data integrity in a relational database.
   Example:
SQL>CREATE   TABLE   UserLogin (
    UserID  NUMBER,
    Email   VARCHAR2(100)   UNIQUE);
  Invalid Insert:
SQL>INSERT INTO UserLogin VALUES (1, 'user@example.com');
SQL>INSERT INTO UserLogin VALUES (2, 'user@example.com');
-- ORA-00001: unique constraint violated

3. CHECK Constraint:
•   In Oracle, a CHECK constraint is used to enforce domain integrity by limiting the values that can be
    placed in a column.
•   CHECK constraint ensures that data entered into a column satisfies a logical condition.
•   The CHECK constraint specifies a condition that must be true for each row in the table.
•   If the condition evaluates to TRUE then only INSERT or UPDATE operation carried out.
•   If the condition evaluates to FALSE, Oracle will reject the INSERT or UPDATE operation.
•   CHECK constraint can be defined at column-level or Table-level also.
   Example:
SQL>CREATE  TABLE  Account (
    AccountID   NUMBER,
    Balance        NUMBER   CHECK (Balance > 0));
  Invalid Insert:
`````

## Page 11

![Original page 11](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-011.jpg)

### Extracted text

`````text
SQL>INSERT INTO Account VALUES (1, -100);
-- ORA-02290: check constraint violated

4. DEFAULT Constraint:
•   In Oracle, a DEFAULT constraint is used to automatically assign a value to a column when no value
    is explicitly provided during an INSERT operation.
•   It helps enforce default business rules and reduces the need for manual value insertion.
•   It Sets a default value for a cell if no value is given while inserting a record in table.
•   It is typically used at the column level.
•   Oracle doesn’t support DEFAULT constraint at table-level.
   Example:
SQL>CREATE  TABLE  Orders (
    OrderID   NUMBER,
    OrderDate  DATE  DEFAULT  SYSDATE);
SQL> INSERT INTO Orders (OrderID) VALUES (1001);
Here, OrderDate will be set to current date (SYSDATE)
Check by result by using SELECT statement.

5. PRIMARY KEY Constraint:
•   Basically, primary key is used to identify a row uniquely i.e. it avoids insertion of duplicate records in
    table.
•   Primary key is a combination of UNIQUE and NOT NULL
•   In Oracle, a PRIMARY KEY constraint is used to uniquely identify each row in a table.
•   It is one of the most important constraints in relational databases and enforces both uniqueness and not
    null rules on the column(s) it is applied to.
•   A PRIMARY KEY constraint ensures that:
    ➢   No two rows have the same value(s) in the primary key column(s).
    ➢   The column(s) cannot be NULL.
•   A table can only have one primary key, but a primary key can consist of multiple columns called
    “composite key primary key”.
•   A primary key constraint can be applied at column level and table level also.
   Example:
SQL>CREATE TABLE Department (
    DeptID       NUMBER    PRIMARY KEY,
    DeptName  VARCHAR2(50));
Equivalent syntax for above query with named constraint:
SQL>CREATE TABLE Department (
    DeptID    NUMBER,
    DeptName VARCHAR2(50),
    CONSTRAINT pk_dept PRIMARY KEY (DeptID));

Executing following insert record operation on above table-
SQL> insert into Department values(1, ‘Science’);
1 row created.

SQL> insert into Department values(2, ‘Arts’);
1 row created.

  Invalid Insert:
SQL> insert into Department values(2, ‘Commerce’);
ERROR at line 1:
ORA-00001: unique constraint (SYSTEM.SYS_C004237) violated
SQL> insert into Department (DeptName) values(‘Commerce’);
ERROR at line 1:
`````

## Page 12

![Original page 12](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-012.jpg)

### Extracted text

`````text
 ORA-01400: cannot insert NULL into ("SYSTEM"."DEPTARTMENT"."DEPTID")

 6. FOREIGN KEY Constraint:
 •   In Oracle, a FOREIGN KEY constraint (also known as a referential integrity constraint) ensures that
     the values in one table match values in another table's primary or unique key.
 •   It establishes a parent-child relationship between two tables.
 •   A foreign key links one or more columns (the "child" table) to the primary key or unique key in another
     table (the "parent" table).
 •   It ensures that you cannot insert or update a value in the child table unless it exists in the parent table.
 •   Basically, Foreign key is used to create a relationship between tables in database.
 •   A FOREIGN key constraint can be applied at column level and table level also.
    Parent Table:
 SQL> CREATE TABLE Department (
     DeptID NUMBER PRIMARY KEY,
     DeptName VARCHAR2(50));
 Executing following insert record operation on above table-

 SQL> insert into Department values(1, ‘Science’);
 1 row created.
 SQL> insert into Department values(2, ‘Arts’);
 1 row created.

    Child Table with Foreign Key:
 (Column Level foreign Key)
 SQL>CREATE    TABLE   Employee(
 EmpID       NUMBER  PRIMARY KEY,
 EmpName  VARCHAR2(50),
 DeptId       NUMBER   REFERENCES   Department(DeptID));

 (Table Level foreign Key)
 SQL>CREATE TABLE Employee (
     EmpID  NUMBER  PRIMARY KEY,
     EmpName VARCHAR2(50),
     DeptID  NUMBER, FOREIGN KEY (DeptID) REFERENCES Department(DeptID));
    Valid Insert:
 SQL>INSERT INTO Employee VALUES (101, 'Ravi', 1);
 1 row created.
   Invalid Insert:
 SQL>INSERT INTO Employee VALUES (102, 'Kiran', 99);
 -- ORA-02291: integrity constraint violated – parent key not found
2)  ALTER command:
➢   The ALTER command in Oracle SQL is DDL command used to modify the structure of an existing
    table.
➢   ALTER command allows you to:
    •   Add, modify (Change data type or size of column) or drop table columns.
    •   Rename columns name or the table name.
    •   Add or drop constraints.
    •   Set or drop default values.
Let’s see ALTER command in details-
2.1) Adding Columns in table-
We can add new columns into existing table using alter command as-
Syntax-
SQL>ALTER  TABLE  tableName   ADD(newCol1  datatype,newCol2  datatype,newCol3    datatype,…);
`````

## Page 13

![Original page 13](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-013.jpg)

### Extracted text

`````text
The above query adds multiple new columns newCol1,newCol2,newCol3 to an existing table.
   Example:
SQL>ALTER  TABLE    Department   ADD(DeptAddress   VARCHAR2(50));
The above query adds single column DeptAddress to an existing table Department.

SQL>ALTER  TABLE    Employee   ADD(eadd   VARCHAR2(10),contact     number(10));
The above query adds multiple columns eadd and contact to an existing table Employee.
2.2) Modify Column (Data Type or Size):
We can modify existing columns data type and also its size using alter command as-
Syntax:
SQL>ALTER   TABLE   tableName   MODIFY(colName    newdatatype(newSize));
The above command changes the data type and size of an existing column in a table.
   Example:
SQL>ALTER   TABLE   Employee  MODIFY(eName    CHAR(150));
The above command changes the data type and size of eName column in Employee table.

❖   Restrictions on Altering Columns:
Note the following important points while altering the column-
    1.  Cannot directly change column order in a table.
    2.  Cannot decrease column size if table having existing data that doesn’t fit to the new size.
    3.  Cannot change datatype if it’s incompatible with existing data.
    4.  Cannot change datatype of a column used in a primary/foreign key unless you drop the
        constraint first.
    5.  Renaming a column may break dependent objects (other table, views, triggers, PL/SQL code)
        unless they are updated.

2.3) Drop Column:
We can drop existing column from table using alter command as-
➢   Dropping single column:
Syntax:
SQL>ALTER  TABLE  tableName   DROP  COLUMN    colName;
The above command drops single column colName from existing table.
   Example:
SQL>ALTER TABLE   Employee   DROP  COLUMN    email;
The above command drops single column email from existing table Employee.
➢   Dropping multiple columns:
Syntax:
SQL>ALTER  TABLE  tableName   DROP (colName1,colName2,…);
The above command drops multiple columns colName1, colName2 from existing table.
   Example:
SQL> ALTER  TABLE  Employee  DROP (addr1, phone);
The above command drops multiple columns addr1,phone from existing table Employee.
❖   Restrictions on Dropping Columns:
Note the following important points while dropping the column-
    1.  Cannot drop all columns — at least one column must remain in table.
    2.  Cannot drop a column that is part of:
            •   A primary key (unless you drop the PK constraint first).
            •   A unique constraint.
            •   A foreign key reference (unless constraint is dropped or disabled).
    3.  Dropping a column permanently deletes data (no undo except backup).
    4.  Large table column drops may require significant time and disk space internally
`````

## Page 14

![Original page 14](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-014.jpg)

### Extracted text

`````text
2.4) Rename columns name or the table name:
Alter command also used for renaming the column name and table name also. We explain it as follow-
2.4.1) Renaming a Column:
Syntax:
SQL> ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name;
Example:
SQL> ALTER  TABLE  emp RENAME COLUMN name  TO  ename;
The above query renames ‘name’ column to ‘ename’ column of table ‘emp’.
❖   Points To remember while renaming the column:
    •   The new column name must be unique in the table.
    •   Renaming a column does not change data in it.
    •   May break dependent objects (views, triggers, PL/SQL code) that refer to the old column name —
        you must update them manually.

2.4.2) Renaming a Table:
Syntax:
SQL> ALTER TABLE  old_table_name   RENAME  TO   new_table_name;
Example:
SQL> ALTER  TABLE  emp RENAME TO  empTbl;
The above query renames ‘emp’ table to ‘empTbl’.

2.5) Add or drop constraints:
We can also add or drop constraints using alter command, which is explained as follow-
2.5.1) Adding Constraints with ALTER:
We can add constraints to an existing table without recreating it.
Syntax:
SQL>ALTER TABLE   table_name  ADD CONSTRAINT  constraint_name    constraint_type (col_name);
Here,
Constraint_name is Name given by user for constraint which is an identifier.
Constraint Types is PRIMARY KEY,UNIQUE,FOREIGN KEY,CHECK,NOT NULL (special case —
handled via MODIFY)
Example-
SQL> ALTER TABLE empTbl ADD CONSTRAINT  ukey   unique   (salary);
The above query add unique constraint for field ‘salary’ of ‘empTbl’  table.

2.5.2) Dropping Constraints with ALTER:
We can also drop constraints from an existing table.
Syntax:
SQL>ALTER    TABLE   table_name   DROP  CONSTRAINT   constraint_name   [CASCADE];
Here,
constraint_name   is name of constraint that we are going to drop.
CASCADE is optional used when other constraints depend on the one you’re dropping (mostly for
PRIMARY KEY that has child foreign keys).
Note that: Dropping a constraint does not delete the column.
Example-
SQL> ALTER TABLE empTbl  DROP  CONSTRAINT  ukey;
The above query, drops the constraint ‘ukey’ that we had previously added.

2.6) Set or drop default values using ALTER command:
2.6.1) Setting a Default Value using ALTER:
We can assign a default value to a column so that when an INSERT statement omits that column, Oracle
automatically assigns the default value for respective column.
Syntax:
SQL> ALTER  TABLE     table_name    MODIFY column_name   DEFAULT   default_value;
`````

## Page 15

![Original page 15](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-015.jpg)

### Extracted text

`````text
Example:
SQL> ALTER TABLE  empTbl  MODIFY   ename    default     'AJAY';
After running above query, table is altered successfully.

Note: if you insert a new row into empTbl without providing a value for ename, Oracle will
automatically insert 'AJAY' in that column.

2.6.2) Dropping a Default Value using ALTER:
To remove or drop an assigned default value, we have to set it to NULL.
Syntax:
SQL>ALTER  TABLE   table_name   MODIFY  column_name   DEFAULT   NULL;
After running above query, table is altered successfully.
Example:
SQL> ALTER TABLE  empTbl   MODIFY ename   DEFAULT    NULL;
The above query, drops assigned default value ‘JIBRAIL’ for ‘ename’ of table empTbl.

3) DROP command:
•   This command also belongs to DDL category which is used to                   Delete database objects such as tables,
    views, index, sequence, user etc. permanently.
•   Once an object is dropped, all the data and structure associated with it are deleted and          cannot be recovered
    unless you have a backup or recycle bin is enabled.
•   Syntax:
        SQL>DROP                   object_type  object_name;
Here:
    •   object_type can be TABLE, VIEW, INDEX, SEQUENCE, etc.
    •   object_name is the name of the object to be dropped.
Example 1: Dropping a table-
        SQL>DROP          TABLE    employee;
    •   This command permanently removes the employee table and all its data from the database.
    •   If the  Recycle Bin      is enabled (in Oracle 10g and later), the table           (which was created on        users
        tablespace) can be recovered using FLASHBACK command.
    •   By default, all tables are created in ‘system tablespace’ but we can create table in ‘users tablespace’
        as follow-
                          CREATE TABLE table_name (
                              column1     datatype      constraint,
                              column2     datatype    constraint,
                              -- ... more columns
                          )TABLESPACE       tablespaceName;
    •   Example -
        SQL> CREATE  TABLE  emp101(eid   number) TABLESAPCE    users;
        Above query creates ‘emp101’ table in users tablespace.

 ➢   Check parameter for the recyclebin whether it is ON or OFF:
          SQL> show   parameter   recyclebin;
 This would produce output as follow-


 If it is OFF then, To enable or ON the recyclebin at the system level:

 Open a SQL*Plus session or a similar tool and connect as a user with ALTER SYSTEM privileges
 (e.g., SYSDBA) and execute the following command
      SQL> ALTER  SYSTEM  SET recyclebin = ON;
 ➢   To view the content of recyclebin:
 SQL> show  recyclebin;
`````

## Page 16

![Original page 16](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-016.jpg)

### Extracted text

`````text
 This would produce list of deleted tables (only users tablespace). As shown bellow-



 ➢   Viewing data from dropped table using ‘Recyclebin name’:

 SQL> Select * from “RecyclebinName”
 Example:
  SQL> Select * from “BIN$zi4E8ESCSKWZL07u6PHRKQ==$0”;
 This would produce output:





 ➢   To recover dropped table from recyclebin:
 SQL> FLASHBACK   TABLE   emp101    TO   BEFORE   DROP;
 The above query recycles back the dropped table.
Note:
•   The DROP command is irreversible unless you are using features like Flashback or Recycle Bin.
•   Important: Only those dropped table shown in recyclebin which are created on               users tablespace.
•   Important: Those dropped table are not shown in recyclebin which are created on                system tablespace.
•   It requires appropriate privileges. For example, dropping a table requires either ownership or DROP
    ANY TABLE privilege.
  Example 2: Dropping a View
        SQL>DROP VIEW emp_view;
•   The above command deletes the view ‘emp_view’.
•   No actual data is deleted, since views are virtual tables based on queries.
  Example 3: Dropping a Sequence
        SQL>DROP SEQUENCE emp_seq;
    •   Removes the sequence ‘emp_seq’ used for generating numbers.
  Example 4: Dropping a User (and their schema)
        SQL>DROP USER hr CASCADE;
    •   Removes the user ‘hr’ and all objects (tables, views, etc.) owned by that user.
    •   CASCADE is required to drop a user along with all dependent objects.

4) TRUNCATE command:
•   This is also DDL command used to delete all rows i.e. all tuples i.e. all records from a table quickly and
    permanently, without logging individual row deletions. (faster than DELETE)
•   It is faster and less resource-intensive than the DELETE command because it doesn't generate as much
    undo and redo data.
Syntax:
        SQL> TRUNCATE    TABLE   table_name;
Example- Let's say we have a table employees:
        SQL>CREATE TABLE employees (
                 emp_id        NUMBER,
                emp_name   VARCHAR2(100));
Insert some data:
SQL>INSERT  INTO  employees VALUES (1, 'AJAY');
SQL>INSERT  INTO  employees VALUES (2, 'VIJAY');
SQL>COMMIT;
Now, truncate the table:
SQL>TRUNCATE TABLE employees;
   This will:
`````

## Page 17

![Original page 17](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-017.jpg)

### Extracted text

`````text
    •   Remove all rows from employees.
    •   Free up the space used by the data.
    •   Not fire any DELETE triggers (if any exist).
    •   Not be rolled back (it's a DDL operation which is auto-commit).

Difference between TURNCATE and DELETE command:
                           TRUNCATE                                                           DELETE
 1.      TRUNCATE command belongs DDL category.                         1. DELETE command belongs to DML
                                                                        category.
 2.      TRUNCATE command not rolled back, since it is DDL              2. DELTE command rolled back, since it is
                                                                        DML
 3.      WHERE clause is Not supported in TRUNCATE                      3. WHERE clause is supported in DELETE
 4.      TRUNCATE command not fires DELETE triggers to                  4. DELETE command fires DELETE triggers to
 delete the record.                                                     delete the record.
 5.      Working speed of TRUNCATE is Faster than DELETE                5. Working speed of DELETE is Slower than
 because it deletes all records at one time and free the space.         TRUNCATE because it deletes record one by
                                                                        one.
 6.   Deletes all records i.e. it does not delete specific row          6. It deletes specific row (record) with WHERE
 (Since, WHERE clause in not supported)                                 clause
4) RENAME command:
This is also DDL command used to Rename a database object such as tables, views, index, sequence etc.
Syntax:
        SQL>RENAME   old_name   TO   new_name;
Here,
        old_name is Current name of the object.
        new_name is New name you want to assign.
Example:
        SQL>RENAME   employees TO   staff;
Above query renames ‘employees’ to new name ‘staff’
➢   Important points to be noticed while performing RENAME command-
    1.  You can only rename your own objects.
    2.  You cannot rename columns using RENAME. Use ALTER TABLE for that.
    3.  You cannot rename objects in another schema.

Explanation of all DML (Data Manipulation Language) Commands-
1) INSERT command-
•   In Oracle (and SQL in general), the INSERT command is used to add new records (rows) into a table.
•   When inserting a single row (record) into the table, the insert operation:
               ▪   First creates a new empty row in table.
               ▪   Then insert statement loads passed values to the specified columns of table.
•   In INSERT INTO statement, table columns and values have one to one relationship. i.e.
    First value inserted into first column, second value inserted into second column and so on.
•   There are different forms of the INSERT statement which are explained as follow-
1) Insert a single row (record) by specifying column name:
Syntax:
SQL>INSERT INTO table_name (column1, column2, ..., columnN)  VALUES (value1, value2, ..., valueN);
Suppose you have a table called employees:
SQL>CREATE TABLE employees (
    emp_id      NUMBER,
    first_name VARCHAR2(50),
    last_name  VARCHAR2(50),
    salary     NUMBER);
`````

## Page 18

![Original page 18](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-018.jpg)

### Extracted text

`````text
You can insert a single row like this:
SQL> INSERT INTO employees (emp_id, first_name, last_name, salary) VALUES (101, 'AMIT', 'ROY',
50000);

2. Insert a single row (record) without specifying column names (all columns):
Syntax:
SQL>INSERT  INTO  table_name VALUES (value1, value2, ..., valueN);
Example:
SQL>INSERT  INTO  employees   VALUES (102, 'JITENDRA', 'KALE', 60000);
Note: The values must match the order and data type of the table’s columns.

3. Insert multiple rows (using INSERT ALL):
Oracle allows multiple inserts in one statement using INSERT ALL:
Syntax:
SQL>INSERT  ALL
               INTO   table_name (col1, col2,col3, ….) VALUES (val1, val2, val3,…)
               INTO   table_name (col1, col2,col3, ….) VALUES (val1, val2, val3,…)
        SELECT * FROM dual;
Example-
SQL>INSERT  ALL
               INTO employees (emp_id, first_name, last_name, salary) VALUES (103, 'Alice', 'Brown', 55000)
               INTO employees (emp_id, first_name, last_name, salary) VALUES (104, 'Bob', 'White', 52000)
        SELECT * FROM dual;
Note:
    •   Here, DUAL is a special one-row table in Oracle often used in insert/select operations.

4. Insert data from one table to another table:
•   This is useful for copying data from one table to another.
Syntax:
SQL>INSERT INTO Dest_table (col1,col2,col3,…..)
          SELECT    col1,col2,col3,….    FROM    Source_table;
Example-
SQL>INSERT INTO empDest (emp_id, first_name, last_name, salary)
          SELECT  emp_id, first_name, last_name, salary   FROM employees;

•   The above query copies data from source table employees into another destination table empDest.
•   Note: While inserting data from one table to another table, destination table should be created first.

➢   Inserting values in table using Substitution Variables (&variable):
    •   & is used in tools like SQL (ORACLE) to prompt the user for input. (interactive data entry)
    •   When the query is run, Oracle will ask the user to enter a value for each variable.
Syntax:
SQL> INSERT   INTO   table_name    VALUES(&Col1,&Col2, …., &ColN);
In above syntax, & is used along with column of table will prompt user for input.
Example:
`````

## Page 19

![Original page 19](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-019.jpg)

### Extracted text

`````text
Note: Use single quote for column having data type varchar2 or char or date
Use of forward slash / on SQL terminal:
    •   /  is used to execute the most recently entered SQL statement or PL/SQL block.
    •   That is forward slash / executes previously executed SQL command ro PL/SQL block.
Example-









In above example, we use forward slash / to execute insert command again.
2) SELECT command-
•   The SELECT command in Oracle is used to retrieve data from one or more tables.
•   Syntax:
        SQL>SELECT column1, column2, .....,columnN    FROM    table_name   WHERE condition;
Here, column1, column2, .....,columnN are the table columns which will retrieve.
table_name   is name of the table from which data is retrieved.
WHERE is clause which is optional used when specific data would be retrieved as per condition.
Example-





Here, above query fetches name and address of student having rollno is 102 from student table.
Different examples of SELECT statement in Oracle:
1. Select all columns:
Syntax:   SQL>SELECT  *  FROM  table_name;
Example-
SQL>SELECT  *  FROM  student;
     This shows all rows and all columns from the student table.
Output:






2. Select specific columns (Project  operations):
Syntax:
        SQL>SELECT  col1,col2,col3,….  FROM   table_name;
Example-
SQL>SELECT name, address FROM   student;
     This shows only the name and address of each student.
`````

## Page 20

![Original page 20](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-020.jpg)

### Extracted text

`````text
Output:






3. Using WHERE clause to retrieve specific records: (Filter)

Syntax:
        SQL>SELECT  col1,col2,col3,….  FROM   table_name  WHERE   condition;
Example:
SQL>SELECT  name, address  FROM  student   WHERE    rollno=102;
     Shows student name and address whose rollno is 102.
Output:






4. Sorting with ORDER BY:
Syntax:
        SQL>SELECT  col1,col2,col3,….  FROM   table_name   ORDER  BY    col_name       order;
Here,
        order may be DESC or ASC.
•   To sort data in descending order use DESC.
•   To sort data in ascending order use ASC.
Example-
SQL>SELECT  *  FROM  student  ORDER BY rollno DESC;
     Shows all student record in descending order of rollno.
Output:





5. Using aliases (alternative name):
Syntax:
        SQL>SELECT  col1 AS  newCol1,col2  AS newCol2,….  FROM   table_name;
Example-
SQL>SELECT rollno AS Roll,name AS FirstName, address AS Add1  FROM student;
     Renames the column headings in the output.
Output:








6. Using functions:

        SQL>SELECT    COUNT(*)  AS   Total_student   FROM   student;
     Shows the total number of students. (counts total number student)
`````

## Page 21

![Original page 21](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-021.jpg)

### Extracted text

`````text
Output:





Note: You can (SELECT) filter records with WHERE, sort with ORDER BY, rename with AS, and use

functions like COUNT, SUM, AVG, etc.

7. Eliminating Duplicate rows (records):
•   In a table, there is possibility to exist a duplicate value. And if we want to filter or retrieve only
    one value from all duplicate values then DISTINCT clause is used along with SELECT.
•   In short, DISTINCT clause is used to retrieve only unique data from table.
•   The functionality of  UNIQUE and DISTINCT clause are same.
•   DISTINCT clause (UNIQUE clause)- Allows to remove duplicates data from the result set
•   This clause only used with SELECT statement. It scans all the values of the specified columns and display
    only unique values. It eliminates rows that have exactly same contents in each column.
Syntax:
SQL>SELECT   DISTINCT   Col1,Col2,….,ColN   From  tablename;
                             OR
SQL>SELECT   DISTINCT   *    from   tablename;
Example:
Suppose we have following ‘student’ table-









The above table have duplicate records of DINESH. We can retrieve all distinct records from student table
as follow-








Also, We can retrieve all distinct name from student table as follow-







3) DELETE command-
•   The DELETE command in Oracle is used to delete or remove all rows or specific rows from a table
`````

## Page 22

![Original page 22](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-022.jpg)

### Extracted text

`````text
    based on a specified condition.
•   Syntax:
    SQL>DELETE            FROM   table_name          WHERE            condition;
Here,
    table_name: The name of the table from which we want to delete data.
    condition: The criteria to determine which rows should be deleted.
    WHERE is clause used to give condition.
Example 1: Delete specific rows:
Syntax:
SQL>DELETE                FROM              table_name       WHERE             condition;
Suppose, we have a table called employee as follows:









Now, we want to delete all employees from the IT department then its query will be-
SQL>DELETE   FROM    employee   WHERE      department = 'IT';
The above query deletes 2 records having department = ‘IT’
The resultant employee table is-







Example 2: Delete all rows:
This will remove all data from the table, but the table still exists and remains empty.
Syntax:
        SQL>DELETE    FROM    table_name;




This will remove all data from the employees table, but the table still exists and is empty.
❖   Important Notes regarding DELETE command:
    •   If you omit the WHERE clause, all rows in the table will be deleted, but the table structure
        remains as it is in database.
    •   The DELETE command can be rolled back if it hasn't been committed. (Since, it belongs to DML
        category)
    •   DELETE affects row-level locks and fires DELETE triggers, if any exist.
4) UPDATE command-
•   The UPDATE command in Oracle is used to modify existing data stored in a table.
•   Syntax:
SQL>UPDATE   table_name   SET  column1 = value1,column2 = value2, ...   WHERE    condition;
Here,
table_name: Name of the table where the update will happen.
SET: Is Keyword used to specify which columns to update and with their new values.
WHERE is clause used to give condition.
condition: The criteria to determine which rows should be updated.
`````

## Page 23

![Original page 23](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-023.jpg)

### Extracted text

`````text
Note: Without a WHERE clause, all rows will be updated.
Suppose, we have a table called employee as follows:










Example1. Update a Specific Row
Suppose we want to change Vijay's department from IT to HR:












  This update only Vijay's record.

2. Update Multiple Columns:
Let’s say we want to change Rajesh’s department to Finance and rename him to Jitendra:










   This update only emp_id = 3 record.
3. Update All Rows:
If we do not include a WHERE clause in UPDATE command then it updates all rows.









   This changes every employee's department to General.
`````

## Page 24

![Original page 24](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-024.jpg)

### Extracted text

`````text
Explanation of all TCL (Transaction Control Language) Commands-
•   We know that, all DML commands are not auto-commit therefore the result of DML commands are not
    save permanently in database.
•   TCL commands are used to manage the changes made in the database by a DML statements called as a
    ‘transaction’. That is, TCL commands are used to manage transactions in database.
Let’s see different TCL commands in detail-
1) COMMIT and ROLLBACK command-
➢   The COMMIT command in Oracle is used to save all changes made during the current transaction
    permanently to the database.
➢   When COMMIT is fired then all transactions (insert,update,delete) is saved permanently into
    database and transaction becomes completed.
•   Syntax:
        SQL>COMMIT;
➢   The ROLLBACK command in Oracle is used to undoes all changes since last commit.
•   Syntax:
        SQL>ROLLBACK;
•   Note: A transaction is a sequence of one or more DML operations (like INSERT, UPDATE, DELETE)
    performed as a single logical unit of work. These changes are temporary until you explicitly save them
    using COMMIT.
•   Until you run COMMIT, you can undo changes with ROLLBACK.
•   Once you COMMIT, changes become permanent in database and visible to other users.
Example-Suppose, we have ‘employee’ table with few records as follow-









Scenario: You want to update Kiran's department from ‘General’ to ‘Finance’ and delete Ajay's record:
Then we execute following SQL queries-
SQL>UPDATE   employee   SET   department = 'Finance'   WHERE   name = 'Kiran';

SQL>DELETE FROM employee WHERE name = 'Ajay';

At this point, these changes are not yet permanent.
    •   If you run:
                         SQL>ROLLBACK;
The changes will be undone. Kiran's department stays ‘General’, and ‘Ajay’ remains in the table.
    •   But if you want to save the changes permanently, run:
                         SQL>COMMIT;
Now, Kiran’s department is updated to Finance, and Ajay’s record is permanently deleted from table.

2) SAVEPOINT command:
•   In Oracle SQL, the SAVEPOINT command is used to set a marker (a checkpoint) within a transaction
    (sequence of DML statements).
•   SAVEPOINT allows you to rollback only a part of the transaction instead of undoing the entire
    transaction.
•   SAVEPOINT is very useful when you want to manage partial rollbacks in a long transaction.
     Key Points about SAVEPOINT:
    •   A savepoint is a named point to which you can roll back during a transaction.
`````

## Page 25

![Original page 25](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-025.jpg)

### Extracted text

`````text
    •   You can create multiple savepoints in a single transaction.
    •   Rolling back to a savepoint undoes only the statements executed after that savepoint.
    •   Savepoints are released automatically when you commit or rollback (without specifying a
        savepoint).
    •   Maximum number of savepoints depends on Oracle version (usually large, like 5 per transaction in
        some versions, higher in later versions).
Syntax:
        SQL>SAVEPOINT            savepoint_name;
Here,
Savepoint_name is a named point to which you can roll back a transaction.
Example:
        Suppose we are working on an EMPLOYEE table.
-- Consider a transaction having sequence of DML commands-
         SQL>INSERT  INTO employee (emp_id, name, salary) VALUES (101, 'Amit', 50000);
         SQL>SAVEPOINT   sp1;
         SQL>INSERT  INTO employee (emp_id, name, salary) VALUES (102, 'Raj', 60000);
         SQL>SAVEPOINT   sp2;
         SQL>INSERT  INTO employee (emp_id, name, salary) VALUES (103, 'Priya', 70000);
Here, we have 3 insert operations with 2 savepoints in between.
Now, We fire ROLLBACK command by considering four cases-
Case 1: Rollback to sp2
        SQL>ROLLBACK   TO    sp2;
     The row for Priya (103) will be removed, but Amit (101) and Raj (102) remain as it is.

Case 2: Rollback to sp1
        SQL>ROLLBACK  TO  sp1;
     Only Amit (101) record remains as it is  where as  Raj (102) and Priya (103) records are removed.
Case 3: Full Rollback
        SQL>ROLLBACK;
     All inserts (Amit, Raj, Priya) are undone.
Case 4: Commit
        SQL>COMMIT;
     All changes saved permanently after COMMIT, and transaction becomes completed. Also, savepoints
are cleared.
i.e here after COMMIT, SQL>ROLLBACK    TO    savepoint;    command not works. That is All
savepoints are erased after COMMIT

3) SET TRANSACTION command:
•   The SET TRANSACTION command in Oracle is used to initialize the properties for a transaction i.e.
    it sets transaction mode and isolation level of transaction before it begins.
•   This command allows you to set the mode of transaction as READ ONLY or  READ WRITE
•   This command also allows you to set the isolation level of transaction (how the transaction is isolated from
    others) as READ COMMITTED or SERIALIZABLE.
Syntax:
1)  Setting mode of transaction:
    SQL>SET   TRANSACTION    mode;
Here,
mode: represents mode of transaction that may be READ ONLY or READ WRITE
         MODE                                                     Description
 READ WRITE                  This is default transaction mode. It allows DML (INSERT, UPDATE,
                             DELETE) operations.
 READ ONLY                   The transaction cannot perform any DML (INSERT, UPDATE, DELETE).
                             Only SELECT or Read operation in transaction is carried out.
`````

## Page 26

![Original page 26](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-026.jpg)

### Extracted text

`````text
Example 1:
    SQL> SET   TRANSACTION   READ  WRITE;
The above query, sets transaction mode to READ WRITE (which is default) therefore we can do all
transaction operations (insert, update, delete) very easily.











Example 2:
    SQL> SET   TRANSACTION   READ   ONLY;
•   The above query, sets transaction mode to READ ONLY therefore we cannot perform transaction
    operations (insert, update, delete).
•   Only transaction read (SELECT) operation can be carried out successfully.















In above example, insert operation failed due to transaction mode is set to READ ONLY mode.

2)  Setting isolation level of transaction:
    SQL>SET   TRANSACTION    ISOLATION   LEVEL        levels;
Here,
levels: represents isolation level of transaction that may be SERIALIZABLE or READ COMMITTED
 ISOLATION LEVEL                                                  Description
 READ COMMITTED               This is default isolation level. Each query sees only committed data as of
                              the start of the query.
 SERIALIZABLE                 Ensures complete isolation. It blocks other transactions.

Example 1:
        SQL> SET   TRANSACTION   ISOLATION   LEVEL   READ COMMITTED                                 ;

      Session-I (First RUN SQL command line)                     Session-II (Second RUN SQL command line)
 SQL> SET   TRANSACTION   ISOLATION                            Transaction 2 (another session):
 LEVEL   READ COMMITTED;                                       SQL>UPDATE employees SET salary = 7000
                                                               WHERE    id = 1;
 Transaction 1:                                                SQL>COMMIT;
`````

## Page 27

![Original page 27](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-027.jpg)

### Extracted text

`````text
 SQL>SELECT salary FROM employees WHERE
 id = 1;
 OUTPUT:
 SALARY
 -----------
    5000
 Back to Transaction 1:
 SQL>SELECT salary FROM employees WHERE                        NOTE:  Even though you're in the same
 id = 1;                                                      transaction, the second query sees the new
 OUTPUT:                                                      committed data. That's because each query gets a
 SALARY                                                       fresh read of committed data.
 -----------
    7000

Example 2:     SQL> SET   TRANSACTION   ISOLATION   LEVEL   SERIALIZABLE;

      Session-I (First RUN SQL command line)                    Session-II (Second RUN SQL command line)
 SQL> SET   TRANSACTION   ISOLATION                           Transaction 2 (another session):
 LEVEL   SERIALIZABLE;                                        SQL>UPDATE employees SET salary = 7000
                                                              WHERE    id = 1;
 Transaction 1:                                               SQL>COMMIT;
 SQL>SELECT salary FROM employees WHERE
 id = 1;
 OUTPUT:
 SALARY
 -----------
    5000
 Back to Transaction 1:
 SQL>SELECT salary FROM employees WHERE                        NOTE:
 id = 1;                                                      In Session-I, both Query 1 and Query 2 would
 OUTPUT:                                                      return the same value (5000) even if another
 SALARY                                                       transaction committed a change.
 -----------
    5000
Note:
    •   SET TRANSACTION must be the first SQL statement in a transaction. That is, we are not able to
        use SET TRANSACTION command after DML operations until we COMMIT transaction first.
    •   If auto-commit is enabled (e.g., in SQL*Plus or some tools), a transaction might be implicitly
        committed, and your SET TRANSACTION won't apply unless you explicitly manage transactions
        using BEGIN.
Explanation of all DCL (DATA Control Language) Commands:
•   In Oracle, DCL (Data Control Language) commands are used to control access the data of the database
    essentially, they deal with permissions and privileges.
•   DCL commands enforce database security in a multiple user database environment.
•   DBA controls the access of users to the database. Only          Database Administrator's or owners           of the
    database object can add / remove privileges on a database object.
Common DCL Commands in SQL are:
  DCL Command                         Purpose
 GRANT                   Gives specific privileges to user
 REVOKE                  Removes privileges from a user

•   In Oracle, the GRANT and REVOKE commands are Data Control Language (DCL) statements used to
    manage user privileges and roles within the database.
Let’s see these commands in details-
`````

## Page 28

![Original page 28](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-028.jpg)

### Extracted text

`````text
1. GRANT Command:
•   The GRANT command is used to give users access rights (object privileges) to database objects (tables,
    views, procedures, index etc.) or system privileges (like creating tables or users).
•   Some Object privileges are:
      Privilege                       Description
 SELECT                  Read data from a table/view
 INSERT                  Insert new rows
 UPDATE                  Update existing rows
 DELETE                  Delete rows
 REFERENCES              Create foreign keys using the table
 INDEX                   Create indexes on the table
 EXECUTE                 Execute a procedure/function
•   Some System privileges are:
        Privilege                          Description
 CREATE TABLE              Create new tables
 CREATE VIEW               Create views
 CREATE USER               Create new users
 DROP ANY TABLE            Drop any table in any schema
 ALTER ANY TABLE           Alter any table
Note:
    •    Only DBAs or users with sufficient privileges can grant/revoke system privileges.
    •    Revoking a privilege will not cascade; it removes the privilege                  only from the specific user, not
         others they may have granted it to.
Syntax:
         SQL>GRANT privilege1, privilege2,... ON object TO user1,user2,...  [WITH GRANT OPTION];
Here,
           Part                                             Description
 GRANT                      Keyword to start granting privileges
 Privilege1, privilege2,... One or more object privileges like SELECT, INSERT, UPDATE
 object                     The table, view, procedure, etc., that the privilege is being granted on
  user1, user2,...          One or more users or roles to whom you're granting the privileges
 [WITH GRANT                (Optional) Allows the user to grant the same privilege to others
 OPTION]
Examples of GRANT command:
         (For me: Show all below practical by opening multiple Run SQL command Line instances one
for system/password and other is for newly created user)
1)  Granting CONNECT privileges to USER:
         SQL> GRANT   CONNECT   to     john;
This query allows ‘john’ to connect with database.
2) Granting SELECT and INSERT privileges on a table:
         SQL>GRANT SELECT, INSERT ON  emp  TO  john;
This allows ‘john’ to view (SELECT) and add records (INSERT) to the ‘emp’ table of SYSTEM user.
Note: Verify SELECT and INSERT commands works or not by login via ‘john’ user.
`````

## Page 29

![Original page 29](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-029.jpg)

### Extracted text

`````text
E.g.










Note: While accessing table of SYSTEM in other user, we have to specify ‘SYSTEM’ user name along with
table name which is shown in above example.
3) Granting UPDDATE privileges on a table:
        SQL>GRANT   UPDATE   ON   emp   TO   john;
This allows ‘john’ to update the ‘emp’ table of SYSTEM user.
Note: Verify UPDATE command works or not by login via ‘john’ user.
E.g.












Note: While accessing table of SYSTEM in other user, we have to specify ‘SYSTEM’ user name along with
table name which is shown in above example.
4) Granting system privileges:
        SQL>GRANT   CREATE   TABLE   TO   hr;
Now, the user ‘hr’ can create tables.
5) Granting a role:
        SQL>GRANT dba TO scott;
Gives all privileges in the DBA role to user scott.
6) Using WITH GRANT OPTION:
        SQL>GRANT   SELECT   ON   employees   TO   sam   WITH GRANT OPTION;
Now, ‘sam’ can grant the SELECT privilege on employees to other users.
7) Granting  SELECT (read) all tables to user ‘john’:
        SQL>GRANT  SELECT  any table  to  john;
Here, Grant SELECT privileges of all tables to user ‘john’

 1) Creating new database user:
 Syntax:          SQL> CREATE  USER  username  IDENTIFIED BY   password;
 The above query, creates new database user with username and password.
 Example-
          SQL> CREATE   USER     john    IDENTIFIED BY   john123;
 The above query, creates new database user ‘john’ having password ‘john123’
 After, creation of user we try to login with ‘john’ user as follow. But it would generate error like-
`````

## Page 30

![Original page 30](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-030.jpg)

### Extracted text

`````text
Imp Note:

When new user is created, it does not have any rights related with database.
Here, only new database user is created. This created user is not capable to connect the database and not
performs any operations on database. Therefore, we have to assign several predefined roles for created
user which are discussed below-

Common Predefined User Roles with typical privileges (Freedom):
               User Role Name                     Description            Typical Privileges       Use Case / Notes
                                                                         CREATE
                                            Basic role that allows       SESSION,                For users needing
         CONNECT                            a user to connect to         CREATE TABLE,           basic access to
                                            the database.                CREATE VIEW,            begin working in
                                                                         CREATE                  their own schema.
                                                                         SEQUENCE, etc.
                                                                         Includes CREATE
                                            This role allowing           PROCEDURE,              For developers
                                            creation of additional       CREATE                  managing
         RESOURCE                           schema objects like          TRIGGER,                application logic
                                            creating table,              CREATE TYPE,            in their own
                                            creating view etc.           CREATE INDEX,           schema.
                                                                         etc.
                                            Full administrative          All system              Should be granted
                                            privileges for the           privileges with         only to trusted
         DBA                                entire database, with        ADMIN                   DBAs due to full
                                            the ability to grant         OPTION                  control over the
                                            privileges to others.                                database.
                                            Role designed for            Privileges needed       Used in backup,
         EXP_FULL_DATABASE                  performing full              to export any           migration, or data
                                            database exports.            schema's data and       archival tasks.
                                                                         metadata.
                                                                         Privileges needed       Used for restoring
                                            Role designed for            to import data into     data or importing
         IMP_FULL_DATABASE                  performing full              any schema,             large database
                                            database imports.            overriding normal       dumps.
                                                                         access controls.






Granting or Assigning CONNECT role to created john user-


Now, user ‘john’ able to connect to oracle database as                       -


Here, we create new table under logged user ‘john’ as                        -
`````

## Page 31

![Original page 31](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-031.jpg)

### Extracted text

`````text
The above query generates error ‘insufficient privileges’. This is                   due to ‘john’ user

does not have privileges to create new table. We have to assign ‘CREATE TABLE’
privileges to john user as-


Now, we try to create new table as-









Again, it generates error ‘no privileges on tablespace ‘SYSTEM’. This is due to we

have not assign tablespace along with memory size (quota) for ‘john’ user.
We can assign tablespace along with memory size for ‘john’ user by altering it as-


Now, again we try to create new table as-







Here, new table creates successfully under ‘john’ user.


Note: If we have assigned DBA role to created user then there is no need to assign several
privileges to created user. Because, DBA role has             Full administrative privileges for the entire
database, with the ability to grant privileges to others also.
Consider following example, we create new user ‘tom’ and assigning DBA role as –
`````

## Page 32

![Original page 32](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-032.jpg)

### Extracted text

`````text
 Here, tom is DBA user that have all rights same as SYSTEM. No need to specify extra privileges to tom.
2. REVOKE Command:
•   In Oracle, the REVOKE command is used to remove previously granted privileges or roles from a user
    from database.
•   This helps in tightening security or controlling access when a user should no longer have certain
    permissions.
•   Syntax:
                  SQL>REVOKE    privilege1, privilege2,...     ON    object   FROM     user1,user2,...;
•   Here,
           Part                                               Description
 REVOKE                      Is Keyword to start revoking assigned privileges
 Privilege1, privilege2,...  One or more object privileges like SELECT, INSERT, UPDATE
 object                      The table, view, procedure, etc., that the privilege is being granted on
 user1, user2,...            One or more users or roles from whom you're revoking the privileges
1. Revoke Object Privilege:
Suppose SYSTEM user has granted SELECT and INSERT on the EMP table to user SCOTT.
To revoke these:
         SQL> REVOKE    SELECT, INSERT   ON   EMP   FROM   SCOTT;
Above query revoke SELECT and INSERT privileges On table EMP from user SCOTT.
2. Revoke System Privilege:
         SQL>REVOKE   CREATE   TABLE   FROM   SCOTT;
Above query revoke CREATE TABLE   privileges from user SCOTT.
3. Suppose SYSTEM user has granted SELECT on all tables to user john, to revoke these:
         SQL> REVOKE    SELECT    any    table   FROM     john;
Note:
    •    You can only revoke privileges that you granted, unless you're a DBA.
    •    When a privilege is revoked, the user loses that access immediately.
 SPOOL in Oracle-
 In Oracle, SPOOL is a SQL*Plus (or SQLcl) command used to write the output of queries or scripts to a file.
 It's commonly used to export results to .txt, .csv, or .log files.
 Basic Syntax to Use SPOOL:

                   SQL>SPOOL       file_path\filename.extension
 E.g.           SQL>SPOOL        d:\3301\practdbms.txt
 The above query will save the all outputs of statements into file d:\3301\practdbms.txt.
 Note:
 1) If file is not present at location   , it will create and output will save in it.
 2) If file is already present at location    , it will clear all previous data and new output will save in it.
 At last, make spool off as- (This will saves all data in spool file)
          SQL>SPOOL     OFF
`````

## Page 33

![Original page 33](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-033.jpg)

### Extracted text

`````text
SQL Operators used in Oracle-
•   Operator- Operator is symbol that operates onto operand and performs specific task.
•   Every operator has its own task which is predefined.
•   Oracle provides a wide range of operators used in SQL statements to perform operations on data. These
    operators are grouped into several categories, each serving different purposes which is shown as follow-
                            Category                                        Description

             Arithmetic Operators                        Perform mathematical operations
             Comparison (Relational) Operators           Compare values
             Logical Operators                           Performs logical operations

             Set Operators                               Combines result sets of multiple queries

Let’s see all these operators in details-
   1. Arithmetic Operators
These operators are used to perform mathematical calculations shown in following table-
     Operator                 Description                                Example
          +            Addition                       SQL>SELECT  10 + 5   FROM    DUAL;
          -            Subtraction                    SQL>SELECT  10 - 5    FROM    DUAL;
          *            Multiplication                 SQL>SELECT  10 * 5   FROM    DUAL;
          /            Division                       SQL>SELECT  10 / 5    FROM    DUAL;
   2. Comparison (Relational) Operators:
These operators are used to compare two values. Returns TRUE, FALSE, or NULL.
All comparison operators are explained in following table-
 Operator         Description                 Example
 =                Equal to                    SQL>SELECT * FROM EMP WHERE SAL = 5000;
 != or < >        Not equal to                SQL>SELECT * FROM EMP WHERE   SAL < > 10;
 >                Greater than                SQL>SELECT * FROM EMP WHERE SAL > 3000;
 <                Less than                   SQL>SELECT * FROM EMP WHERE SAL < 3000;
 >=               Greater than or equal       SQL>SELECT * FROM EMP WHERE SAL >= 3000;
 <=               Less than or equal          SQL>SELECT * FROM EMP WHERE SAL <= 3000;
 BETWEEN          Within a range              SQL>SELECT * FROM EMP WHERE SAL BETWEEN 2000 AND 5000;
 LIKE             Pattern matching            SQL>SELECT * FROM EMP WHERE ENAME LIKE 'S%';
                  Match in a list (Either
      IN          Or)   (Specific   record    SQL>SELECT * FROM EMP WHERE ENO IN (10, 20);
                  selection  from list)
 IS NULL          Check for NULL value        SQL>SELECT * FROM EMP WHERE COMMISSION IS NULL;
Homework:
1) Create table EMP having fields eno,ename,sal,eadd,commission with appropriate data type and size.
2) Insert any 15 records in created table EMP.
3) Run queries shown in above table and write output.

❖   Wildcard characters percentage (%) and underscore ( _ )
•   In Oracle SQL, the wildcard characters % and _ are used with the LIKE operator for pattern matching.
Wildcard character Percentage (%)  :
The % wildcard represents zero or more characters in the string.
Example:   LIKE   'S%'
This matches any string that starts with the letter 'S' and can be followed by any number of characters
(including none).
`````

## Page 34

![Original page 34](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-034.jpg)

### Extracted text

`````text
             o   Matches: 'Smith', 'Scott', 'S', 'Superman'
             o   Does not match: 'Jones', 'Allen'
Wildcard character Underscore ( _ )  :

The ( _ ) wildcard represents exactly one character in the string.
Example:
This matches any string that starts with 'S' and is followed by exactly one characters.
             o   Matches: 'Sm', 'Sz', 'St'
             o   Does not match: 'S', 'Scott'.

We can combine both wildcards in a single query for more complex patterns shown in following examples
Example 1:

This matches strings that:
             o   Start with 'S'
             o   Have zero or more characters in the middle (because of the %)
             o   End with 'a'
             o   Matches: 'Samantha', 'Socotyza'
             o   Does not match: 'Smith', 'S', 'Sarah'
Example 2:

This matches strings that:
    1)  Must start with the letter S.
    2)  Any two characters after S
    3)  '%' → Matches zero or more characters.
    4)  'n' → The string must end with the letter 'n', after any number of characters matched by %
Examples of Matching Strings pattern:
    •   Samson, Stuwn, S14winn, Sxxn, S__n, Spoon,Sopan,Soon
Examples that Do Not Match String pattern:
    •   San, Steve (doesn't end with n), stiven (doesn’t start with capital S), Soap
   3. Logical Operators
Logical operators are used to combine multiple conditions.
All Logical operators are explained in following table-
 Operator      Description                              Example
 AND           All conditions must be true              SELECT * FROM EMP WHERE DEPTNO = 10 AND SAL > 3000
 OR            At least one condition must be true      SELECT * FROM EMP WHERE DEPTNO = 10 OR DEPTNO = 20
                                                        SELECT * FROM EMP WHERE NOT (SAL > 3000)
 NOT           Negates the condition                    Hint: Display employees whose SAL            not greater than 3000 (it
                                                        selects 3000 too because 3000 not greater than 3000)

   4. Set Operators:
Used to combine the result of two SELECT statements.
All set operators are explained in following table-
   Operator                    Description                                                 Example
 UNION             Combines       results,       removes    SELECT  DEPTNO  FROM  EMP              UNION      SELECT  DEPTNO
                   duplicates                               FROM DEPT;
 UNION ALL         Combines     all     results     (with   SELECT   DEPTNO   FROM   EMP               UNION   ALL        SELECT
                   duplicates)                              DEPTNO FROM DEPT;
 INTERSECT         Shows common records                     SELECT   DEPTNO   FROM   EMP                INTERSECT         SELECT
                                                            DEPTNO FROM DEPT;
 MINUS             Shows records in first query after       SELECT  DEPTNO  FROM  EMP              MINUS      SELECT  DEPTNO
                   getting minus from second query.         FROM DEPT;

Built in functions in ORACLE:
•   We know that function is block of statement that has specific task. Programming task becomes easy due
`````

## Page 35

![Original page 35](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-035.jpg)

### Extracted text

`````text
    to function.
•   Oracle SQL has a wide range of built-in functions that fall into several categories which are listed below-
    1)  Arithmetic Functions
    2)  String (Character) Functions
    3)  Date and Time Functions
    4)  Conversion Functions
    5)  Aggregate Functions
    6)  General Functions
Let’s see these Functions in details-
1) Arithmetic Functions-
•   In Oracle, arithmetic functions are used to perform mathematical operations on numeric data. These are
    typically built-in SQL functions that return numeric results.
•   Commonly used arithmetic functions are shown in following table-
                     Function                    Description                                 Example
              ABS()                      Absolute value                   ABS(-15)=15
              CEIL()                     Returns upper integer            CEIL(14.6)=15
                                         value
              FLOOR()                    Returns lower integer            FLOOR(8.4)=8
                                         value
              MOD()                      Remainder of division            MOD(5,3)=2
              POWER()                    Exponentiation                   POWER(4,3)=64
              ROUND()                    Round to decimal places          ROUND(45.154736,3)=45.155
              TRUNC()                    Truncate decimals                TRUNC(45.154736,3)=45.154
              SQRT()                     Square root                      SQRT(64)=8
              SIGN()                     Sign of number (-1, 0, 1)        SIGN(-15)=-1, SIGN(17)=1,SIGN(0)= 0
              EXP()                      Exponential of number            EXP(1) = 2.7182818
              LN()                       Natural logarithm                LN(10)= 2.302585...
              LOG()                      Logarithm with custom            LOG(10, 100)=2
                                         base
              GREATEST()                 Largest of list                  GREATEST(14,28,35,16)=35
              LEAST()                    Smallest of list                 LEAST(30,58,4,36)=4
•   Let's see these functions in detail with examples.
1. ABS() – Absolute Value
Description: Returns the absolute (positive) value of a number.
Syntax:          ABS(n)
Example:  SQL>SELECT ABS(-45) AS Result FROM dual;
                 -- Result: 45
2. CEIL() – Ceiling
Description: Returns upper integer value of fractional number. (i.e. returns integer value greater than or
equal to the number.)
Syntax:          CEIL(n)
Example:         SQL>SELECT  CEIL(12.3)  AS Result FROM dual;
                 -- Result: 13
3. FLOOR() – Floor
Description: Returns lower integer value of fractional number. (i.e. returns the integer value less than or
equal to the number.)
Syntax:          FLOOR(n)
Example:         SQL>SELECT   FLOOR(12.9)   AS   Result   FROM dual;
                 -- Result: 12
4. MOD() – Modulus
Description: Returns the remainder of a division operation.
`````

## Page 36

![Original page 36](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-036.jpg)

### Extracted text

`````text
Syntax:         MOD(n1, n2)
Example:        SQL>SELECT MOD(10, 3) AS Result FROM dual;
                -- Result: 1
5. POWER() – Exponentiation
Description: Returns the value of one number raised to the power of another. (i.e. it calculates base raise to
power)
Syntax:         POWER(n, m)
Example:        SQL>SELECT POWER(2, 3) AS Result FROM dual;
                -- Result: 8
6. ROUND() – Round Number
Description: Rounds a number to a specified number of decimal places.
Syntax:         ROUND(n, decimal_places)
Example:        SQL>SELECT ROUND(123.456, 2) AS Result FROM dual;
                -- Result: 123.46
7. TRUNC() – Truncate Number
Description: Truncates a number to a specified number of decimal places without rounding.
Syntax:         TRUNC(n, decimal_places)
Example:        SQL>SELECT TRUNC(123.456, 2) AS Result FROM dual;
                -- Result: 123.45
8. SQRT() – Square Root
Description: Returns the square root of a number.
Syntax:         SQRT(n)
Example:        SQL>SELECT SQRT(16) AS Result FROM dual;
                -- Result: 4
9. SIGN() – Sign Indicator
Description: Returns -1, 0, or 1 depending on whether the number is negative, zero, or positive.
Syntax:         SIGN(n)
Example:        SQL>SELECT SIGN(-10) AS Result FROM dual;                                                Result    -1
                SQL>SELECT SIGN(0) AS Result FROM dual;                                              Result      0
                SQL>SELECT SIGN(10) AS Result FROM dual;                                             Result     1
10. EXP() – Exponential
Description: Returns e (Euler’s number) raised to the power of the input number.
Syntax:         EXP(n)
Example:        SQL>SELECT EXP(1) AS Result FROM dual;
                -- Result: 2.7182818
11. LN() – Natural Logarithm
Description: Returns the natural logarithm (base e) of a number.
Syntax:         LN(n)
Example:        SQL>SELECT LN(10) AS Result FROM dual;
                -- Result: 2.302585...
12. LOG() – Logarithm with Custom Base
Description: Returns the logarithm of a number with a specific base.
Syntax:         LOG(base, number)
Example:        SQL>SELECT LOG(10, 100) AS Result FROM dual;
                -- Result: 2
13. GREATEST() and LEAST()
Description:
    •   GREATEST() returns the largest value among two or more inputs.
    •   LEAST() returns the smallest value among two or more inputs.
Syntax:
        GREATEST(n1, n2, ..., nN)
        LEAST(n1, n2, ..., nN)
Example:        SQL>SELECT GREATEST(10, 20, 5) AS max_val FROM DUAL,
                         -- max_val = 20
                SQL> SELECT LEAST(10, 20, 5) AS min_val FROM  DUAL;        -- min_val = 5
`````

## Page 37

![Original page 37](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-037.jpg)

### Extracted text

`````text
2) String (Character) Functions:
•   In  Oracle  SQL,    String  (Character)  Functions         are  used  to  manipulate  string  data     (VARCHAR,
    VARCHAR2, CHAR, etc.).
•   These functions help to format, modify, or retrieve specific portions of string values.
•   Here's a list of commonly used String Functions in Oracle SQL, along with their descriptions                      and
    examples:
         Function                   Description                          Example SQL                          Output
 UPPER(str)                   Converts all letters to    SQL>SELECT UPPER('oracle') FROM                    ORACLE
                              uppercase.                 dual;
 LOWER(str)                   Converts all letters to    SQL>SELECT LOWER('OrAcLe')                         oracle
                              lowercase.                 FROM dual;
 INITCAP(str)                 Capitalizes the first      SQL>SELECT INITCAP('oracle sql')                   Oracle Sql
                              letter of each word.       FROM dual;
                              Returns the number
 LENGTH(str)                  of                         SQL>SELECT LENGTH('Oracle')                        6
                              characters.(including      FROM dual;
                              space)
                              Returns substring          SQL>SELECT SUBSTR('OracleSQL', 1,
 SUBSTR(str, start, len)      starting from a            6) FROM dual;                                      Oracle
                              position.
 INSTR(str, substr)           Finds the position of      SQL>SELECT INSTR('OracleSQL', 'S')                 7
                              a substring.               FROM dual;
 LPAD(str, len,               Left-pads string to        SQL>SELECT LPAD('123', 5, '*') FROM                **123
 padchar)                     given length.              dual;
 RPAD(str, len,               Right-pads string to       SQL>SELECT RPAD('123', 5, '*') FROM                123**
 padchar)                     given length.              dual;
                              Removes
 TRIM(char FROM str)          leading/trailing           SQL>SELECT TRIM('O' FROM 'Oracle')                 racle
                              (eighter first or last     FROM dual;
                              character).
 REPLACE(str, search,         Replaces substrings.       SQL>SELECT REPLACE('Oracle DB',                    Oracle
 replace)                                                'DB', 'Cloud') FROM dual;                          Cloud
 CONCAT(str1, str2)           Concatenates two           SQL>SELECT CONCAT('Oracle', 'SQL')                 OracleSQL
                              strings.                   FROM dual;
 TRANSLATE(str,               Replaces each              SQL>SELECT TRANSLATE('12345', '2',
 mat_char, map_char)          character by               'X') FROM dual;                                    1X345
                              mapping.
 ASCII(char)                  Returns ASCII value        SQL>SELECT ASCII('A') FROM dual;                   65
                              of the character.
 CHR(code)                    Returns character for      SQL>SELECT CHR(65) FROM dual;                      A
                              ASCII code.
Let’s see all these functions in details-
1. UPPER(string)
Converts all characters in a string to uppercase.
Example- SQL>SELECT UPPER('oracle') AS upper_example FROM dual;
                -- Output: ORACLE
2. LOWER(string)
Converts all characters in a string to lowercase.
Example- SQL>SELECT LOWER('OrAcLe') AS lower_example FROM dual;
        -- Output: oracle
3. INITCAP(string)
Converts the first character of each word to uppercase and the rest to lowercase.
Example- SQL>SELECT INITCAP('welcome to oracle') AS initcap_example FROM dual;
                -- Output: Welcome To Oracle
`````

## Page 38

![Original page 38](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-038.jpg)

### Extracted text

`````text
4. LENGTH(string)
Returns the number of characters in the string.
Example- SQL>SELECT LENGTH('Oracle') AS length_example FROM dual;
                -- Output: 6
 5. SUBSTR(string, start_position, length)
Returns a part (substring) of a string starting at a given position.
Example- SQL>SELECT SUBSTR('Oracle Database', 1, 6) AS substr_example FROM dual;
                -- Output: Oracle
6. INSTR(string, substring)
Returns the position of the first occurrence of a substring in a string.
If substring is not found in main string then it returns 0.
Example- SQL>SELECT INSTR('Oracle Database', 'D') AS instr_example FROM dual;
                -- Output: 8
7. LPAD(string, length, pad_char)
Left-pads a string with a character to reach a certain length.
Example- SQL>SELECT LPAD('123', 5, '0') AS lpad_example FROM dual;
                -- Output: 00123
8. RPAD(string, length, pad_char)
Right-pads a string with a character to reach a certain length.
Example- SQL>SELECT RPAD('123', 5, '0') AS rpad_example FROM dual;
                -- Output: 12300
9. TRIM([LEADING | TRAILING | BOTH] trim_char FROM string)
Removes specified characters (or spaces by default) from the beginning, end, or both ends of a string.
Example- SQL>SELECT TRIM(' x' FROM 'xOraclex') AS trim_example FROM dual;
                -- Output: Oracle
Example- SQL>SELECT TRIM('O' FROM 'Oracle') AS trim_char_example FROM dual;
                -- Output: racle
10. REPLACE(string, search_string, replacement_string)
Replaces all occurrences of a substring with another substring.
Example- SQL>SELECT REPLACE('Oracle Dbase', 'Dbase', 'Cloud') AS replace_example FROM dual;
                -- Output: Oracle Cloud
11. CONCAT(string1, string2)
Concatenates two strings. (Only two arguments allowed)
Example- SQL>SELECT CONCAT('Oracle', 'DB') AS concat_example FROM dual;
                -- Output: OracleDB
12. TRANSLATE(string, from_chars, to_chars)
Replaces each character in from_chars with the corresponding character in to_chars.
Example- SQL>SELECT TRANSLATE('12345', '123', 'abc') AS translate_example FROM dual;
                -- Output: abc45
13. ASCII(char)
Returns the ASCII code of the first character.
Example- SQL>SELECT ASCII('A') AS ascii_example FROM dual;
                -- Output: 65
14. CHR(ascii_code)
Returns the character corresponding to the ASCII code.
Example- SQL>SELECT CHR(65) AS chr_example FROM dual;
                -- Output: A
`````

## Page 39

![Original page 39](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-039.jpg)

### Extracted text

`````text
3) Date and Time Functions:
•   Oracle provides a rich set of Date and Time functions to handle date, time, timestamp, intervals, and
    time zone operations.
•   Following table shows different date and time functions with description and example-

      Function Name                         Description                                           Example
 SYSDATE                       Returns current date and time of DB      SELECT SYSDATE FROM DUAL;
                               server
                               Returns current timestamp with time
 SYSTIMESTAMP                  zone and fractional seconds of DB        SELECT SYSTIMESTAMP FROM DUAL;
                               server
 CURRENT_DATE                  Returns current date in session time     SELECT CURRENT_DATE FROM DUAL;
                               zone.
 CURRENT_TIMESTAMP             Returns current timestamp in session     SELECT CURRENT_TIMESTAMP FROM DUAL;
                               time zone.
 LOCALTIMESTAMP                Returns current timestamp (no time       SELECT LOCALTIMESTAMP FROM DUAL;
                               zone info).
 DBTIMEZONE                    Returns server database time zone.       SELECT DBTIMEZONE FROM DUAL;
 SESSIONTIMEZONE               Returns session time zone.               SELECT SESSIONTIMEZONE FROM DUAL;
 TO_DATE                       Converts string to date.                 SELECT TO_DATE ('2025-09-04', 'YYYY-MM-DD')
                                                                        FROM DUAL;
 TO_CHAR                       Converts date/timestamp to string        SELECT TO_CHAR (SYSDATE, 'DD-MON-YYYY
                               with format.                             HH24:MI:SS') FROM DUAL;
 TO_TIMESTAMP                  Converts string to timestamp.            SELECT TO_TIMESTAMP ('2025-09-04 10:00:00',
                                                                        'YYYY-MM-DD HH24:MI:SS') FROM DUAL;
                               Adds or subtracts months to/from a
 ADD_MONTHS                    date. (if month val is +ve then          SELECT ADD_MONTHS (SYSDATE, 2) FROM DUAL;
                               months add, if month val is -ve then
                               months subtracts)
 MONTHS_BETWEEN                Returns number of months between         SELECT MONTHS_BETWEEN (SYSDATE, TO_DATE
                               two dates.                               ('2025-01-01', 'YYYY-MM-DD')) FROM DUAL;
 LAST_DAY                      Returns last day of the month for        SELECT LAST_DAY(SYSDATE) FROM DUAL;
                               given date. (e.g. 30-Sep-2025)
 NEXT_DAY                      Returns next occurrence of given         SELECT NEXT_DAY (SYSDATE, 'FRIDAY') FROM
                               weekday.                                 DUAL;
 ROUND(date)                   Rounds date to nearest unit (day,        SELECT ROUND (SYSDATE, 'MONTH') FROM DUAL;
                               month, etc.).
 EXTRACT                       Extracts part (YEAR, MONTH,              SELECT EXTRACT (YEAR FROM SYSDATE) FROM
                               DAY) from date or timestamp.             DUAL;
 NEW_TIME                      Converts date from one time zone to      SELECT NEW_TIME (SYSDATE, 'PST', 'GMT') FROM
                               another (legacy).                        DUAL;
 FROM_TZ                       Assigns time zone to a timestamp.        SELECT FROM_TZ (TIMESTAMP '2025-09-04 10:00:00',
                                                                        'UTC') FROM DUAL;
 INTERVAL (literal)            Adds specific interval duration to       SELECT SYSTIMESTAMP + INTERVAL '2' DAY FROM
                               timestamp.                               DUAL;
 DATE arithmetic               Subtracting dates returns difference     SELECT SYSDATE - TO_DATE ('2025-09-01', 'YYYY-
                               in days.                                 MM-DD') AS days_diff FROM DUAL;
Common Date Format Elements in Oracle:
                              Format                    Meaning                Example
                          YYYY                 4-digit year                    1985
                          YY                   2-digit year                    85
                          MM                   2-digit month                   06
                          MON                  3-letter month                  JUN
                          MONTH                Full month name                 JUNE
                          DD                   Day of month                    20
                          DY                   3-letter day                    THU
                          DAY                  Full day name                   Thursday
`````

## Page 40

![Original page 40](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-040.jpg)

### Extracted text

`````text
                     HH24             24-hour format             17
                     HH               12-hour format             5 AM
                     MI               Minute                     45
                     SS               Second                     25
We explain all above-mentioned date and functions as follow-
  1. SYSDATE
Returns the current date and time of the database server (no fractional seconds).
SQL>SELECT SYSDATE FROM DUAL;
Output example: 04-SEP-25 10:24:00
  2. SYSTIMESTAMP
Returns the current timestamp with time zone and fractional seconds.
SQL>SELECT SYSTIMESTAMP FROM DUAL;
Output example: 04-SEP-25 10.24.00.123456 AM +05:30
  3. CURRENT_DATE
Returns the current date and time in the session time zone.
SQL>SELECT CURRENT_DATE FROM DUAL;
  4. CURRENT_TIMESTAMP
SQL>Returns current timestamp in the session time zone.
SELECT CURRENT_TIMESTAMP FROM DUAL;
  5. LOCALTIMESTAMP
Returns the current timestamp without time zone.
SQL>SELECT LOCALTIMESTAMP FROM DUAL;
  6. DBTIMEZONE
Returns the database server time zone as a string.
SQL>SELECT DBTIMEZONE FROM DUAL;
  7. SESSIONTIMEZONE
Returns the current session's time zone.
SQL>SELECT SESSIONTIMEZONE FROM DUAL;
  8. EXTRACT
Extracts and returns a specific part of a date (like year, month, day).
SQL>SELECT EXTRACT(YEAR FROM SYSDATE) AS YEAR FROM DUAL;
SQL>SELECT EXTRACT(MONTH FROM SYSTIMESTAMP) AS MONTH FROM DUAL;
  9. TO_DATE
Converts a string to a DATE type.
SQL>SELECT TO_DATE('2025-09-04', 'YYYY-MM-DD') FROM DUAL;
  10. TO_CHAR
Converts a date to a string with the specified format.
SQL>SELECT TO_CHAR(SYSDATE, 'DD-MON-YYYY HH24:MI:SS') FROM DUAL;
  11. TO_TIMESTAMP
Converts a string to a TIMESTAMP.
SQL>SELECT TO_TIMESTAMP('2025-09-04 10:30:00', 'YYYY-MM-DD HH24:MI:SS') FROM DUAL;
  12. ADD_MONTHS
Adds or subtracts months to a date.
SQL>SELECT ADD_MONTHS(SYSDATE, 2) FROM DUAL;
SQL>SELECT ADD_MONTHS(SYSDATE, -1) FROM DUAL;
  13. MONTHS_BETWEEN
Returns the number of months between two dates.
SQL>SELECT MONTHS_BETWEEN (SYSDATE, TO_DATE ('2025-01-01', 'YYYY-MM-DD')) FROM
DUAL;
  14. NEXT_DAY
Finds the next date that falls on a specific weekday.
SQL>SELECT NEXT_DAY (SYSDATE, 'FRIDAY') FROM DUAL;
`````

## Page 41

![Original page 41](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-041.jpg)

### Extracted text

`````text
  15. LAST_DAY
Returns the last day of the month for a date. (dd-MON-YY format)
SQL>SELECT LAST_DAY(SYSDATE) FROM DUAL;
  16. ROUND(date)
Rounds a date to the nearest unit (day, month, year, etc.)
SQL>SELECT ROUND (SYSDATE, 'MONTH') FROM DUAL;
  17. NEW_TIME
Converts time from one time zone to another (legacy; limited zones).
SQL>SELECT NEW_TIME (SYSDATE, 'EST', 'GMT') FROM DUAL;
  18. INTERVAL
You can use interval literals to add time.
SQL>SELECT SYSTIMESTAMP + INTERVAL '2' DAY FROM DUAL;
SQL>SELECT SYSTIMESTAMP + INTERVAL '10' MINUTE FROM DUAL;
  19. FROM_TZ
Converts a TIMESTAMP to a TIMESTAMP WITH TIME ZONE.
SELECT FROM_TZ(TIMESTAMP '2025-09-04 10:00:00', 'UTC') FROM DUAL;
  20. CURRENT_DATE - DATE
You can do date arithmetic: subtracting dates gives difference in days.
SQL>SELECT SYSDATE - TO_DATE('2025-09-01', 'YYYY-MM-DD') AS days_diff FROM DUAL;


4) Conversion Functions: (Type conversion functions)
•   Oracle provides several conversion functions to convert data from one type to another, such as converting
    strings to numbers, numbers to strings, or dates to strings, and vice versa.
•   These are essential when handling data with mismatched types in queries or for formatting outputs
•    Following table shows most commonly used Oracle conversion functions, with examples.
              Function               Converts From → To                   Common Usage Example
        TO_CHAR                 Number/Date → String              TO_CHAR (SYSDATE, 'DD-MON-YYYY')
        TO_NUMBER               String → Number                   TO_NUMBER ('12345.67')
        TO_DATE                 String → Date                     TO_DATE ('06-09-2025', 'DD-MM-YYYY')
        TO_TIMESTAMP            String → Timestamp                TO_TIMESTAMP ('2025-09-06 14:30:45', ...)
        CAST                    Any supported types               CAST ('123' AS NUMBER)
Let’s see these functions in details-
1. TO_CHAR:
Used to convert numbers or dates to a string.
Syntax:   TO_CHAR (expr, [format])
Examples:
    1)  -- Convert number to string with formatting
SQL>SELECT TO_CHAR (12345.67, '99999.99') AS Result FROM dual;
     2) -- Convert date to string
SQL>SELECT TO_CHAR(SYSDATE, 'DD-MONTH-YYYY’) AS Result FROM dual;
2. TO_NUMBER:
Used to convert a string to a number.
Syntax:         TO_NUMBER (expr, [format])
Examples:
    1)  -- Convert string to number
SQL>SELECT TO_NUMBER ('12345.67') AS num FROM dual;
    2)  -- Convert formatted string to number
SQL>SELECT TO_NUMBER ('12,345.67', '99,999.99') AS Result FROM dual;
3. TO_DATE:
Used to convert a string into a date using a specific format.
Syntax:         TO_DATE(expr, format)
Examples:
`````

## Page 42

![Original page 42](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-042.jpg)

### Extracted text

`````text
    1)  -- Convert string to date
SQL>SELECT TO_DATE ('06-09-2025', 'DD-MM-YYYY') AS Result FROM dual;
    2)  -- Convert another format
SQL> SELECT TO_DATE ('2025/09/06 14:30', 'YYYY/MM/DD HH24:MI') AS Result FROM dual;
4. TO_TIMESTAMP:
Converts a string to a timestamp, which includes fractional seconds.
Syntax:          TO_TIMESTAMP(expr, format)
Example:
SQL>SELECT TO_TIMESTAMP ('2025-09-06 14:30:45.123', 'YYYY-MM-DD HH24:MI:SS.FF3') AS ts
FROM dual;
5. CAST :
Used to convert between different data types, similar to TO_*, but it is more flexible and ANSI SQL
compliant.
Syntax: CAST(expression AS target_data_type)
Examples:
1) -- Cast string to number
SQL>SELECT CAST('123.45' AS NUMBER(6,2)) AS cast_num FROM dual;
2) -- Cast string to date
SQL>SELECT CAST('2025-09-06' AS DATE) AS cast_date FROM dual;
3) -- Cast number to character
SQL>SELECT CAST(12345 AS VARCHAR2(10)) AS cast_str FROM dual;

5) Aggregate Functions:
•   Oracle aggregate functions perform a calculation on a set of values and return a single value.
•   These functions are commonly used with the GROUP BY clause but can also be used without it to compute
    summary values across entire tables or result sets.
•   Following table shows most commonly used Oracle aggregate functions, with examples.
         Function                       Description                              Example
 SUM(expr)                    Total sum                          SUM(salary)
 AVG(expr)                    Average value                      AVG(salary)
 MIN(expr)                    Minimum value                      MIN(hire_date)
 MAX(expr)                    Maximum value                      MAX(hire_date)
 COUNT(*)                     Total number of rows (record)      COUNT(*)
 COUNT(expr)                  Count of non-null values           COUNT(salary)
 COUNT(DISTINCT field)        Count of unique values             COUNT(DISTINCT department_id)
Let’s see these functions in details-
Consider we have employees table-
                               Employees Table
       eid              ename            salary          deptId      deptName
    emp101             ROHIT              5000              1             IT
    emp102             KIRAN              3000              2            HR
    emp103               RAJ              2000              3           Sales
    emp104             UMESH              2200              2            HR
    emp105              AMIR              2800              2            HR
    emp106             AMOL               1570              3           Sales
    emp107            SANJAY              6000              1             IT

1. SUM(): Finds the Total Sum of all Values
SQL>SELECT               SUM(salary)         AS    total_salary     FROM  employees;
          Returns the total of all salaries in the employees table.
2. AVG( ): Finds the Average Value of given field.
`````

## Page 43

![Original page 43](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-043.jpg)

### Extracted text

`````text
SQL>SELECT                AVG(salary)      AS       average_salary            FROM              employees;
3. COUNT( ) – It counts the Number of Rows i.e. records as well as non-null values in table
-- Count all rows
SQL>SELECT   COUNT(*)   AS                 total_employees            FROM employees;
-- Count non-null values only
SQL>SELECT                COUNT(deptName)   AS     Depts              FROM employees;
4. MIN( ): Finds the Minimum Value of given field.
SQL>SELECT                MIN(salary)      AS       MinSalary         from    DUAL;
5. MAX( ): Finds the Maximum Value of given field.
SQL>SELECT                MAX(salary)      AS       MaxSalary         from    DUAL;
6. COUNT(DISTINCT): It Counts Unique Values from given field.
SQL>SELECT                COUNT(DISTINCT deptName)                    AS      unique_dept       FROM   employees;

6) General Functions:
•   Oracle provides a variety of general functions which are used to manipulate data, handle nulls, perform
    type conversions, and more.
•   These functions are commonly used in SQL queries to customize output or perform logic inside queries.
•   The commonly used general functions in oracle are shown below-
  Function                                    Purpose                                               Example
 NVL            Replace column NULL by specified value                                 NVL(col, 0)
 NVL2           If column value is NOT NULL then return true otherwise false           NVL2(col, 'true', 'false')
 NULLIF         Returns NULL if column value is equal to given value.                  NULLIF(col, 10)
 COALESCE       Returns the first non-NULL expression in the list.                     COALESCE(null,     null, 'A')
 DECODE         Acts like a simple CASE statement.                                     DECODE(col, 1, 'One',2,'Two',
                                                                                       'Other')
 SYSDATE        Returns Current date                                                   SYSDATE
 USER,UID       Returns Current username     and its userid                            USER,UID
Let’s see these functions in details      -
1. NVL( ):
Purpose: Replace NULL with a default value.
Syntax:          NVL(col, replacement_value)
Example: SQL>SELECT eid, NVL(ename, 0) AS   Result     FROM employees;
This replaces NULL ename with 0.
2. NVL2( ):
Purpose: If column value is NOT NULL then return          true otherwise false.
Example:         SQL>SELECT eid, NVL2(ename, 'Yes', 'No') AS status FROM employees;
3. NULLIF( ):
Purpose: Returns NULL if column value is equal to given value.
Example: SQL>SELECT NULLIF(empid, 101)  AS  Result  FROM dual;
4. COALESCE( ):
Purpose: Returns the first non-NULL expression in the list.
Example: SQL>SELECT COALESCE (NULL, NULL, 'Hello', 'World') AS   Result   FROM dual;
5. DECODE( ):
Purpose: Acts like a simple CASE statement.
Syntax: DECODE(expr, search1, result1, search2, result2, ..., default)     ;
Example:
SQL>SELECT eid, DECODE(ename,‘raj’, 'YES', ‘sam’, ‘YES’, ‘No’) AS Result   FROM employees;
6. SYSDATE:
Purpose: Get current date.
Example: SQL>SELECT SYSDATE AS   current_date    FROM   dual;
7. USER, UID:
Purpose: Return username and userid of the current user respectively.
Example:  SQL>SELECT     USER, UID   FROM   dual;
`````

## Page 44

![Original page 44](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-044.jpg)

### Extracted text

`````text
Clauses in Oracle-
•   In Oracle SQL, clauses are components or parts of SQL statements that perform specific functions or task
    like filtering, grouping, sorting, or joining data.
•   Understanding these clauses helps you to write powerful and efficient SQL queries.
•   Let’s see different clauses used in oracle with example as follow-
1) ORDER BY Clause:
•   The ORDER BY clause in Oracle SQL is used to sort the result set of a query by one or more columns,
    in ascending (ASC) or descending (DESC) order.
•   By default, order of sorting is Ascending order (ASC).
•   Note:
    •   ORDER BY is always applied after all other clauses (like WHERE, GROUP BY, etc.).
    •   If ORDER BY is not specified, Oracle does not guarantee any specific order of results.
•   Syntax-
 SQL>SELECT   col1, col2, ...  FROM   table_name  ORDER BY col1 SortOrd, col2 SortOrd, ...;
 Here,
 SortOrd may be DESC (To sort data in Descending order) or ASC(Ascending order)
Example: Suppose we have ‘employees’ table as-
 emp_id       first_name        salary
   101            John          5000
   102           Alice          7000
   103            Bob           6000

   Example 1: Sort by Salary (Ascending)
SQL>SELECT  emp_id, first_name, salary   FROM  employees   ORDER BY salary;
Result:
 emp_id       first_name        salary
   101            John          5000
   103            Bob           6000
   102           Alice          7000
Note: Here, by default ‘salary’ is sorted in Ascending order.

   Example 2: Sort by Salary (Descending)
SQL>SELECT emp_id, first_name, salary              FROM  employees  ORDER BY salary DESC;
Result:
 emp_id       first_name        salary
   102           Alice          7000
   103            Bob           6000
   101            John          5000
   Example 3: Sort by Multiple Columns
SQL>SELECT emp_id, first_name, salary FROM employees  ORDER BY salary DESC, first_name ASC;
    •   First sorts by salary in descending order.
    •   Then sorts by first name in ascending order only if salaries are equal.
Result:






   Example 4: Using Column Numbers
You can also sort by column positions as follow-
SQL>SELECT emp_id, first_name, salary   FROM    employees     ORDER BY   3    ASC;
`````

## Page 45

![Original page 45](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-045.jpg)

### Extracted text

`````text
 -- Here, data is sorted in Ascending order of 3rd column (salary)
Result:





2) GROUP BY Clause:
•   The GROUP BY clause in Oracle SQL is used to group rows i.e records that have the same values in
    specified columns into summary rows, like finding the total, average, count, etc., for each group.
•   GROUP BY clause typically used with aggregate functions like SUM(),AVG(), COUNT(),MAX()
    MIN() etc.
•   Syntax:
SQL>SELECT column1, aggregate_function(column2)                     FROM   table_name        GROUP BY column1;
    •   column1 is the column you want to group by.
    •   aggregate_function(column2) is the calculation you want to perform on another column.
Example: Using GROUP BY
Suppose we have a table SALES with the following structure and data:









   Query: Total Sales amount by Salesman







   Query: Total Sales by Region







   Query: Average sale amount by Region






   Query: Minimum sale amount by Salesman.
`````

## Page 46

![Original page 46](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-046.jpg)

### Extracted text

`````text
❖   You can use GROUP BY with multiple columns like-
I) Total sale amount by salesman and region.







II) Region counts by salesman and region.







3) HAVING Clause:
•   In Oracle SQL, the HAVING clause is used to filter groups of rows i.e. records created by the GROUP
    BY clause.
•   HAVING clause works like a WHERE clause but it works on aggregated or grouped data.
•   Note-
        ➢    WHERE clause filters individual rows before grouping where as HAVING clause filters groups
             (aggregated results) after grouping.
        ➢    We can use HAVING clause with aggregate functions like COUNT(), SUM(), AVG(), MIN(), MAX().
•   Syntax:
SQL>SELECT column1, aggregate_function(column2)                        FROM   table_name          GROUP BY column1
           HAVING   condition;
Here,
    •   column1 is the column you want to group by.
    •   aggregate_function(column2) is the calculation you want to perform on another column.
    •   condition is condition used to filter the group.
Example-Suppose we have a table emp_dept:










1. Find total salary per department (use of GROUP BY clause)
`````

## Page 47

![Original page 47](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-047.jpg)

### Extracted text

`````text
2. Now, we use HAVING to filter groups by condition-

     Example: Show only departments where total salary > 50000







Here,  (SALES is excluded because its total = 25000, which is not > 50000)
3. We can also Combine WHERE + HAVING as follow-

     Example: Show only departments with employees earning salary > 30000, and total salary > 100000








4) ON DELETE CASCADE clause:
•   The ON DELETE CASCADE clause in Oracle SQL is used in foreign key constraints.
•   This clause tells Oracle:
     “If a row in the parent table is deleted, automatically delete all matching rows in the child table.”
•   ON DELETE CASCADE clause ensures referential integrity and avoids orphan records in child
    tables.
  Note-
    1.  ON DELETE CASCADE clause used with FOREIGN KEY definition.
    2.  ON DELETE CASCADE clause allows automatically deletion of rows in child table when the
        parent row is deleted.
    3.  ON DELETE CASCADE clause useful in master-detail (parent-child) relationships.

Syntax- Creating Table with ON DELETE CASECADE clause
 SQL>CREATE TABLE child_table (
    Col1 datatype,
    Col2 datatype,
    ...,
    CONSTRAINT fk_name FOREIGN KEY (child_column)
    REFERENCES parent_table(parent_column)
    ON DELETE CASCADE
 );
`````

## Page 48

![Original page 48](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-048.jpg)

### Extracted text

`````text
Example-
 1) Create PARENT table with PRIMARY KEY constraint-





 2) Create CHILD table with FOREIGN KEY constraint along with ON DELETE CASCADE clause





 3) Inserting records into PARENT table-















 4) Inserting records into CHILD table-
`````

## Page 49

![Original page 49](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-049.jpg)

### Extracted text

`````text
 5) Display records of PARENT and CHILD tables-












 6) DELETE record from PARENT table-



 Note- Here, parent record is deleted that refer to child record also this is because of             ON DELTE

 CASCADE clause.

 7) Display records of PARENT and CHILD tables-













 8. Effect
     •   The row with pid = 1 is deleted from PARENT table.
     •   Automatically, all child’s with pid = 1 are also deleted from CHILD table.
 So now, only KOMAL (pid = 2) remains in the CHILD table.

          Without ON DELETE CASCADE
 If you try to delete a parent that still has child’s, Oracle will throw an integrity constraint error
 (child records exist).
 With ON DELETE CASCADE, Oracle takes care of child rows automatically.
`````

## Page 50

![Original page 50](assets/06_Unit_I_intro_SQL_DDL_DML_TCL_DCL_Operators_built_fun_Clause_Integrity_2/page-050.jpg)

### Extracted text

`````text
                                Theory Assignment-II
        Short Answer Questions
1  What is the difference between DDL and DML commands?
2  Define transaction in SQL. Give two examples of TCL             commands.
3  What is the purpose of the ON DELETE CASCADE clause in Oracle                SQL?
4  Write syntax to rename a table using the ALTER            command.
5  What is the difference between TRUNCATE and DELETE             commands?
6  Define Foreign Key with an example.
7  What are aggregate functions in SQL? Give two            examples.
8  Explain BETWEEN and LIKE operators with examples.
9  What is the role of the COMMIT statement?
10 Write syntax for creating a table with a PRIMARY KEY              constraint.

        Long Answer Questions
1  Explain different categories of SQL commands: DDL, DML, DCL, TCL with suitable
   examples.
2  Discuss various Integrity Constraints in SQL: Primary Key, Foreign Key, Unique,
   Check, Not Null with syntax and examples.
3  Explain operators in SQL with examples: Arithmetic, Comparison, Logical, Set, and
   Special operators.
4  What are built-in functions in SQL? Explain numeric, string, and date functions with
   examples.
5  Describe Clauses in SQL: WHERE, ORDER BY, GROUP BY, HAVING, DISTINCT with
   examples.
6  Explain transaction control in SQL with COMMIT, ROLLBACK, SAVEPOINT, and SET
   TRANSACTION commands. Give examples.
7  Write detailed notes on ALTER TABLE command with examples of adding,
   modifying, renaming columns and adding/dropping constraints.
8  Differentiate between DELETE, TRUNCATE, and DROP commands with                examples.



        Multiple Choice Questions (MCQs)
1  Which of the following is a DDL command? a) SELECT b) INSERT c) CREATE d) UPDATE
   Answer: c) CREATE
2  Which SQL command is used to remove all rows but keep the table structure? a)
   DROP b) DELETE c) TRUNCATE d) REMOVE Answer: c) TRUNCATE
3  Which of the following is a valid TCL command? a) GRANT b) SAVEPOINT c) REVOKE d)
   ALTER Answer: b) SAVEPOINT
4  A Foreign Key is used to: a) Uniquely identify each record in a table b) Link two
   tables together
   c) Enforce NOT NULL condition d) Automatically increment column values                  Answer: b)
   Link two tables together
5  Which of the following functions returns the length of a string? a) SUBSTR() b)
   LENGTH() c) INSTR() d) TRIM() Answer: b) LENGTH()
6  The HAVING clause is used with: a) WHERE b) GROUP BY c) ORDER BY d) DISTINCT
   Answer: b) GROUP BY
7  The ON DELETE CASCADE option ensures: a) Parent rows cannot be deleted if child
   rows exist b) Deleting a parent row automatically deletes matching child rows c)
   Child table is locked when parent is deleted d) None of the above Answer: b)
   Deleting a parent row automatically deletes matching child rows
`````


---

# Source file: 05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views.md

# Unit-II DBMS Subquery Joins- Sequence- Index- Pseudo columns- Views

- Original PDF: `notes\Unit-II DBMS Subquery Joins- Sequence- Index- Pseudo columns- Views.pdf`
- Pages: 32
- Preservation: every original page is rendered below; extracted text follows each page image.

## Page 1

![Original page 1](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-001.jpg)

### Extracted text

`````text
                                                                                      B.Sc(ECS)-II (Semester III)
                                                                                    Database Management System
Unit-II Sub queries, Joins, Sequence, Index, Pseudo columns, Views
Subquery: (Inner query or Nested query)
•   A query embedded inside another query           is called ‘Subquery’
•   OR A query within another query         is called a s ‘subquery   ’ (or nested query    ).
•   In some situation, we have to pass result (i.e. output) of one query as input to main query, in this case
    ‘Sub query’ is used.
•   Here, main query is also called ‘outer query’ to which result of sub query is passed as input.
•   Note that:
    ➢   The subquery executes first and returns a result.
    ➢   The main (outer) query uses that result to complete execution.
•   In Oracle, subqueries are commonly used inside:
    ➢   SELECT clause for returning computed i.e. calculated values
    ➢   WHERE clause for filtering data
    ➢   HAVING clause for filtering groups
    ➢   FROM clause for treating subquery results as a temporary table

❖ Purpose of a Subquery in Oracle:
The main purpose of a subquery is to:
1.  Break down complex queries into smaller, manageable parts.
2.  Provide intermediate results to be used by the main (outer) query.
3.  Perform comparisons against aggregated or calculated values.
4.  Filter data dynamically instead of hardcoding values.
5.  Enhance flexibility such as subqueries almost used anywhere in WHERE, FROM, HAVING, SELECT
    clause

❖ Usage of Subqueries in Oracle:
Following are the several usage of subquery:
1. Subquery is used for Filtering rows based on calculations
2. Subquery is used to work with multiple values.
3. Subquery used for filtering groups that uses aggregated data.
4. Subquery used to create virtual tables (Inline Views)
5. Subquery used for Row-by-row comparison (record comparison) (Correlated Subquery)
General Syntax for subquery-
 SQL>SELECT  col1,col2,… FROM  tablename  WHERE column operator (SELECT column
     FROM   tablename  WHERE  condition );
Here,
Col1,col2,…. → columns to display in the main query
Column is to which result of sub query is passed as input.
operator → comparison operators (=, >, <, IN, ANY, ALL, EXISTS)
subquery → placed inside parentheses ( )
Example-
SQL>SELECT   *   FROM   employee   WHERE   salary=(SELECT  MIN(salary)  FROM  employee );

Here,
➢   Inner Query (Subquery) is:
             SQL>SELECT    MIN(salary)   FROM    employee;
    •   The database first executes this subquery.
    •   It scans the entire ‘employee’ table and finds the minimum salary.
`````

## Page 2

![Original page 2](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-002.jpg)

### Extracted text

`````text
➢   Outer Query (Main Query) is:
SQL>SELECT * FROM employee WHERE salary = <result of subquery>;

Here, Oracle passes the result of the sub query to main query and retrieves all employees whose salary
is equal to the minimum salary.

Types of Subqueries in Oracle:
We can classify subqueries based on result, placement, and correlation which are as follow-
A) Based on Result:
“Based on result” means how many rows/columns the subquery returns to the outer query.
        A.1) Single-row subquery
        A.2) Multi-row subquery
        A.3) Multi-column subquery
        A.4) Scaler subquery
B) Based on Placement:
“Based on Placement” subquery means where the subquery is written inside the SQL statement
        B.1) Subquery in WHERE clause
        B.2) Subquery in FROM clause
        B.3) Subquery in SELECT clause
C) Based on Correlation:
“Based on Correlation” subquery means whether the subquery depends on the outer query or not.
        C.1) Correlated subquery
        C.2) Non-correlated subquery
Let’s see all these types of subqueries in details-
A) Based on Result:
   A.1) Single-row subquery:
    •   A subquery that returns exactly one row             (but it may   contain one or multiple      columns)    is
        called ‘Single   -row subquery’
    •   This subquery     used when you need to compare a column with a             single result   from another
        query.
    •   If the subquery returns     more than one row       , Oracle will throw an error:
    •   ORA-01427: single      -row subquery returns more than one row

  Syntax:
 SQL>   SELECT column1, column2, ...            FROM      table_name       WHERE       column      operator
       (SELECT   single_column       FROM            table_name       WHERE         condition);
Here,
    •   operator    → Single   -row comparison operators only         such as = , > , < , >= , <= , <   >

  Examples       : Consider we have ‘employee’ table as follow            -
`````

## Page 3

![Original page 3](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-003.jpg)

### Extracted text

`````text
1. Compare with Minimum Salary:
Find employees who earn the minimum salary in the company.






     This Subquery returns one value (minimum salary).

2. Compare with Maximum Salary
Find employees who earn less than the maximum salary.









3. Compare with Average Salary
Find employees earning above the company’s average salary.








4. Using in SELECT Clause (Scalar Single-row Subquery)
Show each employee along with the highest salary in the company.









  Key Points of Single-row subquery:
    1.  It returns only one row, one column.
    2.  It must be used with single-row operators.
    3.  If multiple rows are returned then it gives error.
    4.  It can be used in WHERE, HAVING, and SELECT clauses.
`````

## Page 4

![Original page 4](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-004.jpg)

### Extracted text

`````text
A.2) Multi-row subquery:
    •   A subquery that returns        more than one row        but one column      is called ‘Multi  -row subquery’
    •   This subquery     returns multiple values    so we cannot use single      -row operators      (=, <, > etc).
    •   Instead   of using single  -row operators   , we use multi-row operators IN,  ANY (or SOME), ALL
Syntax:
 SQL>SELECT col1, col2, ... FROM   table_name  WHERE column   multi_row_operator
       (SELECT    column_name       FROM     table_name       WHERE   condition);
Here, multi_row_operator is one of:
    •   IN → equal to any value in the list
    •   ANY (or SOME) → compare with at least one value in the list
    •   ALL → compare with all values in the list
  Examples: Consider we have ‘employee’ table as-








1. Using IN (equal to any value in the list)
Find employees who work in the same department as employee 'SHANTA'.







     Subquery may return multiple departments because emp_name ‘SHANTA’ may be more in table.
2. Using ANY (compare with at least one value in the list)
Find employees who earn more than the lowest salary in dept ‘HR’.








     Equivalent to: greater than minimum salary of dept ‘HR’

3. Using ALL (compare with all values in the list)
Find employees who earn more than the highest salary in department ‘IT’.
`````

## Page 5

![Original page 5](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-005.jpg)

### Extracted text

`````text
     Equivalent to: greater than maximum salary of dept ‘IT’.
4. Using NOT IN
Find employees who are not in any department where employee 'RAJESH' works.







  Key Points OF Multi-row subquery-
    1.  Multi-row subqueries return multiple rows but one column.
    2.  Must use multi-row operators (IN, ANY, ALL, NOT IN   etc).
    3.  Very useful when filtering based on lists of values returned from another table.

A.3) Multi-column subquery: (Tuple subquery)
    •   A subquery that returns multiple columns               (also called a  tuple subquery     ) is called ‘Multi  -
        column subquery’
    •   This subquery used      when you need to      compare multiple columns (pairs/tuples)             of data
        together.
    •   In this subquery,    outer query compares its own columns with the            set of column    s returned by the
        subquery.
    •   It is useful when you need to match        combinations of values        (not just a single column) between
        two tables or between a table and a subquery         .

  Syntax
 SQL>     SELECT col1, col2, ...      FROM       table1    WHERE (     colA, colB, ... )  IN
       (SELECT colX, colY, ...    FROM    table2     WHERE   condition);
Here, (colA, colB) is compared pair by pair with (colX, colY) returned by the subquery.
Examples: Consider we have ‘employee’ table as-










1. Matching Department & Job
Find employees whose (dept_id, job_id) combination matches the (dept_id, job_id) of employee
'VIJAY'. (i.e. Employees with Same Job & Department as VIJAY)
`````

## Page 6

![Original page 6](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-006.jpg)

### Extracted text

`````text
     The subquery returns two columns (dept_id, job_id) of VIJAY
The outer query compares both values together.
2. Multiple Column Match Across Different Tables:
Consider, we have two different table viz ‘orders’ and ‘sales’ as












Find orders where (customer_id, product_id) matches the records in a sales table.








  Key Points of multi-column subquery-
    1.  Multi-column subqueries return multiple columns.
    2.  Used when comparison must be done on combinations of values rather than a single column.
    3.  Works with IN, NOT IN (and sometimes EXISTS).
    4.  If you mistakenly use a single-column comparison operator (=), you will get an error.

A.4) Scaler subquery:

•   A subquery that returns exactly one value (one row and one column) is called ‘scalar subquery’.
•   Oracle treats this returned value just like a literal (constant) and allows it to be used anywhere in outer
    query.
•   This subquery must return only one value; otherwise, Oracle throws an error (ORA-01427: single-
    row subquery returns more than one row).
•   In short:
    Scalar Subquery = Subquery that gives a single value which behaves like a constant in your
    SQL.
Syntax
 SQL>SELECT column1, column2, ...FROM table1WHERE columnX = (SELECT single_column
     FROM    table2   WHERE   condition );
`````

## Page 7

![Original page 7](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-007.jpg)

### Extracted text

`````text
Example:  Consider we have ‘employee’ table as follow-







Example 1 (Simple)
Find employees whose salary is greater than salary of ‘KIRAN’ in the table.






Here:
    •    Inner query → returns exact single value (salary of KIRAN).
    •    Outer query → compares salary against that one value.
Example 2 (Column in SELECT list)
You can even use a scalar subquery inside the SELECT clause.
Find all employees whose salary is less than average salary of all employees:







Here:
    •    Subquery returns one value (average salary).
    •    This value is compared with every row and produce the result.
Key Points About Scalar Subqueries
    •    Always return one row, one column.
             o    Can be used in: WHERE clause, SELECT clause, HAVING clause, ORDER BY clause
    •    If it returns more than one row → Oracle error.

Note:
1)  Main difference between Single-Row Subquery and Scalar Subquery
     Aspect                    Single-Row Subquery                                     Scalar Subquery
                   A subquery that returns exactly one row            A subquery that returns exactly one row and
 Definition        (but it may contain one or multiple                one column (i.e., a single value).
                   columns).
 Return Type       One row (can be multiple columns).                 One value (one row + one column).
`````

## Page 8

![Original page 8](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-008.jpg)

### Extracted text

`````text
2)  Main difference between Single-Column Subquery and Multi-Column Subquery
     Aspect                  Single-Column Subquery                                 Multi-Column Subquery

 Definition        A subquery that returns only one column.            A subquery that returns two or more columns.

 Comparison        Compared with a single column of the outer          Compared with multiple columns of the outer
                   query.                                              query as a row pair.
 Operators         =, <, >, IN, ANY, ALL                               (col1, col2) IN (SELECT colA, colB …)
 Used
                   When you need to match/filter based on one          When you need to match/filter based on a
 Use Case          field (e.g., salary, dept_id).                      combination of fields (e.g., salary + dept, dept +
                                                                       job_id).
 Example           SQL> SELECT emp_name FROM employee                  SQL>SELECT emp_name FROM employee
 Query             WHERE dept = (SELECT dept FROM                      WHERE (dept, job_id) IN (SELECT dept, job_id
                   employee WHERE emp_name='VIJAY');                   FROM employee WHERE emp_name='VIJAY');
 Result            Employees in the same dept as VIJAY.                Employees in the same dept and job_id as
                                                                       VIJAY.

B) Based on Placement:
“Based on Placement” subquery means where the subquery is written inside the SQL statement
B.1) Subquery in WHERE clause:
    •    A subquery     inside the WHERE clause is         used to filter rows based on the result of another query          .
    •    It allows you to compare a column in the main query with the output of the subquery                   .
General Syntax      :
 SQL>    SELECT collist          FROM table1       WHERE  column_name               operator (  SELECT
 Column_name  FROM table2 WHERE condition );
Here,
    •    The operator can be =, <, >, IN, ANY, ALL, etc.

     Example- (By considering above ‘employee’ table)
Find employees whose salary is greater than the average salary of all employees.





Explanation:
    •    Inner query returns one value (average salary).
    •    Outer query selects employees with salary above that value.

B.2) Subquery in FROM clause:
•   A subquery in the FROM clause             is also called an   inline view   .
•   It is used when you want to create a        temporary result set       (like a virtual table)
General Syntax
 SQL>    SELECT column_list           FROM ( SELECT column1, column2, ...FROM table_name
 WHERE       condition    ) ;
Note:
    •    The outer query treats the subquery result like a virtual table.
Example: (By considering above ‘employee’ table)
Find employees who earn more than 15000
`````

## Page 9

![Original page 9](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-009.jpg)

### Extracted text

`````text
Explanation:
    •    Inner query (FROM) finds the salary > 15000
    •    Outer query filters employees whose salary is above 15000
B.3) Subquery in SELECT clause:
In Oracle, a subquery in the SELECT clause is also called a scalar subquery.
    •    It is a subquery that returns a single value (one row, one column).
    •    That value can then be displayed as a column in the outer query.
Syntax
 SQL>SELECT column1, column2, …, (SELECT single_column  FROM    table2   WHERE
 condition ) FROM   table1;
Example:  By considering above ‘employee’ table-
Show employee salary along with average salary








Here, the subquery (SELECT AVG(salary) FROM employee) returns one value (the overall average
salary), and that value is compared with every row to get the output.
C) Based on Correlation:
“Based on Correlation” subquery means whether the subquery depends on the outer query or not.
C.1) Correlated subquery:
•   A correlated subquery         is a subquery that   depends on the outer query          for its result.
•   Correlated subquery         executes   once for every row      returned by    the outer query     .
•   Inside correlated    subquery,   we use reference to a column of the outer query              .
•   This correlated subquery       is useful  for row -by-row comparisons.
General Syntax     :
 SQL>    SELECT col     List    FROM       mainTable      m    WHERE        condition   (SELECT   colList
 FROM       otherTable   o   WHERE          o.col = m.col);
Here,
‘m’ is reference to mainTable
‘o’ is reference to otherTable
Also, this subquery depends on outer query for that condition is mentioned o.col=m.col
Example: Consider we have two tables ‘customer’ and ‘orders’ as follow-
`````

## Page 10

![Original page 10](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-010.jpg)

### Extracted text

`````text
Example- 1: Find customers whose maximum order amount is greater than 6000








Explanation:
    •   Outer query → goes row by row in CUSTOMER.
    •   Inner query → finds the maximum order amount for that specific customer (o.cust_id =
        c.cust_id).
    •   Condition → returns only those customers whose max order > 6000.
Example- 2: Find customers whose maximum order amount is less than 5000
 (Without creating reference to tables. Here, we use table name as reference)








Explanation:
    •   Outer query → goes row by row in CUSTOMER.
    •   Inner query → finds the maximum order amount for that specific customer (orders.cust_id =
        customer.cust_id).
    •   Condition → returns only those customers whose max order < 5000.

C.2) Non-correlated subquery: (Independent subquery)
•   A Non-Correlated Subquery           (also called  Independent Subquery        ) is a subquery whose execution
    does not depend on the outer query         .
•   It can be executed    independently     to produce a result,   and this result  takes as input by   outer query.
•   This non-correlated subquery also runs once independently.
•   It is typically used in WHERE, SELECT, or FROM clauses.
•   It does not reference any column from the outer query.
`````

## Page 11

![Original page 11](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-011.jpg)

### Extracted text

`````text
General Syntax:
 SQL>SELECT col1, col2, ...  FROM   table1  WHERE   columnX   operator (SELECT  columnY
            FROM     table2   WHERE   condition);
Example: Consider we have two tables ‘customer’ and ‘orders’ as above.
1: Find customers who made orders greater than 6000





Explanation:
1.  The subquery (SELECT cust_id FROM ORDERS WHERE order_amount > 6000) runs first
    independently.      Output: cust_id = 2, 4
2.  The outer query then selects * from CUSTOMER for these cust_id’s.
3.  This is non-correlated because the subquery does not depend on any value from the outer query.

Handling data retrieval with EXISTS and NOT EXISTS operators in subquery-
•   EXISTS: Returns TRUE if the subquery returns one or more rows.
•   NOT EXISTS: Returns TRUE if the subquery returns no rows.
•   Important: EXISTS does not care about the actual data returned by the subquery. It only checks
    whether rows exist.
Syntax for EXISTS:
 SQL>SELECT columns  FROM table1  outer  WHERE EXISTS
  ( SELECT  1  FROM  table2  inner   WHERE   inner.column = outer.column);
Syntax for NOT EXISTS:
 SQL>SELECT columns FROM table1 outer WHERE NOT EXISTS
  (SELECT   1    FROM   table2    inner   WHERE   inner.column = outer.column );
Here, SELECT  1   is common, but you could select anything—it’s ignored by Oracle.
Example- Consider we have two tables ‘customer’ and ‘orders’ as above.
Example 1: Use of EXISTS
Find customers who have placed at least one order.








Explanation:
    1.  The subquery checks for each customer if a row exists in ORDERS with the same cust_id.
    2.  If at least one order exists, EXISTS returns TRUE.
Example 2: Use of NOT EXISTS
Find customers who have never placed an order.
`````

## Page 12

![Original page 12](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-012.jpg)

### Extracted text

`````text
Explanation:
    •    The subquery checks if there is any order for each customer.
    •    NOT EXISTS returns TRUE if no order exists for that customer.

Joins:
•   A JOIN in Oracle is used to         combine     (join)  rows   i.e. records   i.e. data from two or more tables
    based on a     related column       between them.
•   Join helps to fetch meaningful data         which is spread across multiple tables         .
Advantages or Characteristics or Properties or Importance of Joins:
1.  Combine Related Data            →   Using joins we can       fetch  the data from multiple tables        & combine      it in
    single query.
2.  Avoid Redundancy           → Data duplication is avoided         by using joins.
3.  Efficient Querying        → Joins are    Faster and more powerful         than running multiple separate queries i.e.
    it is efficient in querying.
4.  Flexibility    → Different join types (INNER,          OUTER      , SELF,   CROSS     etc.) helps in different business
    needs hence it is flexible.
5.  Supports Normalization → Joins works well with normalized databases (data split across tables).
6.  Better Data Analysis → Joins fulfils the requirements in                  complex reporting and business area for
    better data analysis.
7.  Data Integrity → Joins ensures relationships between tables are utilized properly.

Types of Joins:
Following are the different types of joins-
    1)   Inner Join
    2)   Outer Join
    3)   Self-Join
    4)   Cartesian Join (Cross-Join)
Let’s see these types in details-
1) Inner Join-
•   It is type of join where it returns only the rows (i.e. records) that have matching values in both tables
•   That is inner join excludes non-matching rows.
Syntax for Inner join-
 SQL>SELECT    colList   FROM    table1    INNER  JOIN   table2   ON  table1.column_name =
 table2.column_name;
Explanation
    •    INNER JOIN keyword specifies the join type.
    •    ON defines the join condition (the relationship between the two tables).
Here, only those rows are returned that satisfy the condition.
Example- Consider we have ‘customer’ and ‘orders’ table as follow-
`````

## Page 13

![Original page 13](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-013.jpg)

### Extracted text

`````text
1) Applying Inner join onto above tables to retrieve only those customers who have placed at least
one order.





2) Outer Join:
•   An Outer Join returns all rows from one table, and the matching rows from the other table.
•   If no match is found, NULL values are returned for missing columns.
•   Outer join helps when you want to see unmatched records also (not just the common ones).
Types of Outer Joins:
2.1) LEFT OUTER JOIN → Returns all rows from left table, and matched rows from right table.
2.2) RIGHT OUTER JOIN → Returns all rows from right table, and matched rows from left table.
2.3) FULL OUTER JOIN → Returns all rows from both tables whether they are matched or
unmatched.
Let’s see these types in details-
2.1) LEFT OUTER JOIN:
A LEFT OUTER JOIN            returns:
➢   All rows from the left table      (even if no match exists in the right table).
➢   Matching rows from the right table.
➢   If there’s no match    , Oracle fills the right table columns      with NULL     .
Syntax for LEFT OUTER              JOIN:
 SQL>    SELECT  colList         FROM   table1    LEFT OUTER JOIN   table2  ON   table1.column =
 table2.column;
Here, table1 → left table (all rows returned).
      table2 → right table (only matched rows returned, unmatched become NULL).
👉 The keyword OUTER is optional, you can simply write LEFT JOIN.
Example- Consider we have ‘customer’ and ‘orders’ table as above.
1) By applying LEFT OUTER JOIN, we get output as-








👉 Explanation:
Amit (CUST_ID = 1) has two orders, so he appears twice.
Ravi (CUST_ID = 2) has one order.
Sita (CUST_ID = 3) has no order, but still appears in the result with NULLs for order columns (because
of the LEFT OUTER JOIN).
2.2) RIGHT OUTER JOIN:
•   A RIGHT OUTER JOIN              returns:
    ➢   All rows from the right table       . (even if no match exists in the left table).
    ➢   It also returns the  matching rows from the left table         .
    ➢   If no match exists, Oracle fills the left table’s columns with NULLs.
•   It is basically the reverse of LEFT OUTER JOIN.
`````

## Page 14

![Original page 14](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-014.jpg)

### Extracted text

`````text
Syntax for RIGHT OUTER JOIN:
 SQL>SELECT colList   FROM   table1    RIGHT OUTER JOIN    table2     ON    table1.column =
 table2.column;
Here,
table1 → left table
table2 → right table (all rows will be included)
Example- Consider we have ‘customer’ and ‘orders’ table as follow-
















1) By applying RIGHT OUTER JOIN, we get output as-








👉 Explanation:
➢   Customers Amit and Ravi appear with their orders.
➢   Order 104 belongs to a customer ID 5 (not in CUSTOMER table), so the customer details show
    NULL.
➢   Customer Sita (3) doesn’t appear, because RIGHT JOIN prioritizes the orders table first.
2.3) FULL OUTER JOIN:
➢   A FULL OUTER JOIN            returns:
    •   All rows from the left table.
    •   All rows from the right table.
    •   If there is no match between the tables       , it fills with NULL    for the missing side.
➢   FULL outer join is combination of       LEFT OUTER JOIN           and RIGHT OUTER JOIN             .
Syntax for FULL OUTER JOIN:
 SQL>   SELECT       columns     FROM      table1   t1    FULL OUTER JOIN   table2    t2
 ON       t1.column_name = t2.column_name;
Example- Consider we have ‘customer’ and ‘orders’ table as above.
1) By applying FULL OUTER JOIN, we get output as-
`````

## Page 15

![Original page 15](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-015.jpg)

### Extracted text

`````text
Explanation:
•   Customer Amit (ID 1) has 2 orders → shows 2 rows.
•   Customer Ravi (ID 2) has 1 order → 1 row.
•   Customer Sita (ID 3) has no order → shows with NULL order columns.
•   Order with CUST_ID = 5 has no matching customer → shows with NULL customer columns.

3) SELF JOIN:
•   A SELF JOIN is a join in which a table is joined with itself.
•   It is useful when rows of the same table need to be compared, for example:
    ➢   Finding customers who live in the same city within same table.
    ➢   Finding employees who are managers of other employees within same table.
Syntax for SELF JOIN-
 SQL>SELECT    a.col, b.col    FROM    table   a,  table    b        WHERE     condition;
Here,
a and b are aliases OR references for the same table.
Example- Consider we have ‘employee’ table as follow-







👉 Note: Here, MANAGER_ID refers to EMP_ID of the manager.
1) Applying SELF JOIN on above table we get output as-








Explanation:
    ➢   Ravi and Sita have Amit as manager.
    ➢   John has Ravi as manager.
    ➢   Amit has no manager (NULL).
`````

## Page 16

![Original page 16](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-016.jpg)

### Extracted text

`````text
4) Cartesian Join (Cross-Join):
•   A Cartesian Join (also called Cross Join) happens when each row of one table is joined with every
    row of another table.
•   It usually happens when you don’t specify a proper join condition.
•   The number of resulting rows after Cartesian join = (rows in table1 × rows in table2)
Syntax:
 SQL>SELECT  x.col,y.col…  FROM   table1  x   CROSS JOIN   table2    y;
Example- Suppose we have two tables as ‘dept’ and ‘emp’ as follow-










Applying CROSS JOIN onto above table we get-









Lossless Join:
•   Lossless join is the concept in       Database Normalization, it means that            when a relation (table) is
    decomposed into two or more smaller relations (tables), we can join them back without losing any
    information.
•   Lossless join ensures that if a table is broken into two or more tables, you can reconstruct the original
    table by joining those decomposed tables without losing any data.
•   This property is important for database design to avoid redundancy and inconsistency.
Syntax for Lossless join:
 When you decompose a table R into two tables R1 and R2,

 SQL>SELECT * FROM R1 NATURAL JOIN R2;

 If the result gives back all rows of the original relation R, then the decomposition is lossless.
Example-
1. Original Table: Employee
EMP_ID | EMP_NAME | DEPT_ID | DEPT_NAME
-------+----------+---------+----------
1      | Amit     | 10      | HR
2      | Ravi     | 20      | IT
3      | Sita     | 10      | HR
`````

## Page 17

![Original page 17](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-017.jpg)

### Extracted text

`````text
2. Decompose into Two Tables

Dept Table

SQL>CREATE TABLE dept (
    dept_id   NUMBER(5) PRIMARY KEY,
    dept_name VARCHAR2(5)
);

SQL>INSERT INTO dept VALUES (10, 'HR');
SQL>INSERT INTO dept VALUES (20, 'IT');

Emp Table

SQL>CREATE TABLE emp (
    emp_id    NUMBER(5) PRIMARY KEY,
    emp_name  VARCHAR2(10),
    dept_id   NUMBER(5)
);

SQL>INSERT INTO emp VALUES (1, 'Amit', 10);
SQL>INSERT INTO emp VALUES (2, 'Ravi', 20);
SQL>INSERT INTO emp VALUES (3, 'Sita', 10);

3. Reconstruct (Join them back)
SQL>SELECT emp_id,emp_name,dept_id,dept_name FROM emp NATURAL JOIN dept;
EMP_ID | EMP_NAME | DEPT_ID | DEPT_NAME
-------+----------+---------+----------
1      | Amit     | 10      | HR
2      | Ravi     | 20      | IT
3      | Sita     | 10      | HR
This is exactly the original table, so the decomposition is lossless join.


SEQUENCE:
•   A SEQUENCE is a database object which is used to generate unique numbers automatically.
•   SEQUENCE basically used for primary keys field in a table (like student roll number, employee
    IDs, invoice numbers, order IDs, etc.) where these fields increments sequentially.
•   SEQUENCE saves you from manually inserting unique values in table.
•   In short a SEQUENCE in Oracle is like an auto-number generator.
Why is SEQUENCE important?
1)  Automatic primary keys → No need to worry about duplicate IDs while inserting rows.
2)  Performance → Sequences are very fast, optimized by Oracle.
3)  Flexibility → You can control start value, increment, min/max values, and whether numbers can cycle
    (start over).
4)  Concurrency     → Even if many users insert rows at the same time, sequence              guarantees unique
    numbers.
5)  Ensures uniqueness → Each call to NEXTVAL generates a unique number (no duplicates).
`````

## Page 18

![Original page 18](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-018.jpg)

### Extracted text

`````text
Let’s see some Oracle SEQUENCE commands-
1. Create a Sequence:
➢  To create new sequence, CREATE SEQUENCE command is used.
 SQL>  CREATE SEQUENCE sequenceName
         START WITH n
         INCREMENT BY m
         MINVALUE x
         MAXVALUE y
         CYCLE | NOCYCLE
         CACHE n | NOCACHE;
Example:
 SQL> CREATE SEQUENCE emp_seq
        START WITH 1
        INCREMENT BY 1
        MINVALUE 1
        MAXVALUE 1000
        NOCYCLE
        CACHE 20;
Here, SEQUENCE ‘emp_seq’ is created having following properties-
   ➢   Starts at 1, increases by 1 each time.
   ➢   Minimum = 1, Maximum = 1000.
   ➢   NOCYCLE → won’t restart after reaching max.
   ➢   CACHE 20 → Oracle pre-allocates 20 numbers in memory (for speed).

2. Retrieve Data from a Sequence:
To retrieve data from sequence, two keywords are used which are as follow-
➢  NEXTVAL → gets the next number in the sequence.
➢  CURRVAL → gets the current value of the sequence.
➢  NOTE: We can use CURRVAL after NEXTVAL has been used once in the session.
Example: We use NEXTVAL and CURRVAL on above created ‘emp_seq’ sequence as follow-
`````

## Page 19

![Original page 19](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-019.jpg)

### Extracted text

`````text
3. Modify a Sequence:
➢   We can modify sequence using ALTER SEQUENCE command.
➢   ALTER SEQUENCE command changes the properties of created sequence.
➢   Note that, we cannot alter or modify the START WITH property of sequence.
➢   Syntax-
 SQL>ALTER SEQUENCE sequence_name
     INCREMENT BY n
     MAXVALUE x
     MINVALUE y
     CYCLE | NOCYCLE
     CACHE n | NOCACHE;

Example-















    •   Here, the sequence ‘emp_seq’ will increase by 5 instead of 1.
4. Drop a Sequence:
➢   To drop created sequence, DROP SEQUENCE command is used.
Syntax:
          SQL> DROP SEQUENCE sequence_name;
Example:
          SQL> DROP SEQUENCE emp_seq;

This completely removes the sequence from the database.
`````

## Page 20

![Original page 20](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-020.jpg)

### Extracted text

`````text
Following example shows actual use of SEQUENCE while inserting record in table-






























SYNONYM:
•   In Oracle Database, a synonym is simply an alias (alternative name) for a database object.
•   SYNONYM allows you to give your own name to the database object (like a table, view, sequence,
    procedure, or another synonym) which is often shorter or more meaningful.

Why to use Synonyms?
    1.  To provide a shorter name for long object names.
    2.  To hide schema details (users don’t need to know the owner’s schema).
    3.  To make it easier for applications to access objects without schema prefix.
    4.  To allow location transparency when accessing remote objects.

 Types of Synonyms:
    1.  Private synonym – Private synonym is accessible only within the user’s schema where it is
        created. (It is default synonym)
    2.  Public synonym – Public synonym is accessible by all users of database. (It is not default
        synonym; PUBLIC keyword is used to make synonym public)
`````

## Page 21

![Original page 21](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-021.jpg)

### Extracted text

`````text
Example 1) PRIVATE synonym: Example shows creating and using the PRIVATE synonym.





















Example 2) PUBLIC synonym: Example shows creating and using the PUBLIC synonym.
`````

## Page 22

![Original page 22](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-022.jpg)

### Extracted text

`````text
Note:
PUBLIC synonym is accessible by all users of database.
PRIVATE synonym is only accessible within user where it is created.
(Show practically for student- OPEN two RUN SQL command Line one for SYSTEM & one for
other created user (is should have CONNCT privileges))
Hint: SQL>Grant   SELECT   ON   synoName   TO   userName;
For both PUBLIC and PRIVATE synonym and check the result on other user terminal)

Index-
In Oracle, an INDEX is a database object basically used for faster access of rows i.e. records from a
table based on values of one or more columns.
     We know that, every book has an index, it contains chapter name and its equivalent page number.
To search any chapter, first we check whether it is present in index or not. If chapter is present in index,
then we directly switch to its page number (location), instead of scanning the whole book.
➢   Thus, index makes searching fast.

Advantages of Index:
1)  Faster Data Retrieval:
    Indexes provide a quick access path to rows (records) of a table.
2)  Improves Query Performance
    Indexes useful in queries with WHERE, JOIN, ORDER BY, and GROUP BY clauses.
    Hence, Sorting and grouping become faster.
3)  Efficient Access Using Rowids:
    Index stores ROWID of each row of a table then Oracle can directly jump to the exact location of
    data.
4)  Speeds up Joins
    Indexes also speed up join columns (like employee_id, department_id) that improve performance of
    multi-table joins.
5)  Helps Enforce Uniqueness:
    Unique indexes are automatically created when you define PRIMARY KEY or UNIQUE
    constraints, ensuring no duplicate values.
6)  Supports Function-Based Queries
    Indexes support for Function-based queries on expressions or strings like UPPER(name) etc. that
    makes faster execution.
7)  Better Sorting and Searching
    Indexes help queries that use ORDER BY and range searches (BETWEEN, <, >) perform
    efficiently.
8)  Improves Aggregation Performance
    Queries with aggregates (SUM, COUNT, AVG) on indexed columns execute faster.

Types of Index:
In Oracle, there are several types of indexes, each type is useful depending on the data and query
requirements. Which are explained as follow-
1. B-tree Index (Default)
    •   It is most common type of index that stores data in a balanced tree structure.
    •   This B-tree index is best for high-cardinality columns (i.e. column has many distinct values).
    •   B-tree index is ideal for searching unique values.
`````

## Page 23

![Original page 23](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-023.jpg)

### Extracted text

`````text
 Syntax:
 SQL>CREATE     INDEX    indexName    ON   tableName(ColName);
Example:
SQL> CREATE    INDEX   idx_name   ON   employees(name);
Here, we create an index ‘idx_name’ on the ‘name’ column of the ‘employees’ table
Now, we retrieve data using created index as-

SQL>SELECT    *   FROM     employees   WHERE   name = 'MAHESH';

Here, Oracle uses the B-tree index (idx_name) to quickly find the ROWID of ‘MAHESH’ and fetch
the row.

2. UNIQUE INDEX
    •   UNIQUE INDEX ensures all values in the indexed column are unique.
    •   If you try to insert a duplicate value in unique index column then oracle generates error.
    •   Note that, UNIQUE INDEX automatically created when you define a PRIMARY KEY or
        UNIQUE constraint for a column.
Syntax:
 SQL>CREATE        UNIQUE INDEX       indexName    ON   tableName(ColName);
Example:

























3. Composite Index (Concatenated Index)
    •   If Index is created on two or more columns of table, then it is called ‘Composite Index’
    •   This COMPOSITE INDEX is useful when filtering is applied on multiple columns.
Syntax:
 SQL>CREATE     INDEX       indexName       ON      tableName(Col1,Col2,…);
`````

## Page 24

![Original page 24](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-024.jpg)

### Extracted text

`````text
Example:
        SQL> CREATE    INDEX   idx_cmp   ON   emp(eid,ename);
Here, we create a composite index ‘idx_cmp’ on the ‘eid’ and ‘e              name’    column  s of the  ‘emp’   table
Now, we retrieve data using created index as         -

        SQL>    SELECT        *   FROM      emp   WHERE    eid= 101   AND   ename= ‘KIRAN’;

-- Above query uses both indexed columns eid and ename for filtering. Hence, data will fetch fast.

4. Bitmap Index
    •   This index uses bitmaps (string of bits, 0s and 1s) for indexing instead of B-trees.
    •   This index is best for low-cardinality columns (few distinct values, like gender, status).
Syntax:
 SQL>CREATE     BITMAP INDEX     indexName      ON      tableName(Column);
Example:
        SQL>CREATE     BITMAP INDEX     idx_bit      ON      emp(gender);
Here, we create a bitmap index ‘idx_bit’ on the ‘gender’            column of the    ‘emp’    table.
Retrieving data with bitmap index       -
        SQL>    SELECT        COUNT(*)        FROM        emp      WHERE        gender = 'M';
-- Above query uses indexed column gender to fetch all Male employees from ‘emp’ table.

5. Function-Based Index
    •   If index is created on the result of a function or result of expression then it is called
        ‘Function-Based Index’.
    •   Function based index helps to optimize queries where functions are used in WHERE clauses.
Syntax:
 SQL>CREATE     INDEX     indexName      ON        tableName(fun_Name(col1,col2));
Here, fun_name( ) is built in function or user defined function in oracle on to which we create index.
Example:
        SQL>CREATE    INDEX   idx_fun    ON   emp(UPPER(ename));
Here, we create a function based index ‘idx_fun’ on the ‘UPPER’                function   having column     ename   .
Retrieving data with function based index        -
        SQL>    SELECT * FROM             emp     WHERE         UPPER(    ename) = 'JAY';

6. Descending Index
    •   Descending Index is used to store data in descending order in table depends on column.
    •   It is useful for queries using ORDER BY ... DESC.
Syntax:
 SQL>CREATE   INDEX   idexName   ON      tableName(Col DESC);
Example:
        SQL>CREATE   INDEX   idx_dec   ON      emp(salary DESC);
Here, we create a descending index ‘idx_dec’ on column ‘             salary’ of table   ‘emp’  .
Retrieving data with descending index        -

        SQL>    SELECT         *     FROM        emp    ORDER BY       salary DESC     ;
`````

## Page 25

![Original page 25](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-025.jpg)

### Extracted text

`````text
Pseudo columns:
•   In Oracle Database, a pseudo column is a special type of column that appears to exist in a table
    but is not actually stored there.
•   Pseudo column is automatically provided by Oracle and can be queried like a normal column,
    but you cannot insert, update, or delete values in it.
•   Pseudo column is virtual column provided by Oracle for special purposes.
Commonly Used Pseudo Columns in Oracle:
1. ROWID
•   The ROWID pseudo column represents the unique physical address of a row in a table.
•   Whenever we insert new row in table, oracle automatically assign ROWID for that row.
Example:








2. ROWNUM
•   ROWNUM pseudo column represents the sequence number of a row present in a table.
•   Basically ROWNUM is used to limit rows of table.
Example:







3. CURRVAL & NEXTVAL
•   CURRVAL & NEXTVAL are pseudo columns used with sequences.
•   NEXTVAL gives the next value from a sequence.
•   CURRVAL gives the current value of a sequence.
Example:











4. LEVEL
•   LEVEL is pseudo column used in hierarchical queries (CONNECT BY) indicates the level of a
    node in a tree structure.
Example:
`````

## Page 26

![Original page 26](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-026.jpg)

### Extracted text

`````text
Explanation-
1. Table assumption (emp)
•   emp_id → Employee ID (unique for each employee).
•   mgr_id → Manager ID (refers to another emp_id).
•   emp_name → Employee’s name.
This means:
•   Each employee may have a manager (mgr_id).
•   The top boss will have mgr_id = NULL. Here, ‘Amit’ is boss.

2. START WITH mgr_id IS NULL
•   This defines the root(s) of the hierarchy.
Here, the hierarchy starts with employees who don’t have a manager (the CEO/top-level bosses).

3. CONNECT BY PRIOR emp_id = mgr_id
•   This defines the parent → child relationship.
•   PRIOR emp_id = the parent’s emp_id (from the row above in the hierarchy).
•   mgr_id = the child’s manager ID.

Views:
➢   In Oracle Database, a view is a virtual table based on the result of a SQL query.
➢   View does not store data physically, but it provides a way to look at data from one or more
    tables in a customized manner.
➢   A view is a named SQL query         stored in the database.   It Acts like a table   but does not store data    .
➢   Use of VIEW:
    •   VIEW used for simplifying complex queries
    •   VIEW provides a level of security for data by restricting access to specific columns/rows.
    •   VIEW used for presenting aggregated or joined data.
    •   VIEW Hides underlying table structures.
Syntax:
 SQL> CREATE [OR REPLACE] [FORCE | NOFORCE]   VIEW view_name   AS
 SELECT   query  [WITH CHECK OPTION]  [WITH READ ONLY];
Here,
    ➢   CREATE OR REPLACE: If view not exists then it creates new view. If view already exists
        then it replaces existing view by new one.
    ➢   FORCE: Creates the view even if the base tables don't exist (use with caution).
    ➢   NOFORCE: Default. Base tables must exist.
    ➢   WITH CHECK OPTION: Ensures that DML operations via the view do not violate.
    ➢   WITH READ ONLY: Makes the view non-updatable (no INSERT/UPDATE/DELETE).
`````

## Page 27

![Original page 27](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-027.jpg)

### Extracted text

`````text
Types of View:
1. Relational View:
•   A Relational View       is simply a   view based on one or more relational tables             and that presents data
    from th  ese tables in a specific format.
•   The relational view    basically, a  virtual table derived from base relational tables            using SQL queries.
•   Relational views help simplify complex data structures by providing               relational data.
Key points about Relational Views:
    •   This view    based on one or more relational tables          .
    •   This view    does not store data physically       , here data is dynamically fetched when queried             .
    •   This view    provides security by restricting columns or rows.
    •   This view can be simple (based on one table) or complex (based on multiple tables, joins, group
        by, etc).
    •   This view can be updatable (allow insert/update/delete) or read-only depending on the SQL
        used WITH READ ONLY etc.
    •   If view is created WITH READ ONLY then it will not updatable. But if view is created
        without READ ONLY then view can be updatable.
    •   If view is updated then its respective table also affects by new values.
Syntax for Creating a Relational View
 SQL>CREATE [OR REPLACE] VIEW view_name   AS
 SELECT column1, column2, ...
 FROM table_name
 [WHERE condition]
 [GROUP BY ...]
 [HAVING ...]
 [ORDER BY ...];
Types of Relational view-
1.1) Simple Relational View-
Definition:
A view is created on a single table without any joins, aggregates, or derived columns is called
‘Simple relational view’
Consider we have two tables ‘dept’ and ‘emp’ as follow-














Example: Simple Relational View (Single Table)
We create a simple relational view to show employees who works in department number 20.
`````

## Page 28

![Original page 28](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-028.jpg)

### Extracted text

`````text
1.2) Complex Relational View- (Multiple Tables Join)
Definition:
A view is created using multiple tables, joins, aggregates, or derived columns is called ‘Complex
relational view’
Purpose:
It combines data from multiple tables into a single virtual table.
Example-
Consider we have tables ‘dept’ and ‘emp’ tables as above-
We create a complex relational view to show employees with department names.














2. Object View:
Definition:
A view is said to be object view if it is created on user-defined object type is called ‘Object view’.
OR
A view that returns rows (records) as objects of a user-defined object type is called ‘Object view’
Purpose:
It enables object-oriented operations in Oracle.
Example-
To create object view, first we have to create Object type. We create object as follow-
 SQL>CREATE  TYPE  emp_dept_obj  AS  OBJECT (
     emp_id NUMBER,
     emp_name VARCHAR2(20),
     salary NUMBER,
     dept_name VARCHAR2(20)
 );
After creating object, we create object view as follow-
`````

## Page 29

![Original page 29](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-029.jpg)

### Extracted text

`````text
Here, object view returns each row as an object.

3. Read-only View
Definition:
A view that cannot be updated (not allow insert/update/delete) is called ‘Read only view’
Purpose:
Read only view provides data security or simplifies complex query without modifying data.
Example-




















Here, Attempt to update is failed.
`````

## Page 30

![Original page 30](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-030.jpg)

### Extracted text

`````text
4. Materialized View
Definition:
A view that stores physical copy of data of one or more tables in the database is called as
“Materialized view”.
Purpose:
Materialized view improves performance for frequent queries. Can be refreshed periodically.
Example-











Here, materialized view stores aggregated data physically for better performance.

5. View with WITH CHECK OPTION
Definition:
A view contains WITH CHECK OPTION that ensures any insert/update through the view satisfies the
view’s WHERE condition.
Purpose:
This view enforces data integrity through the view.
Example-














Here, it ensures data modifications respect to the view’s condition.
`````

## Page 31

![Original page 31](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-031.jpg)

### Extracted text

`````text
                                         Theory Assignment
     Short Answer Questions
    1.  What is a subquery in SQL?
    2.  Define correlated subquery with an example.
    3.  Differentiate between INNER JOIN and OUTER JOIN.
    4.  What is a sequence in Oracle?
    5.  Explain the difference between NEXTVAL and CURRVAL.
    6.  Define a synonym in Oracle.
    7.  What is an index and why is it used?
    8.  List any two advantages of indexes.
    9.  What are pseudo columns? Give two examples.
    10. Define a view in Oracle.

     Long Answer Questions
    1.  Explain types of subqueries based on result, placement, and correlation with examples.
    2.  Discuss the different types of JOINS with syntax and examples.
    3.  What is a sequence? Explain how to create, modify, and delete a sequence with examples.
    4.  Explain various types of Indexes in Oracle with examples.
    5.  What are pseudo columns? Discuss ROWID, ROWNUM, CURRVAL, NEXTVAL, and LEVEL
        in detail.
    6.  Define a view. Explain types of views (Relational, Object, Read-only, Materialized) with
        examples.
    7.  What is the importance of a Lossless Join in database normalization? Explain with example.

     Multiple Choice Questions (MCQs)
Q1. A query inside another query is called:
a) Join
b) Subquery
c) View
d) Sequence
   Answer: b) Subquery
Q2. Which operator is used in multi-row subqueries?
a) =
b) IN, ANY, ALL
c) BETWEEN
d) LIKE
   Answer: b) IN, ANY, ALL
Q3. Which JOIN returns all rows from both tables, matched or unmatched?
a) Inner Join
b) Left Join
c) Right Join
d) Full Outer Join
   Answer: d) Full Outer Join
Q4. NEXTVAL in Oracle sequences is used to:
a) Get the current sequence value
b) Get the next sequence value
`````

## Page 32

![Original page 32](assets/05_Unit-II_DBMS_Subquery_Joins-_Sequence-_Index-_Pseudo_columns-_Views/page-032.jpg)

### Extracted text

`````text
c) Reset the sequence
d) Modify the sequence
   Answer: b) Get the next sequence value
Q5. Bitmap index is best suited for:
a) High cardinality columns
b) Low cardinality columns
c) Primary key columns
d) Foreign key columns
   Answer: b) Low cardinality columns
Q6. Which pseudo column represents the physical address of a row?
a) ROWNUM
b) ROWID
c) LEVEL
d) CURRVAL
   Answer: b) ROWID
Q7. A view that stores a physical copy of data for faster access is:
a) Relational View
b) Read-only View
c) Materialized View
d) Object View
   Answer: c) Materialized View
Q8. Which type of join may lead to a Cartesian product if join condition is missing?
a) Inner Join
b) Outer Join
c) Self Join
d) Cross Join
   Answer: d) Cross Join
Q9. In Oracle, which command is used to delete a sequence?
a) REMOVE SEQUENCE
b) DROP SEQUENCE
c) DELETE SEQUENCE
d) ERASE SEQUENCE
   Answer: b) DROP SEQUENCE
Q10. A private synonym in Oracle is accessible:
a) By all users
b) Only by DBA
c) Only within the schema where it is created
d) Across all schemas
   Answer: c) Only within the schema where it is created
`````


---

# Source file: 07_Views.md

# Views

- Original PDF: `notes\Views.pdf`
- Pages: 7
- Preservation: every original page is rendered below; extracted text follows each page image.

## Page 1

![Original page 1](assets/07_Views/page-001.jpg)

### Extracted text

`````text
  VIEWS
     A view is a virtual table. A view consists of rows and columns like a table.
     We can create a view by selecting fields from one or more tables present in
      the database. But it does not contain any data. At run time it contains the
      data from table and after execution it gets free.
      If data is changing in the original table, the same change is reflected in the
       view. A view can be built on top of a single table or multiple tables &
       another view.
     View requires no memory to store data but some memory required for
      storing definition of view.
     View is defined on which table this table is called as Base table.
     If view is already exit the View can be replaced using ‘replace’ keyword.
     We can create forcefully view on without existing the table.
     View only allows a user to retrieve data.

Types of view:
    Simple view :
       1) The simple view is created from only one single table.
       2) A simple view also does not have any groups of data.
       3) Simple view will not have any expression or group function.
       4) All DML allow in simple views.
       5) If table drop then view will not drop but view become invalid. View
           become valid when table again created with same as dropped table
           column name.
    Complex view:
       1) The complex view is created from than one table and also has group
           function.
       2) A complex view contains groups of data.
       3) DML are not allowed.
       4) Through view we can insert data into child table not in parent table.
Why Views?
      Provides additional level of security by restricting access to a fixed set of
       rows and columns of a table.
      Hide the data complexity.
      Ease of use and Space savings
      To provide data independence
      To present different views of the same data

 Creating Views
Suppose we have EMP and DEPT table. We want to see emp details i.e.
department names where they are working. We have to write a long join query.
`````

## Page 2

![Original page 2](assets/07_Views/page-002.jpg)

### Extracted text

`````text
select e.eno,e.ename,e.sal,e.dno,d.dname,d.loc From emp e, dept d where
e.dno=d.dno;
Instead of writing this join query again and again, we can create a view on these
tables by using a CREATE VIEW command:

create view vw_empdept as select e.empno, e.ename, e.sal, e.deptno,
d.dname, d.loc from emp e, dept d where e.deptno=d.deptno;

Now to see the employee details and department names:
       select * from vw_empdept;  // This will show same result as join query.

 View with Check Option Constraint
Creates view with the constraint that apply on INSERT and UPDATE, DELETE
statements.
Example-suppose all the employee working in Department No. 10 belongs to
accounts department.

create view vw_accounts_staff as select eno, ename, dno from emp where dno=10
with check option constraint ica_accounts_cnst;

select * from vw_accounts_staff;

select sum(sal) from vw_accounts_staff;
select max(sal) from vw_accounts_staff;

In “vw_accounts_staff” view you can insert only rows in these departments
number 10.

INSERT statement successfully inserts a row into the EMP table through the
vw_accounts_staff view: insert into vw_accounts_staff values (110, 'ASHI', 10);

If you insert a row with department number 30, this INSERT statement is rolled
back and raise error because with check constraints apply on vw_accounts_staff
view it allow only dept number 10:

       insert into vw_accounts_staff values(111, 'SAMI', 30);

 Creating View without Having the Base Table
You can create a view without base table but once the base table was created then
the view is validated.
       Create force view vw_stud as select * from student;
`````

## Page 3

![Original page 3](assets/07_Views/page-003.jpg)

### Extracted text

`````text
 Replacing/Altering Views
     A view can be drop or recreate. When a view is dropped, all grants of
      corresponding view rights are revoked from users. After the view is re-
      created, necessary rights must be regranted.
     A view can be replaced or redefining by CREATE OR REPLACE VIEW
      statement. This option replaces the current definition of a view, but
      preserves the present security authorizations.
     If base table was dropped then we will get the message like “view has errors”.
     If base table has been altered but still the view was with the initial definition,
      we have to replace the view to affect the changes.

create or replace view vw_accounts_staff as select empno, ename, deptno from
emp where deptno = 30 with check option constraint ica_accounts_cnst;

INSERT statement successfully inserts a row into the EMP table through the
accounts_staff view because we are change view definition:

       insert into vw_accounts_staff values (199, 'ABID', 30);

 Dropping Views : Remove view from database
       Example: drop view vw_accounts_staff;

 Views without DML
      Read only view: Create view vw_dept as select * from dept with read only;
      View with aggregate functions & group by clause:
      Create view vw_sumsal as select dno, sum(sal) t_sal from emp group by dno;
      View with distinct: Create view vw_stud as select distinct no,name from
       student;

 Updating Views with DML
  EMP base table that cause the view changes and employee 109's name changes
from ASHI to SHRI in the EMP table.
        update vw_empdept set ename='shri' where eno=109;

 Creating View Join (complex view)
To provide users with convenient access to information from multiple tables,
create a complex view.
create view vw_emploc as select e.eno, e.ename, e.dno, e.sal, d.dname, d.loc from
emp e, dept d  where e.dno=d.dno and d.loc in ('HYD', 'BOM', 'DEL');
 Listing Information about VIEWS
To see how many views are there in your database:
select * from user_views;
`````

## Page 4

![Original page 4](assets/07_Views/page-004.jpg)

### Extracted text

`````text
  select * from user_updatable_columns where table_name='vw_empdept';

  Advantages of View
      View provides data security for the same base tables.
      It allows different users to view the same data in different ways at the same
       time.
      It is used to represent additional information like derived columns.
      It is used to hide complex queries.
      It presents a consistent, unchanged image of the database structure, even if
       the tables are split or renamed.
      It does not allow direct access to the tables of the data dictionary.
  Disadvantages of View
      We cannot use DML operations on View, if there is more than one table.
      When table is dropped view becomes inactive.
      View is a database object, so it occupies the space.
      Without table, view will not work.
      Updation is possible for simple view but not for complex views, they are read
       only type of views.


                        Table                                              View
   A table is a database entity that stores          A view is a virtual table used to view or
   data in the form of rows and columns.             manipulate some parts of the table. It

                                                     also has rows and columns as real
                                                     ordered tables.
   A table stores the data.                          A view only extracts data from the table.
   A table can only be created or                    A view can be recreated.
   dropped.
   A table is an independent database                A view is dependent on the table.
   entity.
   It is stored in physical storage as it            It  is  not  stored  physically.  It
   occupies real space on systems.                   only   requires    some     space   in

                                                     memory whenever we run its
                                                     query.
`````

## Page 5

![Original page 5](assets/07_Views/page-005.jpg)

### Extracted text

`````text
A table gives results faster.                      A view gives results slower because it
                                                   has to run its queries each time to
                                                   retrieve the information from the table.
We can add, delete or update the data              We cannot modify data from a view. We
in a table.                                        can change the data in the base


Materialized View
A Materialized View saves the data supplied by the view configuration query and
is updated automatically as data in the underpinning tables changes.A view can be
“materialized” by storing the tuples of the view in the database.
Materialized view is also a logical virtual table, but in this case the result of the
query is stored in the table or the disk.The performance of the materialized view
is better than normal view since the data is stored in the disk.
When the results of a view expression are stored in a database system, they are
called materialized views.SQL does not provides any standard way of defining
materialized view,The process of keeping the materialized views updated is know
as view maintenance.Database system uses one of the three ways to keep the
materialized view updated:
Update the materialized view as soon as the relation on which it is defined is
updated. Update the materialized view every time the view is accessed.
Update the materialized view periodically.

SQL> create materialized view mat_std as
       2  select * from std;
            Materialized view created.
SQL> select * from std;
    ROLLNO NAME
---------- ----------
         1 dddd
         2 asas
         3 vbb
         4 bnm
SQL> select * from mat_std;
    ROLLNO NAME
---------- ----------
         1 dddd
         2 asas
`````

## Page 6

![Original page 6](assets/07_Views/page-006.jpg)

### Extracted text

`````text
         3 vbb
         4 bnm
SQL> insert into std values(5,'Jay');
1 row created.
SQL> select * from std;
    ROLLNO NAME
---------- ----------
         1 dddd
         2 asas
         3 vbb
         4 bnm
         5 Jay
SQL> select * from mat_std;
    ROLLNO NAME
---------- ----------
         1 dddd
         2 asas
         3 vbb
         4 bnm

Read Only view
Read only view did not perform Data manipulation operation like
insert,delete,update.From read only view we can only retrieve data .This is apply
with read only constraint.

SQL> create or replace view vw_std
  2  as select * from std with read only;
       View created.

Object View
Just as a view is a virtual table, an object view is a virtual object table.
Oracle provides object views as an extension of the basic relational view
mechanism. By using object views, you can create virtual object tables from data -
of either built-in or user-defined types - stored in the columns of relational or
object tables in the database.
Object views provide the ability to offer specialized or restricted access to the
data and objects in a database. For example, you might use an object view to
provide a version of an employee object table that doesn't have attributes
containing sensitive data and doesn't have a deletion method.
`````

## Page 7

![Original page 7](assets/07_Views/page-007.jpg)

### Extracted text

`````text
Object views allow the use of relational data in object-oriented applications. They
let users
      Try object-oriented programming techniques without converting existing
       tables.
      Convert data gradually and transparently from relational tables to object-
       relational tables.
Use legacy RDBMS data with existing object-oriented applications

Defining Object Views
Conceptually, the procedure for defining an object view is simple:
   1.  Define an object type to be represented by rows of the object view.
   2.  Write a query that specifies which data in which relational tables contain
       the attributes for objects of that type.
   3.  Specify an object identifier, based on attributes of the underlying data, to
       allow REFs to the objects (rows) of the object view.
The object identifier corresponds to the unique object identifier that Oracle
generates automatically for rows of object tables. In the case of object views,
however, the declaration must specify something that is unique in the underlying
data (for example, a primary key).

   SQL> create table std(rollno number primary key,name varchar(10));
       Table created.
   SQL> create type std_t as object(
           2  rno number,
            3  n varchar(10));
            4  /
Type created.

SQL> create view std_view of std_t
        2  with object identifier(rno) as
       3  select * from std;
  View created.
`````
