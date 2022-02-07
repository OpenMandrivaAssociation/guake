%define _empty_manifest_terminate_build 0

Summary:	A drop-down terminal for Gnome Desktop Environment
Name:     	guake
Version:	3.8.5
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://guake.org
Source0: 	https://github.com/Guake/guake/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
Patch0: https://patch-diff.githubusercontent.com/raw/Guake/guake/pull/2038.patch

BuildRequires:	git
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(pbr)
BuildRequires:	python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  pkgconfig(proj)
BuildRequires:	pkgconfig(glib-2.0)

Requires: vte3
Requires: typelib(Keybinder)
Requires: typelib(Notify)
Requires: typelib(Vte)
Requires: typelib(Pango)
Requires: python3dist(pycairo)
Requires: python3dist(pygobject)
Requires: python3dist(dbus-python)
Requires: libnotify

%description
Guake is a drop-down terminal for Gnome Desktop Environment, so you just
need to press a key to invoke him, and press again to hide.

%prep
%autosetup -p1

%build
%make_build

%install
PBR_VERSION=%{version} %make_install PREFIX=%{_prefix} COMPILE_SCHEMA=0

%{find_lang} %{name}

%files -f %{name}.lang
%{python_sitelib}/%{name}
%{python_sitelib}/*egg-info
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/glib-2.0/schemas/org.guake.gschema.xml
%{_datadir}/pixmaps/guake.png
%{_metainfodir}/guake.desktop.metainfo.xml

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


