
# Please, do not remove this spec nor sources from CVS.
# This would be only one place where it's stored
# - see README file for details.

Summary:	VNCXWrapper
Name:		VNCXWrapper
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	%{name}-%{version}.tgz
#URL:		www.pld.org.pl
BuildRequires:	kylix3_open
Requires:	vnc
Requires:	kylix3_open-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
VNCXWrapper is a simple wrapper for vncviewer. 
At now VNCXWrapper have almost full support for vncviewer.
It can manage all your vnc sessions saving all session settings.

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

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network

cp src/%{name} $RPM_BUILD_ROOT/%{_bindir}
cp *.desktop $RPM_BUILD_ROOT/%{_applnkdir}/Network

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/*.desktop
