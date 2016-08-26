Name:           libpostal
Version:        master
Release:        0.3%{?dist}
Summary:        Nothing to say

Group:          System Environment/Libraries
License:        MIT
URL:            https://github.com/openvenues/libpostal
Source0:        https://github.com/openvenues/libpostal/archive/master.zip

BuildRequires:  snappy,snappy-devel,autoconf,automake,libtool,pkgconfig
Requires:       snappy,snappy-devel,autoconf,automake,libtool,pkgconfig

%description


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
./bootstrap.sh
%configure --disable-static --datadir=/opt/data
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc
%{_libdir}/*.so.*
/usr/bin/libpostal_data
/usr/lib64/libpostal.la
/usr/lib64/pkgconfig/libpostal.pc

%files devel
%defattr(-,root,root,-)
%doc
%{_includedir}/*
%{_libdir}/*.so
/usr/bin/libpostal_data
/usr/lib64/libpostal.la
/usr/lib64/pkgconfig/libpostal.pc


%changelog
