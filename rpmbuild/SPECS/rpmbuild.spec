%global debug_package %{nil}
Version:        2023.06.19
Release:        1757%{?dist}
Source0:        source.tar.gz
Name:           biglinux-package-RPM
License:        GPL3
Summary:        Simple Package Description
Requires:       bash

%description
Long Package Description.

#pre-install scripts
# %prep

# %setup -q

#build scripts
# %build

#install scripts
%install

# Copy files
if [ -d "/$HOME/rpmbuild/BUILD/source/" ]; then
     cp -ra "/$HOME/rpmbuild/BUILD/source/BUILD/SOURCE/." "${RPM_BUILD_ROOT}/"
     echo "arquivos copiados"
fi

#post-install scripts
# %post

#FILES
%files
%dir /
%dir /opt
%dir /opt/xpto
%dir /Nova pasta
%dir /otpx
/opt/xpto/xpto.txt
/Nova pasta/Arquivo de texto.txt
/otpx/Arquivo de texto.txt

#pre-uninstall scripts
# %preun
