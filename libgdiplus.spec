Summary:	An Open Source implementation of the GDI+ API
Summary(pl):	Otwarta implementacja API GDI+
Name:		libgdiplus
Version:	1.1.8
Release:	1
License:	LGPL/MPL/MIT X11
Group:		Libraries
#Source0Download: http://www.mono-project.com/Downloads
Source0:	http://www.go-mono.com/sources/%{name}-1.1/%{name}-%{version}.tar.gz
# Source0-md5:	8b43da0990e43f2e92b7a2bdeb86f725
Patch0:		%{name}-glitz.patch
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	glib2-devel >= 1:2.2.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libungif-devel
BuildRequires:	sed >= 4.0
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Open Source implementation of the GDI+ API.

This is part of the Mono project.

%description -l pl
Otwarta implementacja API GDI+.

Czê¶æ projektu Mono.

%package devel
Summary:	Development files for libgdiplus
Summary(pl):	Pliki programistyczne libgdiplus
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for libgdiplus.

%description devel -l pl
Pliki programistyczne libgdiplus.

%package static
Summary:	Static libgdiplus library
Summary(pl):	Statyczna biblioteka libgdiplus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgdiplus library.

%description static -l pl
Statyczna biblioteka libgdiplus.

%prep
%setup -q
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

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
%doc AUTHORS ChangeLog LICENSE NEWS README
%attr(755,root,root) %{_libdir}/libgdiplus.so.*.*.*
# needed at runtime for mono to load it as gdiplus.dll
%attr(755,root,root) %{_libdir}/libgdiplus.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgdiplus.la
%{_pkgconfigdir}/libgdiplus.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdiplus.a
