
%define LibFastcommonDevel  libfastcommon-devel

Name: libfastcommon
Version: 1.0.21
Release: 1%{?dist}
Summary: c common functions library extracted from my open source projects FastDFS
License: GPL
Group: Arch/Tech
URL:  http://github.com/happyfish100/libfastcommon/
Source: http://github.com/happyfish100/libfastcommon/%{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

#Requires: /sbin/chkconfig
#BuildRequires: perl %{_includedir}/linux/if.h gettext
Requires: %__cp %__mv %__chmod %__grep %__mkdir %__install %__id

%description
c common functions library extracted from my open source projects FastDFS.
this library is very simple and stable. functions including: string, logger,
chain, hash, socket, ini file reader, base64 encode / decode,
url encode / decode, fasttimer etc. 

%package devel
Summary: Development header file
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This pakcage provides the header files of libfastcommon


%prep
%setup -q

%build
./make.sh

%install
rm -rf %{buildroot}
DESTDIR=$RPM_BUILD_ROOT ./make.sh install

%post

%preun

%postun

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/lib64/libfastcommon.so*

%files devel
%defattr(-,root,root,-)
/usr/include/fastcommon/*

%changelog
* Mon Jun 23 2014  Zaixue Liao <liaozaixue@yongche.com>
- first RPM release (1.0)
