# All Terms and Tips

## Glossary of Terms
```{glossary}
:sorted:

integer
    The data type for numbers without a decimal component. Has the type `int`.

    E.g. `0`, `-1230589672983`, `int('4')`.

    [All references →](./genindex.html#I)

float
    The data type for numbers *with* a decimal component. Can be written in scientific notation. Has the type `float`.

    E.g. `4.00000`, `1e2`, `float('1.60982')`

    [All references →](./genindex.html#F)

string
    The data type for text. Has the type `str`.

    E.g. `'single'`, `"double quotes"`, `'escaping isn\'t bad'`, `str(1.0)`

    [All references →](./genindex.html#S)

boolean
    The data type for logical truthiness or falseiness. Often arises from comparisons. Has the type `bool`.

    E.g. `True`, `False`, `1 == 2`, `bool(0)`

    [All references →](./genindex.html#B)

dot notation
    Writing a 'dot' `.` after an object in order to access that object's methods or attributes.

    E.g. `"a string".title()`, `my_array.shape`

    [All references →](./genindex.html#D)

web scraping
    Extracting data from websites, often by using code to parse the  loaded HTML as a string then converting certain snippets of that string into numbers.

    [All references →](./genindex.html#W)

index
    The positional label of an item in a sequence.

    The index of the first item in an array is zero, the index of the second item is one, and so on.

    [All references →](./genindex.html#I)

csv
    Stands for *comma-separated values*

    A format to represent data with columns separated by commas and each row stored in a new line.

    E.g.

    ```
    Name  , Height, Weight
    Adam  , 150   , 170
    Justin, 160   , 180
    ```

    [All references →](./genindex.html#I)

boolean array
    An array that exclusive stores only boolean (True-False) values in it. Usually used for [Querying →](./querying.html#index-2)

    E.g. `[True, False, False, True]`

    [All references →](./genindex.html#I)

keyword argument
    Arguments written in the form `argument_name=argument_value` are called keyword arguments.

    E.g. `by='acres'`, `ascending=False`

    [All references →](./genindex.html#I)

method chaining
     Applying two or more methods, one after the other, in one line of code is called method chaining.

     Think of it as taking the output of one method and directly feeding it into the next method without storing it into an intermediate variable.

    E.g.
    ```
    (
        fires_with_sqmiles
        .assign(square_miles=fires_with_sqmiles.get('sqmiles'))
        .drop(columns='sqmiles')
    )
    ```

    [All references →](./genindex.html#I)

query
    Creating a new table by selecting only certain rows from an existing table which satisfy some condition is called a query.

    E.g. `populations[populations.get('Population') > 1_000_000]`

    [All references →](./genindex.html#I)

dataframe
    Data represented in a tabular form.

    Different frameworks have different names for tabular data. `babypandas` calls them **dataframe** and supports a wide range of operations for the `DataFrame` object including methods like `.assign()` and `.drop()`

    [All references →](./genindex.html#I)

shape
    the count of the number of dimensions along with the number of values stored across each dimension of an n-dimensional array. Similar to the shape of a matrix that you learned in linear algebra.

    E.g.

    - 1-d array. Shape: (3,)
      `[3,4,5]`
    - 2-d array. Shape: (3,4)
      ```
      [[3,4,5]
       [4,5,6]
       [5,6,7]
       [6,7,8]]
      ```

    [All references →](./genindex.html#I)

table index
    The index of each row in a dataframe/table.

    Table index can be treated as the "first column" of a dataframe but usually treated as a special data type by most data manipulation frameworks for rapid indexing and querying. Indices are typically numeric and unique but not necessarily. Another common type of index are time-series.

    E.g.
    ```
    **Index**, Name  , Height, Weight
    **0**    , Adam  , 150   , 170
    **1**    , Justin, 160   , 180
    ```
    [All references →](./genindex.html#I)

```

## General Tips
```{tiplist}
```

## Jupyter Tips
```{jupytertiplist}
```
