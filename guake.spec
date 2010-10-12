Summary:	A drop-down terminal for Gnome Desktop Environment
Name:     	guake
Version:	0.4.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Source0: 	http://guake.org/files/%{name}-%{version}.tar.gz
Patch0:		0001-Retrieve-port-as-int.patch
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
%patch0 -p1

%build
%configure2_5x \
	--disable-schemas-install \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%{find_lang} %{name}

# we don't want this
rm -f %{buildroot}%{_libdir}/%{name}/globalhotkeys.la

%preun
%preun_uninstall_gconf_schemas %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_libdir}/%{name}
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_mandir}/man1/*
%{_datadir}/dbus-1/services/org.guake.Guake.service
%{_datadir}/pixmaps/%{name}
