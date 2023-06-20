%global debug_package %{nil}
Version:        2023.06.20
Release:        0208%{?dist}
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

if [ -d "$HOME/rpmbuild/BUILD/biglinux-package-RPM-2023.06.20/" ]; then
    cp -ra "$HOME/rpmbuild/BUILD/biglinux-package-RPM-2023.06.20/." "${RPM_BUILD_ROOT}/"
fi

#post-install scripts
%post

#FILES
%files
%dir "/otpx"
%dir "/opt"
%dir "/opt/xpto"
%dir "/Nova pasta"
"/otpx/Arquivo de texto.txt"
"/opt/xpto/xpto.txt"
"/Nova pasta/Arquivo de texto.txt"

#pre-uninstall scripts
# %preun
