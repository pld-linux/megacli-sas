Summary:	LSI Logic MegaRAID Linux MegaCLI utility
Summary(pl.UTF-8):	Linuksowe narzędzie MegaCLI dla macierzy LSI Logic MegaRAID
Name:		megacli-sas
Version:	8.07.07
Release:	1
License:	Proprietary
Group:		Applications/System
Source0:	https://docs.broadcom.com/docs-and-downloads/sep/oracle/files/Linux_MegaCLI-8-07-07.zip
# Source0-md5:	bc63f322c725fc9cfc6671e24c1a3e2d
Source1:	LICENSE
URL:        https://docs.broadcom.com/docs/12351351
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

* Starsze kontrolery powinny działać, ale nie zostało to przetestowane.

%prep
%setup -qc
rpm2cpio MegaCli-%{version}*.rpm | cpio -i -d
install %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir}}
%ifarch %{ix86}
install -p opt/MegaRAID/MegaCli/MegaCli $RPM_BUILD_ROOT%{_sbindir}/MegaCli
%endif
%ifarch %{x8664}
install -p opt/MegaRAID/MegaCli/MegaCli64 $RPM_BUILD_ROOT%{_sbindir}/MegaCli
install -p opt/MegaRAID/MegaCli/libstorelibir-2.so.* $RPM_BUILD_ROOT%{_libdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_sbindir}/MegaCli
%ifarch %{x8664}
%{_libdir}/libstorelibir-2.so.*
%endif
