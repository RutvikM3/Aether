Contributing
============

Code
----

Please read the [standards document](doc/design/standards) before
contributing.

### Development

Make new branches for features `git checkout -b my_feature` and commit often
and push a little less often. Try to merge back to main branch as soon as
you have something that works.

#### Linting

For *C++* code make sure to use a static code checker like [cpplint](https://github.com/cpplint/cpplint) to check
the code for any style issues before submitting.  For *Python*, [flake8](https://flake8.pycqa.org/en/latest/) is
a good option.  Both of these may by installed using pip.

To install `cpplint`

```sh
# depending on your system one of these lines applies
pip install --user cpplint
pip install cpplint
python3 -m pip cpplint
python3 -m pip --user cpplint
```

### Commit Styling

The first line of the commit must be *at most* ~50 characters long and
should start with either.

- `FEAT:` For new feature.
- `BUG:` For bug fix.
- `MERGE:` For merging.
- `DOC:` For documentation update.
- `TEST:` For the addition or modification of tests.
- `STY:` For a style update (e.g., linting).
- `DEPREC:` Deprecate something, or removee a deprecated object.
- `REVERT:` Revert an earlier commit.
- `MAINT:` For maintenance such as refactoring, typos, etc.

The commit first line must be in *present* tense so that anyone picking a
commit hash can easily read what they are enabling. For more information
check out [conventional commit messages](https://www.conventionalcommits.org/en/v1.0.0/).

For example,

*do:*

```
FEAT: Hydrostatic density implementation.
```

*don't:*

```
Implemented hydrostatic density. (feature)
```

### Pull Requests

Make sure you have linted and checked your code before asking for a pull
request. Before requesting a review, ensure the pull request check list has
been completed.  Another member must check the code and approve it before merge.

Issues
------

*Issues* are reporting bugs, feature requests, or goals for the project. In
order to submit an issue make sure it follows the [issue
template](.github/ISSUE_TEMPLATE).  Please search through the existing issues
before submitting a new one, as someone else may have already come accross and
reported the problem you've encountered.
