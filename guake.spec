Summary:	A drop-down terminal for Gnome Desktop Environment
Name:     	guake
Version:	0.4.4
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Source0: 	http://guake.org/files/%{name}-%{version}.tar.gz
URL:		http://guake.org
Requires:	pygtk2.0
Requires:	python-vte
Requires:	python-dbus
Requires:	python-notify
Requires:	gnome-python-gconf
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	GConf2
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-vte
BuildRequires:	intltool

%description
Guake is a drop-down terminal for Gnome Desktop Environment, so you just
need to press a key to invoke him, and press again to hide.

%prep
%setup -q

%build
%configure2_5x \
	--disable-schemas-install \
	--disable-static
%make

%install
%makeinstall_std pythondir=%{py_platsitedir}

%{find_lang} %{name}

%preun
%preun_uninstall_gconf_schemas %{name}

%files -f %{name}.lang
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_mandir}/man1/*
%{_datadir}/dbus-1/services/org.guake.Guake.service
%{_datadir}/pixmaps/%{name}
%{_iconsdir}/hicolor/*/apps/*png
%{py_platsitedir}/%{name}

%changelog
* Fri May 06 2011 Jani Välimaa <wally@mandriva.org> 0.4.2-3mdv2011.0
+ Revision: 669798
- require python-notify (mga#1154)
- drop buildroot definition

* Sun Nov 07 2010 Jani Välimaa <wally@mandriva.org> 0.4.2-2mdv2011.0
+ Revision: 594691
- rebuild for python 2.7

* Tue Oct 12 2010 Jani Välimaa <wally@mandriva.org> 0.4.2-1mdv2011.0
+ Revision: 585198
- new version 0.4.2
- add patch from Fedora, fixes Fedora bug #626303
- clean spec a bit

* Fri Mar 05 2010 Jani Välimaa <wally@mandriva.org> 0.4.1-1mdv2010.1
+ Revision: 514480
- fix file list
- new version 0.4.1
- fix url

  + Juan Luis Baptiste <juancho@mandriva.org>
    - Missing python-dbus in Requires, without it fails when run.

* Tue Aug 25 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.0-1mdv2010.0
+ Revision: 421216
- Update to new version 0.4.0

* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-2mdv2009.1
+ Revision: 347819
- rebuild for latest python

* Fri Jul 25 2008 Funda Wang <fwang@mandriva.org> 0.3.1-1mdv2009.0
+ Revision: 249719
- New version 0.3.1

* Fri Jul 18 2008 Funda Wang <fwang@mandriva.org> 0.3-1mdv2009.0
+ Revision: 238013
- import guake


