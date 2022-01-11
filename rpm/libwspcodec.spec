Name: libwspcodec

Version: 2.2.5
Release: 0
Summary: WSP encoder and decoder library
License: GPLv2
URL: https://github.com/sailfishos/libwspcodec
Source: %{name}-%{version}.tar.bz2

BuildRequires: pkgconfig
BuildRequires: glib2-devel >= 2.0

# license macro requires rpm >= 4.11
BuildRequires: pkgconfig(rpm)
%define license_support %(pkg-config --exists 'rpm >= 4.11'; echo $?)

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Provides utilities to encode and decode WSP PDUs.

%package devel
Summary: Development library for %{name}
Requires: %{name} = %{version}

%description devel
This package contains the development library for %{name}.

%prep
%setup -q

%build
make LIBDIR=%{_libdir} KEEP_SYMBOLS=1 release pkgconfig

%install
rm -rf %{buildroot}
make LIBDIR=%{_libdir} DESTDIR=%{buildroot} install-dev

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/%{name}*.so*
%if %{license_support} == 0
%license LICENSE LICENSE.GPL2
%endif

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_includedir}/wspcodec
