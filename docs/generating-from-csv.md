# Generating documents from CSV files

Stereo is perfect for generating large amounts of documents from CSV files.

## Layout
First [create a layout](layout.md) that matches your data in CSV file.
Each field will be matched to consecutive column i.e.:

```csv
First,Last,Email
Foo,Bar,foo@bar.baz
```

could have following layout:

```python

class FirstNameField(TextField):
    # Add placement properties
    pass

class LastNameField(TextField):
    # Add placement properties
    pass

class RoleField(TextField):
    # Add placement properties
    pass

class Badge(Layout):
    fields = [
        FirstNameField,
        LastNameField,
        EmailField
    ]
```

## Generate

Now run generator from command line:

```bash
$ stereo generate --data-file file.csv layout.py
```

You can put data file, template and other default values in layout, but they will be overridden by command line arguments.

Other possible options are:

```
-d, --data-file TEXT       CSV file used to generate documents
-o, --output-dir TEXT      Directory where to store generated documents
-t, --template-file TEXT   PDF file used as template
-s, --skip-first-row TEXT  Skip the first row in CSV file?
```

## Example

An example usage of command line PDF generation can be [found in this project](https://github.com/suda/stereo/tree/master/examples/badges).
