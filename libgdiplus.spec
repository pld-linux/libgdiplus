#
# Conditional build:
%bcond_with	internal_cairo	# internal cairo 1.6.4 instead of system one
%bcond_with	pango		# use pango for text rendering (experimental; system cairo only)
#
# WARNING! libgdiplus will not work if compiled with -fomit-frame-pointer
#
Summary:	An Open Source implementation of the GDI+ API
Summary(pl.UTF-8):	Otwarta implementacja API GDI+
Name:		libgdiplus
Version:	2.4
Release:	2
%if %{with internal_cairo}
License:	LGPL v2.1 or MPL 1.1
%else
License:	MIT X11
%endif
Group:		Libraries
# latest downloads summary at http://ftp.novell.com/pub/mono/sources-stable/
Source0:	http://ftp.novell.com/pub/mono/sources/libgdiplus/%{name}-%{version}.tar.bz2
# Source0-md5:	ddf40d6f21ab7e8942abd063d460e4fa
Patch0:		%{name}-link.patch
Patch1:		%{name}-lt.patch
URL:		http://www.mono-project.com/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
%{!?with_internal_cairo:BuildRequires:	cairo-devel >= 1.6.4}
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel >= 1:2.2.3
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	libtiff-devel
BuildRequires:	libtool
%{?with_pango:BuildRequires:	pango-devel >= 1:1.10}
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXrender-devel
%{!?with_internal_cairo:Requires:	cairo >= 1.6.4}
Requires:	glib2 >= 1:2.2.3
%{?with_pango:Requires:	pango >= 1:1.10}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

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
%{!?with_internal_cairo:Requires:	cairo-devel >= 1.4.12}
Requires:	fontconfig-devel
Requires:	freetype-devel >= 2.0
Requires:	giflib-devel
Requires:	glib2-devel >= 1:2.2.3
Requires:	libexif-devel
Requires:	libjpeg-devel
Requires:	libpng-devel >= 1.2
Requires:	libtiff-devel
%{?with_pango:Requires:	pango-devel >= 1:1.10}
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
%patch1 -p1

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
%configure \
	%{!?with_internal_cairo:--with-cairo=system} \
	%{?with_pango:--with-pango}

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
%doc AUTHORS COPYING ChangeLog %{?with_internal_cairo:LICENSE} NEWS README TODO
%attr(755,root,root) %{_libdir}/libgdiplus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdiplus.so.0
# needed at runtime for mono to load it as gdiplus.dll
%attr(755,root,root) %{_libdir}/libgdiplus.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgdiplus.la
%{_pkgconfigdir}/libgdiplus.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdiplus.a
