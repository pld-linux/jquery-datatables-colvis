%define		plugin	colvis
Summary:	DataTables ColVis plugin
Name:		jquery-datatables-%{plugin}
Version:	1.1.2
Release:	1
License:	BSD
Group:		Applications/WWW
Source0:	http://datatables.net/releases/ColVis-%{version}.zip
# Source0-md5:	c0865feb10b2ee82dd117be8205a83d4
URL:		https://datatables.net/extensions/colvis/
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	jquery-datatables >= 1.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/datatables/%{plugin}

%description
ColVis adds a button to the toolbars around DataTables which gives the
end user of the table the ability to dynamically change the visibility
of the columns in the table

%package demo
Summary:	Demo for jQuery DataTables ColVis plugin
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.datatables %{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery DataTables ColVis plugin.

%prep
%setup -qn ColVis-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cp -p js/dataTables.colVis.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p js/dataTables.colVis.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.src.js

ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js
ln -s %{plugin}-%{version}.src.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

cp -p css/dataTables.colVis.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.css
cp -p css/dataTables.colVis.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.src.css
ln -s %{plugin}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.css
ln -s %{plugin}-%{version}.src.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.css
ln -s %{plugin}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.md License.txt
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
