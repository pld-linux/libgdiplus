Summary:	An Open Source implementation of the GDI+ API
Summary(pl):	Otwarta implementacja API GDI+
Name:		libgdiplus
Version:	1.1.5
Release:	1
License:	LGPL/MPL/MIT X11
Group:		Libraries
Source0:	http://www.go-mono.com/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	369ba22e934364dc6f0052e4a3f662fe
URL:		http://www.go-mono.com/
BuildRequires:	cairo-devel >= 0.3.0
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Open Source implementation of the GDI+ API.

This is part of the Mono project.

%description -l pl
Otwarta implementacja API GDI+.

Czê¶æ projektu Mono.

%package devel
Summary:	%{name} header files
Summary(pl):	Pliki nag³ówkowe %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
%{name} header files.

%description devel -l pl
Pliki nag³ówkowe %{name}.

%package static
Summary:	Static %{name} library
Summary(pl):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl
Statyczna biblioteka %{name}.

%prep
%setup -q

%build
%configure \
	--with-cairo=installed

echo "all:\n\ninstall:" > cairo/Makefile
echo "all:\n\ninstall:" > libpixman/Makefile

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
