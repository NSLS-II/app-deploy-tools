# git-mrt.spec

Name:           git-mrt
Version:        0.1
Release:        2%{?dist}
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

mkdir -p %{buildroot}/usr/local/bin
cp ./git-mrt %{buildroot}/usr/local/bin/git-mrt
chmod a+x %{buildroot}/usr/local/bin/git-mrt

%files
/usr/local/bin/*

%changelog
* Thu Jun 02 2022 Derbenev, Anton <aderbenev@bnl.gov> - 0.1-2
- Script changes, added Requires

* Thu May 19 2022 Anton Derbenev <aderbenev@bnl.gov> - 0.1-1
- RPMized monorepo-tools code
