Summary:	A drop-down terminal for Gnome Desktop Environment
Name:     	guake
Version:	0.4.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Source0: 	http://guake.org/files/%{name}-%{version}.tar.gz
URL:		http://guake.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	pygtk2.0 python-vte python-dbus
BuildRequires:	gtk+2-devel libGConf2-devel
BuildRequires:	pygtk2.0-devel python-vte
BuildRequires:	intltool

%description
Guake is a drop-down terminal for Gnome Desktop Environment, so you just
need to press a key to invoke him, and press again to hide.

%prep
%setup -q

%build
%configure2_5x --disable-schemas-install
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post  

%postun

%files -f %{name}.lang
%defattr(-, root, root)
%{_sysconfdir}/gconf/schemas/*.schemas
%{_libdir}/%name
%{_bindir}/%name
%{_bindir}/%name-prefs
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*
%{_datadir}/dbus-1/services/org.gnome.Guake.service
%{_datadir}/pixmaps/%name
