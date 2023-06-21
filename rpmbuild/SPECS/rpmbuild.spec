%global debug_package %{nil}
Version:        2023.06.21
Release:        0054%{?dist}
Source0:        source.tar.gz
Name:           biglinux-package-RPM
License:        GPL3
Summary:        Simple Package Description
# Requires:       bash
# Requires:       
# Requires:       
# BuildRequires:  

%description
Long Package Description.

#pre-install scripts
%prep
%setup -q

#build scripts
%build

#install scripts
%install

if [ -d "$HOME/rpmbuild/BUILD/biglinux-package-RPM-2023.06.21/" ]; then
    cp -ra "$HOME/rpmbuild/BUILD/biglinux-package-RPM-2023.06.21/." "${RPM_BUILD_ROOT}/"
fi

#post-install scripts
%post

#FILES
%files
%dir "/opt"
%dir "/etc"
%dir "/usr"
"/opt/.file"
"/etc/.file"
"/usr/.file"

#pre-uninstall scripts
# %preun
