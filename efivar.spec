#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : efivar
Version  : 30
Release  : 6
URL      : https://github.com/rhinstaller/efivar/releases/download/30/efivar-30.tar.bz2
Source0  : https://github.com/rhinstaller/efivar/releases/download/30/efivar-30.tar.bz2
Summary  : Tools to manage UEFI variables
Group    : Development/Tools
License  : LGPL-2.1
Requires: efivar-bin
Requires: efivar-lib
Requires: efivar-doc
BuildRequires : glibc-staticdev
BuildRequires : pkgconfig(popt)
BuildRequires : popt-dev

%description
efivar provides a simple command line interface to the UEFI variable facility.

%package bin
Summary: bin components for the efivar package.
Group: Binaries

%description bin
bin components for the efivar package.


%package dev
Summary: dev components for the efivar package.
Group: Development
Requires: efivar-lib
Requires: efivar-bin
Provides: efivar-devel

%description dev
dev components for the efivar package.


%package doc
Summary: doc components for the efivar package.
Group: Documentation

%description doc
doc components for the efivar package.


%package lib
Summary: lib components for the efivar package.
Group: Libraries

%description lib
lib components for the efivar package.


%prep
%setup -q -n efivar-30

%build
export LANG=C
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -flto "
export FCFLAGS="$CFLAGS -O3 -flto "
export FFLAGS="$CFLAGS -O3 -flto "
export CXXFLAGS="$CXXFLAGS -O3 -flto "
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/efivar
/usr/bin/efivar-static

%files dev
%defattr(-,root,root,-)
/usr/include/efivar/efiboot-creator.h
/usr/include/efivar/efiboot-loadopt.h
/usr/include/efivar/efiboot.h
/usr/include/efivar/efivar-dp.h
/usr/include/efivar/efivar-guids.h
/usr/include/efivar/efivar.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
