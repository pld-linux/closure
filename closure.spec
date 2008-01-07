Summary:	Fullscreen shutdown/reboot/logout menu
Summary(pl.UTF8):	Pełnoekranowe menu do zamykania/restartowania/wylogowywania
Name:		closure
Version:	0.1.3
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://closure.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	cb32ce710c4a7bc4535eb8daf567b6f6
Patch0:		%{name}-gconf.patch
Patch1:		%{name}-bin.patch
URL:		http://code.google.com/p/closure/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.6
BuildRequires:	librsvg-devel >= 2.16
BuildRequires:	pkgconfig
BuildRequires:	python-pycairo-devel >= 1.2
BuildRequires:	python-pygtk-devel >= 2:2.10
BuildRequires:	python-gnome-desktop-devel >= 2.16
BuildRequires:	python-gnome-devel >= 2.16
BuildRequires:	rpmbuild(macros) >= 1.198
Requires(post,preun):	GConf2 >= 2.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Closure is a written with eye candy in mine graphical
lock/logout/reboot/shutdown menu.

%description -l pl.UTF-8
Closure to napisane z myślą o upiększeniach graficzne menu do
blokowania ekranu/wylogowywania/restartowania/wyłączania komputera.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{name}.schemas

%preun
%gconf_schema_uninstall %{name}.schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%{_sysconfdir}/gconf/schemas/closure.schemas
%attr(755,root,root) %{_bindir}/*
%{_pkgconfigdir}/closure.pc
%{_desktopdir}/closure.desktop
%{_datadir}/closure
%dir %{py_sitescriptdir}/closure
%{py_sitescriptdir}/closure/*.py[co]
