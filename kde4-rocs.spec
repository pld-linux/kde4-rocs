%define		_state		stable
%define		orgname		rocs

Summary:	K Desktop Environment - Rocs Graph Theory
Summary(pl.UTF-8):	K Desktop Environment - Rocs - teoria grafów
Name:		kde4-rocs
Version:	4.9.0
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	ae8b066e0e6c14ab8cd1f86c010c88e1
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
%{_datadir}/config.kcfg/rocs.kcfg
%{_datadir}/kde4/services/rocs_GMLParser.desktop
%{_datadir}/kde4/services/rocs_assignvaluesplugin.desktop
%{_datadir}/kde4/services/rocs_dotFilePlugin.desktop
%{_datadir}/kde4/services/rocs_generategraphplugin.desktop
%{_datadir}/kde4/services/rocs_plaintxtplugin.desktop
%{_datadir}/kde4/services/rocs_transformedgesplugin.desktop
%{_datadir}/kde4/servicetypes/RocsDataStructurePlugin.desktop
%{_datadir}/kde4/servicetypes/RocsFilePlugin.desktop
%{_datadir}/kde4/servicetypes/RocsToolsPlugin.desktop
%{_datadir}/kde4/services/rocs_GraphStructure.desktop
%{_datadir}/kde4/services/rocs_ListStructure.desktop
%{_datadir}/config/rocs.knsrc

%attr(755,root,root) %{_libdir}/kde4/rocs_GMLParser.so
%attr(755,root,root) %{_libdir}/kde4/rocs_assignvaluesplugin.so
%attr(755,root,root) %{_libdir}/kde4/rocs_dotFilePlugin.so
%attr(755,root,root) %{_libdir}/kde4/rocs_generategraphplugin.so
%attr(755,root,root) %{_libdir}/kde4/rocs_plaintxt.so
%attr(755,root,root) %{_libdir}/kde4/rocs_transformedgesplugin.so
%attr(755,root,root) %{_libdir}/kde4/rocs_GraphStructure.so
%attr(755,root,root) %{_libdir}/kde4/rocs_ListStructure.so
%attr(755,root,root) %{_libdir}/librocslib.so.?
%attr(755,root,root) %{_libdir}/librocslib.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/rocs
%attr(755,root,root) %{_libdir}/librocslib.so
