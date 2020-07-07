# An example of the dterm role

We can give an occurrence of a term the `dterm` role, like so:
```
{dterm}`example term`
```

This {dterm}`example term` should then be a bolded reference that links to the glossary and targets the definition of the term (if it exists).

The index page will create an entry for all terms that show up in the glossary and/or which have been given a `dterm` role. If a glossary definition exists for the term, the main entry for that term on the index will link to the definition.

Each term on the index page will have subentries for every page that uses the `dterm` role on that term. These subentries link to the page and target the occurrence.

Just like default term role, an explicit target can be passed, like so:
```
{dterm}`explicitly targeted terms <example term>`
```

These {dterm}`explicitly targeted terms <example term>` will behave identically to the target term.

```{note}
Moving forward it would be much better to have the definitions and index entries be on the same page. But for now, I'm sticking with this and moving on to more important matters!
```
