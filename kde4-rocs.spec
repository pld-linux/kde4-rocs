%define		_state		stable
%define		orgname		rocs

Summary:	K Desktop Environment - Rocs Graph Theory
Summary(pl.UTF-8):	K Desktop Environment - Rocs - teoria grafów
Name:		kde4-rocs
Version:	4.12.2
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	0a112ecf557a104334ab213486fe25a4
URL:		http://www.kde.org/
BuildRequires:	QtScriptTools-devel
BuildRequires:	boost-devel
BuildRequires:	kde4-kdelibs-devel >= %{version}
Obsoletes:	kde4-kdeedu-rocs < 4.7.0
Obsoletes:	rocs <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graph Theory Tool for Professors and Students.

%description -l pl.UTF-8
Teoria grafów dla profesorów oraz studentów.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kde4-kdeedu-devel < 4.7.0
Obsoletes:	rocs-devel <= 4.8.0

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rocs
%{_desktopdir}/kde4/rocs.desktop
%{_datadir}/apps/rocs
%{_datadir}/apps/rocs_rootedtree
%{_datadir}/config.kcfg/rocs.kcfg
%{_datadir}/kde4/services/rocs_assignvaluesplugin.desktop
%{_datadir}/kde4/services/rocs_dotfileformatplugin.desktop
%{_datadir}/kde4/services/rocs_generategraphplugin.desktop
%{_datadir}/kde4/services/rocs_gmlfileformatplugin.desktop
%{_datadir}/kde4/services/rocs_GraphStructure.desktop
%{_datadir}/kde4/services/rocs_kmlfileformatplugin.desktop
%{_datadir}/kde4/services/rocs_ListStructure.desktop
%{_datadir}/kde4/services/rocs_RootedTreeStructure.desktop
%{_datadir}/kde4/services/rocs_tgffileformatplugin.desktop
%{_datadir}/kde4/services/rocs_tikzfileformatplugin.desktop
%{_datadir}/kde4/services/rocs_transformedgesplugin.desktop
%{_datadir}/kde4/servicetypes/RocsDataStructurePlugin.desktop
%{_datadir}/kde4/servicetypes/RocsGraphFilePlugin.desktop
%{_datadir}/kde4/servicetypes/RocsToolsPlugin.desktop
%{_datadir}/config/rocs.knsrc
%{_iconsdir}/hicolor/*x*/apps/rocs.png
%{_iconsdir}/hicolor/scalable/apps/rocs.svgz

%attr(755,root,root) %{_libdir}/kde4/rocs_assignvaluesplugin.so
%attr(755,root,root) %{_libdir}/kde4/rocs_dotfileformat.so
%attr(755,root,root) %{_libdir}/kde4/rocs_generategraphplugin.so
%attr(755,root,root) %{_libdir}/kde4/rocs_gmlfileformat.so
%attr(755,root,root) %{_libdir}/kde4/rocs_GraphStructure.so
%attr(755,root,root) %{_libdir}/kde4/rocs_kmlfileformat.so
%attr(755,root,root) %{_libdir}/kde4/rocs_ListStructure.so
%attr(755,root,root) %{_libdir}/kde4/rocs_RootedTreeStructure.so
%attr(755,root,root) %{_libdir}/kde4/rocs_tgffileformat.so
%attr(755,root,root) %{_libdir}/kde4/rocs_tikzfileformat.so
%attr(755,root,root) %{_libdir}/kde4/rocs_transformedgesplugin.so
%attr(755,root,root) %ghost %{_libdir}/librocscore.so.?
%attr(755,root,root) %{_libdir}/librocscore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librocsvisualeditor.so.?
%attr(755,root,root) %{_libdir}/librocsvisualeditor.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/rocs
%attr(755,root,root) %{_libdir}/librocscore.so
%attr(755,root,root) %{_libdir}/librocsvisualeditor.so
