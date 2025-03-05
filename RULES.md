# Repo Rules and Standards

---


## Table Of Content

- [Git Guidelines](#git-guidelines)
  - [Git Flows](#git-flows)
  - [Temporary Branches Naming](#temporary-branches-naming)
  - [Commits Messages Guidelines](#commits-messages-guidelines)
  - [Pull Request Naming](#pull-request-naming)
- [Code Guidelines](#code-guidelines)
  - [Pre-Commit](#pre-commit)
  - [SQL Code](#sql-code)
  - [Python Naming Conventions](#python-naming-conventions)
- [Repository Standards](#repository-standards)
- [README](#README)

---
## Git Guidelines

### Git Flows

#### Feature

1. Create a `feat` branch from `development` branch
2. Do a pull request to `development`
3. Do a squash and merge to `development`
4. Create a `release` branch from development
5. Use branch name with this format: `release/<year>.<month>.<day>.<correlative_num>`
6. Do a pull request to `production`
7. Do a merge to `production`

#### Bug Fix

`fix` PR> `development` > `release` PR> `production`

#### Hot Fix

`hotfix` PR> `production`

#### Release
`release` PR> `production`

#### Experimental
If the experimentation generates usefull changes to the proyect:
`experimental` PR> `development` > `release` PR> `production`

### Temporary Branches Naming

Temporary Git branches are the branches that are created and deleted as per requirement. They are not present permanently in the repository.

A typical temporary branch name will look like:

```
<group>/<subject>/<author>
```

"**group**" must be one of the following mentioned below:

- Bug Fix (`fix`): Non urgent fix
- Hot Fix (`hotfix`): Urgent fix 
- Feature (`feat`): New characteristics and changes
- Release (`release`): Set of changes that are ready to be pushed to production
- Experimental (`experimental`): Labs and try outs for testing ideas that not necessarily will be added to the project

"**subject**" provide brief information on what the branch is doing

- precise, descriptive and understandable
- in imperative present tense (as if giving a command or instruction). Eg:
  - use `add` instead of `added` or `adds`
  - `create`, `update`, `delete`, `set`, `fix`, `refactor`, `remove`, `release`, `merge`, ...
- ideally no more than 3 words
- english alphabet (`a` to `m`)
- can have numbers (`0` to `9`)
- lower case
- use hyphens (`-`) for separating words
- should start with a letter
- for `release` branches it should have the following format: `<year>.<mont>.<day>.<correlative_num>`

"**author**" is the name or nickname of the author of the branch

- `kebab-case`: lower, separated by hyphens (`-`)
- not required on `release` branches

references:
- [namingconvention](https://namingconvention.org/git/branch-naming.html)
- [scaler](https://www.scaler.com/topics/git/git-branch-naming-conventions/)
- [atlassian](https://support.atlassian.com/bitbucket-cloud/docs/branch-a-repository/)
- [github](https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53)

### Commits Messages Guidelines

Information in commit messages
- Describe why a change is being made.
- How does it address the issue?
- What effects does the patch have?
- Do not assume the reviewer understands what the original problem was.
- Do not assume the code is self-evident/self-documenting.
- Read the commit message to see if it hints at improved code structure.
- The first commit line is the most important.
- Describe any limitations of the current code.
- Do not include patch set-specific comments.

A typical git commit message will look like:

```
<type>(<scope>): <subject>

<body>
```

"**type**" must be one of the following mentioned below:

- *`build`*: Build related changes (eg: npm related, docker related, cicd, iac, adding external dependencies)
- *`chore`*: A code change that external user won't see (eg: change to .gitignore file, .pre-commit-config.yaml or .prettierrc file)
- *`feat`*: A new feature
- *`fix`*: A bug fix
- *`docs`*: Documentation related changes
- *`refactor`*: A code that neither fix bug nor adds a feature. (eg: You can use this when there is semantic changes like renaming a variable/ function name)
- *`perf`*: A code that improves performance
- *`style`*: A code that is related to styling
- *`test`*: Adding new test or making changes to existing test

"**scope**" represents the section of the codebase. Must be the directory or the file name that better indicates the scope of the changes

"**subject**" is a short, descriptive phrase that summarizes the changes made

- use imperative present tense (as if giving a command or instruction). Eg:
  - use `add` instead of `added` or `adds`
  - `create`, `update`, `delete`, `set`, `fix`, `refactor`, `remove`, `release`, `merge`, ...
- don't use dot (.) at end
- don't capitalize first letter
- limit the line to 50 characters
- should always be able to complete the following sentence: *If applied, this commit will `<subject>`*. Eg:
  - If applied, this commit will `refactor subsystem X for readability`
  - If applied, this commit will `update getting started documentation`
  - If applied, this commit will `remove deprecated methods`
  - If applied, this commit will `release version 1.0.0`
  - If applied, this commit will `merge pull request #123 from user/branch`

"**body**" (optional) gives more details on what was changes and why

- separate the body with a blank line
- explain what and why (not how)
- wrap at 72 characters

references:
- [cbeams](https://cbea.ms/git-commit/)

### Pull Request Naming

A typical pull/merge request title will look like:

```
<status> <type>(<scope/version>): <subject> [<author>]

<description>
```

#### Pull request to `development` branch:

"**status**" (optional) to indicate if there is work in progress

- use `[WIP]` if is a draft pull request and there is work in progress, nothing if the merge request is ready for review
- used to indicate that the pull requestor:
  - has not yet finished his work on the code (thus, work in progress)
  - looks for have some initial feedback (early-pull strategy)
  - wants to use the continuous integration infrastructure of the project

**type**" must be one of the "types" used for commits messages

"**scope/version**" represents the section of the codebase. Must be the directory or the file name that better indicates the scope of the changes

"**subject**" is a short, descriptive phrase that summarizes the changes made. Same characteristics that it has for a commit message

"**author**" (optional) is the name or nickname of the author of the pull request

- `kebab-case`: lower, separated by hyphens (`-`)

#### Pull request to `production` branch:

**type**" must be one of the following mentioned below:

- *`release`*: If the pull request is from a `release` branch
- *`hotfix`*: If the pull request is from a `hotfix` branch

"**scope/version**" represents a section of the codebase or the version of the release
- Must be the directory or the file name that better indicates the scope of the fix if the pull request is from a `hotfix` branch
- The branch "subject" if the pull request is from a `release` branch

"**subject**" is a short, descriptive phrase that summarizes the changes made. Same characteristics that it has for a commit message

#### "**Description**" for both cases:

- Separated with a blank line from the subject
- Explain what, why, etc...
- Max 72 characters
- Each paragraph `Capitalized`
- Contains information of all the commits of the of the branch
- Has a checklist with all validations and previous steps required for the merge



references:
- [namingconvention](https://namingconvention.org/git/pull-request-naming.html)
- [stackoverflow](https://stackoverflow.com/questions/15763059/github-what-is-a-wip-branch)


---

## Code Guidelines

All code, regardless of language, should follow this principles:
- **DRY (Don't Repeat Yourself)**: Don´t repeat two times the same line of code. Create functions, modules or libraries for code you need to reuse.
- **KISS (Keep It Super Simple)**: The simplier the better
- **Clean Code**: Read the code should be like reading english
  - readable code
  - no comments in code
  - descriptive and precise names (variables, functions, clases, ...)

### Pre-Commit

`.pre-commit-config.yaml` file contains most of the required standards and style guides for codes (python) and files (yml, json, ipynb, ...).

Everyone who psubbmits code to this repository has to install it and use pre-commit hooks on every commit.

#### Usage

1. Install pre-commit python library: `pip install pre-commit`
2. install pre-commit hooks in the repo directory: `pre-commit install`

- Run pre-commit over all repo files: `pre-commit run --all-files`
- Run pre-commit over all staged files: `pre-commit run`

### SQL Code

Every SQL code should have this format:

```sql
WITH 
temp_table_1 AS (
  SELECT
    column1
    , column2
    , column3
    , column4
  FROM
    table1
  WHERE TRUE
    AND condition1
    AND condition2
    AND (
      condition3
      OR condition4
    )
  )

, temp_table_2 AS (
  SELECT
    column1
    , column2
    , SUM(other_column) / COUNT(other_column)
  FROM
    table2
  WHERE
    condition1
  GROUP BY
    column1
    , column2
  HAVING
    other condition
)

SELECT
  *
FROM
  temp_table_1 temp1
  LEFT JOIN 
    temp_table_2 temp2
    ON
      temp1.column1 = temp2.column1
      AND temp1.column2 = temp2.column2
;
```

- the comma (`,`) to the right
- all the SQL statements on `UPPER CASE`
- prefer `WITH` statements over nested code
- identation that simplifies the redability
- should be optimized to read from top to bottom, rather than from side to side
- readable aliases and names for columns and tables. Avoid using abreviations and one letter names (`a`, `b`, `c`, `x`, ...)
- semicolon (`;`) at the end on a new line


### Python Naming Conventions

**1. General**
- Avoid using names that are too general or too wordy. Strike a good balance between the two.
- Bad: `data_structure`, `my_list`, `info_map`, `dictionary_for_the_purpose_of_storing_data_representing_word_definitions`
- Good: `user_profile`, `menu_options`, `word_definitions`
- Don’t be a jackass and name things `O`, `l`, or `I`
- Don't use one-character names or abbreviations
- When using `CamelCase` names, capitalize all letters of an abbreviation (e.g. HTTPServer)

**2. Packages**
- `snake_case`: lower case, separated by underscore
- It is preferable to stick to 1 word names
- Should resonate with the class or methods inside the module

**3. Modules**
- `snake_case`: lower case, separated by underscore
- It is preferable to stick to 1 word names
- Should resonate with the class or methods inside the module

**4. Classes**
- `PascalCase`/`UpperCaseCamelCase`: several words are joined together, and the first letter of every word is capitalized
- Python’s built-in classes, however are typically lowercase words
- Exception classes should end in `Error`
- Preferably a noun e.g. Car, Bird, MountainBike
- Avoid acronyms and abbreviations

**5. Global (module-level) Variables**
- `snake_case`: lower case, separated by underscore
- Not begin with the special characters like e.g. & (ampersand), $ (dollar)

**6. Instance Variables**
- `snake_case`: lower case, separated by underscore
- Non-public instance variables should begin with a single underscore
- If an instance name needs to be mangled, two underscores may begin its name

**7. Methods**
- `snake_case`: lower case, separated by underscore
- Non-public method should begin with a single underscore
- If a method name needs to be mangled, two underscores may begin its name
- Must have an imperative present tense verb e.g. get_car(), purchase(), book()

**8. Method Arguments**
- Instance methods should have their first argument named `self`
- Class methods should have their first argument named `cls`

**9. Functions**
- `snake_case`: lower case, separated by underscore
- Must have an imperative present tense verb e.g. get_car(), purchase(), book()

**10. Constants**
- `SCREAMING_SNAKE_CASE`: fully capitalized, separated by an underscore
- May contain digits but not as the first character

references:
- [readthedocs](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html)
- [namingconvention](https://namingconvention.org/python/)

---

## Repository Standards

- Repo name in `kebab-case` (lowercase separeted by hyphens)
- All the directories and files that aren't a code file or package must be named in `kebab-case`
- data files names in `kebab-case` (.yml, .xml, .csv, .tsv, .parquet, .json, .html, .txt, etc...)
- other, when the convention requires otherwise. e.g.
    - Dockerfile
    - Makefile
    - README.md
    - etc...

- Must allways have a README on main directory. And in subdirectories when required.
- All the code documentation should be on the same repository (directly on the code or in README files)
- Favor branching over forking
  - Creating pull requests between branches instead of between repositories. 
  - Forking is best suited for accepting contributions from people that are unaffiliated with a project, such as open-source contributors.
- Protected branches: At least `development` and `production`

references:
- https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories

---

## README

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for?

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up?

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines

* Writing tests
* Code review
* Other guidelines

### Who do I talk to?

* Repo owner or admin
* Other community or team contact