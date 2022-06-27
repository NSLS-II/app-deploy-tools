# git-mrt - Git MonoRepoTools

git-mrt is a developer tool to simplify working with monorepos. It
uses git sparse checkout and git subtree to provide means of working
with monorepo subdirectories as if they were a separate repositories.

## Basic usage

git-mrt sparse-clones the monorepo for local usage. From that, the
following operations are supported:

* `git mrt clone subdir/in/monorepo` - extract a subdirectory from the
monorepo. The target will be created as a separate repository directory
at the location where the command was issued. The tool will create a
`.mrt` file in that repository to preserve the subdirectory information.
That "extracted" repository is further referenced as a "subtree repository".

* `git mrt push [subdir/in/monorepo]` - absorb local, commited changes
from the subtree repository into the monorepo. A branch is created in the
monorepo containing these changes. The tool will use the `.mrt` file to
determine the subdirectory where the changes should go. If that
file is not present, the monorepo subdir can be specified directly. This
allows easily migrating existing repositories into the monorepo.

* `git mrt pull [subdir/in/monorepo]` - update the subtree repository
with any changes present in the monorepo. The tool will use the `.mrt`
file to determine which monorepo subdir to search for changes. If that
file is not present, the monorepo subdir can be specified directly.
