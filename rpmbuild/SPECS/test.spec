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
# %prep

# %setup -q

#build scripts
# %build

#install scripts
%install

# Copy files
# if [ -d "/$USER/rpmbuild/BUILD/SOURCE/usr" ]; then
#     cp -r "/$USER/rpmbuild/BUILD/SOURCE/usr" "${RPM_BUILD_ROOT}"
#     echo "usr"
# fi
# 
# if [ -d "/$USER/rpmbuild/BUILD/SOURCE/etc" ]; then
#     cp -r "/$USER/rpmbuild/BUILD/SOURCE/etc" "${RPM_BUILD_ROOT}"
#     echo "etc"
# fi
# 
# if [ -d "/$USER/rpmbuild/BUILD/SOURCE/opt" ]; then
#     cp -r "/$USER/rpmbuild/BUILD/SOURCE/opt" "${RPM_BUILD_ROOT}"
#     echo "opt"
# fi


#post-install scripts
# %post

#
%files
%dir /SOURCE

#pre-uninstall scripts
# %preun

#post-uninstall scripts
# %postun



#################3

Version: 2023.06.14
Release: 1806%{?dist}
License:        GPL3
Source0:        SOURCE.tar.gz
Name:           biglinux-package-RPM
Summary:        Simple Package Description
Requires:       bash

%description
Long Package Description.

%global debug_package %{nil}

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

#
%files
%dir /opt
/opt/xpto.txt
#pre-uninstall scripts
# %preun
