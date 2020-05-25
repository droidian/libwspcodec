Name: libwspcodec
Version: 2.2.1
Release: 0
Summary: WSP encoder and decoder library
Group: Development/Libraries
License: GPLv2
URL: https://git.sailfishos.org/mer-core/libwspcodec
Source: %{name}-%{version}.tar.bz2
BuildRequires: glib2-devel >= 2.0
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Provides utilities to encode and decode WSP PDUs.

%package devel
Summary: Development library for %{name}
Requires: %{name} = %{version}
Requires: pkgconfig

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

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_includedir}/wspcodec
