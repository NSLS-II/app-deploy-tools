# git-mrt - Git MonoRepoTools

git-mrt is a developer tool to simplify the extraction and reintegration of
subdirectories from a singular "Monorepo", which contains code from a 
variety of locations. Using the tools 'git sparse-checkout' to allow for 
partial cloning of the monorepo and 'git filter-repo' to simplify the 
splitting and reintegration of subdirectories as local git repositories, 
this tool allows developers to work with subsections of a larger repository
using familiar commands with minimal overhead.

## Basic usage

Any usage of this tool creates or modifies a local copy of a partial clone 
of the monorepo, which will be located at "${HOME}/.monorepo" unless
otherwise specified.

Currently, the following operations are supported:

* `git mrt clone <subdir_in_monorepo>` - extract a subdirectory from the monorepo. 
The subdirectory must be specified and it must be specified in the form of something like `xf/srx/mc01`. 
The target (`mc01`) will be created as a separate repository directory
at the location where the command was issued. The tool will create a git configuration variable
`mrt.basepath` in that repository's `.git/config` to preserve the subdirectory base path information.
That "extracted" repository is further referenced as a "subrepo".

* `git mrt push [subdir_in_monorepo]` - absorb local, committed changes
from the subrepo into the monorepo. A branch is created in the
monorepo containing these changes. The tool will try to use the variable
`mrt.basepath` in `.git/config` or the environment variable GIT_MRT_BASE_PATH to
determine the subdirectory where the changes should go. If neither
variable is present, the monorepo subdir must be specified directly. This
allows easily migrating existing repositories into the monorepo.

* `git mrt pull [subdir_in_monorepo]` - update the subrepo
with any changes present in the monorepo. The tool will try to use the variable
`mrt.basepath` in `.git/config` or the environment variable GIT_MRT_BASE_PATH to
determine which monorepo subdir to search for changes. If neither
variable is present, the monorepo subdir must be specified directly.

* `git mrt status <[subdir_in_monorepo]` - show the local repo status compared to the remote monorepo.
