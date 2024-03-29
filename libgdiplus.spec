#
# Conditional build:
%bcond_without	pango		# pango based text rendering
#
# WARNING! libgdiplus will not work if compiled with -fomit-frame-pointer
#
Summary:	An Open Source implementation of the GDI+ API
Summary(pl.UTF-8):	Otwarta implementacja API GDI+
Name:		libgdiplus
Version:	6.1
Release:	2
License:	MIT
Group:		Libraries
Source0:	https://download.mono-project.com/sources/libgdiplus/%{name}-%{version}.tar.gz
# Source0-md5:	c017987f3434e0dcd5fa5e5c5631afeb
Patch0:		%{name}-pango.patch
URL:		https://www.mono-project.com/docs/gui/libgdiplus/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	cairo-devel >= 1.6.4
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	giflib-devel >= 5.0
BuildRequires:	glib2-devel >= 1:2.2.3
BuildRequires:	gtk+2-devel
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.6
BuildRequires:	libtiff-devel
BuildRequires:	libtool
%{?with_pango:BuildRequires:	pango-devel >= 1:1.40.14}
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
%{!?with_pango:BuildConflicts:	pango-devel}
Requires:	cairo >= 1.6.4
Requires:	glib2 >= 1:2.2.3
%{?with_pango:Requires:	pango >= 1:1.40.14}
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
Requires:	cairo-devel >= 1.6.4
Requires:	fontconfig-devel
Requires:	freetype-devel >= 2.0
Requires:	giflib-devel
Requires:	glib2-devel >= 1:2.2.3
Requires:	libexif-devel
Requires:	libjpeg-devel
Requires:	libpng-devel >= 2:1.6
Requires:	libtiff-devel
%{?with_pango:Requires:	pango-devel >= 1:1.40.14}
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

# disable gtest tests (not run, require cmake and -Werror fixes)
%{__sed} -i -e '/^if HAVE_CMAKE/,/^endif/ d' tests/Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_pango:--with-pango}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgdiplus.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS README.md TODO
%attr(755,root,root) %{_libdir}/libgdiplus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdiplus.so.0
# needed at runtime for mono to load it as gdiplus.dll
%attr(755,root,root) %{_libdir}/libgdiplus.so

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/libgdiplus.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdiplus.a
