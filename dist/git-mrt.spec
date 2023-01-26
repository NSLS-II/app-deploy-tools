# git-mrt.spec

Name:           git-mrt
Version:        1.5
Release:        4%{?dist}
Summary:        Git MonoRepo Tools - utilities to work with monorepos

License:        BSD-3-Clause
URL:            https://github.com/NSLS2/app-deploy-tools
Source0:        %{name}-%{version}.tar.gz

Requires:       git, git-subtree

%description
Git MonoRepo Tools - utilities to work with monorepos.
Provides tools to handle importing and exporting code and changes.

%global debug_package %{nil}

%prep
%autosetup -p1

%build

%install
rm -rf %{buildroot}/usr/local/bin/git-mrt
rm -rf %{buildroot}/usr/local/bin/git-fiter-repo
rm -rf %{buildroot}/usr/local/man/man1/git-mrt.1.gz

mkdir -p %{buildroot}/usr/local/bin
cp ./git-mrt %{buildroot}/usr/local/bin/git-mrt
cp ./git-filter-repo %{buildroot}/usr/local/bin/git-filter-repo
chmod a+x %{buildroot}/usr/local/bin/git-mrt
chmod a+x %{buildroot}/usr/local/bin/git-filter-repo

mkdir -p %{buildroot}/usr/local/man/man1
cp ./git-mrt.1 %{buildroot}/usr/local/man/man1
gzip %{buildroot}/usr/local/man/man1/git-mrt.1

%files
/usr/local/bin/*
/usr/local/man/*

%changelog
* Thu Jan 26 2023 Schaffer, Robert <rschaffer@bnl.gov> - 1.5-4
- Removed references to man-db, added /usr/local/man to files

* Fri Jan 20 2023 Derbenev, Anton <aderbenev@bnl.gov> - 1.5-3
- Also added man-db to BuildRequires

* Fri Jan 20 2023 Derbenev, Anton <aderbenev@bnl.gov> - 1.5-2
- Usage of mandb requires man-db package install, added to Requires

* Thu Oct 20 2022 Hu, Yong <yhu@bnl.gov> - 1.5-1
- Added the command 'git-mrt status'
- update the basepath metadata after a successful push/pull

* Mon Sep 19 2022 Schaffer, Robert <rschaffer@bnl.gov> 1.4-1
- Added man page for git-mrt command

* Mon Aug 29 2022 Hu, Yong <yhu@bnl.gov> - 1.3-1
- Using 'git pull --rebase' to avoid fast-forward problem during push
- The option '--prune-empty=always ...' works for pruning PR & merge commits
- Spec update for script version 1.3

* Fri Aug 26 2022 Derbenev, Anton <aderbenev@bnl.gov> - 1.2-1
- The monorepo URL can now be set by cli, git config, env var, or default value

* Thu Aug 25 2022 Hu, Yong <yhu@bnl.gov> - 1.1-1
- Enhanced history filtering to avoid redundant commits
- It makes sense cleaning-up only needs to be done in 'sparse_pull_mono'
- Spec update for script version 1.1

* Fri Aug 19 2022 Derbenev, Anton <aderbenev@bnl.gov> - 1.0-1
- Spec update for script version 1.0 (filter-repo)

* Tue Jul 19 2022 Derbenev, Anton <aderbenev@bnl.gov> - 0.4-1
- Added a check to not create intermediate dirs
- Logging support and more descriptive info messages
- Early return code checks to fail early
- Var renames for consistency

* Tue Jul 12 2022 Derbenev, Anton <aderbenev@bnl.gov> - 0.3-1
- Default squash on push added, minor arg parsing and error printouts enhancements

* Mon Jun 27 2022 Derbenev, Anton <aderbenev@bnl.gov> - 0.2-1
- Revised script logic and improved checks. Script help and README updated.

* Thu Jun 02 2022 Derbenev, Anton <aderbenev@bnl.gov> - 0.1-2
- Script changes, added Requires

* Thu May 19 2022 Anton Derbenev <aderbenev@bnl.gov> - 0.1-1
- RPMized monorepo-tools code
