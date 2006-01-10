#
# We still statically link in Cairo (and include the Cairo sources as part of
# our libgdiplus tree). Two main reasons for that: First, it eases the
# dependency hell a bit, there's not yet another lib you have to get and/or
# build, second reason is that until we use Pango for text (see below), we can
# do some private stuff to cairo to improve text-display related performance.
# --- but: the first reason is meaningless in PLD, the second seems only theoretical
#
# WARNING! libgdiplus will not work if compiled with -fomit-frame-pointer
#
Summary:	An Open Source implementation of the GDI+ API
Summary(pl):	Otwarta implementacja API GDI+
Name:		libgdiplus
Version:	1.1.13
Release:	1
License:	LGPL/MPL/MIT X11
Group:		Libraries
#Source0Download: http://www.go-mono.com/sources/
Source0:	http://www.go-mono.com/sources/libgdiplus-1.1/%{name}-%{version}.tar.gz
# Source0-md5:	9f655b0032603d653b52ce12b6c29a50
Patch0:		cairo-gcc4.patch
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
cd cairo
%patch0 -p1

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
%doc AUTHORS ChangeLog LICENSE NEWS README TODO
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
