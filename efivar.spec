#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : efivar
Version  : 0.21
Release  : 3
URL      : https://github.com/rhinstaller/efivar/releases/download/0.21/efivar-0.21.tar.bz2
Source0  : https://github.com/rhinstaller/efivar/releases/download/0.21/efivar-0.21.tar.bz2
Summary  : Tools to manage UEFI variables
Group    : Development/Tools
License  : LGPL-2.1
Requires: efivar-bin
Requires: efivar-lib
Requires: efivar-doc
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
%setup -q -n efivar-0.21

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/efivar

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
