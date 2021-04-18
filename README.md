# Fix Code Quality Issues

This program converts between US state names, and abbreviations. For example, converting "MN" to "Minnesota" or converting "California" to "CA".

## Instructions

1. **Fork** this repository
2. Clone it to your computer 
3. Make a branch with an appropriate name 
4. Fix the code quality issues
5. Push your branch to your fork
6. Make a Pull Request to the original repo
7. Watch for feedback in the PR review

When you create a PR, PyLint will run on your code and make some style checks. If it finds issues, you'll see a failing checks message in your PR. If all the checks pass, this doesn't mean that everything is good - there are numerous ther things that should be fixed that PyLint does not check for. 

## Code quality issues to look for 

* Consistency in using single and double quotes. Single quotes are prefered
* Spelling errors in comments, variable names, messages shown to the user 
* Spacing around operators. Use one space around operators, e.g. `if a == b:` and no space before a the : at the end of an if or for statement.
* Consistent line spacing between lines of code. Use exactly two blank lines between functions/methods. Avoid blank lines after for, if, elif, else statements. 
* Spacing between parameters, use one space after commas, and no spaces around the parenthesis e.g. `example_method(1, var, another_var)`
* Use underscore_names for variables and methods
* There are no classes in this example, but you should use UppercaseCamelCase for class names 
* Remove redundant comments
* Remove unnecessary print statements 
* Avoid very long lines, revise into two or more shorter lines 
* Variable names should be specific and descriptive. `data` is always a bad variable name - everything is data
* Avoid reasigning variables to store a different type of data
* Repetitive code can often be replaced with a function 
* Complex functions should be broken into simpler functions
* Comments should have a space after the #.  If a comment follows a line of code, preface the comment with two spaces. For example `default = 'cat'  # the most common choice`

There are other code quality issues. 

Further reading: https://google.github.io/styleguide/pyguide.html




