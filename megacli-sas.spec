Summary:	LSI Logic MegaRAID Linux MegaCLI utility
Summary(pl.UTF-8):	Linuksowe narzędzie MegaCLI dla macierzy LSI Logic MegaRAID
Name:		megacli-sas
Version:	8.05.06
Release:	3
License:	LSI
Group:		Applications/System
# http://www.lsi.com/downloads/Public/MegaRAID%20Common%20Files/8.05.06_MegaCLI.zip
# EULA acceptance required to download
Source0:	%{version}_MegaCLI.zip
# Source0-md5:	c3421608c7e3427318e41da18f91c38b
Source1:	LICENSE.LSI
BuildRequires:	rpm-utils
BuildRequires:	unzip
Requires:	sysfsutils >= 2.2.0
Requires:	sysfsutils < 2.3.0
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

# no debug symbols
%define		_enable_debug_packages	0

%description
Tool to control MegaRAID controllers:
- MegaRAID SAS 9270-8i
- MegaRAID SAS 9271-4i
- MegaRAID SAS 9271-8i
- MegaRAID SAS 9271-8iCC
- MegaRAID SAS 9286-8e
- MegaRAID SAS 9286CV-8e
- MegaRAID SAS 9286CV-8eCC
- MegaRAID SAS 9265-8i
- MegaRAID SAS 9285-8e
- MegaRAID SAS 9240-4i
- MegaRAID SAS 9240-8i
- MegaRAID SAS 9260-4i
- MegaRAID SAS 9260CV-4i
- MegaRAID SAS 9260-8i
- MegaRAID SAS 9260CV-8i
- MegaRAID SAS 9260DE-8i
- MegaRAID SAS 9261-8i
- MegaRAID SAS 9280-4i4e
- MegaRAID SAS 9280-8e
- MegaRAID SAS 9280DE-8e
- MegaRAID SAS 9280-24i4e
- MegaRAID SAS 9280-16i4e
- MegaRAID SAS 9260-16i
- MegaRAID SAS 9266-4i
- MegaRAID SAS 9266-8i
- MegaRAID SAS 9285CV-8e
- MegaRAID SAS 8704ELP
- MegaRAID SAS 8704EM2
- MegaRAID SAS 8708ELP
- MegaRAID SAS 8708EM2
- MegaRAID SAS 8880EM2
- MegaRAID SAS 8888ELP
- MegaRAID SAS 8308ELP*
- MegaRAID SAS 8344ELP*
- MegaRAID SAS 84016E*
- MegaRAID SAS 8408E*
- MegaRAID SAS 8480E*
- MegaRAID SATA 300-8ELP*

* These older controllers should work but have not been tested.

%description -l pl.UTF-8
Narzędzie do sterowania kontrolerami MegaRAID:
- MegaRAID SAS 9270-8i
- MegaRAID SAS 9271-4i
- MegaRAID SAS 9271-8i
- MegaRAID SAS 9271-8iCC
- MegaRAID SAS 9286-8e
- MegaRAID SAS 9286CV-8e
- MegaRAID SAS 9286CV-8eCC
- MegaRAID SAS 9265-8i
- MegaRAID SAS 9285-8e
- MegaRAID SAS 9240-4i
- MegaRAID SAS 9240-8i
- MegaRAID SAS 9260-4i
- MegaRAID SAS 9260CV-4i
- MegaRAID SAS 9260-8i
- MegaRAID SAS 9260CV-8i
- MegaRAID SAS 9260DE-8i
- MegaRAID SAS 9261-8i
- MegaRAID SAS 9280-4i4e
- MegaRAID SAS 9280-8e
- MegaRAID SAS 9280DE-8e
- MegaRAID SAS 9280-24i4e
- MegaRAID SAS 9280-16i4e
- MegaRAID SAS 9260-16i
- MegaRAID SAS 9266-4i
- MegaRAID SAS 9266-8i
- MegaRAID SAS 9285CV-8e
- MegaRAID SAS 8704ELP
- MegaRAID SAS 8704EM2
- MegaRAID SAS 8708ELP
- MegaRAID SAS 8708EM2
- MegaRAID SAS 8880EM2
- MegaRAID SAS 8888ELP
- MegaRAID SAS 8308ELP*
- MegaRAID SAS 8344ELP*
- MegaRAID SAS 84016E*
- MegaRAID SAS 8408E*
- MegaRAID SAS 8480E*
- MegaRAID SATA 300-8ELP*

* Te starsze kontrolery powinny działać, ale nie zostało to przetestowane.

%prep
%setup -qcT
unzip %{SOURCE0} MegaCli_Linux/* %{version}_MegaCLI.txt
rpm2cpio MegaCli_Linux/MegaCli-%{version}*.rpm | cpio -i -d
install %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
%ifarch %{ix86}
install -p opt/MegaRAID/MegaCli/MegaCli $RPM_BUILD_ROOT%{_sbindir}/MegaCli
%endif
%ifarch %{x8664}
install -p opt/MegaRAID/MegaCli/MegaCli64 $RPM_BUILD_ROOT%{_sbindir}/MegaCli
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.LSI %{version}_MegaCLI.txt
%attr(755,root,root) %{_sbindir}/MegaCli
