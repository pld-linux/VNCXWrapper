
# Please, do not remove this spec nor sources from CVS.
# This would be only one place where it's stored
# - see README file for details.

Summary:	VNCXWrapper - a simple wrapper for vncviewer
Summary(pl):	VNCXWrapper - prosty interfejs do vncviewera
Name:		VNCXWrapper
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	%{name}-%{version}.tgz
# Source0-md5:	1d732e29379909360a571c743c4470b4
#URL:		http://www.pld.org.pl/
BuildRequires:	kylix3_open
Requires:	vnc
Requires:	kylix3_open-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
VNCXWrapper is a simple wrapper for vncviewer. At now VNCXWrapper
has almost full support for vncviewer. It can manage all your VNC
sessions saving all session settings.

%description -l pl
VNCXWrapper to prosty interfejs do vncviewera. Aktualnie ma prawie
pe³n± obs³ugê vncviewera. Mo¿e obs³u¿yæ wszystkie sesje VNC zapisuj±c
ich wszystkie ustawienia.

%prep
%setup -q

%build
cd src
BCB="/usr/share/kylix3_open/"
export BCB
$BCB/bin/bpr2mak \
    -t$BCB/bin/default.gmk \
    -oMakefile \
    %{name}.bpr

%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Network}

install src/%{name} $RPM_BUILD_ROOT%{_bindir}
install *.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/*.desktop
