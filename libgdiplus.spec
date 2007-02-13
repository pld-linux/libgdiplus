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
Summary(pl.UTF-8):	Otwarta implementacja API GDI+
Name:		libgdiplus
Version:	1.2.3
Release:	1
License:	LGPL/MPL/MIT X11
Group:		Libraries
#Source0Download: http://www.go-mono.com/sources/
Source0:	http://www.go-mono.com/sources/libgdiplus/%{name}-%{version}.tar.gz
# Source0-md5:	a29d56304aca9236754e61bf8ee518ee
Patch0:		%{name}-link.patch
URL:		http://www.go-mono.com/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel >= 1:2.2.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXrender-devel
Requires:	glib2 >= 1:2.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Open Source implementation of the GDI+ API.

This is part of the Mono project.

%description -l pl.UTF-8
Otwarta implementacja API GDI+.

Część projektu Mono.

%package devel
Summary:	Development files for libgdiplus
Summary(pl.UTF-8):	Pliki programistyczne libgdiplus
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fontconfig-devel
Requires:	freetype-devel >= 2.0
Requires:	giflib-devel
Requires:	glib2-devel >= 1:2.2.3
Requires:	libjpeg-devel
Requires:	libpng-devel >= 1.2
Requires:	libtiff-devel
Requires:	xorg-lib-libXrender-devel

%description devel
Development files for libgdiplus.

%description devel -l pl.UTF-8
Pliki programistyczne libgdiplus.

%package static
Summary:	Static libgdiplus library
Summary(pl.UTF-8):	Statyczna biblioteka libgdiplus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgdiplus library.

%description static -l pl.UTF-8
Statyczna biblioteka libgdiplus.

%prep
%setup -q
%patch0 -p1

%build
cd cairo
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd -

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
