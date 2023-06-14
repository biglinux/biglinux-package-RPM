Version:        #preenchimento-automatico
Release:        #preenchimento-automatico
License:        GPL3
Source0:        SOURCE.tar.gz
Name:           biglinux-package-RPM
Summary:        Simple Package Description
Requires:       bash

%description
Long Package Description.

%global debug_package %{nil}

#pre-install scripts
%prep

%setup -q

#build scripts
%build

#install scripts
%install
rm -rf $RPM_BUILD_ROOT

#post-install scripts
%post

#
%files

#pre-uninstall scripts
%preun

#post-uninstall scripts
%postun
